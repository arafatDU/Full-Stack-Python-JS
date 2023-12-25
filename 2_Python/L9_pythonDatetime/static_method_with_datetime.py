import datetime


class TimeUtilityManager:

    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now()

    @staticmethod
    def get_date_difference(date_from):
        return datetime.datetime.now() - date_from


print(TimeUtilityManager.get_current_datetime())
birth_day = datetime.datetime(2003, 7, 7)
print(TimeUtilityManager.get_date_difference(birth_day))
