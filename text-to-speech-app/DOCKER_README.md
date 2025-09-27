# 🐳 Docker Setup for Bangladeshi Bangla TTS Application

This guide explains how to run the complete Bangladeshi Bangla TTS application using Docker.

## 🚀 Quick Start

### One Command to Start Everything:

```bash
docker-compose up
```

That's it! The entire application will start with:
- ✅ Backend API server (FastAPI)
- ✅ Frontend web application (React + Vite served directly)
- ✅ Automatic model download from Hugging Face
- ✅ Health checks and monitoring
- ✅ All dependencies handled automatically

## 📍 Access Points

Once started, access your application at:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 🔧 Docker Commands

### Start the Application
```bash
# Start in foreground (see logs)
docker-compose up

# Start in background
docker-compose up -d

# Build and start (if you made changes)
docker-compose up --build
```

### Monitor the Application
```bash
# View logs
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# View specific service logs
docker-compose logs backend
docker-compose logs frontend
```

### Stop the Application
```bash
# Stop services
docker-compose down

# Stop and remove volumes (clears cached models)
docker-compose down -v
```

### Manage Services
```bash
# Restart a specific service
docker-compose restart backend

# Scale services (if needed)
docker-compose up --scale backend=2

# Check service status
docker-compose ps
```

## 📊 What Happens on First Run

1. **Docker builds** both backend and frontend containers with all dependencies
2. **Backend startup** automatically downloads models from Hugging Face:
   - Downloads `EMTIAZZ/bangladeshi-bangla-tts-vits` (997MB model + config)
   - Downloads Coqui TTS pre-trained model
   - Caches models for future use
3. **Frontend builds** the React application and serves it directly with Node.js
4. **Health checks** ensure both services are running properly (3-minute startup window)
5. **Network setup** allows frontend to communicate with backend
6. **All dependencies** are automatically installed and configured

## 🔍 Troubleshooting

### Common Issues:

1. **Port Already in Use**:
   ```bash
   # Check what's using the ports
   sudo lsof -i :3000
   sudo lsof -i :8000
   
   # Kill processes if needed
   sudo kill -9 <PID>
   ```

2. **Model Download Issues**:
   ```bash
   # Check backend logs
   docker-compose logs backend
   
   # Restart backend if needed
   docker-compose restart backend
   ```

3. **Frontend Not Loading**:
   ```bash
   # Check frontend logs
   docker-compose logs frontend
   
   # Rebuild frontend
   docker-compose up --build frontend
   ```

4. **Clear Everything and Start Fresh**:
   ```bash
   # Stop and remove everything
   docker-compose down -v
   docker system prune -f
   
   # Start fresh
   docker-compose up --build
   ```

## 📁 Directory Structure

```
text-to-speech-app/
├── backend/
│   ├── Dockerfile              # Backend container config
│   ├── .dockerignore          # Files to ignore in backend
│   ├── main.py                # FastAPI application
│   ├── requirements.txt       # Python dependencies
│   └── utils/                 # TTS utilities
├── frontend/
│   ├── Dockerfile             # Frontend container config
│   ├── .dockerignore         # Files to ignore in frontend
│   ├── package.json          # Node.js dependencies
│   ├── vite.config.ts        # Vite configuration
│   └── src/                  # React source code
└── docker-compose.yml        # Main Docker configuration
```

## 🌐 Network Configuration

The application uses a custom Docker network (`tts-network`) that allows:
- Frontend to communicate with backend API
- WebSocket connections for real-time TTS streaming
- Proper service discovery between containers

## 💾 Data Persistence

The following data is persisted:
- **Hugging Face Cache**: Models downloaded once, reused on restart
- **Audio Files**: Generated audio files (temporary)
- **Logs**: Application logs for debugging

## 🔒 Security Notes

- The application runs in isolated Docker containers
- No sensitive data is exposed in environment variables
- Models are downloaded securely from Hugging Face
- Frontend serves static files directly via Node.js serve

## 🚀 Production Deployment

For production deployment:

1. **Use environment-specific configs**:
   ```bash
   docker-compose -f docker-compose.prod.yml up
   ```

2. **Set up reverse proxy** (Nginx/Apache) for SSL termination and load balancing

3. **Configure monitoring** and logging solutions

4. **Set up backup** for persistent volumes

## 📈 Performance Tips

- **First run**: May take 5-15 minutes due to automatic model downloads (~1GB total)
- **Subsequent runs**: Start in ~30 seconds with cached models
- **Memory usage**: ~2-4GB RAM for the complete application with loaded models (24GB VRAM recommended for GPU acceleration)
- **Storage**: ~1.5GB for cached models and dependencies
- **Model download**: Happens automatically on first startup, cached for future use

## 🆘 Getting Help

If you encounter issues:

1. Check the logs: `docker-compose logs -f`
2. Verify services are healthy: `docker-compose ps`
3. Test individual components: `curl http://localhost:8000/health`
4. Restart if needed: `docker-compose restart`

Your Bangladeshi Bangla TTS application is now fully containerized and ready for deployment! 🎉
