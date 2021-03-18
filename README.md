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
공통점<br/>

![image](https://user-images.githubusercontent.com/44639709/111310732-c3a21200-86a0-11eb-9040-34959b61a24d.png)

차이점<br/>

![image](https://user-images.githubusercontent.com/44639709/111310798-d3215b00-86a0-11eb-980a-bd4b999e97c8.png)
<br/>
ex > list[idx] => pop 할 경우 값이 달라질 수 있으나 dict['key'] 의 경우, key 를 기준으로 사용하므로 달라지지 않는다.<br/>
ex > dict1.update(dict2) 를 할 경우, dict1 과 중복되는건 dict2 로 엎어지고 추가한다.

## 튜플
- 한번 정해진 순서를 바꿀 수 없다.
튜플 선언

<pre>
<code>
tuple1 = (1, 2, 3, 4)

tuple2 = 1, 2, 3, 4

mylist = [1,2,3,4]
tuple3 = tuple(mylist)
</code>
</pre>

- 튜플은 값의 변경과 삭제가 불가능

## 튜플을 이용한 packing, unpacking
- packing
: 하나의 변수에 여러개의 값을 넣는 것
- unpacking
: 패킹된 변수에서 여러개의 값을 꺼내오는 것
<pre>
<code>
c = (3, 4)
d, e = c    # c의 값을 언패킹하여 d, e에 값을 넣었다
f = d, e    # 변수 d와 e를 f에 패킹
</code>
</pre>

- 튜플의 활용
1) 두 변수의 값을 바꿀 때 임시변수가 필요 없다.
    ex> x,y = y,x
2) 함수의 리턴 값으로 여러 값을 전달할 수 있다.
    ex> return 1,2,3,4...
