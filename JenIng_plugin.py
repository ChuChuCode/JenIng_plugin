# -*- coding: utf-8 -*- 
import json
import os
import subprocess
from opencc import OpenCC
from pathlib import Path
import traceback  

# https://github.com/BYVoid/OpenCC
converter = OpenCC('s2t')

def check_0(str,n):
    s  = ""
    if len(str) < n:
        for j in range( n - len(str) ):
            s = s + "0"
    s = s + str
    return s

try:
    file_path = os.getcwd()
    
    #p = subprocess.Popen("cd", stdout=subprocess.PIPE, stderr=None, shell=True)
    #file_path = p.communicate()[0].encoding("utf-8")[:-2]
    #print(file_path)
    #text = input('Press Enter')

    #Read setting.dll
    with open("setting.dll",'r',encoding="utf-8") as setting :
        for se in setting:
            if 'App_path' in se:
                app_path = se.split("=")[1].split("\n")[0]
            elif 'export_path' in se:
                ex_path = se.split("=")[1].split("\n")[0]
    #get application path
    app_path = app_path + r"\User Data\Projects\com.lveditor.draft"
    #os.chdir(r'{}'.format(app_path))
    
    #read json
    input_file = open(app_path + r'\root_draft_meta_info.json','r',encoding="utf-8")
    json_array = json.load(input_file)

    for i in json_array['all_draft_store']:
        file_name =  i['draft_name']
        path1 = app_path + r'\\' +  i["draft_id"]
        my_file = Path(path1+r'\draft.json')
        if my_file.is_file():
            
            #reaad name of project
            input_file = open (path1+r'\draft.json' ,'r',encoding="utf-8")
            lyrics = json.load(input_file)
            time={}

            for i in lyrics['materials']['texts']:
                conv = converter.convert(i['content'])  # translate
                time[i['id']] = [ conv ]
                
            for i in lyrics['tracks'][1]['segments']:
                id = i['material_id']
                sta = i['target_timerange']['start']//1000
                dur = i['target_timerange']['duration']//1000
                end = sta+ dur  
                    
                time[id].append(check_0(str(sta//3600//1000),2)+':'+check_0(str(sta//1000//60%60),2) +':' + check_0(str(sta//1000%60),2)+','+check_0(str(sta%1000),3))
                time[id].append(check_0(str(end//3600//1000),2)+':'+check_0(str(end//1000//60%60),2) +':' + check_0(str(end//1000%60),2)+','+check_0(str(end%1000),3))

            num = 1
                
            if ex_path == "" :
                ex_path = file_path
            with open(ex_path + r'\\' + file_name + r'.srt',"w",encoding="utf-8") as f:
                for i in time:
                    if num != 1:
                        f.write("\n")
                    f.write(str(num)+"\n")
                    f.write(time[i][1] +' --> '+time[i][2]+"\n")
                    f.write(time[i][0]+"\n")
                    num = num + 1
            print("Generate {}.srt".format(file_name))
except Exception as e :
    traceback.print_exc()  