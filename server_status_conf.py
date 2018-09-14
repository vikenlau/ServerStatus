import json
list=[]

username=input('username: ')
name=input('name: ')
type=input('type: ')
host=input('host: ')
location=input('location ')
password=input('pass ')

dic={'username':username,'name':name,'type':type,'host':host,'location':location,'password':password}

with open('config.json','r') as load_f:
    load_dict = json.load(load_f)
    for i in load_dict['servers']:
        list.append(i)
list.append(dic)
new_dic = {'servers':''}

new_dic['servers']=list

with open('config.json','w') as load_w:
    json.dump(new_dic,load_w)


