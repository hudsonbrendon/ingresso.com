import requests
from requests.models import Response


class Ingresso(object):

    __URL = "https://api-content.ingresso.com/v0/"

    def __init__(self, city_id: int, partnership: str) -> None:
        self.__city_id = city_id
        self.__partnership = partnership

    @property
    def city_id(self) -> int:
        return self.__city_id

    @property
    def partnership(self) -> str:
        return self.__partnership

    @property
    def url(self) -> str:
        return self.__URL

    def get_full_url(self, path: str) -> str:
        return f"{self.url}{path}"

    def _request(self, path: str, params: dict = {}) -> Response:
        return requests.get(self.get_full_url(path), params=params)
