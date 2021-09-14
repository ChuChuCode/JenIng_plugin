# -*- coding: utf-8 -*- 
import json
import os
import subprocess
from opencc import OpenCC
from pathlib import Path
import traceback  

# https://github.com/BYVoid/OpenCC


def check_0(str,n):
    s  = ""
    if len(str) < n:
        for j in range( n - len(str) ):
            s = s + "0"
    s = s + str
    return s

def get_project_list(path):
    #check is path
    path = path + r"\User Data\Projects\com.lveditor.draft" 
    input_file = open(path + r'/root_draft_meta_info.json','r',encoding="utf-8")
    json_array = json.load(input_file)
    project_list =[]
    for i in json_array['all_draft_store']:
        project_list.append([i['draft_name'],i["draft_id"]])
    return project_list, path

def generate_srt(gen_list,path,save_path):
    converter = OpenCC('s2tw',os.getcwd())
    for project in gen_list:
        path1 = os.path.join(path ,project[0])
        my_file = Path( path1 +r'\draft_content.json')
        if my_file.is_file():
            #reaad name of project
            input_file = open (path1+ r'\draft_content.json' ,'r',encoding="utf-8")
            lyrics = json.load(input_file)
            time={}

            for i in lyrics['materials']['texts']:
                conv = converter.convert(i['content'])  # translate
                time[i['id']] = [ conv ]
                        
            for i in lyrics['tracks'][1]['segments']:
                id = i['material_id']
                sta = i['target_timerange']['start']//1000
                dur = i['target_timerange']['duration']//1000
                end = sta + dur  
                     
                time[id].append(check_0(str(sta//3600//1000),2)+':'+check_0(str(sta//1000//60%60),2) +':' + check_0(str(sta//1000%60),2)+','+check_0(str(sta%1000),3))
                time[id].append(check_0(str(end//3600//1000),2)+':'+check_0(str(end//1000//60%60),2) +':' + check_0(str(end//1000%60),2)+','+check_0(str(end%1000),3))

            num = 1  
            with open(os.path.join(save_path,project[0]) + r'.srt',"w",encoding="utf-8") as f:
                for i in time:
                    if num != 1:
                        f.write("\n")
                    f.write(str(num)+"\n")
                    f.write(time[i][1] +' --> '+time[i][2]+"\n")
                    f.write(time[i][0]+"\n")
                    print(time[i][0])
                    num = num + 1
            print("Generate {}.srt".format(project[0]))

if __name__ == "__main__":
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
        with open( os.path.join(app_path ,r'\root_draft_meta_info.json'),encoding="utf-8") as f :
            json_array = json.load(f)

        for i in json_array['all_draft_store']:
            file_name =  i['draft_name']  #檔案名稱(吐給UI)
            path1 = app_path + r'\\' +  i["draft_id"] #檔案ID(資料夾用)
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