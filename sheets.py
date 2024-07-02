import os
import base64
import json
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

load_dotenv()

SERVICE_ACCOUNT_KEY = os.environ.get("SERVICE_ACCOUNT_KEY")
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")


def get_service():
    service_account_key_base64 = SERVICE_ACCOUNT_KEY
    service_account_key_json = base64.b64decode(service_account_key_base64).decode(
        "utf-8"
    )
    service_account_info = json.loads(service_account_key_json)

    credentials = Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=credentials)
    return service


def append_values(values):
    service = get_service()
    range_name = "stock_history_DB!A1:F"

    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption="USER_ENTERED",
        body={"values": values},
    ).execute()


def append_logs(date, result, message, type, platform):
    service = get_service()
    range_name = "logs!A1:E"

    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption="USER_ENTERED",
        body={"values": [[date, result, message, type, platform]]},
    ).execute()
