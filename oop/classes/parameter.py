class Parameter:
    #default Constructor function
    def __init__(self, name):
        self.name = name
    user_age = 0

    def age_calculate(self,year):
        return 2024 - year



hello = Parameter(name="MIN MIN")
hello.user_age = hello.age_calculate(1997)
print(hello.name)
print(hello.user_age)