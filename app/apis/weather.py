from . import tool_router
from app.script import get_weather_data
from .util import resp


@tool_router.get("/weather/{station_id}")
def weather(station_id):
    data = get_weather_data(station_id)
    if data is None:
        return resp(code=-1, msg="error")
    else:
        return resp(data=data)
