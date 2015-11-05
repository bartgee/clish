#

class Shell(object):
    def __init__(self, banner="Welcome to Interactive Shell", prompt=" >>> "):
        self.banner = banner
        self.prompt = prompt
        self.commands = { }
        self.add_command(self._HelpCommand(self.commands))
        self.add_command(self._ExitCommand())

    def add_command(self, command):
        command_name = command.name()
        if command_name in self.commands:
            raise Exception('Command {command_name!r} already exist!'.format(command_name=command_name))
        #
        self.commands[command_name] = command

    def processInput(self, command_line):
        command_line = command_line.strip() # TODO - switch to sheel parser method ...

        # Get command
        command_args = ""
        if " " in command_line:
            command_line_index = command_line.index(" ")
            command_name = command_line[:command_line_index]
            command_args = command_line[command_line_index+1:]
        else:
            command_name = command_line

        # Show message when no command
        if not command_name in self.commands:
            print('Unknown command: {command_name!r}. Type "help" for a list of commands.'.format(command_name=command_name))
            return

        command = self.commands[command_name]

        args = []
        # TODO - parse parameters in line ...
        try:
            command.processCommand(*args)
        except Exception as err:
            print("Exception occurred while processing command.")
            traceback.print_exc( )

    def run(self):
        print(self.banner)
        print()
        print('Type "help" at any time for a list of commands.')
        self.__running = True
        while self.__running is True:
            try:
                print()
                command_line = raw_input(self.prompt)
            except KeyboardInterrupt as err
                break
            except EOFError as err:
                break
            #
            self.processInput(command_line)
