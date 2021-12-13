#If there is an object ide having an method execute() that is it.
#We are not concern about the which class object it is, it must have execute() only.

class Pycharm:
    def execute(self):
        print("Compile")
        print("Run")

class MyEditor:
    def execute(self):
        print("Compile")
        print("Run")
        print("SpellCheck")
        print("Debug")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = Pycharm()

a = Laptop()
a.code(ide)