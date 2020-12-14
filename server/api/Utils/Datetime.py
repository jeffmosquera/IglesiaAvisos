
import pytz
from datetime import datetime, timedelta


class Datetime:

    @staticmethod
    def get_current_datetime():
        tz_ny = pytz.timezone('America/New_York')
        datetime_ny = datetime.now(tz_ny)
        now = datetime_ny.utcnow() - timedelta(hours=5)
        return now

    @classmethod
    def get_current_timestamp(cls):
        now = cls.get_current_datetime()
        return datetime.timestamp(now)

    @staticmethod
    def convert_timestamp_to_datetime(timestamp):
        return datetime.fromtimestamp(timestamp)
