import pytest
import json
import time

from datetime import date, timedelta
from src.api.api_client import ApiClient
from src.assertions.assertion_base import Asserts
from src.utils.data_generator import DataGenerator


class TestBook:
    """Набор тестов по букингу"""
    @pytest.mark.book
    @pytest.mark.regress
    @pytest.mark.testrail(id="C123")
    def test_normal_book_hotel(self):
        """Тест букинга на API V3 бронирование картой на обычный договор"""

        client = ApiClient()
        asserts = Asserts()

        # шаг 1 хотел пейдж
        url = "http://dapi.p.ostrovok.ru/api/b2b/v3/search/hp"

        checkin = str(date.today() + timedelta(days=10))
        checkout = str(date.today() + timedelta(days=12))

        payload = json.dumps({
            "checkin": checkin,
            "checkout": checkout,
            "residency": "ru",
            "language": "ru",
            "guests": [
                {
                    "adults": 2,
                    "children": []
                }
            ],
            "id": "holiday_inn_express_moscow_baumanskaya",
            "currency": "RUB",
            "timeout": 200
        })
        headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Basic NTgyMTpkYWVkYjM1NC1jNjIwLTQxOWYtOGQyNy0zYWMzYmIyNjIyOGM=',
          'Cookie': 'uid=rBEAC2Uv6sBijABOAwMFAg==; uid=rBEAC2VtybJ19gBVAwMKAg=='
        }
        response = client.request(url, headers, payload)

        asserts.assert_response_code(response.status_code)
        asserts.assert_more(60.0, response.elapsed.total_seconds())
        # TODO Возможно добавить доп проверки
        try:
            for i in response.json()["data"]["hotels"][0]["rates"]:
                for k in i["payment_options"]["payment_types"]:
                    if k["type"] == "now":
                        hotel_book_hash = i["book_hash"]
                        raise StopIteration
            else:
                raise AssertionError('Нет подходящих рейтов для отеля с типом оплаты now') from None
        except StopIteration:
            pass

        # шаг 2 букинг форма
        url = "https://partner.p.ostrovok.ru/api/b2b/v3/hotel/order/booking/form/"

        partner_order_id = DataGenerator().generate_order_id()

        payload = json.dumps({
            "partner_order_id": partner_order_id,
            "book_hash": hotel_book_hash,
            "language": "ru",
            "user_ip": "82.29.0.86"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic NTgyMTpkYWVkYjM1NC1jNjIwLTQxOWYtOGQyNy0zYWMzYmIyNjIyOGM=',
            'Cookie': 'uid=rBEABl3NKlRFGAAhAwS7Ag==; uid=rBEALmUtbjGwPwAVBK+lAg==; uid=rBEALmWBjGIWhgAVA5q4Ag=='
        }
        response = client.request(url, headers, payload)

        asserts.assert_response_code(response.status_code)
        asserts.assert_more(60.0, response.elapsed.total_seconds())
        asserts.assert_equal(response.json()["status"], "ok")
        object_id = str(response.json()["data"]["item_id"])
        amount = response.json()["data"]["payment_types"][0]["amount"]

        # шаг 3 оплата
        url = "https://payota.p.ostrovok.ru/api/public/v1/manage/init_partners"

        pay_uuid = DataGenerator().generate_uuid()
        init_uuid = DataGenerator().generate_uuid()

        payload = json.dumps({
            "object_id": object_id,
            "pay_uuid": pay_uuid,
            "init_uuid": init_uuid,
            "user_last_name": "LastName",
            "cvc": "123",
            "is_cvc_required": True,
            "credit_card_data_core": {
                "year": "24",
                "card_number": "4242424242424242",
                "card_holder": "HAN SOLO",
                "month": "12"
            },
            "user_first_name": "Name"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic NTgyMTpkYWVkYjM1NC1jNjIwLTQxOWYtOGQyNy0zYWMzYmIyNjIyOGM='
        }
        response = client.request(url, headers, payload)

        asserts.assert_response_code(response.status_code)
        asserts.assert_more(60.0, response.elapsed.total_seconds())
        asserts.assert_equal(response.json()["status"], "ok")

        # шаг 4 оплата
        url = "https://partner.p.ostrovok.ru/api/b2b/v3/hotel/order/booking/finish/"

        payload = json.dumps({
            "arrival_datetime": checkin + "T15:00:00",
            "book_timeout": None,
            "ignore_group_booking_error": None,
            "language": "ru",
            "partner": {
                "amount_sell_b2b2c": None,
                "partner_order_id": partner_order_id
            },
            "payment_type": {
                "amount": amount,
                "currency_code": "RUB",
                "pay_uuid": pay_uuid,
                "init_uuid": init_uuid,
                "type": "now"
            },
            "return_path": "https://link.konsierge.com/A2kC0",
            "rooms": [
                {
                    "guests": [
                        {
                            "age": None,
                            "first_name": "Гурам",
                            "gender": None,
                            "is_child": None,
                            "last_name": "Тестовыйтаймаут"
                        },
                        {
                            "age": None,
                            "first_name": "Гурам",
                            "gender": None,
                            "is_child": None,
                            "last_name": "Тестовыйтаймаут"
                        }
                    ]
                }
            ],
            "supplier_data": {
                "email": "grechka@mail.ru",
                "first_name_original": "Guram",
                "last_name_original": "Galtsev",
                "phone": "+78005556677"
            },
            "user": {
                "comment": None,
                "email": "grechka@mail.ru",
                "phone": "+78005556677"
            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic NTgyMTpkYWVkYjM1NC1jNjIwLTQxOWYtOGQyNy0zYWMzYmIyNjIyOGM=',
            'Cookie': 'uid=rBEALmUtbjGwPwAVBK+lAg==; uid=rBEALmWBjGIWhgAVA5q4Ag=='
        }
        response = client.request(url, headers, payload)

        asserts.assert_response_code(response.status_code)
        asserts.assert_more(60.0, response.elapsed.total_seconds())
        asserts.assert_equal(response.json()["status"], "ok")

        # Шаг 5 проверить что оплата прошла хорошо
        url = "https://partner.p.ostrovok.ru/api/b2b/v3/hotel/order/booking/finish/status/"

        payload = json.dumps({
            "partner_order_id": partner_order_id
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic NTgyMTpkYWVkYjM1NC1jNjIwLTQxOWYtOGQyNy0zYWMzYmIyNjIyOGM=',
            'Cookie': 'uid=rBEALmUtbjGwPwAVBK+lAg==; uid=rBEALmWBjGIWhgAVA5q4Ag=='
        }


        t = time.time()
        while time.time() - t < 120:
            response = client.request(url, headers, payload)
            print(response.text)
            asserts.assert_response_code(response.status_code)
            asserts.assert_more(60.0, response.elapsed.total_seconds())
            if response.json()["data"]["percent"] == 100:
                asserts.assert_equal(response.json()["status"], "ok")
                break
            time.sleep(10)
        else:
            raise AssertionError('Ордер не был обработан за отведенное время') from None