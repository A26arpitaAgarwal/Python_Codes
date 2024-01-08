#lambda function
def func(fx, value):
    return 6 + fx(value)
print(func(lambda x:x*x*x,2))
    
