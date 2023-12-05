from .api import Api
from icecream import ic
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel

class TrainService(BaseModel):
	service_uid: Optional[str] = None
	origin_name: Optional[str] = None
	destination_name: Optional[str] = None
	arrival_time: Optional[str] = None
	departure_time: Optional[str] = None
	expected_arrival_time: Optional[str] = None
	expected_departure_time: Optional[str] = None
	platform: Optional[int] = None
	company: Optional[str] = None
	minutes_delayed: Optional[int] = None

class DepartureBoard:
	"""
	Use this class to get departure board data from the Realtime Trains API. Only the data that is relevant to the departure
	board is returned.

	Args:
		username (str): Username provided by Realtime Trains.
		password (str): Password provided by Realtime Trains.
	"""

	def __init__(self, username: str, password: str) -> None:
		self.api = Api(username, password)

	def get_search_data(self, from_station: str, to_station: str = None, date: Optional[date] = None, time: str = None, platform: Optional[int] = None, num_results: Optional[int] = None) -> dict:
		"""
		Get departure board data from the Realtime Trains API.

		Args:
			from_station (str): CRS code of the station to get departure board data for.
			to_station (str, optional): CRS code of the station to filter the departure board data by. Defaults to None.
			date (str, optional): Date to get departure board data for. Defaults to None.
			time (str, optional): Time to get departure board data for. Defaults to None.

		Returns:
			dict: Departure board data from the Realtime Trains API.
		"""
		services = []

		try:
			# Get the search data from the Realtime Trains API
			search_data = self.api.fetch_search_data(from_station=from_station, to_station=to_station, date=date, time=time)

			# Loop through the list of services and remove any that are not on the desired platform
			if platform is not None:
				board_data = [service for service in search_data.services if service.locationDetail.platform == platform]
			else:
				board_data = search_data.services

			# If we specified the number of results to return, only return that number of results
			if num_results is not None:
				board_data = board_data[:num_results]

			# Convert the data to a format that is easier to work with
			for board_item in board_data:
				service = TrainService()
				service.service_uid = board_item.serviceUid
				service.expected_arrival_time = datetime.strptime(board_item.locationDetail.realtimeArrival, "%H%M").strftime("%H:%M") if board_item.locationDetail.realtimeArrival is not None else ""
				service.expected_departure_time = datetime.strptime(board_item.locationDetail.realtimeDeparture, "%H%M").strftime("%H:%M") if board_item.locationDetail.realtimeDeparture is not None else ""
				service.arrival_time = datetime.strptime(board_item.locationDetail.gbttBookedArrival, "%H%M").strftime("%H:%M") if board_item.locationDetail.gbttBookedArrival is not None else ""
				service.departure_time = datetime.strptime(board_item.locationDetail.gbttBookedDeparture, "%H%M").strftime("%H:%M") if board_item.locationDetail.gbttBookedDeparture is not None else ""
				service.platform = board_item.locationDetail.platform
				service.origin_name = board_item.locationDetail.origin[0].description
				service.destination_name = board_item.locationDetail.destination[0].description
				service.company = board_item.atocName

				if service.expected_departure_time > service.departure_time:
					service.minutes_delayed = int(service.expected_departure_time.split(":")[1]) - int(service.departure_time.split(":")[1])

				services.append(service)

		except Exception as e:
			print(e)

		return services