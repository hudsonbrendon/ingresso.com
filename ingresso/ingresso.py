import requests
from requests.models import Response


class Ingresso(object):

    __URL = "https://api-content.ingresso.com/v0/"

    def __init__(self, city_id: int, partnership: str) -> None:
        """Uma classe que representa a API do ingresso.

        Args:
            city_id (int): O ID da cidade.
            partnership (str): O parceiro que deseja usar.
        """
        self.__city_id = city_id
        self.__partnership = partnership

    @property
    def city_id(self) -> int:
        """Retorna o da cidade.

        Returns:
            int: O ID da cidade.
        """
        return self.__city_id

    @property
    def partnership(self) -> str:
        """Retorna o parceiro.

        Returns:
            str: O parceiro.
        """
        return self.__partnership

    @property
    def url(self) -> str:
        """Retorna a URL da API.

        Returns:
            str: A URL da API.
        """
        return self.__URL

    def get_full_url(self, path: str) -> str:
        """Retorna a URL completa da API com parâmetros.

        Args:
            path (str): A URL completa da API.

        Returns:
            str: _description_
        """
        return f"{self.url}{path}"

    def request(self, path: str, params: dict = {}) -> Response:
        """Faz uma requisição à API.

        Args:
            path (str): A path da requisição.
            params (dict, optional): Parâmetros da requisição. O padrão é {}.

        Returns:
            Response: A resposta da requisição.
        """
        return requests.get(self.get_full_url(path), params=params)

    def theaters(self, _id: int = None) -> dict:
        """Retorna os cinemas da cidade.

        Args:
            _id (int): O ID do cinema. O padrão é None.

        Returns:
            dict: A resposta da requisição.
        """
        params = params = {"partnership": self.partnership}

        if _id:
            return self.request(f"theaters/{_id}", params=params).json()
        return self.request(path="theaters", params=params).json()
