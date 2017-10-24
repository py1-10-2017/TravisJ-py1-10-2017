
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.name
        print self.health


class Dog(Animal):
    def __init__(self, name, *health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name, *health):
        super(Dragon, self).__init__(name, health)
        self.health = 170

    def fly(self):
        self.health -= 10

    def display_health(self):
        print "I am a dragon"
        super(Dragon, self).display_health()


mydog = Dog("Fido", 20)

mydog.walk().walk().walk().run().run().pet().display_health()

mydragon = Dragon("Draco")

mydragon.display_health()
