#!/usr/bin/env python
import json
from lambda_function import lambda_handler


with open('test_event.json') as json_data:
    event = json.load(json_data)


response = lambda_handler(event, None)

print json.dumps(response, indent=4, sort_keys=True)
