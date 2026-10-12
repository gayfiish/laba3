
import unittest

from counter import Counter
from student import Student


class TestCounter(unittest.TestCase):
    def test_initial_value(self):
        counter = Counter()
        self.assertEqual(counter.show(), 0)

    def test_increment(self):
        counter = Counter()
        counter.increment()
        self.assertEqual(counter.show(), 1)

    def test_decrement(self):
        counter = Counter()
        counter.increment()
        counter.decrement()
        self.assertEqual(counter.show(), 0)

    def test_reset(self):
        counter = Counter()
        counter.increment()
        counter.increment()

        counter.reset()

        self.assertEqual(counter.show(), 0)


class TestStudent(unittest.TestCase):
    def test_show_info(self):
        student = Student("Test Student", "100", 18)

        expected = (
            "Name: Test Student\n"
            "Group: 100\n"
            "Age: 18"
        )

        self.assertEqual(student.show_info(), expected)


if __name__ == "__main__":
    unittest.main()