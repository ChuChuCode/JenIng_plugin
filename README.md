# JenIng_plugin

***************************************************
* 歡迎使用 剪映的提取字幕小工具   我是朱朱ChuChu  *
***************************************************
首先此小工具會用到兩個檔案  setting.dll  Start.bat

setting.dll - 可使用任何文字編輯軟體打開(記事本、notepad++ 等)
----------------------------------------------------------------------------------------------
App_path  這邊是放上剪映的檔案位置 若當初安裝時沒有調整安裝位置就不需要處理

**若有做修改的**
可以對桌面的剪映點右鍵>查看檔案位置
這時..檔案總管應該會帶你來到 ..\AppData\Local\JianyingPro\Apps  (..為省略)
請回到上一層 ..\AppData\Local\JianyingPro 並把整個路徑填入 App_path= 的 = 後面(不要有空格!!!)

export_path  選擇你要輸出 *.srt 的位置

若不設定的話就會直接儲存到現在這個資料夾位置裡
想要更換位置，請將位置填入 export_path= 的 = 後面(不要有空格!!!)
----------------------------------------------------------------------------------------------

Start.bat - 顧名思義就是開始執行的bat檔
----------------------------------------------------------------------------------------------
這邊要注意 檔案儲存會按照你 剪映的專案標題當作 *.srt檔 的檔案名稱

另外！目前還沒做指定專案的輸出，所以若你的剪映裡有n個專案且都有生成字幕的話
-->程式會生出n隻 *.srt 檔
這部分會在接下來的版本去做調整(應該會做成UI版本)
還請大家敬請期待
