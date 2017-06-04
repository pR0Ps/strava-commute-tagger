#!/usr/bin/env python

import contextlib
import os

from stravalib import Client

CONFIG_DIR = os.path.join(os.environ['HOME'], '.config')
API_TOKEN_FILE = os.path.join(CONFIG_DIR, 'strava-api-token.conf')


def write_token(token):
    """Write the token out to a config file"""
    with contextlib.suppress(OSError):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(API_TOKEN_FILE, 'wt') as f:
            f.write(token)


def get_token():
    """Get a token from the config file or prompt for one from the user"""

    token = None
    with contextlib.suppress(OSError):
        with open(API_TOKEN_FILE, 'rt') as f:
            token = "".join(f.readlines()).strip()

    if token:
        return token

    token = input("Enter your Strava API token: ")
    if token:
        write_token(token)
        return token

    return None


def main():

    token = get_token()
    if not token:
        print("No API token available, can't continue")
        return

    client = Client(token)
    activities = client.get_activities()

    print("Looking for activites that have 'commute' in the title, but don't "
          "have the commute property set on them...")

    interactive = True
    for a in activities:
        if not a.commute and "commute" in a.name.lower():
            print("Found activity '{}' on {} - https://www.strava.com/activities/{}"
                  "".format(a.name, a.start_date.astimezone(tz=None), a.id))
            i = ""
            if not interactive:
                i = "y"

            while i not in ("y", "n", "a", "q"):
                i = input("Add the commute tag to this activity? [y/n/a/q]: ").lower()

            if i == "y":
                client.update_activity(a.id, commute=True)
                print("Added commute tag")
            elif i == "q":
                break
            elif i == "a":
                interactive = False
    print("Done")


if __name__ == "__main__":
    main()
