# 🚀 Hostinger Deployment Guide

## Overview

This guide will help you deploy the Wilderness Destinations Chatbot to Hostinger hosting. Hostinger supports both static websites and Python applications, so we'll cover both deployment options.

---

## 📋 Prerequisites

- Hostinger hosting account (Premium or Business plan recommended)
- FTP client (FileZilla recommended) or use Hostinger File Manager
- Your domain name configured in Hostinger
- Git installed (for version control)

---

## 🎯 Deployment Options

### Option 1: Static Frontend Only (Recommended for Start)

Deploy just the frontend with a mock backend for demonstration purposes.

### Option 2: Full Stack with Python Backend

Deploy both frontend and backend using Hostinger's Python support.

---

## 🌐 Option 1: Static Frontend Deployment

This option deploys the chatbot frontend to Hostinger. The backend will need to be hosted elsewhere (PythonAnywhere, Heroku, etc.) or you can use mock data for demonstration.

### Step 1: Prepare Files

1. **Update config.js** with your backend API URL:

```javascript
const CONFIG = {
    // Replace with your actual backend URL
    API_URL: 'https://api.yourdomain.com/api',
    // Or use a third-party backend service
    // API_URL: 'https://your-backend.pythonanywhere.com/api',
};
```

1. **Test locally** to ensure everything works

### Step 2: Upload to Hostinger

#### Using File Manager (Easy)

1. Log in to Hostinger hPanel
2. Go to **Files** → **File Manager**
3. Navigate to `public_html` folder
4. Upload these files from the `frontend` folder:
   - `index.html`
   - `styles.css`
   - `chatbot.js`
   - `config.js`

#### Using FTP (Recommended)

1. Get FTP credentials from hPanel → **Files** → **FTP Accounts**
2. Connect using FileZilla:
   - Host: `ftp.yourdomain.com`
   - Username: Your FTP username
   - Password: Your FTP password
   - Port: 21

3. Navigate to `public_html` directory
4. Upload frontend files

### Step 3: Configure Domain

1. In hPanel, go to **Domains**
2. Ensure your domain points to the `public_html` folder
3. Enable SSL certificate (free Let's Encrypt)

### Step 4: Test

Visit: `https://yourdomain.com`

---

## 🐍 Option 2: Full Stack Deployment (Python Backend)

Hostinger Business and higher plans support Python applications.

### Step 1: Check Python Support

1. Log in to hPanel
2. Check if **Python** is available under **Advanced** section
3. Verify Python version (should be 3.8+)

### Step 2: Prepare Backend

Create a `requirements.txt` in your backend folder:

```txt
Flask==3.0.0
flask-cors==4.0.0
gunicorn==21.2.0
```

### Step 3: Create Application Entry Point

Create `wsgi.py` in the backend folder:

```python
from app import app

if __name__ == "__main__":
    app.run()
```

### Step 4: Upload Backend Files

Using FTP or File Manager:

1. Create a folder: `public_html/api` (or `backend`)
2. Upload all backend files:
   - `app.py`
   - `chatbot.py`
   - `requirements.txt`
   - `wsgi.py`

### Step 5: Install Dependencies

Via SSH (if available):

```bash
cd public_html/api
pip3 install -r requirements.txt --user
```

Or use Hostinger's Python app setup in hPanel.

### Step 6: Configure Python App

In hPanel:

1. Go to **Advanced** → **Python**
2. Create new Python application:
   - **Application root**: `/home/username/public_html/api`
   - **Application URL**: `api.yourdomain.com` or `/api`
   - **Application startup file**: `wsgi.py`
   - **Python version**: 3.8 or higher

### Step 7: Update Frontend Config

Update `frontend/config.js`:

```javascript
const CONFIG = {
    API_URL: 'https://yourdomain.com/api',
    // Or if using subdomain:
    // API_URL: 'https://api.yourdomain.com/api',
};
```

### Step 8: Upload Frontend

Upload frontend files to `public_html`:

- `index.html`
- `styles.css`
- `chatbot.js`
- `config.js`

---

## 🔧 Alternative: Backend on External Service

If Hostinger doesn't support Python or you prefer separation:

### Deploy Backend to PythonAnywhere

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com) (free tier available)
2. Upload backend files
3. Install dependencies
4. Configure web app
5. Get your API URL: `https://yourusername.pythonanywhere.com/api`

### Deploy Backend to Heroku

1. Install Heroku CLI
2. Create `Procfile`:

```
web: gunicorn app:app
```

1. Deploy:

```bash
heroku create wilderness-chatbot-api
git push heroku main
```

1. Get your API URL: `https://wilderness-chatbot-api.herokuapp.com/api`

### Update Frontend Config

```javascript
const CONFIG = {
    API_URL: 'https://yourusername.pythonanywhere.com/api',
    // Or Heroku:
    // API_URL: 'https://wilderness-chatbot-api.herokuapp.com/api',
};
```

---

## 📁 Recommended File Structure on Hostinger

```
public_html/
├── index.html              # Main chatbot page
├── styles.css              # Styling
├── chatbot.js              # Client logic
├── config.js               # Configuration
├── api/                    # Backend (if hosting on Hostinger)
│   ├── app.py
│   ├── chatbot.py
│   ├── requirements.txt
│   └── wsgi.py
└── .htaccess               # URL rewriting (optional)
```

