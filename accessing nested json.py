import json
with open('med12345_20211116_235951.json') as  access_json:
    read_content=json.load(access_json)
value1=input()
def getjsonfunc(value1):
       for key, values in read_content.items():
        if type(values) is str:
            if val1==key:
              yield(values)
        elif type(values) is dict:
              for key2, values2 in values.items():
                if val1 == key2:
                   yield(values2)
                elif type(values2) is dict:
                     for key3, values3 in values2.items():
                        if val1 == key3:
                           yield(values3)
getjsonfunc(value1)
