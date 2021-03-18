
list = [10,20,30,40,50]

for i, v in enumerate(list):
    print('{}번째 값 : {}'.format(i,v))

for a in enumerate(list):
    print('{}번째 값 : {}'.format(a[0], a[1]))
    
for a in enumerate(list):
    print('{}번째 값 : {}'.format(*a))

ages = {'Tod':35, 'Jane':23, 'Paul':62 }
for key, val in ages.items():
    print('{}의 나이는:{}'.format(key,val))
    
for a in ages.items():
    print('{}의 나이는:{}'.format(a[0],a[1]))
    
for a in ages.items():
    print('{}의 나이는:{}'.format(*a))