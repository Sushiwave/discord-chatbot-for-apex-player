import json
from modules.command     import commands    as c
from modules.globalvalue import globalvalue as v
from discord.ext         import commands



config_dict = json.load(open('../config.json', 'r'))
token        = config_dict['token']
v.channel_id = int(config_dict['channel_id'])

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

bot.add_command(c.grenade)
bot.add_command(c.weapon)
bot.add_command(c.help)

bot.run(token)
