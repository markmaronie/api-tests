import string
import random
import uuid


class DataGenerator:
    """
    Генерация необходимых рандомных данных
    """

    @staticmethod
    def generate_order_id():
        """
        Гененрация рандомного id заказа для букинг формы
        """

        return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])

    @staticmethod
    def generate_uuid():
        """
        Гененрация рандомного uuid
        """

        return str(uuid.uuid4())