
class Human() :
    '''인간'''

    def __init__(self, name, weight) :
        '''초기화 함수'''
        '''print("__init__실행")
        print("이름은 {}, 몸무게는 {}".format(name,weight))'''
        
        self.name = name
        self.weight = weight
        
    def __str__(self) :
        '''문자열화 함수'''
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
        
    def create(name, weight) :
        person = Human()
        person.name = name
        person.weight = weight
        return person

    
person = Human("사람", 60.5)
print(person)


## 인자를 전달해주지 않을 경우 에러가 발생하는데 self 로 파라미터를 지정하면 생략 시, 인스턴스 자신을 매개로 실행한다.