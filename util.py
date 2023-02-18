import json

def formated(json_data):
    load = json.loads(json_data)
    dump = json.dumps(load, indent=4)
    return dump