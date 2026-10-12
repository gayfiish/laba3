class PriceStrategy:
    def calculate(self, price):
        raise NotImplementedError


class RegularPrice(PriceStrategy):
    def calculate(self, price):
        return price


class DiscountPrice(PriceStrategy):
    def __init__(self, discount):
        self.discount = discount

    def calculate(self, price):
        return price * (1 - self.discount / 100)


class PriceCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate_price(self, price):
        return self.strategy.calculate(price)


if __name__ == "__main__":
    price = 1000

    calculator = PriceCalculator(RegularPrice())
    print("Regular price:", calculator.calculate_price(price))

    calculator.set_strategy(DiscountPrice(20))
    print("Price with 20% discount:", calculator.calculate_price(price))