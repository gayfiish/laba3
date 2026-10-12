class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

    def show(self):
        return self.value


if __name__ == "__main__":
    counter = Counter()

    print("Initial value:", counter.show())

    counter.increment()
    print("After increment:", counter.show())

    counter.increment()
    print("After second increment:", counter.show())

    counter.decrement()
    print("After decrement:", counter.show())