'''
클래스의 상속
subcalss 는 어떤 클래스로부터 상속을 받은 클래스를 의미한다.
subclass 관점에서 상속을 해준 부모 클래스를 super 클래스라고 한다.
super()함수는 부모 클래스를 반환한다
subclass로 부터 생성된 객체는 super 클래스의 모든 메소드를 사용할 수 있다
'''

class person:
  person_id:int = 0    # static variable
  def __init__(self, name:str="Unknown", age:int=0) -> None:
    """person 클래스의 생성자 입니다, name과 age속성을 초기화 합니다."""
    self.name = name    #person class의 name 속성에 파라미터 name의 값을 대입함
    self.age = age      #person class의 age 속성에 파라미터 age의 값을 대입함
    person.person_id += 1
    self.__id = person.person_id
    
  def __del__(self) -> None:
    print(f'{self}가 삭제됩니다.')
    
  def __str__(self) -> str:
    return f'{self.name} {type(self)}'
    
  def sayHello(self, msg:str="안녕하세요") -> str:
    """자기소개로 인사를 하는 메소드입니다."""
    return f'{msg}, 저의 이름은 {self.name}이고, 나이는 {self.age}살 입니다.'
  
  @classmethod
  def getLastId(cls) -> int:
    return cls.person_id
  
  @staticmethod
  def getType():
    return person
  

class student(person):
  '''person class로부터 상속을 받은 subclass'''
  def __init__(self, name: str = "Unknown", age: int = 0) -> None:
    super().__init__(name, age)
    self.__grade = self.__setGrade()
    
  def __setGrade(self) -> int:  # 메소드 이름에 언더바 2개를 붙여서 시작하면 private method 임
    """나이를 이용하여 학년을 결정하는 내부 메소드(private method)"""
    if self.age < 8:
      return 0
    elif self.age == 8:
      return 1
    elif self.age == 9:
      return 2
    elif self.age == 10:
      return 3
    else:
      return 4
    

          
iam = person("유재석, 10")
you = student("강호동", 10)
#you.__setGrade()     # private method는 외부에서 호출할 수 없음
# print(you.__grade)      # student 클래스의 grade 속성을 사용할 수 있음
# print(you.sayHello("반갑습니다"))   # person class의 sayHello() method를 사용할 수 있음

kang = student("강호동", 10)
kang.__id = 8
print(kang.__id)
