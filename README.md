clish
=====

Command Line Shell Framework is application framework to create application with shell interactive interface.

```python
#!/usr/bin/python

import os
import time

from clish import InteractiveCommand, InteractiveShell


class Application(object):
    def __init__(self):
        self.client = None

    def run(self):
        shell = InteractiveShell(banner="Welcome to CLI Shell v0.1", prompt="clish> ")
        shell.run()


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
```

This application will return follow interactive console:


```
Welcome to CLI Shell v0.1

Type "help" at any time for a list of commands.

clish> hello
Unknown command: "hello". Type "help" for a list of commands.

clish> help
The following commands are available:

  exit     Exit the program.

clish> exit
```
