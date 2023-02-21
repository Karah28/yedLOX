import sys


a = int(input("Int:"))     #int обозначает целое число

b =bool(input("bool:"))    #bool принимает True, False, для возвращения операции

c = input("String:")   #String обозначает строку

d = complex(input("Complex:"))
e = float(input("float:"))   #Float обозначает число с плавающей точкой

print("Int:", int(a))       #int обозначает целое число

print("bool:", bool(b))     #bool принимает True, False, для возвращения операции

print("String:", str(c))    #String обозначает строку

print("Complex:", complex(d))
print("float:", float(e))   #Float обозначает число с плавающей точкой

print("Max_Int:", (sys.maxsize))
print("Max_Float:", (sys.float_info.max))


print("cp1251:", len('я люблю динамическую типизацию'.encode('cp1251')))
print("Utf-8:", len('я люблю динамическую типизацию'.encode('utf-8')))
print("Utf-16:", len('я люблю динамическую типизацию'.encode('utf-16')))
print("Utf-32:", len('я люблю динамическую типизацию'.encode('utf-32')))




