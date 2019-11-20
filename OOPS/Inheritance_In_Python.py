# Inheritance :
"""
Inheritance is a way of creating new class for using details of existing 
class without modifying it. 

The newly formed class is a derived class (or child class). 

Similarly, the existing class is a base class (or parent class).

"""
# Example-3: Use of Inheritance in Python

# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):
    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

"""
In the above program, we created two classes i.e. 

Bird (parent class) and Penguin (child class). 

The child class inherits the functions of parent class. 

We can see this from swim() method. Again, the child class modified the behavior of parent class. 

We can see this from whoisThis() method. 

Furthermore, we extend the functions of parent class, by creating a new run() method.

Additionally, we use super() function before __init__() method. 

This is because we want to pull the content of __init__() method from the 
parent class into the child class.

"""