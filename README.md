clish
=====

[![Documentation Status](https://readthedocs.org/projects/clish/badge/?version=latest)](http://clish.readthedocs.org/en/latest/?badge=latest)

Command Line Shell Framework is application framework to create application with shell interactive interface.

```python
#!/usr/bin/python

import os
import time

from clish import Command, Shell


class Application(object):
    def __init__(self):
        self.client = None

    def run(self):
        shell = Shell(banner="Welcome to CLI Shell v0.1", prompt="clish> ")
        shell.run()


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
```

This application will return follow interactive console:


```
Welcome to CLI Shell v0.4

Type "help" at any time for a list of commands.

>>> hello
Unknown command: "hello". Type "help" for a list of commands.

>>> help
The following commands are available:

  exit     Exit the program.

>>> exit
```
