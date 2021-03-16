# PythonStudy

## REPL
1) Powershell에서 파일 이름 없이 python이라고만 입력하면 나오는 창
2) 파이썬 코드를 한 줄씩 입력해 가면서 테스트 해 볼 수 있는 입력창
3) REPL창을 종료하려면 exit()라고 입력

## 모듈
- 미리 만들어진 코드를 가져와 쓰는 방법
- import <모듈이름>
- 사용 : <모듈이름>.<모듈안의 구성요소>
- ex > math.pi / random.choice()

## 딕셔너리
- 여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능으로 이름표를 이용하여 값을 꺼내 사용한다.
- 사용할 때는 리스트와 비슷한 방식으로 사용한다.
<pre>
<code>
wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위',
}

print(wintable['가위'])
</code>
</pre>

## 딕셔너리 수정하기
추가
dict['three'] = 3

수정
dict['one'] = 11

삭제
del(dict['one'])
dict.pop('two')

## 리스트와 비교
공통점
![image](https://user-images.githubusercontent.com/44639709/111310732-c3a21200-86a0-11eb-9040-34959b61a24d.png)

차이점
![image](https://user-images.githubusercontent.com/44639709/111310798-d3215b00-86a0-11eb-980a-bd4b999e97c8.png)

ex > list[idx] => pop 할 경우 값이 달라질 수 있으나 dict['key'] 의 경우, key 를 기준으로 사용하므로 달라지지 않는다.
ex > dict1.update(dict2) 를 할 경우, dict1 과 중복되는건 dict2 로 엎어지고 추가한다.
