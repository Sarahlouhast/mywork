#messingwithdictionaries
#Author: Sarah Hastings

car = {
    "make" : "ford",
    "model" : "mondeo",
    "year" : 2006,
    "owner": {
        "name" : "andrew",
        "driver-number": 1123
    }
}
print(car["year"])
print(car ["owner"].get("names")) #print(car ["make"]) make code as simple as possible

#.get if not certain if some there name/names Andrew/none
#attr = "make"
#print (car[attr])