import json
with open('med12345_20211116_235951.json') as  access_json:
    read_content=json.load(access_json)
value1=input()
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
                    pass
                else:
                    getvaluebykey(val,val1)
getvaluebykey(read_content,val1)

