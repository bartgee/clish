#

import apipkg
apipkg.initpkg(__name__, {
    'commands': {
        "HelpCommand": "clish._commands._HelpCommand:HelpCommand",
        "ExitCommand": "clish._commands._ExitCommand:ExitCommand",
    },

    'Command'  : "clish._Command:Command",
    'Shell'    : "clish._Shell:Shell",

    # DEPRECATE NAMES
    'InteractiveCommand' : "clish._Command:Command",
    'InteractiveShell'   : "clish._Shell:Shell",
})
