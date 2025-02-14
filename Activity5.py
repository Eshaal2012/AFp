class Robot:
    species="Robot"
    def __init__(self,name,age):
        self.name=name
        self.age=age
Robo=Robot("Robo",5)
print("Robo is a {}".format(Robo.species))
print("{} is {} years old".format(Robo.name,Robo.age))

