#

from __future__ import print_function

import shlex
import logging

from clish import Namespace
from clish.commands import HelpCommand, ExitCommand


class Shell(object):
    def __init__(self, banner="Welcome to Interactive Shell", prompt=" >>> "):
        self.__log = logging.getLogger('clish.shell')
        #
        namespace = Namespace()
        #
        self.__banner = banner
        self.__prompt = prompt
        self.__commands = {}
        self.__namespace = namespace
        self.__namespaces = {}
        #
        namespace.attachCommand(HelpCommand(parent=self))
        namespace.attachCommand(ExitCommand(parent=self))

    def namespace(self):
        return self.__namespace

    def createNamespace(self, name):
        namespace = Namespace()
        self.__namespaces[name] = namespace
        return namespace

    def attachNamespace(self, name, namespace):
        self.__namespaces[name] = namespace

    def switchNamespace(self, name):
        namespace = self.__namespaces.get(name)
        if namespace is None:
            raise ValueError("No namespace")
        self.__namespace = namespace

    def commands(self):
        """ Returns commands
        """
        return self.__namespace.commands()

    def attachCommand(self, command):
        self.__namespace.attachCommand(command)

    def run(self):
        print(self.__banner)
        print()
        print('Type "help" at any time for a list of commands.')
        self.__running = True
        while self.__running is True:
            try:
                print()
                prompt = self.__namespace.prompt()
                command_line = raw_input(prompt)
            except KeyboardInterrupt as err:
                break
            except EOFError as err:
                break
            #
            self.__namespace.processInput(command_line)
