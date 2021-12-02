import json
with open('med12345_20211116_235951.json') as  access_json:
    read_content=json.load(access_json)
value1=input()
def getjsonfunc(value1):
       if value1 == 'Unioncomponents':
            question_acess = read_content['Details']
            comp_access= question_acess['FilteringCoditions']
            final_op = comp_access['UNIONComponents']
            with open("sample1.json", "w") as outfile:
               json.dump(final_op, outfile)
       elif value1 == 'Component:Demographics':
           question_acess = read_content['Details']
           comp_access = question_acess['FilteringCoditions']
           final_op = comp_access['UNIONComponents']
           demo_value = final_op['Conditions']
           final_op2= demo_value[0]
           with open("sample2.json", "w") as outfile2:
               json.dump(final_op2, outfile2)
       else:
           print('Data not found')
getjsonfunc(value1)