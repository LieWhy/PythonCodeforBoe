sites={'gogoing','zhihu','zijie','yahoo','baidu'}

print(sites)

if 'zhihu' in sites:
    print('属于')
else:
    print('不属于')

a=set('abcdefghijklmnopqrst')

b=set('defghijklmn')

print(a)
print(a-b)
print(a^b)
print(a|b)
print(a&b)
