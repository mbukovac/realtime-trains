import credentials
from icecream import ic
from realtime_trains.departure_board import DepartureBoard
from datetime import date, datetime

today = date.today()
now = datetime.now()
board = DepartureBoard(credentials.RTT_API_USERNAME, credentials.RTT_API_PASSWORD)
services = board.get_search_data(from_station="NEM", date=today, time=now)

for service in services:
	ic(service)

