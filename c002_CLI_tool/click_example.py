#! /usr/bin/python3

import click

"""
Click был придуман для Flask и использует декораторы.

декоратор берет функцию, внутри создаем еще ф-ию wrapper, и возвращаем ее результат
"""
# simple decorator example

def say_name():
  print("John")

def decorator_function(wrapped_func):

  def wrapper():
    print("Hello")
    wrapped_func()

  return wrapper

f = decorator_function(say_name)
# f()
# decorator with argument:
def decorator_with_arg(name: str):
  def decorator_function2(wrapped_func):
    def wrapper():
      print("Hello")
      wrapped_func(name)
    return wrapper
  return decorator_function2

@decorator_with_arg("Bill")
def say_name2(name: str):
  print(name)

# say_name2()

# CLICK example begins here
'''
This means that you tie your flags and options directly to the
parameters of the functions that they expose. You can create a simple
command-line tool from your functions using click command and
option functions as decorators before your function.
'''

@click.command()
@click.option('--greeting', default="Hi", help="How do you want to greet")
@click.option('--name', default="Andrew", help="Who to greet")
def greet(greeting, name):
  print(f"{greeting, name}")

if __name__ == '__main__':
  greet()

