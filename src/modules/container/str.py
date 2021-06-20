import difflib





def pick_most_similar_element(strlist_to_be_compared, str_to_be_compared):
    picked_element       = ''
    picked_element_index = -1
    maxRatio = -1
    for i,e in enumerate(strlist_to_be_compared): 
        ratio = difflib.SequenceMatcher(None, e.lower(), str_to_be_compared.lower()).ratio()
        if maxRatio < ratio:
            maxRatio = ratio
            picked_element = strlist_to_be_compared[i]
            picked_element_index = i
    return (picked_element_index, picked_element, maxRatio)