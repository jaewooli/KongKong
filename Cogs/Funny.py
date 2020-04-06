import discord
from discord.ext import commands
import random
import time
class 오락(commands.Cog):
    def __init__(self,bot):
        self.client=bot

    @commands.command(usage='(prefix)주사위',help='주사위를 굴려봅시다!     (prefix)주사위', aliases=['dice','DICE','Dice'])
    async def 주사위(self,ctx):
        randomNum= random.randrange(1,7)
        print(randomNum)
        if randomNum == 1:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :one:', colour=discord.Colour.red()))
        elif randomNum == 2:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :two:', colour=discord.Colour.blue()))
        elif randomNum == 3:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :three:', colour=discord.Colour.orange()))
        elif randomNum == 4:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :four:', colour=discord.Colour.gold()))
        elif randomNum == 5:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :five:', colour=discord.Colour.green()))
        else:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :six:', colour=discord.Colour.purple()))
    
    @commands.command(aliases=['8ball', 'test'], hidden=True)
    async def 질문받는다(self,ctx,*, question):
        response = ['확실해요',
                '아마.. 그럴걸요?',
                '아.. 잘 몰겠다',
                '그런 거 여기다 묻지 말고 지식인한테나 물어봐',
                '그으..거는 생각좀 해봐야 할듯']
        await ctx.send(f'질문: {question}\n답:{random.choice(response)}')

    @commands.command(aliases=['lottery', 'lotto'], help='복권을 긁어봅시다!     (prefix)복권',usage='(prefix)복권')
    async def 복권(self,ctx):
        number = [0]*7
        count = 0
        text=''
        for i in range(0,7):
            num= random.randrange(1,46)
            number[i] == num
            if count >=1:
                for i2 in range(0,i):
                    if number[i] == number[i2]:
                        numberText = number[i]
                        print("작동 이전값 : "+ str(numberText))
                        number[i] = random.randrange(1,46)
                        numberText = number[i]
                        print('작동 현재값 : ' + str(numberText))
                        if number[i] == number[i2]:
                            numberText = number[i]
                            print('작동 이전값 : ' + str(numberText))
                            number[i] = random.randrange(1,46)
                            numberText = number[i]
                            print('작동 현재값 : ' + str(numberText))
                            if number[i] == number[i2]:
                                await ctx.send('대단합니다!! 극적인 확률을 뚫고 숫자가 중복되었어요!')
            if count==6:
                text= text +' 보너스 숫자: '+str(number[i])
            else:
                count+=1
                text= text +' '+ str(number[i])
        await ctx.send(embed=discord.Embed(title=' ༼ つ ◕_◕ ༽つ', description=text, colour=discord.Color.red()))

def setup(bot):
    bot.add_cog(오락(bot))