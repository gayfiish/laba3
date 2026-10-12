class Student:
    def __init__(self, name, group, age):
        self.name = name
        self.group = group
        self.age = age

    def show_info(self):
        return (
            f"Name: {self.name}\n"
            f"Group: {self.group}\n"
            f"Age: {self.age}"
        )


if __name__ == "__main__":
    student = Student("Anastasia Potapova", "221341", 20)
    print(student.show_info())