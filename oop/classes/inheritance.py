class animal:
    number_of_legs = 0

    def sleep(slef):
        print("zzz")

    def count_legs(self):
        print("I have {} legs".format(self.number_of_legs))


class dog(animal):
    def __init__(self):
        self.number_of_legs = 4
    def bark(self):
            print("Woof")


mydog = dog() # create object instance
mydog.sleep()
mydog.count_legs()
mydog.bark()


