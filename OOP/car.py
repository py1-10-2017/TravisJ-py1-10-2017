class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12

        def display_info():
            print "Price: ", self.price
            print "Speed: ", self.speed
            print "Fuel: ", self.fuel
            print "Mileage: ", self.mileage
            print "Tax: ", str(self.tax * 100) + "%"
            print "-------------------------"

        display_info()


durango = Car(40000, "40mph", "full", 15000)

pinto = Car(500, "5mph", "empty", 150000)

porsche = Car(60000, "75mph", "half full", 45000)

geo = Car(1100, "21mph", "mostly full", 67000)

raptor = Car(80000, "57mph", "almost empty", 23000)

volvo = Car(18000, "36mph", "half full", 123000)

cars = [durango, pinto, porsche, geo, raptor, volvo]
