class Cat:
    def __init__(self):
        self.sleepy = True
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def setAge(self, Age):
        self.age = Age
        print('set ago to {0}.'.format(Age))
    def showAge(self):
        print('{0} years old.'.format(self.age)) #__ 비공개 속성
    def snack(self):
        print("먀옹")

minyong = KoShort()
minyong.setAge(7)
minyong.snack() #자식에서 새로 지정한 스낵이 출력
minyong.showAge()
print(minyong.age)

print()
#########################
class Cat:
    def __init__(self):
        self.sleepy = True
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def snack_Kor(self):
        print("meow")

minyong = KoShort()

minyong.snack()
print(minyong.sleepy)

print()


class Cat:
    def __init__(self):
        self.sleepy = True
    def snack(self):
        print('myeo~')

class KoShort(Cat): #상속받기 위한 (부모클래스)
    def snack_Kor(self):
        print("야옹")

        
minyong = KoShort()

minyong.snack()
print(minyong.sleepy)

print()
#############################

class Person():
    nation = 'A nation'
    def __init__(self, country):
        self.nation = country
    def showNation(self):
        print(self.nation)

yune = Person('Korea')
yune.showNation()

#############################

