#x = [4, 6, 1, 3, 5, 7, 25]
#y = []
#stars = ""
#for i in x:
#    y = str(x[i])
#    stars.extend("*" * y)
#    print stars
# I tryed doing it this way but got a alot of errors.
#    *********************************
#defining and setting genaric array
def stars (arr):
#    starting for loop in genearic array
    for x in arr:
#        calling a set of actions
        print "*" * x
#setting variables to be exacuted 
y = [4, 6, 1, 3, 5, 7, 25]
#calling function with given vareable
stars(y)
#defining new function
def stars2(arr):
#    start for look with ginaric array
    for x in arr:
#        if condition ( inside the insance variable check if            its an intager)
        if isinstance(x, int):
#            call action 
            print "*" * x
#        outherwise if condition is not met (check if                   instance is a string)
        elif isinstance(x, str):
#            set the length to be the length of the given                   string
            length = len(x)
#            set letter to be the first position of the given               string
            letter = x[0].lower()
#            call action
            print letter * length
#set variable 
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
#call fuction with praramaders of x
stars2(x)