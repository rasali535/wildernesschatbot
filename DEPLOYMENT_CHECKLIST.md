# 📦 Hostinger Deployment Checklist - Updated Version

## 🎯 What to Upload After All Changes

After adding **Wilderness Destinations customizations** and **Setswana language support**, here's exactly what you need to upload to Hostinger.

---

## 📁 Files to Upload

### **Frontend Files** (Upload to `public_html/`)

These are the **ESSENTIAL** files for your chatbot to work:

#### ✅ **Core Files (REQUIRED)**

1. **`index.html`** - Main chatbot page with bilingual welcome
2. **`styles.css`** - All styling and animations
3. **`chatbot.js`** - Client-side chat logic
4. **`config.js`** - API configuration (see below)

#### 📝 **Optional Documentation Files**

These are for reference only, **NOT required** for the chatbot to work:

- `README.md`
- `WILDERNESS_CUSTOMIZATION.md`
- `SETSWANA_INTEGRATION.md`
- `SETSWANA_QUICK_REFERENCE.md`
- Other `.md` files

---

### **Backend Files** (Upload to `public_html/api/` or external service)

#### ✅ **Core Backend Files (REQUIRED)**

1. **`app.py`** - Flask API server
2. **`chatbot.py`** - Chatbot logic with 15 camps & Setswana support
3. **`translations.py`** - Setswana language translations (NEW)
4. **`sheets_logger.py`** - Google Sheets integration
5. **`email_notifier.py`** - Email notifications
6. **`requirements.txt`** - Python dependencies
7. **`wsgi.py`** - WSGI entry point (create if needed)

#### 🔐 **Configuration Files**

8. **`.env`** - Environment variables (Google Sheets credentials, email settings)

---

## 🔧 Step-by-Step Deployment

### **Step 1: Prepare Configuration Files**

#### A. Create `frontend/config.js`

```javascript
const CONFIG = {
    // OPTION 1: If backend is on Render (recommended)
    API_URL: 'https://your-backend.onrender.com/api',
    
    // OPTION 2: If backend is on Hostinger
    // API_URL: 'https://yourdomain.com/api',
    
    // OPTION 3: If backend is on PythonAnywhere
    // API_URL: 'https://yourusername.pythonanywhere.com/api',
};
```

**⚠️ IMPORTANT**: Replace with your actual backend URL!

#### B. Update `backend/.env`

```env
# Google Sheets Configuration
GOOGLE_SHEETS_CREDENTIALS_JSON={"type":"service_account",...}
GOOGLE_SHEETS_SPREADSHEET_ID=your-spreadsheet-id

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
NOTIFICATION_EMAIL=notifications@yourdomain.com
```

---

### **Step 2: Upload Frontend to Hostinger**

#### **Using Hostinger File Manager:**

1. Log in to **Hostinger hPanel**
2. Go to **Files** → **File Manager**
3. Navigate to `public_html/` folder
4. Upload these files from `frontend/` folder:
   - ✅ `index.html`
   - ✅ `styles.css`
   - ✅ `chatbot.js`
   - ✅ `config.js` (with correct API_URL)

#### **Using FTP (FileZilla):**

1. Connect to Hostinger FTP:
   - **Host**: `ftp.yourdomain.com`
   - **Username**: Your FTP username
   - **Password**: Your FTP password
   - **Port**: 21

2. Navigate to `public_html/`
3. Drag and drop the 4 frontend files

---

### **Step 3: Deploy Backend**

You have **3 options** for backend deployment:

#### **Option A: Render (Recommended - Already Set Up)**

Your backend is likely already on Render. Just ensure it's updated:

1. Push latest changes to GitHub:

   ```bash
   git push origin main
   ```

2. Render will auto-deploy from GitHub

3. Get your Render URL: `https://your-backend.onrender.com`

4. Update `frontend/config.js` with this URL

#### **Option B: Hostinger (If Python Supported)**

1. Create folder: `public_html/api/`
2. Upload all backend files:
   - `app.py`
   - `chatbot.py`
   - `translations.py` ← NEW
   - `sheets_logger.py`
   - `email_notifier.py`
   - `requirements.txt`
   - `wsgi.py`
   - `.env`

3. In hPanel → **Advanced** → **Python**:
   - Create Python app
   - Point to `wsgi.py`
   - Install dependencies

#### **Option C: PythonAnywhere**

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload backend files
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure web app
5. Get URL: `https://yourusername.pythonanywhere.com`

---

### **Step 4: Update Dependencies**

Your `requirements.txt` should include:

```txt
Flask==3.0.0
flask-cors==4.0.0
gspread==5.12.0
google-auth==2.23.4
python-dotenv==1.0.0
```

