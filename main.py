import argparse
import sys
from calendar import Calendar
from datetime import date

from factorial.exceptions import ApiError, AuthenticationTokenNotFound, UserNotLoggedIn
from factorial.factorialclient import FactorialClient
from factorial.loader import JsonCredentials, JsonWork

if __name__ == "__main__":
    settings_file = "factorial_settings.json"
    parser = argparse.ArgumentParser(
        description="Log time to factorialhr",
    )
    parser.add_argument(
        "-t", "--today", action="store_true", help="log time just for today"
    )
    parser.add_argument("-d", "--day", type=int)
    parser.add_argument("-m", "--month", type=int)
    parser.add_argument("-y", "--year", type=int)

    args = parser.parse_args()

    today = date.today()
    year = args.year or today.year
    month = args.month or today.month
    day = args.day or today.day

    if args.today:
        days = [today]
    elif args.day:
        days = [date(year, month, day)]
    elif args.month:
        c = Calendar()
        days = [
            d for d in [x for x in c.itermonthdates(year, month) if x.month == month]
        ]
    else:
        parser.print_usage()
        sys.exit(1)

    client = FactorialClient.load_from_settings(JsonCredentials(settings_file))
    for day in days:
        client.worked_day(JsonWork(settings_file), day=day)
