class Car:
    model_number ="MOF1997"
    engine_type ="HP 3000"

    def start_engine(self):
        print("Car is Start engine ")

    def break_engine(self):
            print("Car is Break engine ")

#class inheritance extends
class Toyota(Car) :
    def stop_engine(self):
        print("Car is Stop engine ")




class Honda(Car):
    def open_light(self):
        print("Car is Open light ")


toyota = Toyota()
toyota.break_engine()
toyota.stop_engine()
toyota.start_engine()
print(toyota.engine_type)
print(toyota.model_number)

honda = Honda()
honda.start_engine()
honda.break_engine()
honda.open_light()
print(honda.engine_type)
print(honda.model_number)

