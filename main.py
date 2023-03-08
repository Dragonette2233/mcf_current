class Vampire:
    def __init__(self, name, age) -> None:
        self.name: str = name
        self.age: int = age

    def vamp_info(self):
        print(f'Name: {self.name} | Age: {self.age}')