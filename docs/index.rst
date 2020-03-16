ty_cli: A very opinionated command line parser
==============================================

`ty_cli` is an extremely opinionated command line parsing
library. Because it decides everything for you, its interface is dead
simple. Its particularly good if you need a quick CLI interface with
almost zero effort.

It is based on and requires type annotations (à la mypy). Uses Python
3.8 or above.

Here is a first example::


  from typing import Optional

  from ty_cli import cli


  @cli
  def hello_complex(name: str, *, birth_place: str, age: Optional[int] = None) -> None:
      print(f"Hello {name}, you were born in {birth_place}")
      if age:
          print(f"You are {age} years old")


  if __name__ == "__main__":
      hello_complex()

.. highlight:: shell

For example like this::


  python hello.py Randi --birth-place Manchester
  Hello Randi, you were born in Manchester

  python hello.py Randi --birth-place Manchester --age 4
  Hello Randi, you were born in Manchester
  You are 4 years old

This would **not** work as `four` is not an integer::
  
  python hello.py Randi --birth-place Manchester --age four


You could also request help::

  python hello.py --help

  
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   development
   api/modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
