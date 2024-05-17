from datetime import datetime, timedelta


def get_yesterday():
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    return yesterday_str
