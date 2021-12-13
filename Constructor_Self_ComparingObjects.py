#Constructor
#In heap memory whenever we create an object it will be stored
#But how much memory it will take depends on the no of vars and size of each variable
#To allocate memory constructor is responssible.

# Constructor_Self_ComparingObjects() is an constructor here which will call __init__ automatically.

#Self
#It a pointer which will help us objects present i.e referring to object (current instance)
class Constructor_Self_ComparingObjects:

    def __init__(self):
        self.name ="Harshal"
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            print("They are same.")
        else:
            print("They are different.")


c1 = Constructor_Self_ComparingObjects()
c2 = Constructor_Self_ComparingObjects()

c1.update()
print(c1.age)
print(c2.age)
c1.compare(c2)
