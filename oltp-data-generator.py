from numpy import random as rnd
from faker import Faker
from datetime import UTC


class OLTPGenerator:


    def __init__(self) -> None:
        """Инициализирует генератор."""
        self.fake = Faker("ru_RU")
        self.segments = ["Bronze", "Silver", "Gold"]


    def customer_generator(self, number: int) -> list[tuple]:
        """Создаёт список кортежей клиентов заданного количества."""
        # Создаём список клиентов
        customers = []

        # Создаём кортеж клиента
        for _ in range(number):

            name = self.fake.name()  # имя
            email = self.fake.email()  # почта
            phone = self.fake.phone_number()  # телефон
            city = self.fake.city()  # Город

            generator = rnd.default_rng(42)

            # Выбираем сегмент случайно с разными весами
            segment = generator.choice(self.segments, p=[0.7, 0.25, 0.05]).item()  # Сегмент: золото, серебро, бронза
            loyalty_card = self.fake.bothify(text="LC-########", letters="ABCDE")  # номер карты лояльности
            birth_date = self.fake.date_of_birth(minimum_age=18, maximum_age=70)  # дата рождения
            reg_date = self.fake.date_time_between(start_date="-2y", end_date="now", tzinfo=UTC)  # дата регистрации
            upd_date = self.fake.date_time_between(start_date=reg_date, end_date="now", tzinfo=UTC)  # дата обновления

            customer = (
                name, email, phone, city, segment, loyalty_card, birth_date, reg_date, upd_date
            )
            customers.append(customer)
        return customers



if __name__ == "__main__":
    test = OLTPGenerator()

    client = test.customer_generator(1)
    print(client)
