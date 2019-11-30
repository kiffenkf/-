
class Dispacher:
    cmds = {}

    def reg(self, cmd, fn):
        self.cmds[cmd] = fn

    def run(self):
        pass





