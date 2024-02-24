import json
import datetime
from view import*
from controll import*

class corrNotice:
    
    
    def corrNote():
        
        menuCor=viewDisplay
        # Go=controll

        menuCor.menuCorr()
        choice=menuCor.choice()
        
        current_date = datetime.datetime.now().date().strftime('%Y:%m:%d')
        current_time = datetime.datetime.now().time().strftime('%H:%M:%S')

        
        
        
        with open('data.json','r') as file:
            data_json=file.read()
                    
        data=json.loads(data_json)
        
        sizeNotice=len(data['notices'])
        
        flag=True
        
        while flag==True:
            if choice=='1':
                
                num=input("Выберите номер заметки: ")
                if isinstance(int(num), int):
                
                        if int(num)<1 or int(num)>sizeNotice:
                            print("Такой записи нет")
                            break
                        else:
                            tema=input("Введите новый текст:\n")
                
                            data['notices'][int(num)-1]['name']=tema
                            data['notices'][int(num)-1]['date']=current_date
                            data['notices'][int(num)-1]['time']=current_time
                            with open('data.json','w') as file:
                                json.dump(data,file,indent=2,ensure_ascii=True)
                            break
                else:
                    print("Ошибка ввода")
                    break
            
            elif choice=='2':
                
                num=input("Выберите номер заметки: ")
                if isinstance(int(num), int):
                    if int(num)<1 or int(num)>sizeNotice:
                        print("Такой записи нет")
                        break
                    else:
                        text=input("Введите новый текст:\n")
                
                        data['notices'][int(num)-1]['text']=text
                        data['notices'][int(num)-1]['date']=current_date
                        data['notices'][int(num)-1]['time']=current_time
                        with open('data.json','w') as file:
                            json.dump(data,file,indent=2,ensure_ascii=True)
                        break
                else:
                    print("Ошибка ввода")
                    break
            
            elif choice=='3':
                
                num=input("Выберите номер заметки: ")
                if isinstance(int(num), int):
                    if int(num)<1 or int(num)>sizeNotice:
                        print("Такой записи нет")
                        break
                    else:
                        tema=input("Введите новый текст темы:\n")
                        text=input("Введите новый текст заметки:\n")
                
                        data['notices'][int(num)-1]['name']=tema
                        data['notices'][int(num)-1]['date']=current_date
                        data['notices'][int(num)-1]['time']=current_time
                        data['notices'][int(num)-1]['text']=text
                        with open('data.json','w') as file:
                            json.dump(data,file,indent=2,ensure_ascii=True)
                        break
                else:
                    print("Ошибка ввода")
                    break
            elif choice=='4':
                break
            else:
                print("Неверно введены данные")
                break
                    


