# WebStatusChecker

Check and store the availability of websites with this simple command-line utility.

## Features:
- Enter any URL to quickly determine its online status.
- Keeps a history of websites checked, so you can review past results.
- Uses the `requests` library for HTTP requests and `sqlite3` for history storage.

## History:
The history of checked websites is stored in an SQLite database named `db.sqlite`. This allows you to easily track and review the status of websites you've checked over time.

## Usage
Install `requests` library:

```
pip install -r requirements.txt
```

Run the script using:

```
python web_checker.py
```

You'll be presented with a menu that lets you check a website's status or view the history of checked websites. Mostly just experimenting with sqlite on this one.
