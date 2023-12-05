from pydantic import BaseModel, Field
from typing import Dict, Optional
from datetime import date, datetime

class Location(BaseModel):
	name: str
	crs: str
	country: str
	system: str

class OriginDestination(BaseModel):
	tiploc: str
	description: str
	working_time: Optional[str] = None
	public_time: Optional[str] = None

class LocationDetail(BaseModel):
	realtimeActivated: Optional[bool] = None
	crs: str
	description: str
	gbttBookedArrival: Optional[str] = None
	gbttBookedDeparture: Optional[str] = None
	isCall: Optional[bool] = None
	isPublicCall: Optional[bool] = None
	realtimeArrival: Optional[str] = None
	realtimeArrivalActual: Optional[bool] = None
	realtimeDeparture: Optional[str] = None
	realtimeDepartureActual: Optional[bool] = None
	platform: Optional[int] = None
	platformConfirmed: Optional[bool] = None
	platformChanged: Optional[bool] = None
	displayAs: Optional[str] = None
	origin: list[OriginDestination]
	destination: list[OriginDestination]

class Service(BaseModel):
	locationDetail: LocationDetail
	serviceUid: str
	runDate: date
	trainIdentity: str
	runningIdentity: Optional[str] = None
	atocCode: str
	atocName: str
	serviceType: str
	isPassenger: bool

class Search(BaseModel):
	location: Location
	services: list[Service]

