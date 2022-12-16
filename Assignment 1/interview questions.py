'''
str = "pynative"
print (str[1:3])

sampleList = ["Jon", "Kelly", "Jessa"]
sampleList.append("Scott")
print(sampleList)


def calculate(num1, num2=4):
    res = num1 * num2
    print(res)


calculate(5, 6)

var = "James" * 2  * 3
print(var)

x = 36 / 4 * (3+2) * 4 + 2
print(x)

var1 ="pooja"
var2 = "Jyoti"
var3 = "Shraddha"


var= "James Bond"
print(var[2::-1])

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]
print(listOne == listTwo)
print(listOne is listTwo)

for i in range(10, 15, 1):
  print( i, end=', ')

for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )

p, q, r = 10, 20 ,30
print(p, q, r)

valueOne = 5 ** 2
valueTwo = 5 ** 3
print(valueOne)
print(valueTwo)

salary = 8000
def printSalary():
  salary = 12000
  print("Salary:", salary)
printSalary()
print("Salary:", salary)

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

print(type([]))

def func1():
    x = 50
    return x
func1()
print(x)
'''
global x
x=20
def fun1():
    # your code to assign global x = 20
    fun1()
print(x)  # it should print 20

#print(type(0*FF))

print(type(range(5)))
aTuple = (1, 'Jhon', 1+3j)
print(aTuple[2:3])
print(type({}))

print(type(10))
str1='Jyoti\'Korade'
str2="""jyoti 'korade"""
print(str1)
print(str2)

x = 50
def fun1():
    x = 25
    print(x)
fun1()
print(x)
