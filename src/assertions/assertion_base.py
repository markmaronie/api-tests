def assert_status_code(response, expected_code):
    """
    сравнивает код ответа от сервера с ожидаемым
    :param response: полученный от сервера ответ
    :param expected_code: ожидаемый код ответа
    """
    assert expected_code == response.status_code
