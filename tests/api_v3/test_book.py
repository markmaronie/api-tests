from http import HTTPStatus
import pytest
import requests
import json
from src.assertions.assertion_base import assert_status_code
from dynaconf import settings as cfg
import logging


@pytest.mark.book
class TestBook:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.regress
    def test_normal_book_hotel(self):
        url = f"{cfg.BASE_URL}api/b2b/v3/search/hp"

        payload = json.dumps({
            "checkin": "2024-03-19",
            "checkout": "2024-03-20",
            "language": "en",
            "currency": "RUB",
            "residency": "ru",
            "guests": [
                {
                    "adults": 2
                }
            ],
            "id": "swissotel_krasnye_holmy",
            "timeout": 2
        })
        headers = {
            'Content-Type': 'application/json',
            'X-Include-Debug': '1',
            'Authorization': 'Basic MTMwNDowMjVjMmVmMi1kMzQ5LTQ4ZjMtOWMzYy01OTZhYTA5YjgyN2I=',
            'Cookie': 'uid=rBEAC2VtybJ19gBVAwMKAg=='
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert_status_code(response, HTTPStatus.OK)
        # TODO добавить проверку времени ответа
        # TODO добавить проверку схемы ответа
        # TODO сравнить ответ с эталоном
        # TODO взять book_hash из ответа
        logging.info(response.text)
