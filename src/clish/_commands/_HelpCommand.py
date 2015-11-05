#

from clish import Command


class _HelpCommand(Command):
    """
    Prints a list of available commands and their descriptions, or the help
    text of a specific command. Requires a list of the available commands in
    order to display text for them. 
        
    @ivar commands: A dictionary of available commands, bound to L{InteractiveShell.commands}
    @type commands: C{dict}
    """
    def __init__(self, commands):
        """
        Constructor function for L{_HelpCommand}.
        
        @param commands: A dictionary of available commands, usually L{InteractiveShell.commands}
        @type commands: C{dict}
        """
        self.commands = commands

    def name(self):
        return 'help'

    def processCommand(self, *args):
        """
        Prints a list of available commands and their descriptions if no
        argument is provided. Otherwise, prints the help text of the named
        argument that represents a command. Does not throw an error if the
        named argument doesn't exist in commands, simply prints a warning.
            
        @param opts: Will be an empty dictionary
        @type opts: C{dict}
        @param args: The raw string passed to the command, either a command or nothing
        @type args: C{list}
            
        @return: Returns nothing, sends messages to stdout
        @rtype: None
        """
            
        if len(args) == 0:
            self.do_command_summary( )
            return

        if args[0] not in self.commands:
            print 'No help available for unknown command "%s"' % args[0]
            return
            
        print self.commands[args[0]].get_help_message( )
            

    def do_command_summary(self):
        """
        If no command is given to display help text for specifically, then
        this helper method is called to print out a list of the available
        commands and their descriptions. Iterates over the list of commands,
        and gets their summary from L{InteractiveCommand.get_short_description}
            
        @return: Returns nothing, sends messages to stdout
        @rtype: C{None}
        """
        print 'The following commands are available:\n'

        cmdwidth = 0
        for name in self.commands.keys( ):
            if len(name) > cmdwidth:
                cmdwidth = len(name)

        cmdwidth += 2
        for name in sorted(self.commands.keys( )):
            command = self.commands[name]

            if name == 'help':
                continue
                
            print '  %s   %s' % (name.ljust(cmdwidth), command.description())
                

    def description(self):
        return 'Show main help'
