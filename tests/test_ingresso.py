from requests.models import Response

from ingresso import Ingresso, __version__


def test_version():
    assert __version__ == "0.1.0"


class TestIngresso:
    def test_init(self):
        ingresso = Ingresso(42, "cinepolis")
        assert isinstance(ingresso, Ingresso)

    def test_city_id(self):
        ingresso = Ingresso(42, "cinepolis")
        assert ingresso.city_id == 42

    def test_partnership(self):
        ingresso = Ingresso(42, "cinepolis")
        assert ingresso.partnership == "cinepolis"

    def test_get_url(self):
        ingresso = Ingresso(42, "cinepolis")
        assert (
            ingresso.get_url("cinemas") == "https://api-content.ingresso.com/v0/cinemas"
        )

    def test_request(self):
        ingresso = Ingresso(42, "cinepolis")
        assert isinstance(ingresso._request("cinemas"), Response)
