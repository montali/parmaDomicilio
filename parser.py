import re, json
from collections import defaultdict
attivita = {}

regex =re.compile(r"(?P<activity>'[a-zA-Zòèàó3\.10 \-&'’]*) (?P<phone>'[\d]+ [\d]+)(?P<phone2>'[\d ]*) (?P<genre>'[a-zA-Z\-\/&'’]*)")
with open('altro', 'r') as fileLista:
    for linea in fileLista.readlines():
        m = regex.search(linea)
        if m.group('genre') not in attivita:
            attivita[m.group('genre')] = {"data": []}
        if m.group('phone2'):
            tel = [m.group('phone'),m.group('phone2')]
        else:
            tel = m.group('phone')
        thisActivity = {"name":m.group('activity'), "tel": tel}
        attivita[m.group('genre')]["data"].append(thisActivity)

with open('parsed.json', 'w') as outfile:
    json.dump(attivita, outfile)