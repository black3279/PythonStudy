
class Human() :
    '''인간'''

    def create(name, weight) :
        person = Human()
        person.name = name
        person.weight = weight
        return person
        
    def eat(self) :
        self.weight += 0.1
        print("{}가 먹어서 {}kg 이 되었습니다".format(person.name, person.weight))
    
    def walk(person) :
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(person.name, person.weight))
        
    def speak(self, message) :
        print(message)
    
person = Human.create("철수", 60.5)

person.speak("안녕하세요.")

## 인자를 전달해주지 않을 경우 에러가 발생하는데 self 로 파라미터를 지정하면 생략 시, 인스턴스 자신을 매개로 실행한다.