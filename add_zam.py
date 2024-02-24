import json
import datetime
import os.path

class CreateNotice:
    
    def CreateNote():
    
        name=input("Введите тему заметки: ")
        text=input("Введите текст заметки:\n")
    
        note={}
        current_date = datetime.datetime.now().date().strftime('%Y:%m:%d')
        current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        

        note['notices']=[]
        
        path="data.json"
        if(os.path.exists(path)):       
        
            with open('data.json','r') as file:
                data_json=file.read()
                        
            data=json.loads(data_json)
        
            size=len(data['notices'])+1
            data['notices'].append({
                                    "Number":size,
                                    "name":name,
                                    "date":current_date,
                                    "time":current_time,
                                    "text":text})
            with open('data.json','w') as file:
                json.dump(data,file,indent=2,ensure_ascii=True)
        else:
            size=1
            note['notices'].append({
                                    "Number":size,
                                    "name":name,
                                    "date":current_date,
                                    "time":current_time,
                                    "text":text})   
  
            with open('data.json','w') as file:
                json.dump(note,file,indent=2,ensure_ascii=True)
  
