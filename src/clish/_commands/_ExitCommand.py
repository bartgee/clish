class _ExitCommand(InteractiveCommand):
    """
    Exits the interactive shell. 
    """
    def name(self):
        return 'exit'

    def handle_command(self, opts, args):
        sys.exit(0)

    def description(self):
        return 'Exit the program.'
