def hello(name):
    return "hello" + name


def calcule(age):
    if age > 18:
        return 'person is adult'
    
    elif age<18:
        return 'Person is under age'
    
    else:
        return 'person is 18year old'
    

print(calcule(25))