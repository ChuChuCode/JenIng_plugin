import tkinter as tk
from tkinter.filedialog import askdirectory
import os
import JenIng_plugin as Jp
import traceback  

#Parameter
app_path_str,save_path_str ="",""
project_list = [] #存入當前 Project 和 ID
radio_btn1 = []  #Radio Button list
do_list =[] #給輸出用

def init():
    global app_path_str,save_path_str
    with open("setting.dll",'r',encoding="utf-8") as setting :
        for se in setting:
            if 'App_path' in se:
                app_path_str = se.split("=")[1].split("\n")[0]
            elif 'Save_path' in se:
                save_path_str = se.split("=")[1].split("\n")[0]
    return app_path_str,save_path_str
    
# Open GUI

# https://www.hackster.io/techno_z/using-the-tkinter-library-in-python-24f01f
# https://blog.csdn.net/liuxu0703/article/details/54428405

# temp
# project_list =["EP1","EP2","EP3","EP4","EP5","EP6","EP7","EP8","EP9","EP10","EP11","EP12"]
    
# 建立事件處理函式（event handler），透過元件 command 參數存取
def Create_Radio_Button(path):
    #獲取 Project List
    global project_list,file_path
    project_list, file_path = Jp.get_project_list(path)
    
    # 建立 Radio Button
    l = len(project_list)
    for row in range(l//4 + 1 ) :
        for line in range(4):
            if row*4 + line < l:
                temp_var = tk.StringVar(value=0)
                temp = tk.Checkbutton(top_center, text=project_list[row*4 + line][0], var=temp_var,font=("Arial", 12))
                temp.grid(row = row,column=line)
                #radio_btn1.append(temp_var)
                radio_btn1.append([temp_var,temp])
                
def set_app_path():
    global app_path_str
    app_path_str = askdirectory(initialdir=os.getcwd())
    app_path.set('剪映檔案位置 :' + app_path_str)
    Create_Radio_Button(app_path_str)
    
    
def set_save_path():
    global save_path_str
    save_path_str = askdirectory(initialdir=os.getcwd()) 
    save_path.set('輸出檔案位置 :' + save_path_str)
  
def check_checkbox():
    #若檔案位置&儲存位置都有拿到
    global app_path_str,save_path_str
    if (app_path.get().split(" ")[1][1:]) and (save_path.get().split(" ")[1][1:]) :
        #有勾選->寫檔案
        if int(save_CheckBtn_var.get()):
            with open("setting.dll",'w',encoding="utf-8") as setting : #w 為覆蓋寫入 未來需要append 可用a
                setting.write("App_path=" + app_path_str + "\n")
                setting.write("Save_path=" + save_path_str + "\n")
        #確認勾選項目
        temp = []
        do_list = []
        for check in radio_btn1:
            if int(check[0].get()):
                temp.append(check[1]['text'])  
        for pro in project_list:
            if pro[0] in temp:
                do_list.append([ pro[0],pro[1] ])
        #call function do srt
        Jp.generate_srt(do_list,file_path,save_path_str)
        
        window1 = tk.Tk()
        window1.title('完成')
        window1.geometry('200x50+'+str(window.winfo_x()+200)+'+'+str(window.winfo_y()+150))
        window1.configure()
        window1.attributes("-topmost", True)
        
        frame1 = tk.Frame(window1)
        frame1.pack()
        
        exit_button = tk.Button(frame1, text='OK', command = window1.destroy)
        exit_button.grid(row=0,column=0)
        window1.mainloop()
        
if __name__ == "__main__":
    try:
        #讀取 dll 檔案(initial)
        app_path_str,save_path_str = init()
        
        # 建立主視窗和 Frame（把元件變成群組的容器）
        window = tk.Tk()
        window.title('srt 抓取、生成器')
        window.geometry('600x300')
        #window.configure(background='white')
        window.configure()
        
        # 將元件分為 top/bottom 兩群並加入主視窗
        # 關於 pack / grid / place http://yhhuang1966.blogspot.com/2018/10/python-gui-tkinter_12.html
        top_frame = tk.Frame(window)
        top_frame.pack()
        bottom_frame = tk.Frame(window)
        bottom_frame.pack(side=tk.BOTTOM)

        # 以下為 top_frame 群組
        # 剪映檔案位置
        top_up = tk.Frame(top_frame)
        top_up.pack(pady=20)
        # RadioButton
        top_center = tk.Frame(top_frame)
        top_center.pack(pady=20)
        # 輸出檔案位置
        top_down = tk.Frame(top_frame)
        top_down.pack(pady=20,side=tk.BOTTOM)

        #top_up
        #顯示剪映檔案位置
        app_path = tk.StringVar()
        app_path.set('剪映檔案位置 :'+ app_path_str) #填入儲存的路徑
        file_entry = tk.Label(top_up,textvariable=app_path,font=("Arial", 12))
        file_entry.pack(side=tk.LEFT) # 讓系統自動擺放元件，預設為由上而下（靠左）

        #選擇檔案位置
        # 綁定 set_save_path 事件處理，點擊該按鈕會觸發 set_app_path()
        select_app_path_button = tk.Button(top_up, text='選擇路徑', fg='black', command=set_app_path)
        select_app_path_button.pack(side=tk.LEFT)

        #top_center
        if app_path_str :
            Create_Radio_Button(app_path_str)
        #top_down
        #顯示輸出檔案位置
        save_path = tk.StringVar()
        save_path.set('輸出檔案位置 :'+ save_path_str) #填入儲存的路徑
        file_entry = tk.Label(top_down,textvariable=save_path,font=("Arial", 12))
        file_entry.pack(side=tk.LEFT) # 讓系統自動擺放元件，預設為由上而下（靠左）
        
        #選擇檔案位置
        select_save_path_button = tk.Button(top_down, text='選擇路徑', fg='black', command=set_save_path)
        select_save_path_button.pack(side=tk.LEFT)
             
        # 以下為 bottom_frame 群組
        buttom_up = tk.Frame(bottom_frame)
        buttom_up.pack()
        buttom_down = tk.Frame(bottom_frame)
        buttom_down.pack(pady=10)
        
        save_CheckBtn_var = tk.StringVar(value=0)
        save_CheckBtn = tk.Checkbutton(buttom_up, text="執行時將設定儲存", var=save_CheckBtn_var,font=("Arial", 12))
        save_CheckBtn.pack()

        exec_button = tk.Button(buttom_down, text='執行', command = check_checkbox)
        exec_button.pack(side=tk.LEFT)
        exit_button = tk.Button(buttom_down, text='離開', command = window.quit)
        exit_button.pack(side=tk.LEFT)

        # 運行主程式
        window.mainloop()
    except Exception as e :
        traceback.print_exc() 
        a = input("press...")