---

## 🔐 Security Considerations

### 1. Enable HTTPS

In hPanel:

- Go to **SSL** → **Install SSL**
- Choose **Let's Encrypt** (free)
- Enable **Force HTTPS**

### 2. Protect Backend Files

Create `.htaccess` in `public_html/api`:

```apache
# Deny access to Python files
<FilesMatch "\.(py|pyc)$">
    Order allow,deny
    Deny from all
</FilesMatch>

# Allow only API endpoints
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /api/
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ wsgi.py [QSA,L]
</IfModule>
```

### 3. Environment Variables

For sensitive data, use environment variables:

Create `.env` file (don't upload to public):

```env
SECRET_KEY=your-secret-key-here
API_KEY=your-api-key
```

Update `app.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
```

---

## 🎯 Quick Deployment Checklist

### Frontend Only

- [ ] Update `config.js` with backend API URL
- [ ] Upload `index.html`, `styles.css`, `chatbot.js`, `config.js` to `public_html`
- [ ] Enable SSL certificate
- [ ] Test at `https://yourdomain.com`

### Full Stack

- [ ] Upload backend files to `public_html/api`
- [ ] Install Python dependencies
- [ ] Configure Python app in hPanel
- [ ] Upload frontend files to `public_html`
- [ ] Update `config.js` with correct API URL
- [ ] Enable SSL certificate
- [ ] Test both frontend and API endpoints

---

## 🧪 Testing After Deployment

### Test Frontend

1. Visit `https://yourdomain.com`
2. Check if page loads correctly
3. Open browser console (F12) for errors
4. Verify styles and animations work

### Test Backend API

1. Visit `https://yourdomain.com/api/health`
2. Should return: `{"status": "healthy", ...}`
3. Test chat endpoint with curl:

```bash
curl -X POST https://yourdomain.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I want to see big cats"}'
```

### Test Chat Widget

1. Click chat toggle button
2. Send a test message
3. Verify bot responds correctly
4. Test enquiry form submission

---

## 🐛 Troubleshooting

### Issue: 404 Error on API Calls

**Solution:**

- Check `config.js` has correct API URL
- Verify Python app is running in hPanel
- Check `.htaccess` configuration

### Issue: CORS Errors

**Solution:**
Update `app.py`:

```python
from flask_cors import CORS

CORS(app, origins=['https://yourdomain.com'])
```

### Issue: CSS/JS Not Loading

**Solution:**

- Clear browser cache (Ctrl+Shift+R)
- Check file paths in `index.html`
- Verify files uploaded to correct directory

### Issue: Python Dependencies Not Installing

**Solution:**

- Use `pip3 install --user` flag
- Check Python version compatibility
- Contact Hostinger support for Python app help

---

## 📊 Performance Optimization

### 1. Enable Caching

Create `.htaccess` in `public_html`:

```apache
# Enable compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript
</IfModule>

# Browser caching
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType text/html "access plus 1 hour"
</IfModule>
```

### 2. Minify Files

Before uploading, minify:

- CSS: Use [cssminifier.com](https://cssminifier.com)
- JavaScript: Use [javascript-minifier.com](https://javascript-minifier.com)

### 3. Use CDN (Optional)

Hostinger includes Cloudflare integration:

- Go to hPanel → **Advanced** → **Cloudflare**
- Enable Cloudflare CDN
- Configure caching rules

---

## 🔄 Continuous Deployment

### Using Git

1. **Initialize Git** in your project
2. **Connect to GitHub** (already done)
3. **Set up FTP deployment** with GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Hostinger

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: FTP Deploy
        uses: SamKirkland/FTP-Deploy-Action@4.3.0
        with:
          server: ftp.yourdomain.com
          username: ${{ secrets.FTP_USERNAME }}
          password: ${{ secrets.FTP_PASSWORD }}
          local-dir: ./frontend/
          server-dir: /public_html/
```

Add secrets in GitHub:

- Settings → Secrets → New repository secret
- Add `FTP_USERNAME` and `FTP_PASSWORD`

---

## 📞 Support Resources

- **Hostinger Help Center**: [support.hostinger.com](https://support.hostinger.com)
- **Hostinger Live Chat**: Available 24/7
- **Python on Hostinger**: Check hPanel documentation
- **Community Forums**: [community.hostinger.com](https://community.hostinger.com)

---

## ✅ Post-Deployment

After successful deployment:

1. **Test thoroughly** on different devices
2. **Monitor performance** using Hostinger analytics
3. **Set up backups** in hPanel
4. **Configure email** for enquiry notifications
5. **Add Google Analytics** (optional)
6. **Submit sitemap** to Google Search Console

---

## 🎉 You're Live

Your Wilderness Destinations Chatbot is now deployed on Hostinger!

**Frontend URL**: `https://yourdomain.com`  
**API URL**: `https://yourdomain.com/api` (if full stack)

---

**Need help?** Check the troubleshooting section or contact Hostinger support.

**Built with ❤️ for Africa's Wilderness**
