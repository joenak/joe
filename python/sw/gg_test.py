#!/usr/local/bin/python

import coreapi

client = coreapi.Client()
schema = client.get("https://swgoh.gg/api/")

action = ["player", "read"]
params = {
    "ally_code": 457519732
}

result = client.action(schmea, action, params=params)