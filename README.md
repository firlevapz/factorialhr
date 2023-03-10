# Factorialhr
Python adapter to use the factorialhr api and automate
sign tasks.

## Configure env file
Easiest to configure to create a `.env` file with the
cookie from your browser session copied there with
`FACTORIAL_COOKIE=...`

## Configure settings file
Configuring the settings file we can use the `main.py`
to automatically sign the work of today (default) 
or for a different day.
By default the name of the settings file is
`factorial_settings.json` you can always change it.
```json5
{
  "work": {
    // Work start time
    "start": "7:30",
    // Work end time
    "end": "15:30",
    /* Random minutes to variate, for example if the variation
    is 10, the sign time will be max 15:40 and min 7:20,
    always with the same hours worked, eg:
    start: 7:32
    end: 15:32
    -----
    start: 7:36
    end: 15:36
    If the minutes_variation is 0 the start and end will
    not variate in this case:
    start: 7:30
    end: 15:30
    */
    "minutes_variation": 10,
    /* If a day we have already sign the work and we
    save it again, we should delete the saved worked and save it again
    or not
    */
    "resave": false,
    /* List of breaks to take, following the same
    structure of start and end of work
    */
    "breaks": [
      {
        /*
          A random break min: 9:30 and max 11:00, for example 9:45 - 10:15
        */
        "start": "10:00",
        "end": "10:30",
        "minutes_variation": 30
      }
    ]
  }
}
```

## Usage

Install python3 and pip and run `pip install -r requirements.txt`
preferably in an own venv!

```
usage: main.py [-h] [-t] [-d DAY] [-m MONTH] [-y YEAR]

Log time to factorialhr

options:
  -h, --help            show this help message and exit
  -t, --today           log time just for today
  -d DAY, --day DAY     set day of month, if not set log all days of month
  -m MONTH, --month MONTH
                        set month, default: current month
  -y YEAR, --year YEAR  set year, default: current year
```
