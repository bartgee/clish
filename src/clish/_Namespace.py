#

import shlex
import logging


class Namespace(object):
    def __init__(self, prompt=">>> "):
        self.__log = logging.getLogger('clish.namespace')
        self.__prompt = prompt
        self.__commands = {}

    def prompt(self):
        return self.__prompt

    def attachCommand(self, command):
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
        except Exception as err:
            self.__log.exception(err)
        #
        return result

    def processInput(self, command_line):
        command_line = command_line.strip()
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

    def commands(self):
        """ Returns commands
        """
        return self.__commands
