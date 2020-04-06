import discord
from discord.ext import commands
import json
from hanspell import spell_checker

class 명령(commands.Cog):
    def __init__(self, bot):
        self.client=bot

    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    @commands.command()
    async def help(self,ctx):
        await ctx.send_help()
        
    @commands.command(help='prefix를 마음대로 바꿔보세요!    (prefix)changeprefix   [바꿀 prefix]')
    async def changeprefix(self,ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(ctx.author.guild.id)] = prefix
        with open('prefixes.json','w') as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f'Prefix 가 {prefix} (으)로 바뀌었습니다')    

    @commands.command(aliases=['디엠', 'Dm', 'DM', 'dM'], help='대신 dm을 보내드려요!   (prefix)dm  [유저]  [보낼메세지]',usage='(prefix)dm (수신자 이름) (보낼 매세지)')
    async def dm(self,ctx, user, *,info):
        with open('prefixes.json','r') as f:
            prefixes = json.load(f)
            prefix =prefixes[str(ctx.author.guild.id)]
        if not ctx.guild.get_member_named(user):
            await ctx.send(embed=discord.Embed(title='명령어 에러!!', description=f'디엠 명령어는\n\n{prefix}dm (수신자) (내용)\n\n의 형식으로 이루어졌습니다', color=discord.Color.red()))
        else:    
            user = ctx.guild.get_member_named(user)
            await user.send(info)     
            await ctx.channel.purge(limit=1)

    @dm.error
    async def dm_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            with open('prefixes.json','r') as f:
                prefixes = json.load(f)
                prefix =prefixes[str(ctx.author.guild.id)]
            await ctx.send(embed=discord.Embed(title='명령어 에러!!', 
            description=f'모든 요소가 입력되지 않았습니다.\n\n {prefix}dm (수신자 이름) (보낼 메세지)\n\n  \
                의 순서로 입력해주세요', color=discord.Color.red()))

    @commands.command(aliases=['나가','킥',' Kick'], help='서버에서 추방시킵시다!    (prefix)dm [유저] [이유]',usage='(prefix)kick (유저) (이유)')
    @commands.has_permissions(kick_members = True)
    async def kick(self,ctx, user,*,reason):
        user = ctx.guild.get_member_named(user)
        await user.send(f'{reason}\n(으)로 인해 {ctx.guild.name}서버에서 추방당하셨습니다.')
        await ctx.guild.kick(user=user,reason=reason)
        await ctx.send(f'{user}가 서버에서 퇴출됐습니다')

    @kick.error
    async def kick_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            with open('prefixes.json','r') as f:
                prefixes = json.load(f)
                prefix =prefixes[str(ctx.author.guild.id)]
            await ctx.send(embed= discord.Embed(title='명령어 에러!!', 
            description=f'모든 요소가 입력되지 않았습니다\n {prefix}kick (유저) (이유)\n \
            의 순서로 입력해주세요', color= discord.Color.red()))
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(description=f'{ctx.author}님은 유저를 추방할 권리가 없습니다', color=discord.Color.blue()))
    
    @commands.command(aliases=['ㅁㅊㅂ', '맞춤법', '검사'], help='않이;; 그개 맛는 맏춤뻡임?    (prefix)grammer [검사할 메세지]')
    async def grammer(self, ctx,*,content:str): 
        result = spell_checker.check(u'%s' % content)
        result = result.as_dict()
        if result['original'] == result['checked']:
            await ctx.send(embed=discord.Embed(title='정확하네요!', description=f'{content}\n는 올바른 문장입니다', color=discord.Color.green()))
        else:
            await ctx.send(embed= discord.Embed(title=':no_entry:' + '삐입', description=f'~~{content}~~\n 는 올바르지 못합니다! \n\n {result["checked"]}\n 가 올바른 문장이에요!', color=discord.Color(0xFF0000)))

    @grammer.error
    async def grammer_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            with open('prefixes.json','r') as f:
                prefixes = json.load(f)
                prefix =prefixes[str(ctx.author.guild.id)]
            await ctx.send(embed=discord.Embed(title='명령어 에러!!', description=f'모든 요소가 입력되지 않았습니다\n{prefix}grammer (검사할 메세지)\n \
                의 순서로 입력해주세요', color=discord.Color.red()))
def setup(bot):
    bot.add_cog(명령(bot))