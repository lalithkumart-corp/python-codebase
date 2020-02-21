
# Without using __init__.py file
import folder2.stringUpper
print(folder2.stringUpper.stringToUpper('hello'))


#With __init__.py file
from folder3.folder3utils import stringify, parseJson
print(stringify({'msg': 'hello'}))
print(parseJson('{msg: "hello"}'))

#With __init__.py file
from folder4 import stringify4, parseJson4
print(stringify4({'msg': 'hello'}))
print(parseJson4('{msg: "hello"}'))

#With __init__.py file
from folder4 import *
print(stringify4({'msg': 'hello'}))
print(parseJson4('{msg: "hello"}'))

#With __init__.py file
import folder4
print(folder4.stringify4({'msg': 'hello'}))
print(folder4.parseJson4('{msg: "hello"}'))

from carrierEasypost import Rate, Shipment
r1 = Rate()
print(r1.getRates())
