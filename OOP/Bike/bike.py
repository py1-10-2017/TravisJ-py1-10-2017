class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price, self.max_speed, self.miles

    def ride(self):
        self.miles += 10
        print "Riding"
        return self

    def reverse(self):
        self.miles -= 5
        print "Reversing"
        return self


bike_1 = Bike(300, "25mph", 0)

bike_1.ride().ride().ride().reverse().displayInfo()

# createing bike 2 and making sure miles get reset to 0
bike_2 = Bike(500, "35mph", 50)

bike_2.ride().ride().reverse().reverse().displayInfo()

bike_3 = Bike(4000, "55mph", 0)

bike_3.reverse().reverse().reverse().displayInfo()
