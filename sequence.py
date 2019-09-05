n = int(input("Enter the length of the sequence: "))
counter = 4
x1 = 1
x2 = 2
x3 = 3
print(x1,x2,x3,end=' ')
while counter <= n:
    sum_ = x1+x2+x3
    print(sum_,end=' ')
    x1 = x2 
    x2 = x3
    x3=sum_
    counter = counter + 1
    



