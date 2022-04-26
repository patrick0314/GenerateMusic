# GenerateMusic

## Usage

可以用 `python hw3.py --help` 指令來檢視程式所需的參數：

![](https://i.imgur.com/ootFUlZ.jpg)

* **score**:

    輸入要播出or儲存的音樂的簡譜。在 default condition 之中，`1` 代表 Do、`2` 代表 Re、`3` 代表 Mi，以此類推。

* **beat**:

    輸入 score 中每個音符的拍子長度。在 default condition 之中，`1` 代表 1 拍、`2` 代表 2 拍，以此類推。
    另外，只能輸入整數，也就是說，如果有 1/4 拍的節奏出現，就要將所有拍子 * 4 來做輸入。
    
* **name**:

    如果希望最後 output 出 `.wav` 的檔案，在這邊輸入檔名；如果沒有輸入，則不會輸出檔案。
    
* **key**:

    代表的是自然大調。`1` 代表的是 C major、`2` 代表的是 D major、`3` 代表的是 E major，以此類推。
    另外，default key = 1，如果有所更改的話，score 中的數字所代表的音階也會隨之更改。
    
* **speed**: 

    可以控制音樂播放的速度，但也會造成音調的些許變化。
    
* **volume**: 

    可以調節音量的大小聲，range = 0 - 2，如果超出範圍則會出現 error。
    
* **play**:

    如果希望執行檔案後會播出音樂，則輸入 `1`；反之則不要輸入。
    
## Demo

* Basic Function:

    只用 score、beat、name 三個參數，結果為輸出 `twinkle.wav`，並且從音檔可以聽出符合輸入的小星星簡譜。

![](https://i.imgur.com/IoyXsUL.jpg)

* Advanced Function:

    使用了所有參數，結果為輸出 `twinkle_2.wav`，從圖中可以看出有成功播放音樂 & 輸出音檔。另外，在聆聽音檔後，可以發現有符合輸入的將大調改成 D 大調、加速音樂，並且成功縮小音量。

![](https://i.imgur.com/HLiLLXX.jpg)

###### tags: `Github`
