class C:
    def __init__(self):
        print("class C의 인스턴스가 생성")
        self.name = "ccc" 
        self.age = 0

    def say_hi(self):
        print("hi")

    def add_age(self, n:int):
        self.age += n

    def __str__(self):
        return "__str__ 호출됨"

    def __repr(self):
        return "__repr__ 호출됨"

    def __abs__(self):
        print("__abs__ 호출됨")
  
    def __len__(self):
        pirnt("__len__ 호출됨")

    def __add__(self, other):
        return self.age + other.age
