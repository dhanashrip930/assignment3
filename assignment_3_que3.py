#Sample String : 'The quick Brow Fox'

#Expected Output :

#No. of Upper case characters : 3

#No. of Lower case Characters : 12

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
           pass 

    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case characters : ",d["LOWER_CASE"])

string_test('The quick Brow Fox')