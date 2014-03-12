#Spair fyrir verdbolgu fyrir arin 2014-2017...
#skilar verbolgu spa 2017 fyrir allt haerra en 2017
 
def verdbolgu_spa(ar):
    if int(ar) <= 2013:
        return "Timabil lidid"
    elif ar == "2014":
        return (2.7 / 100)
    elif ar == "2015":
        return (3.4 / 100)
    elif ar == "2016":
        return (3.2 / 100)
    elif int(ar) >= 2017:
        return (2.9 / 100)
 
       
       
 
if __name__ == '__main__':
    while(True):
        ar = raw_input()
        x = verdbolgu_spa(ar)
        print x