import json

def stringify4(obj):
    return json.dumps(obj)
def parseJson4(string):
    try:
        return json.loads(string)
        #pass
    except:
        return string