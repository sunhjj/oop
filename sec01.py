'''
O : Object
O : Oriented
P : Programming

클래스를 디자인(설계)하여 객체들을 생성하고
객체들을 이용하여 프로그래밍하는 방법

클래스 : 객체의 설계 프로그램, 속성, 행위들을 정의하는 프로그램, list(), dict(), ...
객체 : 클래스로 생성되어 메모리에 로드된 인스턴스, li1 = list(), dic1 = dict()

클랙스의 기본
속성 과 메소드
생성자 와 소멸자
class 변수와 class 메소드 그리고... static 메소드

'''
# #객체 = 클래스
# li1 = list()
# li2 = list()
# li3 = list()

# class person:
  # def __init__(self) -> None:   # 생성자, Constructor
  #   self.name = "Unknown"   # person class의 멤버 변수 = 속성(Peroperty, attribute)
  #   self.age = 0
  #   __name__ = "person"
  
class person:
  person_id:int = 0    # static variable
  def __init__(self, name:str="Unknown", age:int=0) -> None:
    """person 클래스의 생성자 입니다, name과 age속성을 초기화 합니다."""
    self.name = name    #person class의 name 속성에 파라미터 name의 값을 대입함
    self.age = age      #person class의 age 속성에 파라미터 age의 값을 대입함
    person.person_id += 1   #self.person_id 가 아님에 주의!!!
    self.id = person.person_id
    
  def __del__(self) -> None:
    print(f'{self}가 삭제됩니다.')
    
  def __str__(self) -> str:
    return f'{self.name} {type(self)}'
    
  def sayHello(self, msg:str="안녕하세요") -> str:
    """자기소개로 인사를 하는 메소드입니다."""
    return f'{msg}, 저(id:{person.person_id})의 이름은 {self.name}이고, 나이는 {self.age}살 입니다.'
    
  @classmethod
  def getLastId(cls) -> int:
    return cls.person_id
  
  @staticmethod
  def getType():
    return person
    
  

def class_test() -> None:
  iam = person()
  print(iam)
  print(iam.sayHello())
  print(iam.id)

  iam = person("유재석", 10)
  print(iam.sayHello())
  print(iam.id)

  you = person("김종국", 7)
  print(you.sayHello())
  print(you.id)

  print(f'last person_id = {iam.getLastId()}')
  print(f'iam객체의 person_id??? = {iam.person_id}')
  
  print(f'person class의 타입 : {person.getType()}')
  print(type(person))
  
def another_fuction() -> None:
  print("class_test()를 호출후에 이 함수가 호출됩니다.")
  
class_test()
another_fuction()

print("프로그램이 종료됩니다!!!")