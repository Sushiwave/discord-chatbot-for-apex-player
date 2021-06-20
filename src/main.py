import os
from modules.command     import commands    as c
from modules.globalvalue import globalvalue as v
from discord.ext         import commands





token        = os.environ['TOKEN']
v.channel_id = int(os.environ['CHANNEL_ID'])

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

bot.add_command(c.grenade)
bot.add_command(c.weapon)
bot.add_command(c.help)

bot.run(token)
