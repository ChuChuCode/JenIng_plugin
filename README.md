# JenIng_plugin

***************************************************
* 歡迎使用 剪映的提取字幕小工具   我是朱朱ChuChu  *
***************************************************
此工具主要用來針對剪映所使用的小工具
剪映內建字幕生成，但不見得大家都喜歡他們的介面和字體模板
所以就有了「輸出 .srt」 的想法

[載點](http://www.mediafire.com/file/rg1nigy5qu0186v/JenIng_plugin.zip/file)

可能會被防毒擋下，正在找辦法解決...但請安心地讓他允許下載吧！

這是初步版本 未來會加上UI 讓他更 Fansy 一點  載點

	教學
----------------------------------------------------------------------------------------------

![新建](https://media.discordapp.net/attachments/726760885816918096/813355474497568798/unknown.png?width=677&height=447)

進入剪映，新增一個專案

![放入素材](https://media.discordapp.net/attachments/726760885816918096/813356561517903872/unknown.png?width=725&height=393)

匯入影片，並將影片拉到下方的時間軸上

![識別聲音](https://media.discordapp.net/attachments/726760885816918096/813357065350545418/unknown.png?width=725&height=393)

點選文本>識別字幕>開始識別，並等待其跑完

![字幕](https://media.discordapp.net/attachments/726760885816918096/813357237857943563/unknown.png?width=1440&height=178)

若成功應該會出現一票的字幕，生成後就可以關閉剪映了

![更名](https://media.discordapp.net/attachments/726760885816918096/813358134571434004/unknown.png)

出來後 將剛剛建立的專案重新命名 (建議英文，我還沒處理字串問題w)  命名完就關掉視窗吧！

![主角登場](https://media.discordapp.net/attachments/726760885816918096/813358904029216768/unknown.png)

先將 zip 解壓縮

![進到資料夾](https://media.discordapp.net/attachments/726760885816918096/813361897793257512/unknown.png?width=725&height=398)

進到 JenIng_plugin 資料夾，裡面密密麻麻的檔案，但你要關注的就只有這兩隻檔案  Start.bat setting.dll

![使用者填入](https://media.discordapp.net/attachments/726760885816918096/813363050768760832/unknown.png?width=725&height=406)

請對剪映點右鍵，並開啟檔案位置，你會看到 C:\Users\<你的使用者名稱>\AppData\Local\JianyingPro

打開 setting.dll 將使用者填入 App_path 後面的<User_Name>    Ex: App_path=C:\Users\Chu\AppData\Local\JianyingPro

而下面 export_path 則是你希望 .srt 輸出的位置  Ex: 放到桌面  export_path=C:\Users\zero7\Desktop

**記住=後面不要有空格**

![開始！]()

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

Start.bat - 顧名思義就是開始執行的bat檔
----------------------------------------------------------------------------------------------
這邊要注意 檔案儲存會按照你 剪映的專案標題當作 *.srt檔 的檔案名稱

另外！目前還沒做指定專案的輸出，所以若你的剪映裡有n個專案且都有生成字幕的話
-->程式會生出n隻 *.srt 檔
這部分會在接下來的版本去做調整(應該會做成UI版本)
還請大家敬請期待
