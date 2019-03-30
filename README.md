# DiscordLoginCount
mysqlでdiscordサーバーでの発言回数・発言文字数・発言日数を集計してくれるbot

mainにあるファイルでbotが起動します。
logにはユーザーのコマンドの履歴やデータ作成の記録が書き込まれます。

以下必須ライブラリ
discord.py
mysql_conecter
mysql-connector-python

必須環境
python3.6(3.7では作動しません)
mysql
任意のデータベースで以下のコマンドでテーブルを作成する必要とconfigファイルに適切な値を入力する必要あり
create databse discord(user_id varchar(500),user_name varchar(500),server_id varchar(500),message_count int,word_count int,month int,day int,login_count int)
