import json

def stringify(obj):
    return json.dumps(obj)
def parseJson(string):
    try:
        return json.loads(string)
        #pass
    except:
        return string