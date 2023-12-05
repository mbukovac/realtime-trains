from pydantic import BaseModel

class Model_Location(BaseModel):
	name: str
	crs: str
	tiploc: str