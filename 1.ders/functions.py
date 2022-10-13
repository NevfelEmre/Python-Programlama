a = 5
def b():
    a = 10
    print(a)
def c():
    global a
    a = 10
    print(a)

b()      #10
print(a) #5
c()      #10
print(a) #10