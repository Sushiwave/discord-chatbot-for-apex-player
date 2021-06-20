from . import util as ut





def no_info_found(valid_value_list, invalid_value_list, value_type):
    message = 'No information found on the specified '
    message += value_type.lower()+' [ '
    for invalid_opt in invalid_value_list:
        message += invalid_opt+', '
    message = message[:-2]+' ].\n\n'
    message += value_type+'\n'
    for v in valid_value_list:
        message += '  ・'+v+"\n"
    return ut.code_block_fix(message)
