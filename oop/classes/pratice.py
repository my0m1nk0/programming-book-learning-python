class Car:
    oil = ""
    key = ""
    #constructor
    def __init__(self, oil, key):
        self.oil = oil
        self.key = key
    def engine_start(self):
        return "Start Engine"
    def gear_one(self):
        return "Gear No 1"
    def back(self):
        return "Back"



chair = Car("Oil","KEY")
print(chair.engine_start())
gear = chair.gear_one()
print(gear)
print(chair.key)
print(chair.oil)
