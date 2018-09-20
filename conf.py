import json
list=[]

username=raw_input('username: ')
name=raw_input('name: ')
type=raw_input('type: ')
host=raw_input('host: ')
location=raw_input('location: ')
password=raw_input('pass: ')

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


