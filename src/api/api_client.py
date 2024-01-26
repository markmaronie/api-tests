import os

import requests
import logging


class ApiClient:
    """
    Расширение стандартного клиента requests, добавление к нему логирования
    """

    def request(self, url, headers, data, method="POST"):
        """
        Обычный запрос
        Логировать или нет задается в файле .env
        :param method: метод, который мы используем (по умолчанию POST)
        :param url: путь на домене, по которому отправляем запрос
        :param headers: заголовок запроса
        :param data: тело запроса
        """
        try:
            # if eval(os.getenv("USE_LOGS")):
            logging.info(f'{method} {url} {headers} {data}')
            return requests.request(method, url, headers=headers, data=data)
        except requests.exceptions.HTTPError as err:
            logging.info(err)

