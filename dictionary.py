
dict = {'b' : 'beijing', 's' : 'shanghai', 'w' : 'wuhan', 'g' : 'guangzhou'}
print (dict)
print("\n")

#search
print(dict['b'])
print (dict.get('b'))

#add
dict['a'] = 'Sydney'
print(dict)

#modify
dict['w'] = 'Wuchang'
print(dict)

#items方法主要用于实现字典的遍历操作，返回的是由若干元组组成的列表。
print(dict.items())

#delete
dict.pop('s')
print(dict)

#keys方法用于返回字典中的key的列表。
print(dict.keys())

#values方法用于返回字典中的value的列表。
print(dict.values())