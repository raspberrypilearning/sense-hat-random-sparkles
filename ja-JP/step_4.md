## ピクセルをランダムに設定する

まず、いくつかランダムな数を思いうかべて、`set_pixel`関数を使ってSense HATのディプレイのランダムな位置にランダムな色を配置します。

+ IDLEエディタを開きます。

[[[rpi-gui-idle-opening]]]

+ 新しいファイルを作成し、`sparkles.py`という名前で保存します。

+ 新しいファイルで`SenseHat`モジュールをインポートします。

    ```python
    from sense_hat import SenseHat
    ```

+ 次に、以下のコードを追加して、Sense HATへ接続します。

    ```python
    sense = SenseHat()
    ```


xとyを定義して、Sense HATのどのピクセルを点灯するか選びます。

+ `x`という変数を作成し、0から7までの数で好きな数を選んで設定します。 これはディスプレイ上でのピクセルのx座標になります。 
[[[generic-python-creating-a-variable]]]

+ `y`という別の変数を作成し、0から7までの数のうち好きな数を選んで設定します。 これはディスプレイ上でのピクセルのy座標になります。


+ ピクセルの色を選ぶために、0から`255`までの数のうち3つの数を思いうかべ、それらを`r`、`g`、`b`という変数に割り当てます。 これらの変数はピクセルの色を赤（r），緑（g），青（b）の量で表します。


+ `set_pixel`関数を使ってピクセルをランダムに選んだ色でランダムに選んだ位置に配置します。

**注意：**以下の折りたたみ部分の指示では、今までと別のファイル名を使っていて、IDLEのかわりにTrinketを使っています。

[[[rpi-sensehat-single-pixel]]]

`set_pixel`メソッドは次の順でデータを受け取ります：x座標、y座標、赤、緑、青。

`set_pixel`メソッドを定義するために、コード行のクエスチョンマークに正しい順序で変数の名前を入れます：x座標、y座標、赤、緑、青。

```python
sense.set_pixel(?, ?, ?, ?, ?)
```

わからないときは以下のヒントを表示してしましょう。

--- hints ---


--- hint ---

完成したコードは次のようになります。おそらく選んだ数字は違っているはずです。

![ランダムなピクセルの解き方](images/random-pixel-solution.png)

--- /hint ---

--- /hints ---


+ <kbd>F5</kbd>キーを押してコードを実行します。 Sense HATのLEDディスプレイ上のLEDが1つ点灯するのがわかります。

+ 次に、プログラム内のすべての数字を変更して、プログラムをもう一度実行します。 2つ目のLEDが点灯します。
