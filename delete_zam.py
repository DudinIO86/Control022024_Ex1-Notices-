import json

class DelNotice:
    
    def delNotices():
        
        with open('data.json','r') as file:
            data_json=file.read()
            
        data=json.loads(data_json)
                
        sizeNotice=len(data['notices'])
        
        delNumb=input("Введите номер записи для удаления: ")
        
        if isinstance(int(delNumb), int):
        
            if int(delNumb)<1 or int(delNumb)>sizeNotice:
                print("Такой записи нет")
            
        
            
            else:
                del data['notices'][int(delNumb)-1]
                i=1
                for p in data['notices']:
                    p['Number']=i
                    i+=1
                    with open('data.json','w') as file:
                        json.dump(data,file,indent=2,ensure_ascii=True)
        else:
            print("Неверные данные")
        
        
        
        

