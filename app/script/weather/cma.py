"""
来源：中国气象数据网（http://data.cma.cn）
"""
import time
from typing import Optional

import requests

from app.utils.decorators import FunctionResultCache

day_and_night_data_url = "http://data.cma.cn/weatherGis/web/weather/weatherFcst/getDayNigntData"


# 结果缓存 6 小时，防止被封
@FunctionResultCache(interval=3600 * 6, debug=True)
def get_weather_data(station_id: int, retry=3, interval=2) -> Optional[dict]:
    for _ in range(retry):
        try:
            res = requests.post(day_and_night_data_url, data={"staIds": station_id}, timeout=10)
            return res.json()["list"][-1]

        except requests.exceptions.Timeout:
            time.sleep(interval)
        except Exception as e:
            return None


if __name__ == '__main__':
    print(get_weather_data(54511))
    time.sleep(3)
    print(get_weather_data(54511))
