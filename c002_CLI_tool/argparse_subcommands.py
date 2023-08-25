#! /usr/bin/python3
import argparse

"""
короче subparser это ф-ия, которую можно вызвать и даже одну за другой
"""

def sail():
    ship_name = "Мой корабль"
    print("%s поднял паруса" % ship_name)

def list_ships():
    ships = ["Стремительный", "Перехватчик", "Жемчужина"]
    print(f"Корабли: {', '.join(ships)}")

def greet(greeting, name):
    print(f"{greeting} {name}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="New CLI program")

    parser.add_argument('--twice', '-t',  # - or -- means the args are optional (всё до help будет относиться к одному аргументу)
                        help="Do it twice.",  
                        action='store_true'  # make it boolean                        
                        )
    
    subparsers = parser.add_subparsers(dest="func")  # имя объекта сабпарсера, который будет ф-ии содержать
    ship_parser = subparsers.add_parser('ships',
                                        help="Команды для корабля")
    ship_parser.add_argument('command',
                             choices=["list", "sail"])
    
    sailor_parser = subparsers.add_parser("sailors",
                                          help="Поговорить с моряком.")
    sailor_parser.add_argument("name",
                               help="Имя моряка")
    
    sailor_parser.add_argument("--greeting", "-g",
                               help="Приветствие",
                               default="Йохохо"
                               )

    args = parser.parse_args()
    if args.func == "sailors":
        greet(args.greeting, args.name)
    elif args.command == "list":
        list_ships()
    else:
        sail()