@echo off
REM Wilderness Destinations Chatbot - Quick Deployment Package Creator
REM This script creates a deployment-ready package for Hostinger

echo ========================================
echo Wilderness Chatbot Deployment Packager
echo ========================================
echo.

REM Create deployment folder
set DEPLOY_DIR=wilderness-chatbot-deploy
if exist %DEPLOY_DIR% rmdir /s /q %DEPLOY_DIR%
mkdir %DEPLOY_DIR%

echo [1/5] Creating deployment directory...
mkdir %DEPLOY_DIR%\frontend
mkdir %DEPLOY_DIR%\backend

echo [2/5] Copying frontend files...
copy frontend\index.html %DEPLOY_DIR%\frontend\
copy frontend\styles.css %DEPLOY_DIR%\frontend\
copy frontend\chatbot.js %DEPLOY_DIR%\frontend\
copy frontend\config.js %DEPLOY_DIR%\frontend\
copy frontend\.htaccess %DEPLOY_DIR%\frontend\

echo [3/5] Copying backend files...
copy backend\app.py %DEPLOY_DIR%\backend\
copy backend\chatbot.py %DEPLOY_DIR%\backend\
copy backend\requirements.txt %DEPLOY_DIR%\backend\
copy backend\wsgi.py %DEPLOY_DIR%\backend\
copy backend\Procfile %DEPLOY_DIR%\backend\

echo [4/5] Copying documentation...
copy HOSTINGER_DEPLOYMENT.md %DEPLOY_DIR%\
copy README.md %DEPLOY_DIR%\
copy START_HERE.md %DEPLOY_DIR%\

echo [5/5] Creating deployment package...
powershell Compress-Archive -Path %DEPLOY_DIR%\* -DestinationPath wilderness-chatbot-hostinger.zip -Force

echo.
echo ========================================
echo Deployment package created successfully!
echo ========================================
echo.
echo Package: wilderness-chatbot-hostinger.zip
echo.
echo Next steps:
echo 1. Extract the ZIP file
echo 2. Update frontend/config.js with your API URL
echo 3. Upload frontend files to public_html/
echo 4. Upload backend files to public_html/api/ (if using Python)
echo 5. Follow HOSTINGER_DEPLOYMENT.md for detailed instructions
echo.
echo Press any key to exit...
pause >nul
