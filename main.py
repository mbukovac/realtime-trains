import credentials
from realtime_trains.api import RealtimeTrainsApi, SearchOptions

rtt = RealtimeTrainsApi(credentials.RTT_API_USERNAME, credentials.RTT_API_PASSWORD)
options = SearchOptions(from_station="NEM", to_station="SHP")
services = rtt.get_search_services(options)