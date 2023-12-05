import httpx
from icecream import ic
from typing import Optional
from datetime import date, time
from .models import Search, Service

"""
Realtime Trains API wrapper.

Raises:
	httpx.HTTPError: Request failed with status code {response.status_code}

Returns:
	_type_: _description_
"""
class Api:
	base_url: str = "https://api.rtt.io/api/v1/json/"

	def __init__(self, username: str, password: str) -> None:
		"""Constructor.

		Args:
			username (str): Username provided by Railtime Trains.
			password (str): Password provided by Realtime Trains.
		"""
		self.username = username
		self.password = password

	def _fetch(self, url: str) -> None:
		"""Fetch data from the Realtime Trains API.

		Args:
			url (str): URL to fetch data from.

		Raises:
			httpx.HTTPError: Error thrown if the request fails.

		Returns:
			str: json data returned from the Realtime Trains API.
		"""
		response = httpx.get(url, auth=(self.username, self.password))

		if response.status_code == 200:
			return response.json()

		raise httpx.HTTPError(f"Request failed with status code {response.status_code}")


	def fetch_search_data(self, from_station: str, to_station: Optional[str] = None, date: Optional[date] = None, time: Optional[time] = None) -> Search:
		"""Fetch data from the Realtime Trains API search endpoint.

		Args:
			from_station (str): CRS code of the station to get departure board data for.
			to_station (Optional[str], optional): CRS code of the end destination. Defaults to None.
			date (Optional[date], optional): Date for which to get the data. Defaults to None.
			time (Optional[time], optional): Time for which to get the data. Defaults to None.

		Returns:
			Search: Object containing the data returned from the Realtime Trains API.
		"""
		access_point = self.base_url + "search/" + from_station

		if to_station is not None:
			access_point += "/to/" + to_station

		if date is not None:
			formattedDate = date.strftime("%Y-%m-%d")
			year, month, day = formattedDate.split("-")
			access_point += f"/{year}/{month}/{day}"

		if time is not None:
			access_point += "/" + time.strftime("%H%M")

		ic(access_point)

		json = self._fetch(access_point)

		""" Convert json to a Search object """
		return Search(**json)

