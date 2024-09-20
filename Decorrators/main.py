import my_dec as dec

@dec.check

def multiple(a, b):
    
    return a * b

a = input()
b = input()

result = multiple(a, b)

print(result)