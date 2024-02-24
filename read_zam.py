import json
from view import*

class ReadNotice:
    
    def ReadNote():
        read=viewDisplay
        
        read.showNote()
        choice=read.choice()
        
        

        with open('data.json','r') as file:
            dataJson=file.read()
    
    
        data=json.loads(dataJson)
        
        Flag=True
        
        while Flag==True:
            if choice=='1':
                print("Перечень заметок:")
                for p in data['notices']:
                    print("Номер:"+str(p["Number"]))
                    print("Тема:"+p["name"])
                    print("Дата:"+p["date"])
                    print("Время:"+p["time"])
                    print("Текст:\n"+p["text"])
                    print("\n")
                break
            
            elif choice=='2':
                print("Введите номер заметки\n")
                num=read.choice()
                print("Номер:"+str(data['notices'][int(num)-1]["Number"]))
                print("Тема:"+data['notices'][int(num)-1]["name"])
                print("Дата:"+data['notices'][int(num)-1]["date"])
                print("Время:"+data['notices'][int(num)-1]["time"])
                print("Текст:\n"+data['notices'][int(num)-1]["text"])
                print("\n")
                break
            
            elif choice=='3':
                dataInput=input("Введите дату в формате YYYY:MM:DD\n")
                print("\n")
                for p in data['notices']:
                    if p["date"]==dataInput:
                        print("Номер:"+str(p["Number"]))
                        print("Тема:"+p["name"])
                        print("Дата:"+p["date"])
                        print("Время:"+p["time"])
                        print("Текст:\n"+p["text"])
                        print("\n")
                break
               
            
            elif choice=='4':
                Flag=False
                break
            
            else:
                print("Ошибка ввода")
                break

       