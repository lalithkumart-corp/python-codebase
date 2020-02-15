import json # importing json module

class Utils:
    def stringify(self, obj):
        return json.dumps(obj)
    def parseJson(self, string):
        try:
            return json.loads(string)
            #pass
        except:
            return string
            #pass
