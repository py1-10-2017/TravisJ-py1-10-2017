name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider",
                   "giraffe", "ticks", "dolphins", "llamas", "sharks"]


def make_dictionary(list1, list2):
    if len(list1) > len(list2):
        x = zip(list1, list2)
        newDictionary = dict(x)
        return newDictionary

    else:
        x = zip(list2, list1)
        newDictionary = dict(x)
        return newDictionary


print make_dictionary(name, favorite_animal)
