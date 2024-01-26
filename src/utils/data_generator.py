import string
import random
import uuid


class DataGenerator:
    """
    Генерация необходимых рандомных данных
    """

    def generate_order_id(self):
        """
        Гененрация рандомного id заказа для букинг формы
        """

        return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])

    def generate_uuid(self):
        """
        Гененрация рандомного uuid
        """

        return str(uuid.uuid4())