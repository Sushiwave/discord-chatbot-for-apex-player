import sys
from modules.command     import commands    as c
from modules.globalvalue import globalvalue as v
from discord.ext         import commands





token        = sys.argv[1]
v.channel_id = int(sys.argv[2])

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

bot.add_command(c.grenade)
bot.add_command(c.weapon)
bot.add_command(c.help)

bot.run(token)
