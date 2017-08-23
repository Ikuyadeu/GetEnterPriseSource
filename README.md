# データ取得方法
* 適当なフォルダを作成して移動
* GetData.pyをダウンロード
* hostnameとオーナー名、プロジェクト名を変更して以下を実行してください
```
python3 GetData.py http(s)://hostname/api/v3 ログインユーザー名 オーナー名 プロジェクト名
```
例：
https://developer.com/Fuji/helloプロジェクトにアカウントTaroでログインする場合
```
python3 GetData.py http(s)://developer.com/api/v3 Taro Fuji hello
```
