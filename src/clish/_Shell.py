#

from __future__ import print_function

import shlex
import logging

from clish.commands import HelpCommand, ExitCommand


class Shell(object):
    def __init__(self, banner="Welcome to Interactive Shell", prompt=" >>> "):
        self.__log = logging.getLogger('clish.shell')
        #
        self.__banner = banner
        self.__prompt = prompt
        self.__commands = {}
        #
        self.add_command(HelpCommand(parent=self))
        self.add_command(ExitCommand(parent=self))

    def commands(self):
        """ Returns commands
        """
        return self.__commands

    def add_command(self, command):
        command_name = command.name()
        if command_name in self.__commands:
            raise Exception('Command {command_name!r} already exist!'.format(command_name=command_name))
        #
        self.__commands[command_name] = command

    def processLine(self, command_line):
        """ Write parser there
        """
        # Get command
        result = []
        #
        try:
            result = shlex.split(command_line, False, True)
            self.__log.debug("Parse string is {args!r}".format(args=args))
        except Exception as err:
            self.__log.exception(err)
        #
        return result

    def processInput(self, command_line):
        command_line = command_line.strip() # TODO - switch to sheel parser method ...
        #
        args = self.processLine(command_line)
        if len(args) > 0:
            command_name = args[0]
            command_args = args[1:]
        else:
            command_name = command_line
            command_args = []
        #
        command = self.__commands.get(command_name)
        if command is not None:
            args = []
            try:
                command.processCommand(*command_args)
            except Exception as err:
                self.__log.exception("Exception occurred while processing command.")
        else:
            print('Unknown command: {command_name!r}. Type "help" for a list of commands.'.format(command_name=command_name))


    def run(self):
        print(self.__banner)
        print()
        print('Type "help" at any time for a list of commands.')
        self.__running = True
        while self.__running is True:
            try:
                print()
                command_line = raw_input(self.__prompt)
            except KeyboardInterrupt as err:
                break
            except EOFError as err:
                break
            #
            self.processInput(command_line)
