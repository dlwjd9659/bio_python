


##########################

class Student:
    def __init__(self, Kor, Eng, Mat):
        self.__kor = Kor
        self.__eng = Eng
        self.__mat = Mat
    def showKorean(self):
        print("Korean :",self.__kor)
    def showEnglish(self):
        print("English :",self.__eng)
    def showMath(self):
        print("Math :",self.__mat)
    def showEverage(self):
        total_s = self.__kor
        total_s += self.__eng
        total_s += self.__mat
        print(total_s/3)

yune = Student(Kor = 10, Eng = 20, Mat = 30)
yune.showMath()
yune.showEnglish()
yune.showKorean()
yune.showEverage()
