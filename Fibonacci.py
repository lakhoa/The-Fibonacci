#0 1 2 3 5 8 13 21 33 54 87 141 228 369 597....

def fibonacci(n):
    i = 2
    sum = [0,1]
    while i < n:
        int(sum[i-2])
        int(sum[i-1])
        sum = sum + [""]
        sum[i] = sum[i-1]+sum[i-2]
        i = i+1
    return(sum)


while True:
    m= input("You want a string (s) or a number (n)_s/n : ")
    if m =='s':   
        x = int(input("Enter the string of fibonacci : "))
        print(fibonacci(x))
        print("")
        p = input("Do you want continue _ y/n : ")
        if p== 'y':
            continue
        elif p=='n':
            break
        else:
            print("Enter not correct !")
            break
    elif m =='n':
        y = int(input("Enter the numerical order of fibonacci you want : "))
        z = fibonacci(y)
        print("Number in ",y, " in fibonacci is : ",z[y-1])
        print("")
        p = input("Do you want continue _ y/n : ")
        if p == 'y':
            continue
        elif p=='n':
            break
        else:
            print("Enter not correct !")
            break
    else:
        print("Enter not correct !_Please try again !")
        print("")
        p = input("Do you want continue _ y/n : ")
        if p == 'y':
            continue
        elif p=='n':
            break
        else:
            print("Enter not correct !")
            break



'''
a= [1,2,3]
b=[7,8,2]
c=list('3')
print(type(c))
print(a+c)
print(int(c[0]))
'''