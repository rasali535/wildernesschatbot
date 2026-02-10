@echo off
echo ========================================
echo  Wilderness Destinations Chatbot
echo  Frontend Server
echo ========================================
echo.
echo Starting HTTP server for frontend...
echo.
echo Open your browser and navigate to:
echo   http://localhost:8000
echo.
echo Make sure the backend is running on port 5000!
echo.
echo Press Ctrl+C to stop the server
echo.
cd frontend
python -m http.server 8000
