# Data Ingestion

A script to ingest data from an API periodically and analyze it.

## What it does

This script calls the [provided API](https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi) exactly once every minute for 60 minutes, starting at the top of the next hour. It places each API response into a table in a local SQLite database (which will be created if it does not exist).

## Installation

Requirements: Python 3.8 or higher with pip. Using a virtual environment is highly recommended.

Install dependencies:
```
pip install -r requirements.txt
```
Run the bot:
```
python3 main.py
```

You may need to manually kill the script with a `KeyboardInterrupt` (`Ctrl-C` or `Cmd-C`) after it has finished running and is no longer pulling from the API.

## How it works

The script makes use of the [schedule](https://schedule.readthedocs.io/en/stable/) package to start the API calls at the top of the hour and subsequently run an API request exactly once a minute. It uses [SQLAlchemy](https://www.sqlalchemy.org/) to create the database table if it does not exist, and clears the table if it already exists. It inserts a row into this table every minute.

## Output

The terminal output is below:
```
Time until start of job:  49  minutes  20  seconds
{'factor': 205379, 'pi': 3.141597522636734, 'time': '2022-05-07 13:59:59'}       2022-05-07 14:00:00.000128
{'factor': 1, 'pi': 4.0, 'time': '2022-05-07 14:00:59'}          2022-05-07 14:01:00.000015
{'factor': 8, 'pi': 3.017071817071818, 'time': '2022-05-07 14:02:00'}    2022-05-07 14:02:00.000014
{'factor': 8, 'pi': 3.017071817071818, 'time': '2022-05-07 14:02:59'}    2022-05-07 14:03:00.000017
{'factor': 64, 'pi': 3.125968606973288, 'time': '2022-05-07 14:04:00'}   2022-05-07 14:04:00.000016
{'factor': 125, 'pi': 3.1495925256000317, 'time': '2022-05-07 14:05:00'}         2022-05-07 14:05:00.000026
{'factor': 125, 'pi': 3.1495925256000317, 'time': '2022-05-07 14:05:59'}         2022-05-07 14:06:00.000118
{'factor': 216, 'pi': 3.1369630487667557, 'time': '2022-05-07 14:06:59'}         2022-05-07 14:07:00.000016
{'factor': 343, 'pi': 3.1445080992896712, 'time': '2022-05-07 14:07:59'}         2022-05-07 14:08:00.000014
{'factor': 512, 'pi': 3.139639530452431, 'time': '2022-05-07 14:08:59'}          2022-05-07 14:09:00.000015
{'factor': 729, 'pi': 3.1429643950569854, 'time': '2022-05-07 14:09:59'}         2022-05-07 14:10:00.000015
{'factor': 1000, 'pi': 3.140592653839794, 'time': '2022-05-07 14:10:59'}         2022-05-07 14:11:00.000017
{'factor': 1331, 'pi': 3.14234396828467, 'time': '2022-05-07 14:11:59'}          2022-05-07 14:12:00.000084
{'factor': 1728, 'pi': 3.141013949934539, 'time': '2022-05-07 14:12:59'}         2022-05-07 14:13:00.000016
{'factor': 2197, 'pi': 3.142047819701858, 'time': '2022-05-07 14:13:59'}         2022-05-07 14:14:00.000013
{'factor': 2744, 'pi': 3.1412282221150143, 'time': '2022-05-07 14:14:59'}        2022-05-07 14:15:00.000018
{'factor': 3375, 'pi': 3.14188894987959, 'time': '2022-05-07 14:15:59'}          2022-05-07 14:16:00.000027
{'factor': 4096, 'pi': 3.141348512968434, 'time': '2022-05-07 14:16:59'}         2022-05-07 14:17:00.000016
{'factor': 4913, 'pi': 3.1417961952119438, 'time': '2022-05-07 14:17:59'}        2022-05-07 14:18:00.000014
{'factor': 5832, 'pi': 3.141421185826989, 'time': '2022-05-07 14:18:59'}         2022-05-07 14:19:00.000017
{'factor': 6859, 'pi': 3.141738447436511, 'time': '2022-05-07 14:19:59'}         2022-05-07 14:20:00.000016
{'factor': 8000, 'pi': 3.141467653590268, 'time': '2022-05-07 14:20:59'}         2022-05-07 14:21:00.000024
{'factor': 9261, 'pi': 3.141700633289284, 'time': '2022-05-07 14:21:59'}         2022-05-07 14:22:00.000031
{'factor': 12167, 'pi': 3.141674843118693, 'time': '2022-05-07 14:23:00'}        2022-05-07 14:23:00.000023
{'factor': 12167, 'pi': 3.141674843118693, 'time': '2022-05-07 14:23:59'}        2022-05-07 14:24:00.000016
{'factor': 13824, 'pi': 3.141520315626915, 'time': '2022-05-07 14:24:59'}        2022-05-07 14:25:00.000022
{'factor': 15625, 'pi': 3.141656653589722, 'time': '2022-05-07 14:25:59'}        2022-05-07 14:26:00.000016
{'factor': 19683, 'pi': 3.1416434588531876, 'time': '2022-05-07 14:27:00'}       2022-05-07 14:27:00.000012
{'factor': 19683, 'pi': 3.1416434588531876, 'time': '2022-05-07 14:27:59'}       2022-05-07 14:28:00.000014
{'factor': 21952, 'pi': 3.141547099653953, 'time': '2022-05-07 14:28:59'}        2022-05-07 14:29:00.000026
{'factor': 24389, 'pi': 3.1416336556808755, 'time': '2022-05-07 14:29:59'}       2022-05-07 14:30:00.000024
{'factor': 27000, 'pi': 3.1415556165527665, 'time': '2022-05-07 14:30:59'}       2022-05-07 14:31:00.000018
{'factor': 29791, 'pi': 3.1416262207744947, 'time': '2022-05-07 14:31:59'}       2022-05-07 14:32:00.000037
{'factor': 35937, 'pi': 3.1416204800638963, 'time': '2022-05-07 14:33:00'}       2022-05-07 14:33:00.000035
{'factor': 39304, 'pi': 3.141567210886769, 'time': '2022-05-07 14:34:00'}        2022-05-07 14:34:00.000014
{'factor': 39304, 'pi': 3.141567210886769, 'time': '2022-05-07 14:34:59'}        2022-05-07 14:35:00.000030
{'factor': 42875, 'pi': 3.1416159772049452, 'time': '2022-05-07 14:35:59'}       2022-05-07 14:36:00.000016
{'factor': 46656, 'pi': 3.1415712201192867, 'time': '2022-05-07 14:36:59'}       2022-05-07 14:37:00.000014
{'factor': 54872, 'pi': 3.1415744293588412, 'time': '2022-05-07 14:38:00'}       2022-05-07 14:38:00.000016
{'factor': 54872, 'pi': 3.1415744293588412, 'time': '2022-05-07 14:38:59'}       2022-05-07 14:39:00.000014
{'factor': 59319, 'pi': 3.141609511594793, 'time': '2022-05-07 14:39:59'}        2022-05-07 14:40:00.000015
{'factor': 68921, 'pi': 3.141607162955563, 'time': '2022-05-07 14:41:00'}        2022-05-07 14:41:00.000015
{'factor': 74088, 'pi': 3.1415791561272712, 'time': '2022-05-07 14:42:00'}       2022-05-07 14:42:00.000016
{'factor': 74088, 'pi': 3.1415791561272712, 'time': '2022-05-07 14:42:59'}       2022-05-07 14:43:00.000073
{'factor': 79507, 'pi': 3.141605231098648, 'time': '2022-05-07 14:43:59'}        2022-05-07 14:44:00.000015
{'factor': 85184, 'pi': 3.1415809142959636, 'time': '2022-05-07 14:44:59'}       2022-05-07 14:45:00.000022
{'factor': 97336, 'pi': 3.141582379898584, 'time': '2022-05-07 14:46:00'}        2022-05-07 14:46:00.000015
{'factor': 103823, 'pi': 3.1416022853668917, 'time': '2022-05-07 14:47:00'}      2022-05-07 14:47:00.000016
{'factor': 110592, 'pi': 3.1415836113443634, 'time': '2022-05-07 14:48:00'}      2022-05-07 14:48:00.000015
{'factor': 117649, 'pi': 3.1416011534494763, 'time': '2022-05-07 14:49:00'}      2022-05-07 14:49:00.000014
{'factor': 125000, 'pi': 3.141584653589728, 'time': '2022-05-07 14:50:00'}       2022-05-07 14:50:00.000018
{'factor': 125000, 'pi': 3.141584653589728, 'time': '2022-05-07 14:50:59'}       2022-05-07 14:51:00.000020
{'factor': 132651, 'pi': 3.1416001921684225, 'time': '2022-05-07 14:51:59'}      2022-05-07 14:52:00.000018
{'factor': 140608, 'pi': 3.1415855416188876, 'time': '2022-05-07 14:52:59'}      2022-05-07 14:53:00.000016
{'factor': 148877, 'pi': 3.141599370544006, 'time': '2022-05-07 14:53:59'}       2022-05-07 14:54:00.000016
{'factor': 157464, 'pi': 3.1415863029318056, 'time': '2022-05-07 14:54:59'}      2022-05-07 14:55:00.000015
{'factor': 175616, 'pi': 3.141586959347785, 'time': '2022-05-07 14:56:00'}       2022-05-07 14:56:00.000016
{'factor': 185193, 'pi': 3.1415980533619163, 'time': '2022-05-07 14:57:00'}      2022-05-07 14:57:00.000015
{'factor': 195112, 'pi': 3.1415875283283916, 'time': '2022-05-07 14:58:00'}      2022-05-07 14:58:00.000070
{'factor': 195112, 'pi': 3.1415875283283916, 'time': '2022-05-07 14:58:59'}      2022-05-07 14:59:00.000015
```

**NOTE**: In this example output, some minutes have been represented twice and others have been skipped because of tiny time mismatches between my machine and the API server. To fix this issue in the future, I have changed the script to run at :30 every minute instead of :00. This way, even if the mismatch still exists, it won't accidentally read different data then intended.

## Explanation of trends

The `factor` appears to increase every minute for the entire hour. On closer inspection, `factor` is the cube of the minute of the hour, with minute 0 having factor 1 as a special case. The factor appears to dictate how precise the calculated value of `pi` is, with higher `factor`s resulting in `pi` values closer to the real value (This meant that `pi` got more accurate by the minute throughout the hour). 