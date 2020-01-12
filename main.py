# Check the versions of libraries

# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))


'''
PYTHON FOR DATA SCIENCE - LISTS
'''
squareList = [22, 43, 12, 76, 98, 27]
print(squareList)
print('\n\nItem at Index 0 = ',squareList[0])
print('\n\n Items from index 2 to 4 = ', squareList[2:4])
print('\n\nThe second last element of the list is :', squareList[-2])


from src.tutString import StringConcepts
rr = StringConcepts()
rr.handle()

from src.tuplesAndDict import TuplesDict
td = TuplesDict()
td.handle()

from src.iterations import Iterations
it = Iterations()
it.handle()