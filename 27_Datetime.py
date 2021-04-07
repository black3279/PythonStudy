
import datetime

print(datetime.datetime.now())

start_time = datetime.datetime.now()
print(start_time, " / type : {}".format(type(start_time)) )

start_time = start_time.replace(year=2017, month=2, day=1)
print(start_time)

start_time = datetime.datetime(2022,2,1)

print(start_time)

how_long = start_time - datetime.datetime.now()

print(how_long, " / type : {}".format(type(how_long)))

print(how_long.days, how_long.seconds)

print("2월 1일까지는 {}일 {}시간이 남았습니다.".format(how_long.days, how_long.seconds//3600))

print("\ntimedelta!\n")

hundred = datetime.timedelta(days=100)

print(datetime.datetime.now() + hundred)

hundred_before = datetime.timedelta(days = - 100)
print(datetime.datetime.now() + hundred_before)

tomorrow = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days=1)

print(tomorrow)