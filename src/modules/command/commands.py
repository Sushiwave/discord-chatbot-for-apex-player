from discord.ext        import commands as c

from ..scraper.apexwiki import scraper  as sc

from ..container        import str      as st

from .base.message      import util     as ut
from .base.message      import error    as er
from .base.message      import help     as h

from .base.ctx          import ctx      as ct





SIMILARIY_THRESHOLD = 0.5

def make_gameinfo_attribute_message(gameinfocontainer_dict):
    attrib_list = gameinfocontainer_dict[next(iter(gameinfocontainer_dict))].attrib_list
    attrib_name_list = [n.name for n in attrib_list]
    message = ''
    for an in attrib_name_list:
        message += "・"+an+"\n"
    return ut.code_block_fix(message)

def make_gameinfo_message(gameinfocontainer_dict, arg1_name, arg2_attributes, gameinfocontainer_str):
    message_list = []

    #Options
    if arg1_name == '--attribute':
        return [make_gameinfo_attribute_message(gameinfocontainer_dict)]
    elif arg1_name == '--all':
        for gameinfocontainer in gameinfocontainer_dict.values():
            message = ''
            for attrib in gameinfocontainer.attrib_list:
                message += ut.make_attrib_message(attrib)
            message += '\n'
            message_list.append(ut.code_block(message))
        
        return message_list

    #Default
    index_element_similarity = st.pick_most_similar_element(list(gameinfocontainer_dict.keys()), arg1_name)
    attribute_list = gameinfocontainer_dict[index_element_similarity[1]].attrib_list
    attribute_name_list = [a.name for a in attribute_list]
    similarity = index_element_similarity[2]

    if SIMILARIY_THRESHOLD < similarity:        

        if len(arg2_attributes) == 0:
            message = ''
            for attrib in attribute_list:
                message += ut.make_attrib_message(attrib)
            message_list.append(ut.code_block(message))
        else:
            displayed_attribute_list = []
            invalid_arg_list = []

            message = ''
            for arg_attrib in arg2_attributes:
                index_element_similarity = st.pick_most_similar_element(attribute_name_list, arg_attrib)
                attrib     = attribute_list[index_element_similarity[0]]
                similarity = index_element_similarity[2]

                if SIMILARIY_THRESHOLD < similarity:
                    if len(displayed_attribute_list) == len(attribute_list):
                        continue
                    if attrib in displayed_attribute_list:
                        continue

                    displayed_attribute_list.append(attrib)

                    message += ut.make_attrib_message(attrib)
                else:
                    invalid_arg_list.append(arg_attrib)

            message_list.append(ut.code_block(message))
            
            if 0 < len(invalid_arg_list):
                message_list.append(er.no_info_found(attribute_name_list, invalid_arg_list, 'Attribute'))
    else:
        message_list.append(er.no_info_found(list(gameinfocontainer_dict.keys()), [arg1_name], gameinfocontainer_str))
    
    message_list = [m for m in message_list if len(m) != 0]
    return message_list

@c.command()
async def weapon(ctx, arg1_name='', *arg2_attributes):
    await ct.send_message_list(ctx, make_gameinfo_message(sc.scrape_weapon_info(), arg1_name, arg2_attributes, 'Weapon'))

@c.command()
async def grenade(ctx, arg1_name='', *arg2_attributes):
    await ct.send_message_list(ctx, make_gameinfo_message(sc.scrape_grenade_info(), arg1_name, arg2_attributes, 'Grenade'))





@c.command()
async def help(ctx, arg1_name=''):   
    await ct.send(ctx, h.help())


