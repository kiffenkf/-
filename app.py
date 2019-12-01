from dispatcher import Dispacher

if __name__ == '__main__':
    print('welcome to www.kiffen.com')
    dis = Dispacher()
    dis.reg('ls', lambda: print('ls'))
    dis.run()
