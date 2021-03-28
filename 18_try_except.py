def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except:
        print('{} 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3], 5)
