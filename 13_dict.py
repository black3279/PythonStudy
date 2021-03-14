
wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
    }
    
def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

result = rsp(input('가위바위보 ?'),'바위')

messages = {
    'win':'승리',
    'draw':'비김',
    'lose':'졌다'
}

print(messages[result])