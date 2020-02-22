class Iterations:
    def handle(self):
        myData = {'name': 'lalith', 'age': 25}
        for i in myData:
            print(myData[i])

## Working with Tuples
    # Tuples are immutable. (Modification: "Cannot be modified". Deletion: "Cannot remove an individual item. It could be removed fully only")
    # Syntax:
        ''' 
            tup1 = ('physics', 'chemistry', 1997, 2000)
            tup2 = (1, 2, 3, 4, 5 )
            tup3 = "a", "b", "c", "d" 

        EMPTY TUPLE: 
            tup1 = ();

        SINGLE TUPLE:
            tup1 = (50,)
        '''

#1 --> iteration --> for in loop
for x in (1,2,3) : print (x, end = ' ')

#2 --> Membership --> exists?
res = 3 in (1, 2, 3)
print(res)

#3 --> Repetition
print( ('Hi!',) * 4 ) 

#4 --> length
print( len((1, 2, 3)) )

#5 --> Concatenation
print( (1, 2, 3) + (4, 5, 6) )

#6
atup1 = ('C++', 'Java', 'Python')
print(atup1[2])
print(atup1[-2])
print(atup1[1:])
