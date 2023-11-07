#1 it will print 5
def a():
    return 5
print(a())

#2 it will print 5+5=10
def a():
    return 5
print(a()+a())
#3  It will print 5. The second return statement is unreachable.
def a():
    return 5
    return 10
print(a())
# 4  It will print 5. The print(10) statement is unreachable.
def a():
    return 5
    print(10)
print(a())
# 5 It will print 5 then x will be None, and it will print None.
def a():
    print(5)
x = a()
print(x)
# 6 It will print 3 (from the first function call) and then raise a TypeError because you can't add None (the return value of the second function call) to an integer
def a(b, c):
    print(b + c)
print(a(1, 2) + a(2, 3))
# 7  It will print "25" as a concatenated string of 2 and 5.
def a(b, c):
    return str(b) + str(c)
print(a(2, 5))
# 8 It will print 100
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#9 For the first call, it will print 7.
# For the second call, it will print 14.
# For the third line, it will print 7 + 14 = 21.
def a(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(a(2, 3))
print(a(5, 3))
print(a(2, 3) + a(5, 3))

#10  It will print 8 (3 + 5).
def a(b, c):
    return b + c
    return 10
print(a(3, 5))
# 11 It will print 500, 500, 300, 500.
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#12  It will print 500, 500, 300, 500.
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#13 It will print 500, 500, 300, 300.
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b = a()
print(b)
# 14  It will print 1, then raise an error because b() is called before it's defined.
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# 15 It will print 1, then 3, and then print 5, and finally print 10.
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
