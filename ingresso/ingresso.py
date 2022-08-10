import requests
from requests.models import Response


class Ingresso(object):

    URL = "https://api-content.ingresso.com/v0/"

    def __init__(self, city_id: int, partnership: str) -> None:
        self.__city_id = city_id
        self.__partnership = partnership

    @property
    def city_id(self) -> int:
        return self.__city_id

    @property
    def partnership(self) -> str:
        return self.__partnership

    def get_url(self, path: str) -> str:
        return f"{self.URL}{path}"

    def _request(self, path: str, params: dict = {}) -> Response:
        url = self.get_url(path)
        return requests.get(url, params=params)
