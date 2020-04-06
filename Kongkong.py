# -*- coding:utf-8 -*- 
import asyncio, discord, random
from discord.ext import commands

token = "Njg0OTQ1MzM2MDIzNjQ2MzEw.XmBmOA.0XylX-wE7LElc1zQCaY1aCWaQD4"
client=discord.Client()
user=discord.User
permissions = discord.Permissions()
@client.event 
async def on_ready():
    for i in range(2):
        await client.change_presence(status=discord.Status.online, activity=discord.Game("ㅎㅇ!")) 
    print("내가 와따!!")

@client.event 
async def on_message(message):
    if message.content =='!앙 만희띠':
        await message.channel.send("앙 만희띠 라니 그런 저급한 용어는 쓰지 않았으면 합니다")
    elif message.content =='!이만희':
        await message.channel.send('제가 이런 거 만들어 봤어요!   https://jaewooli.github.io/Mueanhee')
    elif message.content =='!안녕':
        num = random.randint(0,2)
        if num == 0:
            await message.channel.send("나...나도 안녕")
        else:
            await message.channel.send("아니")
    elif message.content.startswith('.아이디'):
        author= message.author
        await message.channel.send(author.id)
    elif message.content.startswith('.id'):
        author= message.author
        await message.channel.send(author.id)

    elif message.content == '.직업':        #개발 중...
        await message.channel.send(embed=discord.Embed(title='여기 서버의 길드 멤버들입니다!!', 
        description=list(message.guild.roles)))

    elif message.content.startswith('.디엠 '):
        list1=message.content.split(' ')
        author=message.guild.get_member_named(list1[1])
        msg=' '.join(list1[2:])
        await author.send(msg)
        await message.delete()
    
    elif message.content.startswith('.밴'):
        list2=message.content.split(' ')
        if list2[1] == None:
            await message.channel.send(embed=discord.Embed(title='형식을 잘못 입력하셨네요!', 
            description='.밴 (유저) (밴 사유)\n__**주의※ 밴 자격이 없다면 밴을 할 수 없습니다!!**__', color=discord.Colour.red()))
        elif list2[2] == None:
            await message.channel.send(embed=discord.Embed(title='형식을 잘못 입력하셨네요!', 
            description='.밴 (유저) (밴 사유)\n__**주의※ 밴 자격이 없다면 밴을 할 수 없습니다!!**__'))
        if message.author == message.guild.owner: 
            author=message.guild.get_member_named(list2[1])
            await message.guild.kick(author, reason=list2[2])
            await message.channel.send(embed =discord.Embed(description=list2[1]+'님이 밴을 당하셨어요~ 다시 들어올려면 ㅎㅎ 꽤 힘들겠네요', color=discord.Colour.red()))

@client.event
async def on_message_delete(message):
    if message.author.bot == True:
        await message.channel.send('ㅋㅋ 야 누가 메세지 지웠는데?')
client.run(token)