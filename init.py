#To initialise the variables we need to use __init__ fn inside the class.
#In 'init' 'self' is coming automatically so its compulsory to have those args.
#'init' is constructor.Its a function which can be executed automatically.
import self as self

class init:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is: ", self.cpu, self.ram)

com1 = init('i5',16)
com2 = init('Rayen',8)

com1.config()
com2.config()


