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
    
## 튜플을 이용한 함수의 리턴값
- 튜플 리스트 활용
<pre>
<code>
for a in enumerate(list):
    print('{}번째 값: {}'.format(a[0], a[1]))

for a in enumerate(list):
    print('{}번째 값: {}'.format(*a))
</code>
</pre>

- 튜플 딕셔너리 활용
<pre>
<code>
for a in dict.items():
    print('{}의 나이는:{}'.format(a[0], a[1]))

for a in dict.items():
    print('{}의 나이는:{}'.format(*a))
</code>
</pre>

## while문
<pre>
<code>
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')
</code>
</pre>
for 반복문으로 작성한 코드는 while 반복문으로 작성 할 수 있다.

## try except 문

Index Error 처리의 경우, if index < len(list) else 형태로 구현 가능하다.
반면에, ImportError 와 같은 경우에는 try except 로만 가능하다
<pre>
<code>
except Exception as ex :
    print(ex)
</code>
</pre>
와 같은 형태로 발생한 예외의 종류를 알수있다.

raise Exception #(예외종류) 를 통해 예외를 발생시킬 수 있는데,
for문이 여러개일때 한번에 탈출하기위해 break 대신 raise StopIteration(Exception) 을 활용할 수도 있다.

- 단락평가란 파이썬에서 and or 연산도중 실행할 필요가 없으면 더이상 True False 연산을 진행하지않는 것을 말한다.

Bool(0) : Bool 함수는 0인 경우 False 를 나머지 숫지는 모두 True 를 리턴한다.
빈 딕셔너리나 리스트는 False 그 외에는 True 를 리턴한다.
None(아무 값 없음) 도 False 이며 빈문자열은 False 를 그 외 문자열은 모두 True 를 리턴한다.
이는 if 문에서 해당 문자열의 True False판단에도 적용된다.

value = input('입력주세요 > ') or 'No input'

으로도 단락평가를 이용할수있다

## List의 기능

list.index( value ) : 값을 이용하여 위치를 찾는 기능
list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가, 더하기 연산으로도 가능
list.insert( index, value ) : 원하는 위치에 값을 추가, - 는뒤부터 계산
인덱스 범위보다 클경우 마지막에 넣는다
list.sort( ) : 값을 순서대로 정렬
list.reverse( ) : 값을 역순으로 정렬

## List와 String
리스트와 문자열은 유사하다.
문자열도 배열 인덱스로 가져오거나 in 연산으로 포함여부 알수있고 위 리스트 기능도 사용가능하다
서로 변환이 가능하다.
list("str") 시 문자단위로 저장한다
list = str.split( ) : 문자열에서 리스트로 각 단어단위로 저장한다
혹은 split 함수인자로 구분자를 준다
" ".join( list ) : 리스트에서 문자열으로 만든다

## Slice
- 리스트나 문자열에서 값을 여러개 가져오는 기능

slice를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어 준다.
시작과 끝부분을 얻어 오는 방법

list[ 2: ] : 2번째부터 끝까지 반환
list[ : 2 ] : 처음부터 2번째 까지 반환 (end inx 전까지 )
list[ : ] : 처음부터 끝까지 전부 반환

## step
slice한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
list[ 시작값:끝값:step ]
큰값에서 작은값으로 step을 음수로 줄수도있다
