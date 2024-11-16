"""def b(name):2221
    print("Hi",+name)

"""
    

fact=1

a=int(input("enter a number "))
if a<0:
    print("factorial does not exist")
elif a==0:
    print('factorial exist')

else:
    for i in range(1,a+1):
        fact=fact*i
    print('factorial of',a,'is',fact)    
    
    
    