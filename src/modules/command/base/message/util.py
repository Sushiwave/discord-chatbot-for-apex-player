from ....gameinfocontainer.base.attribute import constant as c





def make_attrib_message(attrib):
    separate_name_and_value_with_new_line = True if '\n' in attrib.value else False
    separator = '\n' if separate_name_and_value_with_new_line else ' '
    return attrib.name+" :"+separator+attrib.value+"\n"



def code_block(text, tag=''):
    if len(text) == 0:
        return text 
    else:
        return '```'+tag+'\n'+text+'```'
    
def code_block_fix(text):
    return code_block(text, 'fix')