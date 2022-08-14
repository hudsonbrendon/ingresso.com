from requests.models import Response

from ingresso import Ingresso, __version__


def test_version():
    assert __version__ == "0.1.0"


class TestIngresso:
    def test_init(
        self,
        ingresso,
    ):
        assert isinstance(
            ingresso,
            Ingresso,
        )

    def test_city_id(
        self,
        ingresso,
    ):
        assert ingresso.city_id == 48

    def test_partnership(
        self,
        ingresso,
    ):
        assert ingresso.partnership == "cinepolis"

    def test_url(
        self,
        ingresso,
    ):
        assert ingresso.url == "https://api-content.ingresso.com/v0/"

    def test_get_full_url(
        self,
        ingresso,
    ):
        assert ingresso.get_full_url("cinemas") == "https://api-content.ingresso.com/v0/cinemas"

    def test_request(
        self,
        ingresso,
    ):
        assert isinstance(
            ingresso.request("cinemas"),
            Response,
        )

    def test_theaters(
        self,
        requests_mock,
        ingresso,
        theaters,
    ):
        url = f'{ingresso.get_full_url(path="theaters")}?partnership={ingresso.partnership}'
        requests_mock.get(
            url=url,
            json=theaters,
        )
        assert theaters == ingresso.theaters()

    def test_theaters_with_id(
        self,
        requests_mock,
        ingresso,
        theater,
    ):
        url = f'{ingresso.get_full_url(path="theaters/1005")}?partnership={ingresso.partnership}'
        requests_mock.get(
            url=url,
            json=theater,
        )
        assert theater == ingresso.theaters(1005)

    def test_theaters_city(
        self,
        requests_mock,
        ingresso,
        theaters_by_city,
    ):
        url = f'{ingresso.get_full_url(path=f"theaters/city/{ingresso.city_id}/")}?partnership={ingresso.partnership}'
        requests_mock.get(
            url=url,
            json=theaters_by_city,
        )
        assert theaters_by_city == ingresso.teathers_by_city()

    def test_sessions_by_theater(
        self,
        requests_mock,
        ingresso,
        sessions_by_theater,
    ):
        url = f'{ingresso.get_full_url(path=f"sessions/city/{ingresso.city_id}/theater/1005/")}?partnership=cinepolis'
        requests_mock.get(
            url=url,
            json=sessions_by_theater,
        )
        assert sessions_by_theater == ingresso.sessions_by_theater(1005)

    def test_highlights(
        self,
        requests_mock,
        ingresso,
        highlights,
    ):
        url = f'{ingresso.get_full_url(path=f"templates/highlights/city/{ingresso.city_id}/")}?partnership={ingresso.partnership}'
        requests_mock.get(
            url=url,
            json=highlights,
        )
        assert highlights == ingresso.highlights()

    def test_now_playing(
        self,
        requests_mock,
        ingresso,
        now_playing,
    ):
        url = f'{ingresso.get_full_url(path=f"templates/nowplaying/city/{ingresso.city_id}/")}?partnership={ingresso.partnership}'
        requests_mock.get(
            url=url,
            json=now_playing,
        )
        assert now_playing == ingresso.now_playing()

    def test_soon(
        self,
        requests_mock,
        ingresso,
        soon,
    ):
        url = f'{ingresso.get_full_url(path=f"templates/soon/city/{ingresso.city_id}/")}?partnership={ingresso.partnership}'
        requests_mock.get(
            url=url,
            json=soon,
        )
        assert soon == ingresso.soon()
