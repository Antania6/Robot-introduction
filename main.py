# Define a Robot class
class Robot:
    def __init__(self, name):
        self.name = name

    def introduce_yourself(self):
        print(f"Hello, my name is {self.name}!")

# Create objects for Tom and Jerry
tom = Robot("Tom")
jerry = Robot("Jerry")

# Have Tom and Jerry introduce themselves
tom.introduce_yourself()
jerry.introduce_yourself()