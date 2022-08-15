class car:

    def __init__(self, body, enign, tyre):
        self.body = body
        self.engin = enign
        self.tyre = tyre

    def milage(self):
        print("milage of this car")


class tata(car):
    pass


c = car("solid", "v6", "radial")

t = tata("solid1", "v7", "radial1")
print(t.milage())
