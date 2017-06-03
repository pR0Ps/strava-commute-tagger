#!/usr/bin/env python

from stravalib import Client

def main():
    token = input("Enter your Strava API token: ")
    if not token:
        print("No token entered, not continuing")
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
