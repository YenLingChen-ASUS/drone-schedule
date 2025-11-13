from __future__ import print_function
import os
import json
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

def main():
    # 從環境變數中載入 Google 憑證
    creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    creds = service_account.Credentials.from_service_account_info(
        creds_info, scopes=["https://www.googleapis.com/auth/calendar"]
    )

    service = build("calendar", "v3", credentials=creds)

    # 建立一個範例事件（實際上可從 GitHub event payload 帶入）
    event = {
        "summary": "Drone Flight Test",
        "location": "ASUS Drone Field",
        "description": "Created automatically from GitHub Actions",
        "start": {
            "dateTime": (datetime.utcnow() + timedelta(hours=8)).isoformat(),
            "timeZone": "Asia/Taipei",
        },
        "end": {
            "dateTime": (datetime.utcnow() + timedelta(hours=9)).isoformat(),
            "timeZone": "Asia/Taipei",
        },
    }

    calendar_id = "e875e7dd28801421793f43bc61291b87e796db8dea7b6b99d97395a9f7e8cfb1@group.calendar.google.com
"  # 或者改成你的共用日曆 ID
    event_result = service.events().insert(calendarId=calendar_id, body=event).execute()
    print(f"✅ Event created: {event_result.get('htmlLink')}")

if __name__ == "__main__":
    main()
