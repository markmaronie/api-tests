from datetime import datetime


class Asserts:
    """ Класс для проверок и всего, связанного с ними """

    def assert_response_code(self, received):
        """Проверка, что в ответе мы получили нужный код 200 статус ОК"""
        if received != 200:
            raise AssertionError('Не верный код ответа. Получили: "{0}", Ожидали: "{1}"'
                                 .format(str(received), str(200))) from None

    def assert_equal(self, received, expected):
        """Сравнение, что одно значение эквивалентно другому"""
        if str(received) != str(expected):
            raise AssertionError('Значение не совпадают. Получили: "{0}", Ожидали: "{1}"'
                                 .format(str(received), str(expected))) from None

    def assert_not_equal(self, received, expected):
        """Сравнение, что одно значение не равно другому"""
        if str(received) == str(expected):
            raise AssertionError('Значение совпадают. Получили: "{0}", Ожидали НЕ: "{1}"'
                                 .format(str(received), str(expected))) from None

    def assert_element_in_list(self, received, expected):
        """Сравнение, что значение входит в список"""
        if str(received) in expected:
            raise AssertionError('Значения не совпадают. Получили: "{0}", Ожидали: "{1}"'
                                 .format(str(received), str(expected))) from None

    def assert_list_in_list(self, received, expected):
        """Сравнение, что один список входит в другой список"""
        list_errors = []
        for element in received:
            if element not in expected:
                list_errors.append(element)
        if len(list_errors) != 0:
            raise AssertionError('Значения не совпадают. Получили: "{0}", Ожидали: "{1}". '
                                 'Значения, которые не входят в список: "{2}"'
                                 .format(str(received), str(expected), str(list_errors))) from None

    def assert_list_equal(self, received, expected):
        """Сравнение, что один список эквивалентно равен другому"""
        received.sort()
        expected.sort()
        list_errors = []
        if received != expected:
            for element in expected:
                if element not in received:
                    list_errors.append(element)
            raise AssertionError('Значения не совпадают. Получили: "{0}", Ожидали: "{1}". '
                                 'Значения, которые отсутствуют в ожидаемом списке: "{2}"'
                                 .format(str(received), str(expected), str(list_errors))) from None

    def assert_more(self, received, expected):
        """Сравнение, что одно значение больше другого"""
        if received <= expected:
            raise AssertionError('Значение: ' + str(received) + ' <= чем ' + str(expected)) from None

    def assert_in_str(self, received, expected):
        """Сравнение, что значение входит в строку"""
        if str(received) not in str(expected):
            raise AssertionError('Значение: ' + str(received) + ' не входит в ' + str(expected)) from None