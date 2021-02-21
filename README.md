# LowestRatedParkingLot

## Info

This web app uses the yelp api to find the lowest rated parking lots in a given area. Locations you could check include cities, like "Los Angeles" or "Seattle".

## Setup (tested on linux)

Create an environment: <br>
`python3 -m venv venv`

Activate environment: <br>
`source venv/bin/activate`

Install requirements:<br>
`pip install -r requirements.txt`

Create database: <br>
`python manage.py migrate`

Start app: <br>
`python manage.py runserver`

