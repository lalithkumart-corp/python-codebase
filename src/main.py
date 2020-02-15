
# Without using __init__.py file
import folder2.stringUpper
print(folder2.stringUpper.stringToUpper('hello'))


#With __init__.py file
from folder3.folder3utils import stringify, parseJson
print(stringify({'msg': 'hello'}))
print(parseJson('{msg: "hello"}'))


#With __init__.py file
from folder4 import *
print(stringify4({'msg': 'hello'}))
print(parseJson4('{msg: "hello"}'))