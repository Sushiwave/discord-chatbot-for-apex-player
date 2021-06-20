from . import util as ut
from ....language import constant as lc





def help(): 
    if lc.ENG:
        message  = 'Commands\n'
        message += '  help            Help command\n'
        message += '  weapon          You can check the information of the weapon information.\n'
        message += '  grenade         You can check the information of the grenade information.\n'

        message += '\n'
        
        message += 'Options\n'
        message += '  --attribute     A list of weapon/grenade attributes will be returned.\n'
        message += '  --all           Information on all weapons/grenades will be returned.\n'
        
        message += '\n'

        message += 'Arguments\n'
        message += '  arg1            Specify the name of the weapon you want to check.\n'
        message += '  arg2...         Specify the attribute you want to check.\n'
    else:
        message = ''

    return ut.code_block_fix(message)