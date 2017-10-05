my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}


def dictionaryToTuple(dic):
    newList = []
    for k, v in dic.iteritems():
        newList.append((k, v))
    print newList


dictionaryToTuple(my_dict)
