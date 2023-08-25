#! /usr/bin/python3

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
f()
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

say_name2()
