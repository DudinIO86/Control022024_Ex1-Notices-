##импорт классов и модулей
from view import*
from add_zam import*
from read_zam import*
from delete_zam import*
from corr_zam import*
##создание объектов класс
Display=viewDisplay
AddNote=CreateNotice
ReadNote=ReadNotice
DelNote=DelNotice
CorrNote=corrNotice

class controll:
    
    def run():
               
        flag=True
        
        while flag==True:
            Display.menu()
            ch=Display.choice()
            if ch == '1':
                AddNote.CreateNote()

            elif ch == '2':
                CorrNote.corrNote()

            elif ch == '3':
                DelNote.delNotices()

            elif ch == '4':
                ReadNote.ReadNote()

            elif ch == '5':
                flag = False
            else:
                print("Неверно введены данные")