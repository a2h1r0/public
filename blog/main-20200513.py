import discord
from discord.ext import commands
from modules.make_room import MakeRoom

token = 'トークン'
bot = commands.Bot(command_prefix='/')



###*** 起動処理 ***###
@bot.event
async def on_ready():
    print('-----Logged in info-----')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------------------------')




###*** コマンド ***###
### チーム分け ###
capacity_default = 4
rooms = [':cherry_blossom::cherry_blossom::cherry_blossom:桜の間:cherry_blossom::cherry_blossom::cherry_blossom:',
        ':bamboo::bamboo::bamboo:竹の間:bamboo::bamboo::bamboo:',
        ':evergreen_tree::evergreen_tree::evergreen_tree:林の間:evergreen_tree::evergreen_tree::evergreen_tree:',
        ':cyclone::cyclone::cyclone:風の間:cyclone::cyclone::cyclone:',
        ':maple_leaf::maple_leaf::maple_leaf:楓の間:maple_leaf::maple_leaf::maple_leaf:']

@bot.command()
async def zawazawa(ctx, capacity=capacity_default):
    make_room = MakeRoom()
    msg = make_room.make_room(ctx, capacity, rooms)
    await ctx.channel.send(msg)
    

    

###*** botの起動 ***###
bot.run(token)