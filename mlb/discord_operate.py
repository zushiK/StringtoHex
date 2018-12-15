import discord
import main

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("hex "):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            msg = main.compile_hex(message.content.split()[1])
            # msg = "黙ってｽﾏﾌﾞﾗしろ " + message.author.name + message.content.split()[1] + "！"

            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, msg)

client.run("NTIzNTA3NjM2NDQ5MzEyNzc4.Dvaiug.ryIDB9ATgYy17cHzw6lgMpPBd5c")
