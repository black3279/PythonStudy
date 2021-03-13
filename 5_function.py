
def function_name1(a) :
    return a*a
    
def print_round(a) :
    print('{}'.format(round(a)))
    return round(a)

a=1
b=2
c=3

print('Function Test 1 : {} 2 : {}'.format(a+b, b+c) )

print('Function Test 2 : {} / {} / {} '.format(function_name1(a), function_name1(b), function_name1(c) ) )

print('Function Test 3 : {} / {}'.format(print_round(6.2), print_round(7.5)))

