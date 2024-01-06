# common sequence operation
# List,Tuple, Range
# List -> mutable
# Tuple -> immutable
# in

myTuple1 = ("Arafat", "Bohubrihi", 25)
myTuple2 = ("Hussain", )
myList = ["Arafar", "Bohubrihi", 25]
myRange = range(0, 51)

result = "Arafat" in myTuple1
print(result)


result = "Sakib" in myList
print(result)



result = 100 in myRange
print(result)



result = myTuple1 + myTuple2
myList.count("Arafat")
print(result)





# unpacking Tuples and lists
myTuple = ("Bangladesh", "Phalestine", "Iran")
c1, c2, c3 = myTuple

print(c1, c2, c3)


myList2 = ["Bangladesh", "Phalestine", "Iran", "Turkey", [1,2,3]]
c1, c2, c3, c4, [c5, c6, c7] = myList2

print(c1, c2, c3, c4, c5, c6, c7)





myList2 = ["Bangladesh", "Phalestine", "Iran", "Turkey"]
c1, c2, *c3 = myList2

print(c1, c2, c3)