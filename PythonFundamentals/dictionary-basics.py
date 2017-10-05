me = {"name": "Travis", "age": 3245,
      "birth country": "USA", "favorite language": "Python"}


def person_info(dic):
    for k, v in dic.iteritems():
        print "My", k, "is", v


person_info(me)
