import json
with open('med12345_20211116_235951.json') as  access_json:
    read_content = json.load(access_json)
keyinput1 = input()
keyinput2 = input()
valueinput2 = input()
class Json:
            def getvaluebykey(self,read_content,inpkeyvalue):
                for key, value in read_content.items():
                    if type(value) is dict:
                        Json.getvaluebykey(self,value,inpkeyvalue)
                    elif inpkeyvalue==key:
                        print(value)
                    elif type(value) is type(list()):
                        for val in value:
                            if type(val) is type(str()):
                                pass
                            elif type(val) is type(list()):
                                pass
                            else:
                                Json.getvaluebykey(self,val,inpkeyvalue)
            def getvaluebycomponent(self,read_content,inp2key,inp2value):

                for key,value in read_content.items():
                   try:
                       if type(value) is dict:
                          Json.getvaluebycomponent(self,value,inp2key,inp2value)

                       elif type(value) is type(list()) and type(value[0]) is dict:
                            if (value[0][inp2key]) == inp2value:
                                with open("sample1.json","w") as outfile:
                                  json.dump(value[0],outfile,indent=2)

                            elif (value[1][inp2key]) == inp2value:
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
                                Json.getvaluebycomponent(self,val, inp2key,inp2value)
obj = Json()
print(obj.getvaluebykey(read_content,keyinput1))
obj.getvaluebycomponent(read_content,keyinput2,valueinput2)