**NEW**: No additional dependencies needed for Setswana (it's built-in!)

---

### **Step 5: Enable SSL (HTTPS)**

In Hostinger hPanel:

1. Go to **SSL** → **Install SSL**
2. Choose **Let's Encrypt** (free)
3. Click **Install**
4. Enable **Force HTTPS**

---

### **Step 6: Test Your Deployment**

#### **Test Frontend:**

1. Visit: `https://yourdomain.com`
2. Check if chatbot loads
3. Verify bilingual welcome message appears
4. Open browser console (F12) - no errors should appear

#### **Test Backend API:**

1. Visit: `https://your-backend-url/api/health`
2. Should return: `{"status": "healthy"}`

#### **Test Chat Functionality:**

1. Click chat widget
2. Enter your name
3. Test English: "I want to see big cats"
4. Test Setswana: Type "Setswana" then "Ke batla go bona dikatse tse dikgolo"
5. Verify language switching works

#### **Test New Features:**

1. **15 Camps**: Ask "What camps do you have in Botswana?" (should show 5)
2. **New Experiences**: Ask "Tell me about helicopter safaris"
3. **Setswana**: Type "Dumela" (should auto-detect and respond in Setswana)

---

## 📋 Complete Upload Checklist

### Frontend (to `public_html/`)

- [ ] `index.html` (with bilingual welcome)
- [ ] `styles.css`
- [ ] `chatbot.js`
- [ ] `config.js` (with correct API_URL)

### Backend (to `public_html/api/` or external service)

- [ ] `app.py`
- [ ] `chatbot.py` (with 15 camps + Setswana)
- [ ] `translations.py` ← **NEW FILE**
- [ ] `sheets_logger.py`
- [ ] `email_notifier.py`
- [ ] `requirements.txt`
- [ ] `wsgi.py`
- [ ] `.env` (with credentials)

### Configuration

- [ ] Updated `config.js` with backend URL
- [ ] Updated `.env` with Google Sheets credentials
- [ ] Updated `.env` with email settings
- [ ] SSL certificate enabled
- [ ] CORS configured in `app.py`

### Testing

- [ ] Frontend loads at `https://yourdomain.com`
- [ ] API health check works
- [ ] Chat widget opens and closes
- [ ] English messages work
- [ ] Setswana language switching works
- [ ] Auto-detection works (type "Dumela")
- [ ] All 15 camps are accessible
- [ ] New experiences (helicopter, rhino tracking, etc.) work
- [ ] Lead capture works (Google Sheets + Email)

---

## 🚀 Quick Deployment Commands

If using Git + FTP automation:

```bash
# 1. Ensure all changes are committed
git status

# 2. Push to GitHub
git push origin main

# 3. If using Render, it auto-deploys
# If using Hostinger, use FTP or File Manager
```

---

## 🎯 Recommended Deployment Strategy

**BEST APPROACH:**

1. **Frontend on Hostinger** (static files)
   - Fast loading
   - Easy to update
   - No server management

2. **Backend on Render** (Python app)
   - Free tier available
   - Auto-deploys from GitHub
   - Easy scaling
   - Already configured

3. **Update Process:**

   ```bash
   # Make changes locally
   git add .
   git commit -m "Your changes"
   git push origin main
   
   # Render auto-deploys backend
   # Manually upload frontend to Hostinger (or use FTP automation)
   ```

---

## 📊 What's New in This Version

### ✅ **Wilderness Destinations Customizations**

- 15 luxury camps (up from 10)
- 25+ experiences (added helicopter, rhino tracking, ballooning, etc.)
- Enhanced recommendation engine
- 8 feature cards on homepage
- 8 quick reply buttons

### ✅ **Setswana Language Support**

- **NEW FILE**: `translations.py`
- Bilingual welcome message
- 50+ Setswana translations
- Auto-detection of Setswana keywords
- Manual language switching
- All experiences translated

### ✅ **Updated Documentation**

- `WILDERNESS_CUSTOMIZATION.md`
- `SETSWANA_INTEGRATION.md`
- `SETSWANA_QUICK_REFERENCE.md`
- Updated `README.md`

---

## 🐛 Common Issues & Solutions

### Issue: "translations module not found"

**Solution**: Make sure you uploaded `translations.py` to backend folder

### Issue: Setswana not working

**Solution**:

1. Check `translations.py` is uploaded
2. Verify `chatbot.py` imports it: `from translations import SetswanaTranslations`
3. Restart backend server

### Issue: Only 10 camps showing instead of 15

**Solution**: Upload the latest `chatbot.py` with all 15 camps

### Issue: CORS errors

**Solution**: Update `app.py`:

```python
from flask_cors import CORS
CORS(app, origins=['https://yourdomain.com'])
```

---

## 📞 Need Help?

- **Hostinger Support**: 24/7 live chat in hPanel
- **Render Support**: [render.com/docs](https://render.com/docs)
- **GitHub Repository**: Check your commits for version history

---

## ✅ Final Verification

After deployment, verify:

1. ✅ Chatbot loads on `https://yourdomain.com`
2. ✅ Bilingual welcome message shows
3. ✅ Can switch to Setswana (type "Setswana")
4. ✅ Auto-detection works (type "Dumela")
5. ✅ All 15 camps are accessible
6. ✅ New experiences work (helicopter, rhino, ballooning)
7. ✅ Lead capture works (test with your email)
8. ✅ No console errors (F12)

---

**🎉 You're ready to deploy!**

Your chatbot now has:

- ✅ 15 luxury camps across 8 countries
- ✅ 25+ unique experiences
- ✅ Bilingual support (English + Setswana)
- ✅ Enhanced recommendation engine
- ✅ Lead capture with Google Sheets + Email

**Built with ❤️ for Africa's Wilderness**
