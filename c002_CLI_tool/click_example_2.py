#! /usr/bin/python3

import click

'''
такой же пример, как с argparse и кораблями
'''

    
@click.group()  # группа верхнего уровня
def cli():
    pass

@click.group(help="Команды для корабля.")  # группа для команд корабля
def ships():
    pass

cli.add_command(ships)  # добавляем команду с кораблями верхнеуровневой группе

@ships.command(help="Поднять паруса.")  # регистрация команды для группы 
def sail():
    ship_name = "Мой корабль"
    print("%s поднял паруса" % ship_name)

@ships.command(help="Получить список кораблей.")
def list_ships():
    ships = ["Стремительный", "Перехватчик", "Жемчужина"]
    print(f"Корабли: {', '.join(ships)}")

@click.command(help="Поговорить с моряком.")
@click.option("--greeting", help="Приветствие", default="Йохохо")
@click.argument('name')
def sailors(greeting, name):
    print(f"{greeting} {name}")

if __name__ == "__main__":
    cli()
    

"""
run in console:
./click_example_2.py --help
display: 
Commands:
  ships  Команды для корабля.

далее добавляю ships:
./click_example_2.py ships --help
Commands:
  list-ships  Получить список кораблей.
  sail        Поднять паруса.

./click_example_2.py ships sail
or
./click_example_2.py ships list-ships
"""
