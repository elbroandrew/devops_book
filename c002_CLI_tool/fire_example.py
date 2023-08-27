#! /usr/bin/python3

import fire

"""
fire package allows create CLI automatically.
"""

# def greet(greeting="Привет", name="Андрей"):
#   print(f"{greeting, name}")

# if __name__ == '__main__':
#   fire.Fire(greet)

"""
run:
./fire_example.py --name Dron
or
./fire_example.py --greeting Hello --name Dron

"""

# fire CLI tool with Class example with Ships

class Ships:
    
    def sail(self):
        ship_name = "Мой корабль"
        print("%s поднял паруса" % ship_name)

    def list_ships(self):
        ships = ["Стремительный", "Перехватчик", "Жемчужина"]
        print(f"Корабли: {', '.join(ships)}")

def sailors(greeting, name):
    print(f"{greeting} {name}")

class Cli:
    
    def __init__(self) -> None:
        self.sailors = sailors
        self.Ships = Ships()

if __name__ == "__main__":
    fire.Fire(Cli)

"""
run:
./fire_example.py Ships list-ships
./fire_example.py sailors Hello John
"""

