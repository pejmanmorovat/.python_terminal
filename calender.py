from datetime import datetime
import jdatetime
from convertdate import islamic
def show_calendars():
    gregorian_date = datetime.now()
    persian_date = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
    islamic_date = islamic.from_gregorian(gregorian_date.year,     gregorian_date.month, gregorian_date.day)
    print(f"Today: {persian_date.strftime('%A')}")
    print(f"Persian Date: {persian_date.strftime('%Y/%m/%d')}")
    print(f"Month: {persian_date.strftime('%B')}")
    print(f"Gregorian  Date: {gregorian_date.strftime('%Y/%m/%d')}")
    print(f"Month: {gregorian_date.strftime('%B')}")
    print(f"Islamic Date: {islamic_date[0]}/{islamic_date[1]}/{islamic_date[2]}")
    print(f"Time: {persian_date.strftime('%H:%M:%S')}\n")
if __name__ == "__main__":
    show_calendars()
