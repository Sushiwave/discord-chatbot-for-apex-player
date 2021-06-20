from ....container                        import list       as l
from ....gameinfocontainer.base.attribute import attribute  as a
from ....gameinfocontainer.item.basic     import weapon     as w
from ....gameinfocontainer.item.basic     import grenade    as g
from ....gameinfocontainer.base.attribute import constant   as ac 





#https://apexlegends.fandom.com/wiki/Weapon
def parse_weapon_info(soup):
    weapon_html_list = soup.select('body > #global-wrapper > #pageWrapper > #content > #bodyContent > #mw-content-text > div > table > tbody')[0].find_all('tr')
    del weapon_html_list[0]

    weapon_info = {}
    for weapon_html in weapon_html_list:
        attrib_html_list = weapon_html.find_all('td')
        attrib_html_list = l.delm(attrib_html_list, [1, 2, 3, 11])
    
        attrib_text_list = []
        for attrib_html in attrib_html_list:
            attrib_text_list.append(attrib_html.getText().replace('\n', ''))

        name        = a.attribute(ac.ATTRIBUTE_NAME_NAME,        attrib_text_list[0])
        body_damage = a.attribute(ac.ATTRIBUTE_NAME_BODY_DAMAGE, attrib_text_list[1])
        head_damage = a.attribute(ac.ATTRIBUTE_NAME_HEAD_DAMAGE, attrib_text_list[2])
        leg_damage  = a.attribute(ac.ATTRIBUTE_NAME_LEG_DAMAGE,  attrib_text_list[3])
        mag_size    = a.attribute(ac.ATTRIBUTE_NAME_MAG_SIZE,    attrib_text_list[4])
        RPM         = a.attribute(ac.ATTRIBUTE_NAME_RPM,         attrib_text_list[5])
        body_dps    = a.attribute(ac.ATTRIBUTE_NAME_BODY_DPS,    attrib_text_list[6])
        UPS         = a.attribute(ac.ATTRIBUTE_NAME_UPS,         attrib_text_list[7])

        weapon_info[name.value] = w.weapon(name, body_damage, head_damage, leg_damage, mag_size, RPM, body_dps, UPS)

    return weapon_info



#https://apexlegends.fandom.com/wiki/Grenade
def parse_grenade_info(soup):
    grenade_html_list = soup.select('body > #global-wrapper > #pageWrapper > #content > #bodyContent > #mw-content-text > div')[0].find_all('div', class_='ability-container')

    grenade_info = {}
    for grenade_html in grenade_html_list:
        attrib_html_list = grenade_html.find('table').find_all('tr')
        del attrib_html_list[1]
        del attrib_html_list[2]

        attrib_text_list = []
        for i,attrib_html in enumerate(attrib_html_list):
            attrib_text_list.append(attrib_html.getText().split('\n')[-2])
        
        info_html_list = grenade_html.find('div').find('div').find('div').find('ul').find_all('li')
        info_text = ''
        for info_html in info_html_list:
            info_text += '・'+info_html.getText().replace('  ', ' ')+'\n'

        attrib_text_list.append(info_text)

        name          = a.attribute(ac.ATTRIBUTE_NAME_NAME,          attrib_text_list[0])
        ignition_time = a.attribute(ac.ATTRIBUTE_NAME_IGNITION_TIME, attrib_text_list[1])
        info          = a.attribute(ac.ATTRIBUTE_NAME_INFO,          attrib_text_list[2])
        
        grenade_info[name.value] = g.grenade(name, ignition_time, info)

    return grenade_info

            