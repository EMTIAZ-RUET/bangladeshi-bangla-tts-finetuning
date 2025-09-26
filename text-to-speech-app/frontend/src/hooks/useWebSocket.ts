import { useState, useEffect, useRef, useCallback } from 'react';

interface UseWebSocketReturn {
  isConnected: boolean;
  sessionId: string | null;
  connect: () => void;
  disconnect: () => void;
  sendMessage: (message: string) => void;
}

export const useWebSocket = (url: string): UseWebSocketReturn => {
  const [isConnected, setIsConnected] = useState(false);
  const [sessionId, setSessionId] = useState<string | null>(null);
  const wsRef = useRef<WebSocket | null>(null);
  const audioContextRef = useRef<AudioContext | null>(null);
  const audioBuffersRef = useRef<AudioBuffer[]>([]);
  const isPlayingRef = useRef(false);

  const initAudioContext = useCallback(() => {
    if (!audioContextRef.current) {
      audioContextRef.current = new (window.AudioContext || (window as any).webkitAudioContext)();
    }
  }, []);

  const playAudioBuffer = useCallback(async (audioBuffer: AudioBuffer) => {
    if (!audioContextRef.current) return;

    const source = audioContextRef.current.createBufferSource();
    source.buffer = audioBuffer;
    source.connect(audioContextRef.current.destination);
    
    return new Promise<void>((resolve) => {
      source.onended = () => resolve();
      source.start();
    });
  }, []);

  const processAudioQueue = useCallback(async () => {
    if (isPlayingRef.current || audioBuffersRef.current.length === 0) return;
    
    isPlayingRef.current = true;
    
    while (audioBuffersRef.current.length > 0) {
      const buffer = audioBuffersRef.current.shift();
      if (buffer) {
        await playAudioBuffer(buffer);
      }
    }
    
    isPlayingRef.current = false;
  }, [playAudioBuffer]);

  const connect = useCallback(() => {
    if (wsRef.current?.readyState === WebSocket.OPEN) return;

    wsRef.current = new WebSocket(url);

    wsRef.current.onopen = () => {
      setIsConnected(true);
      initAudioContext();
      console.log('WebSocket connected');
    };

    wsRef.current.onmessage = async (event) => {
      if (typeof event.data === 'string') {
        try {
          const data = JSON.parse(event.data);
          if (data.topic === 'client_id') {
            setSessionId(data.session_id);
            console.log('Session ID received:', data.session_id);
          }
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      } else if (event.data instanceof Blob) {
        // Handle audio data
        try {
          const arrayBuffer = await event.data.arrayBuffer();
          if (audioContextRef.current && arrayBuffer.byteLength > 0) {
            const audioBuffer = await audioContextRef.current.decodeAudioData(arrayBuffer);
            audioBuffersRef.current.push(audioBuffer);
            processAudioQueue();
          }
        } catch (error) {
          console.error('Error processing audio data:', error);
        }
      }
    };

    wsRef.current.onclose = () => {
      setIsConnected(false);
      setSessionId(null);
      console.log('WebSocket disconnected');
    };

    wsRef.current.onerror = (error) => {
      console.error('WebSocket error:', error);
      setIsConnected(false);
    };
  }, [url, initAudioContext, processAudioQueue]);

  const disconnect = useCallback(() => {
    if (wsRef.current) {
      wsRef.current.close();
      wsRef.current = null;
    }
    setIsConnected(false);
    setSessionId(null);
  }, []);

  const sendMessage = useCallback((message: string) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(message);
    }
  }, []);

  useEffect(() => {
    return () => {
      disconnect();
      if (audioContextRef.current) {
        audioContextRef.current.close();
      }
    };
  }, [disconnect]);

  return {
    isConnected,
    sessionId,
    connect,
    disconnect,
    sendMessage,
  };
};
