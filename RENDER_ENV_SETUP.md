# Setting Up Email & Google Sheets Integration on Render

To make the lead collection work, you need to add Environment Variables in your Render Dashboard.

## 1. Email Notifications (Easiest)

Get instant email alerts when a user completes the chat.

1. **Go to Render Dashboard** -> **Environment** -> **Add Environment Variable**.
2. Add these variables:
    * `EMAIL_USER`: Your Gmail address (e.g., `you@gmail.com`).
    * `EMAIL_PASS`: **Your App Password** (NOT your normal password).
        * *To get App Password:* Go to [Google Account](https://myaccount.google.com/) -> Security -> 2-Step Verification -> App Passwords -> Create new "Mail" app.
    * `EMAIL_RECEIVER`: (Optional) The email where you want to receive alerts. If not set, it sends to `EMAIL_USER`.

## 2. Google Sheets Logging (Advanced)

Save all leads to a permanent Google Sheet.

1. **Create Service Account**:
    * Go to [Google Cloud Console](https://console.cloud.google.com/).
    * Create a Project -> Enable **Google Sheets API** and **Google Drive API**.
    * Go to **Credentials** -> Create **Service Account**.
    * Keys -> Create New Key -> **JSON**. Download the file.
2. **Prepare Sheet**:
    * Create a new Google Sheet named `Wilderness Leads`.
    * **Share** the sheet with the `client_email` found in your JSON file (give "Editor" access).
3. **Add to Render**:
    * Open your JSON key file in Notepad. Copy everything.
    * Add Variable `GOOGLE_CREDENTIALS_JSON`: Paste the entire JSON content.
    * Add Variable `GOOGLE_SHEET_NAME`: `Wilderness Leads` (or whatever you named it).

---

Once these are added, the chatbot will automatically send emails and update the sheet!
