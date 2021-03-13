
patterns = ['가위', '바위', '보', '보', '바위', '가위', '가위', '보', '바위']

for pattern in patterns :
    print(pattern)
    
for i in [0,1,2,3,4,5] :
    print(i)
    
for i in range(10) :
    print(i)
    
names = ['철수','영희','바둑이','귀도']

for i in range(len(names)):
    print('{}번 : {}'.format(i+1, names[i]) )
    
for i, name in enumerate(names):
    print('{}번 : {}'.format(i+1, name) )
    
for i in range(11172) :
    print(chr(44032 + i), end='')

