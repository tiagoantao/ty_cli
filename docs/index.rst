ty_cli: A very opinionated command line parser
==============================================

`ty_cli` is an extremely opinionated command line parsing
library. Because it decides everything for you, its interface is dead
simple. Its particularly good if you need a quick CLI interface with
almost zero effort.

It is based on and requires type annotations (à la mypy). Uses Python
3.8 or above.


Simple examples
---------------

Single command example
^^^^^^^^^^^^^^^^^^^^^^

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


Multi command example
^^^^^^^^^^^^^^^^^^^^^

.. highlight:: python

You can have multiple commands on a file::

  from typing import Optional

  from ty_cli import cli


  @cli
  def greet(*, first_name: str, last_name: Optional[str]) -> None:
      if last_name is None:
          print(f"Howdy {first_name}!")
      else:
          print(f"Greetings {first_name} {last_name}")


  @cli
  def bye(*, name: str) -> None:
      print(f"Bye {name}!")


  if __name__ == "__main__":
      cli()

               
.. highlight:: shell

This can be used as follows::

  python multi_hello.py greet --first-name Randi
  Howdy Randi!

  python multi_hello.py greet --first-name Randi --last-name Taira
  Greetings Randi Taira
  
  python multi_hello.py bye --name Randi
  Bye Randi!


You can find more examples_ in the repository.

Installation
------------

Via pip: `pip install ty_cli`

Via conda: `conda install -c conda-forge ty_cli`


Deep dive
---------

There is actually not much to dive in, as the library is trivial to
use and has strict rules. Durrently there is **nothing** you can
parametrize. Here is the gist of things:

#. You need to decorate all functions to be accessible with the
   decorator `cli`
#. If you are on the main block (`if __name__ == '__name__'`) you
   should call... `cli` with no parameters (the function is kinda
   polymorphic)
#. Types are enforced: If a parameter has type `int` the CLI will only
   accept integers
#. Function parameters before an `*` are positional parameters
   **unless** they have defaults, then they are named
#. The same for anything typed `Optional`
#. Parameters after the `*` are always named (like Python). They are
   optional if marked `Optional` or have a default.

You can have a single command per file, or multiple.

If the rules above seem to abstract, check the examples_. In practice
this stuff is very easy.

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

.. _examples: https://github.com/tiagoantao/ty_cli/tree/master/examples
