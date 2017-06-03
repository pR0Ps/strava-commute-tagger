#!/usr/bin/env python

from setuptools import setup

setup(name="strava-commute-tagger",
      version="0.0.1",
      description="Add the commute tag to rides on Strava that have 'commute' in their titles",
      url="https://github.com/pR0Ps/strava-commute-tagger",
      license="MPLv2",
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
      ],
      packages=["strava_commute_tagger"],
      install_requires=["stravalib>=0.6.6,<1.0.0"],
      entry_points={'console_scripts': ["strava-commute-tagger=strava_commute_tagger:main"]}
)
