
import os
import json
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SheetsLogger:
    def __init__(self):
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        self.creds = None
        self.client = None
        self.sheet = None

    def _authenticate(self):
        """Authenticates with Google Sheets API using environment variables."""
        if self.client:
            return True

        try:
            # We will use an environment variable 'GOOGLE_CREDENTIALS_JSON'
            # which will contain the entire content of the key file
            json_creds = os.environ.get('GOOGLE_CREDENTIALS_JSON')
            
            if not json_creds:
                print("Error: GOOGLE_CREDENTIALS_JSON environment variable not found.")
                return False

            creds_dict = json.loads(json_creds)
            self.creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, self.scope)
            self.client = gspread.authorize(self.creds)
            return True
        except Exception as e:
            print(f"Authentication Error: {e}")
            return False

    def log_lead(self, name, email, phone):
        """Logs a new lead to the Google Sheet."""
        if not self._authenticate():
            return False

        sheet_name = os.environ.get('GOOGLE_SHEET_NAME', 'Wilderness Leads')
        
        try:
            # Open the sheet
            self.sheet = self.client.open(sheet_name).sheet1
            
            # Prepare row data
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            row = [timestamp, name, email, phone]
            
            # Append row
            self.sheet.append_row(row)
            print(f"Successfully logged lead: {name}")
            return True
        except Exception as e:
            print(f"Error logging to sheet: {e}")
            return False
