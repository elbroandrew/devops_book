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
# and for much easier approach just do:
@decorator_function
def say_name2():
  print("Bill")

say_name2()
