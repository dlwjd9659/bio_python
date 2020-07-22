class Person():
    s_str1 = 'str1'
    s_str2 = 'str2'
    def prtStr(self):
        out = self.s_str1 + self.s_str2
        print(out)
    def showS_str1(self):
        print(self.s_str1)

p1 = Person()
print(p1.s_str1) #사용x
p1.showS_str1() #위 대신 사용


p1.prtStr()





class Person:
    nation = 'A nation'
    def greeting(self):
        print('(method)greeting:', 'Hi')

    def hi1(self):
        self.greeting() #method greeting
    def hi2(self):
        greeting() #function greeting

def greeting():
    print('(function)greeting:', 'Hello!')

yune = Person()
yune.greeting()
print()
yune.hi1()
yune.hi2()

print()
########################

d_persons = {'Guilaume':'Canada','Niklas':'Germany','Mark':'USA','Alex':'Swiss','Alberto':'Italia'}
class Person():
    nation = 'A nation'
    name = 'username'
    def setName(self, target):
        self.name = target
    def findNation(self, d_dict):
        self.nation = d_dict[self.name]
    def showNation(self):
        print(d_persons[self.name])
    def showName(self):
        print(self.name)


yune = Person()
yune.setName('Mark')
yune.showNation()


print()
###################

#자료형 확인하기


out0 = isinstance(1, (int,str)) #int or str 을 묻는 형식
out1 = isinstance('aa', int)

print(out0)
print(out1)



print()
##################

class Person():
    nation = "A nation" #속성 = 변수

    def greeting(self): #메소드
        print('greeting!')
    def printNation(self):
        print(self.nation)
    def changeNation(self, target):
        self.nation = target
        print('changeNation to {}'.format(target))



yune = Person()
#print(yune.nation) #속성
#print(yune.printNation) #error 메소드는 () 필요
#print(yune.printNation())
yune.printNation()
yune.changeNation('Korea')
yune.printNation()
    

Person().printNation()


# if isinstance 


print()
##########################

class Coffee():
    numCoffee = 10
    def Hello(self):
        print('Hello')
        return "Hi!"


group1_coffee = Coffee()

print(group1_coffee.numCoffee) #10

group1_coffee.Hello()
