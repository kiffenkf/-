
class Dispacher:
    cmds = {}

    def reg(self, cmd, fn):
        self.cmds[cmd] = fn

    def run(self):
        while True:
            cmd = input('>>')
            if cmd.strip() == 'quit':
                break
            self.cmds.get(cmd, lambda : print('unknown cmd'))()




