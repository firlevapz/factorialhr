import argparse
import sys
from calendar import Calendar
from datetime import date

from factorial.factorialclient import FactorialClient
from factorial.loader import EnvCredentials, JsonWork

settings_file = "factorial_settings.json"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Log time to factorialhr",
    )
    parser.add_argument(
        "-t", "--today", action="store_true", help="log time just for today"
    )
    parser.add_argument(
        "-d",
        "--day",
        type=int,
        help="set day of month, if not set log all days of month",
    )
    parser.add_argument(
        "-m",
        "--month",
        type=int,
        help="set month, default: current month",
    )
    parser.add_argument(
        "-y", "--year", type=int, help="set year, default: current year"
    )

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
        # generate list of all working weekdays of the month
        days = [
            d
            for d in [
                x
                for x in c.itermonthdates(year, month)
                if x.month == month and x.weekday() not in (5, 6)
            ]
        ]
    else:
        parser.print_usage()
        sys.exit(1)

    client = FactorialClient.load_from_settings(EnvCredentials())
    for day in days:
        client.worked_day(JsonWork(settings_file), day=day)
