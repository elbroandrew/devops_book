#! /usr/bin/python3

import fire

"""
fire package allows create CLI automatically.
"""

def greet(greeting="Привет", name="Андрей"):
  print(f"{greeting, name}")

if __name__ == '__main__':
  fire.Fire(greet)

"""
run:
./fire_example.py --name Dron
or
./fire_example.py --greeting Hello --name Dron

"""