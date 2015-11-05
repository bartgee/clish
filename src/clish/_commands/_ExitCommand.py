#

import sys

from clish import Command


class ExitCommand(Command):
    """
    Exits the interactive shell. 
    """
    def __init__(self, parent):
        self.__parent = parent

    def name(self):
        return 'exit'

    def processCommand(self, *args):
        sys.exit(0)

    def description(self):
        return 'Exit the program.'
