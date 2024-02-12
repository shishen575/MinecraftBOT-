# インストールした discord.py を読み込む
import discord

# アクセストークンを読み込み
import env

# インテントの設定
intents = discord.Intents.all()

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print(f"{client.user}が起動しました")


# メッセージ受信時に動作する処理
@client.event
async def on_message(message: discord.Message):
    # 「～」と発言したら「～」が返る処理
    if message.content.startswith("!アプデ内容"):
        await message.channel.send("お待ち下さい")
    if message.content.startswith("VSCスタート"):
        await message.channel.send("python ./discord_bot/main.py")
    if message.content.startswith("マイクラサーバスタート依頼"):
        await message.channel.send("<@1084318050976796832>マイクラサーバスタート依頼")
    if message.content.startswith("マイクラサーバ参加希望"):
        await message.channel.send("<@1084318050976796832>マイクラサーバ参加依頼")
    if message.content.startswith("W"):
        await message.channel.send("植樹活動するんやな・・・")
    if message.content.startswith("X"):
        await message.channel.send("https://twitter.com/Iruya_Karuma")
    if message.content.startswith("webサイト"):
        await message.channel.send("https://sites.google.com/view/iruyakaruma/home")
    if message.content.startswith("カルマッチ鯖BOT起動中？"):
        await message.channel.send("オンライン")
    if message.content.startswith("BOTのバージョン？"):
        await message.channel.send("```v1.0.2```")
        await message.channel.send("```Pythonバージョン```")
        await message.channel.send("```Python 3```")
    if "/stop" in message.content:
        if message.author.id == 1084318050976796832:
            await message.channel.send("stop")
            await client.logout()
        else:
            await message.channel.send("shishen575専用コマンドだよ!!")



# Botの起動とDiscordサーバーへの接続
client.run(env.BOT_TOKEN)
