import json
import pymysql

with open("JSONFile.json") as access_json:
    read_content=json.load(access_json)

direct = input()

def getvalueofdirectors(read_content,direct):
     for key,value in read_content.items():
         if type(value) is dict:
             getvalueofdirectors(value,direct)

         elif type(value) is list and direct==key:
                print(value)










getvalueofdirectors(read_content,direct)


