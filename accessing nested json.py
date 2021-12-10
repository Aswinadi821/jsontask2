import json

with open('med12345_20211116_235951.json') as  access_json:
    read_content=json.load(access_json)
val1=input()
val2=input()
val3=input()
def getvaluebykey(read_content,val1):
    for key, value in read_content.items():
        if type(value) is dict:
            getvaluebykey(value,val1)
        elif val1==key:
            print(value)
        elif type(value) is type(list()):
            for val in value:
                if type(val) is type(str()):
                    pass
                elif type(val) is type(list()):
                    pass  # use recursive call in this line if the json structure has a nested list  
                else:
                    getvaluebykey(val,val1)

def getvaluebycomponent(read_content,val2,val3):

    for key,value in read_content.items():
       try:
           if type(value) is dict:
              getvaluebycomponent(value,val2,val3)

           elif type(value) is type(list()) and type(value[0]) is dict:
                if (value[0][val2]) == val3:
                    with open("sample1.json","w") as outfile:
                      json.dump(value[0],outfile,indent=2)

                elif (value[1][val2]) == val3:
                    with open("sample1.json", "w") as outfile:
                        json.dump(value[1], outfile,indent=2)
       except IndexError:
           print("Data not found in Intercept components")

           for val in value:
                if type(val) is type(str()):
                    pass
                elif type(val) is type(list()):
                    pass
                else:
                    getvaluebycomponent(val, val2,val3)
getvaluebykey(read_content,val1)
getvaluebycomponent(read_content,val2,val3)


