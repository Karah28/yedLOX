import sys

a = 5

print("Int:", int(a))       #int обозначает целое число

print("bool:", bool(a))     #bool принимает True, False, для возвращения операции

print("String:", str(a))    #String обозначает строку

print("Complex:", complex(a))
print("float:", float(a))   #Float обозначает число с плавающей точкой

print("Max_Int:", (sys.maxsize))
print("Max_Float:", (sys.float_info.max))


print("cp1251:", len('я люблю динамическую типизацию'.encode('cp1251')))
print("Utf-8:", len('я люблю динамическую типизацию'.encode('utf-8')))
print("Utf-16:", len('я люблю динамическую типизацию'.encode('utf-16')))
print("Utf-32:", len('я люблю динамическую типизацию'.encode('utf-32')))




