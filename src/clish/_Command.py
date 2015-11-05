#

class Command(object):

    @property
    def name(self):
        raise NotImplementedError()

    def processCommand(self, *args):
        raise NotImplementedError()

    @property
    def description(self):
        raise NotImplementedError()
