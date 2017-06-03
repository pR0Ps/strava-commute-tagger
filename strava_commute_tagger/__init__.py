#!/usr/bin/env python


import contextlib
import os

from stravalib import Client

CONFIG_DIR = os.path.join(os.environ['HOME'], '.config')
API_TOKEN_FILE = os.path.join(CONFIG_DIR, 'strava-api-token.conf')


def write_token(token):
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
    athlete = client.get_athlete()
    activities = client.get_activities()

    for a in activities:
        if not a.commute and "commute" in a.name.lower():
            print ("Adding the commute tag to {}".format(a))
            client.update_activity(a.id, commute=True)

if __name__ == "__main__":
    main()
