import requests
from requests.models import Response


class Ingresso(object):
    __URL = "https://api-content.ingresso.com/v0/"

    def __init__(
        self,
        city_id: int,
        partnership: str,
    ) -> None:
        """Uma classe que representa a API do ingresso.

        Args:
            city_id (int): O ID da cidade.
            partnership (str): O parceiro que deseja usar.
        """
        self.__city_id = city_id
        self.__partnership = partnership

    @property
    def city_id(
        self,
    ) -> int:
        """Retorna o da cidade.

        Returns:
            int: O ID da cidade.
        """
        return self.__city_id

    @property
    def partnership(
        self,
    ) -> str:
        """Retorna o parceiro.

        Returns:
            str: O parceiro.
        """
        return self.__partnership

    @property
    def url(
        self,
    ) -> str:
        """Retorna a URL da API.

        Returns:
            str: A URL da API.
        """
        return self.__URL

    def get_full_url(
        self,
        path: str,
    ) -> str:
        """Retorna a URL completa da API com parâmetros.

        Args:
            path (str): A URL completa da API.

        Returns:
            str: _description_
        """
        return f"{self.url}{path}"

    def get_params(self, params: dict = {}) -> dict:
        """Retorna os parâmetros da requisição.

        Args:
            params (dict, optional): Parâmetros da requisição. O padrão é {}.

        Returns:
            dict: Os parâmetros da requisição.
        """
        return {
            "partnership": self.partnership,
            **params,
        }

    def request(
        self,
        path: str,
        params: dict = {},
    ) -> Response:
        """Faz uma requisição à API.

        Args:
            path (str): A path da requisição.
            params (dict, optional): Parâmetros da requisição. O padrão é {}.

        Returns:
            Response: A resposta da requisição.
        """
        return requests.get(
            self.get_full_url(path),
            params=params,
        )

    def theaters(
        self,
        _id: int = None,
    ) -> dict:
        """Retorna os cinemas da cidade.

        Args:
            _id (int): O ID do cinema. O padrão é None.

        Returns:
            dict: A resposta da requisição.
        """

        if _id:
            return self.request(
                f"theaters/{_id}",
                params=self.get_params(),
            ).json()
        return self.request(
            path="theaters",
            params=self.get_params(),
        ).json()

    def teathers_by_city(
        self,
    ) -> dict:
        """Retorna os cinemas da cidade.

        Returns:
            dict: A resposta da requisição.
        """
        return self.request(
            f"theaters/city/{self.city_id}/",
            params=self.get_params(),
        ).json()

    def sessions_by_theater(
        self,
        id_theater: int,
    ) -> dict:
        """Retorna as sessões de um cinema.

        Args:
            id_theater (int): O ID do cinema.

        Returns:
            dict: A resposta da requisição.
        """
        return self.request(
            f"sessions/city/{self.city_id}/theater/{id_theater}/",
            params=self.get_params(),
        ).json()

    def highlights(
        self,
    ) -> dict:
        """Retorna os destaques da cidade.

        Returns:
            dict: A resposta da requisição.
        """
        return self.request(
            f"templates/highlights/city/{self.city_id}/",
            params=self.get_params(),
        ).json()

    def now_playing(
        self,
    ) -> dict:
        """Retorna os filmes em cartaz.

        Returns:
            dict: A resposta da requisição.
        """
        return self.request(
            f"templates/nowplaying/city/{self.city_id}/",
            params=self.get_params(),
        ).json()

    def soon(
        self,
    ) -> dict:
        """Retorna os filmes em breve.

        Returns:
            dict: A resposta da requisição.
        """
        return self.request(
            f"templates/soon/city/{self.city_id}/",
            params=self.get_params(),
        ).json()
