import React, { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import { useWebSocket } from '@/hooks/useWebSocket';
import { Volume2, Loader2, Mic } from 'lucide-react';

const API_BASE_URL = 'http://localhost:8000';
const WS_URL = 'ws://localhost:8000/ws/tts';

export const TextToSpeechApp: React.FC = () => {
  const [text, setText] = useState('');
  const [selectedModel, setSelectedModel] = useState('finetuned');
  const [isProcessing, setIsProcessing] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  const { isConnected, sessionId, connect, disconnect } = useWebSocket(WS_URL);

  useEffect(() => {
    connect();
    return () => disconnect();
  }, [connect, disconnect]);


  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!text.trim()) {
      setError('Please enter some text');
      return;
    }

    if (!isConnected || !sessionId) {
      setError('WebSocket not connected. Please refresh the page.');
      return;
    }

    setIsProcessing(true);
    setError(null);
    setSuccess(null);

    try {
      const response = await fetch(`${API_BASE_URL}/tts`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: text.trim(),
          session_id: sessionId,
          model_type: selectedModel,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to process text');
      }

      await response.json();
      setSuccess('বাংলা টিটিএস প্রক্রিয়া সফলভাবে শুরু হয়েছে!');
      
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setIsProcessing(false);
    }
  };


  const handleClear = () => {
    setText('');
    setError(null);
    setSuccess(null);
  };

  const sampleTexts = [
    'আমি বাংলা টেক্সট টু স্পিচ ব্যবহার করছি।',
    'অনুমোদিতভাবে ছুটি নেওয়া শৃঙ্খলাভঙ্গ হিসেবে গণ্য হয় এবং এধরনের আচরণের জন্য প্রশাসনিক ব্যবস্থা নেওয়া হতে পারে।',
    'তোমার জীবনের এমন একটি ঘটনা কি আছে যা তোমার চিন্তাধারা, বিশ্বাস বা ভবিষ্যৎ পরিকল্পনায় গভীর প্রভাব ফেলেছে?',
    'ছুটি গ্রহণের ক্ষেত্রে প্রত্যেক কর্মীরই উচিৎ প্রতিষ্ঠানের নির্ধারিত নিয়ম অনুসরণ করা এবং পূর্বানুমতি নিয়ে আবেদন করা।',
    'সময়কে সম্মান করো, কারণ একবার হারিয়ে গেলে তা আর কখনো ফিরে আসে না।',
    'জীবনে সফলতা অর্জন করতে হলে ধৈর্য এবং পরিশ্রমের কোনো বিকল্প নেই।',
    'আমি গতকাল বিকেলে যখন বাসা থেকে বেরিয়ে বইমেলায় যাচ্ছিলাম, তখন হঠাৎ করে আকাশ মেঘে ঢেকে যায়।',
    'যেকোনো সিদ্ধান্ত নেওয়ার আগে, চিন্তা করো, পরামর্শ নাও, ভেবেচিন্তে পদক্ষেপ নাও, এবং ফলাফল সম্পর্কে আগে থেকেই ধারণা রাখো।'
  ];

  const loadSampleText = (sampleText: string) => {
    setText(sampleText);
    setError(null);
    setSuccess(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2 flex items-center justify-center gap-3">
            <Volume2 className="h-10 w-10 text-blue-600" />
            বাংলা TTS মডেল তুলনা
          </h1>
          <p className="text-gray-600 text-lg">
            Fine-tuned এবং Pre-trained মডেলের মধ্যে তুলনা করুন
          </p>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <Volume2 className="h-5 w-5" />
            মডেল তুলনা প্রক্রিয়া
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-gray-600">
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-semibold text-xs">
                ১
              </div>
              <div>
                <p className="font-medium text-gray-900">টেক্সট ও মডেল নির্বাচন</p>
                <p>বাংলা টেক্সট লিখুন অথবা নমুনা টেক্সট বাটন চেপে নির্বাচন করুন এবং একটি মডেল নির্বাচন করুন</p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-semibold text-xs">
                ২
              </div>
              <div>
                <p className="font-medium text-gray-900">অডিও জেনারেট করুন</p>
                <p>"নির্বাচিত মডেল" বাটন চাপুন</p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-semibold text-xs">
                ৩
              </div>
              <div>
                <p className="font-medium text-gray-900">অডিও শুনুন</p>
                <p>জেনারেট হওয়া অডিও শুনুন এবং মানের মূল্যায়ন করুন</p>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
          <div className="flex items-center gap-2 mb-4">
            <div className={`w-3 h-3 rounded-full ${isConnected ? 'bg-green-500' : 'bg-red-500'}`}></div>
            <span className="text-sm text-gray-600">
              {isConnected ? 'Connected' : 'Disconnected'}
            </span>
            {sessionId && (
              <span className="text-xs text-gray-400 ml-2">
                Session: {sessionId.slice(0, 8)}...
              </span>
            )}
          </div>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="space-y-2">
              <Label>নমুনা টেক্সট (Sample Texts)</Label>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
                {sampleTexts.map((sample, index) => {
                  const labels = [
                    'সাধারণ', 'প্রশাসনিক', 'ব্যক্তিগত', 'নিয়মকানুন',
                    'জীবনদর্শন', 'অনুপ্রেরণা', 'বর্ণনামূলক', 'পরামর্শ'
                  ];
                  const colors = [
                    'bg-green-50 border-green-200 hover:bg-green-100 text-green-800',
                    'bg-blue-50 border-blue-200 hover:bg-blue-100 text-blue-800',
                    'bg-purple-50 border-purple-200 hover:bg-purple-100 text-purple-800',
                    'bg-orange-50 border-orange-200 hover:bg-orange-100 text-orange-800',
                    'bg-indigo-50 border-indigo-200 hover:bg-indigo-100 text-indigo-800',
                    'bg-pink-50 border-pink-200 hover:bg-pink-100 text-pink-800',
                    'bg-teal-50 border-teal-200 hover:bg-teal-100 text-teal-800',
                    'bg-amber-50 border-amber-200 hover:bg-amber-100 text-amber-800'
                  ];
                  return (
                    <Button
                      key={index}
                      type="button"
                      variant="outline"
                      size="sm"
                      onClick={() => loadSampleText(sample)}
                      className={`text-xs h-auto py-3 px-3 border-2 transition-all duration-200 ${colors[index]}`}
                      title={sample.length > 50 ? sample.substring(0, 50) + '...' : sample}
                    >
                      <div className="text-center">
                        <div className="font-semibold text-sm">{labels[index]}</div>
                        <div className="text-[10px] opacity-70 mt-1">
                          {sample.length} অক্ষর
                        </div>
                      </div>
                    </Button>
                  );
                })}
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="text">
                বাংলা টেক্সট লিখুন
              </Label>
              <Textarea
                id="text"
                placeholder="এখানে আপনার বাংলা টেক্সট লিখুন..."
                value={text}
                onChange={(e) => setText(e.target.value)}
                className="min-h-[120px] text-base"
                disabled={isProcessing}
              />
              <div className="text-sm text-gray-500">
                অক্ষর সংখ্যা: {text.length}
              </div>
            </div>

            <div className="space-y-2">
              <Label>মডেল নির্বাচন (Model Selection)</Label>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <div className="flex items-center space-x-2">
                    <input
                      type="radio"
                      id="pretrained"
                      name="model"
                      value="pretrained"
                      checked={selectedModel === 'pretrained'}
                      onChange={(e) => setSelectedModel(e.target.value)}
                      className="w-4 h-4 text-blue-600"
                    />
                    <label htmlFor="pretrained" className="text-sm font-medium text-gray-900">
                      Pre-trained Model (মূল মডেল)
                    </label>
                  </div>
                </div>
                
                <div className="space-y-2">
                  <div className="flex items-center space-x-2">
                    <input
                      type="radio"
                      id="finetuned"
                      name="model"
                      value="finetuned"
                      checked={selectedModel === 'finetuned'}
                      onChange={(e) => setSelectedModel(e.target.value)}
                      className="w-4 h-4 text-blue-600"
                    />
                    <label htmlFor="finetuned" className="text-sm font-medium text-gray-900">
                      Fine-tuned Model (আপনার কাস্টম মডেল)
                    </label>
                  </div>
                </div>
              </div>
            </div>

            {error && (
              <div className="bg-red-50 border border-red-200 rounded-md p-3">
                <p className="text-red-800 text-sm">{error}</p>
              </div>
            )}

            {success && (
              <div className="bg-green-50 border border-green-200 rounded-md p-3">
                <p className="text-green-800 text-sm">{success}</p>
              </div>
            )}

            <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
              <Button
                type="submit"
                disabled={isProcessing || !isConnected || !text.trim()}
                className="w-full"
              >
                {isProcessing ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    প্রক্রিয়া করা হচ্ছে...
                  </>
                ) : (
                  <>
                    <Mic className="mr-2 h-4 w-4" />
                    নির্বাচিত মডেল
                  </>
                )}
              </Button>
              
              <Button
                type="button"
                variant="outline"
                onClick={handleClear}
                disabled={isProcessing}
                className="w-full"
              >
                পরিষ্কার
              </Button>
            </div>
          </form>
        </div>

      </div>
    </div>
  );
};
