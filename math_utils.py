class MathUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    if MathUtils.is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")