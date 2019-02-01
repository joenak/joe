#!/usr/local/bin/python

import swgohhelp

creds = swgohhelp.settings('joenak', 'M3nt0s88!!2015', '123', 'abc')
client = swgohhelp.SWGOHhelp(creds)

allycode = 457519732

#player = client.get_data('player', allycode)

guild = client.get_data('guild', allycode)

print(guild[0]['name'])
print(guild[0]['raid'])
print(guild[0]['members'])


for m in guild[0]['roster']:
    print('Name:' + m['name'] + ' - GP:' + str(m['gp']) + ' - lvl:' + str(m['level']) + ' - ally:' + str(m['allyCode']))