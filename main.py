# Operations on List

myTuple = ()
print(myTuple)


myTuple = (1,2,3)
print(myTuple)


myTuple = (1,"Hello",3.14)
print(myTuple)


myTuple = ("Hello", [3,5,2] ,(2,5,8))
print(myTuple)



myTuple = ('T', 'A','N' ,'M', 'A' , 'Y')
print(myTuple[0])
print(myTuple[4])

print("Sliced" , myTuple[2:5])

for letter in(myTuple):
    print("Hello", letter)


nestedTuple = ("Hello", [3,5,2] ,(2,5,8))
print(nestedTuple[0][3])
print(nestedTuple[1][2])
print(nestedTuple[2][1])


