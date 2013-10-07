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
