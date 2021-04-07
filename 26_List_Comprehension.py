
areas=[]

for i in range(1,11):
    if i%2 == 0:
        areas = areas + [i*i]
print(areas)

areas2 = [ i*i for i in range(1,11) if i%2 == 0 ]
print(areas2)

print( [ (x,y) for x in range (15) for y in range (15) ] )

print("\n딕셔너리\n")

students = ["태연",'진우','정현','하늘','성진']

for number, name in enumerate(students):
    print("{}번의 이름은 {} 입니다.".format(number,name))

students_dict = {"{}번".format(number+1) : name for number, name in enumerate(students) }

print(students_dict)

scores = [85, 92, 78, 90, 100]

for x,y in zip(students, scores):
    print(x,y)
    
score_dic = {student : score for student, score in zip(students, scores) }

print(score_dic)