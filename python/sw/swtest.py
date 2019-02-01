#!/usr/local/bin/python

import swgohhelp

creds = swgohhelp.settings('joenak', 'M3nt0s88!!2015', '123', 'abc')
client = swgohhelp.SWGOHhelp(creds)

allycode = 457519732 #me
allycod = 119521416 ##r

player = client.get_data('player', allycode)
guild = client.get_data('guild', allycode)

print(guild)
