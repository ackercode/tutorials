#Defina exceptions customizadas em Python

class MyException(Exception):
    pass

raise MyException("Minha condição de erro")

#Result

#    raise MyException("Minha condição de erro")
#__main__.MyException: Minha condição de erro