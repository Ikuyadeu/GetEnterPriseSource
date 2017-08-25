## 取得データ
各１００件
* issue
* Pull Request
* issueコメント
* PRコメント
* assignee(担当者)
* contributors(開発者)
* 開発言語とその数

## データ取得方法
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

## 開発者分析方法
* 上のデータ取得を行う
* GetDevelopers.pyをダウンロード
* jsonファイルの入ったディレクトリとプロジェクト名を指定して実行
上の例だと
```
python3 GetDevelopers.py . hello
```

## パッチ収集
* GetDatapyで`XXXX-pulls.json`のようなファイルを取得
* GetPatch.pyをダウンロード
* jsonファイルの入ったディレクトリとユーザー名、パスワードを指定して実行
```
mkdir Patchs
python3 GetPatch.py hello-pulls.json ./Patchs Taro password
```
