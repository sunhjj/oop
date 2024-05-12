'''
파이썬의 특별한 Variables
'''
import pickle
from typing import Any
from typing_extensions import SupportsIndex



a = 10
b = 20
str1 = "hello python"

# read-only 변수로 변경 불가능
# __name__ = "__sec11__"

# module_name = "__sec11__"
# __name__ = module_name

print(__name__) # 해당 모듈의 이름을 반환한다.
print(__doc__)  # 해당 모듈의 doc. string을 반환한다.
print(__file__) # 해당 모듈의 파일 경로를 반환한다


print(print.__name__) # 해당 오브젝트의 이름을 반환한다.
print(print.__qualname__) # 해당 오브젝트의 경로 이름을 반환한다.

print(print.__module__) # 해당 오브젝트의 모듈명을 반환한다


# 함수(메소드)의 오버로딩 구현
def myFunction(a:str|object=None) -> None:
  if isinstance(a, str):
    print(a)
  elif isinstance(a, object):
    print(help(a))
  else:
    print("None object")
    
    
# 함수(메소드)의 오버로딩 구현으로 인한 오류를 최대한 회피하기
def Add(a:int|float|str=0, b:int|float|str=0) -> int|float|str|None:
  if isinstance(a, int) and isinstance(a, float) and isinstance(a, str):
    return None
  
  if isinstance(b, int) and isinstance(b, float) and isinstance(b, str):
    return None
  
  if isinstance(a,str) and not isinstance(b, str):
    return None
  
  if isinstance(b,str) and not isinstance(a, str):
    return None
  
  c = 0
  try:
    c = a + b
  except TypeError as e:
    raise TypeError(f"TypeError : {a}와 {b}로 더하기 연산을 수행할 수 없습니다.")
  except ValueError as e:
    raise ValueError(f"ValueError : {a}와 {b}로 더하기 연산을 수행할 수 없습니다.")
  except:
    return f"Unknown Error : {a}와 {b}로 더하기 연산을 수행할 수 없습니다."
  
  return c

  
print(Add(1, 1.0))
print(Add(2, 2))
print(Add('2', 2))
print(Add('2', '2'))
print(Add(3, -1))
print(Add(3))
    
# myFunction(a)
# myFunction(str1)
# myFunction()
# print(a.__pow__)


class Person:
  '''Person 클래스입니다. name, age 멤버 변수를 갖습니다, hi propery도 있습니다.'''
  
  
  instances = {}
  subclasses = 0
  
  def __init__(self, name:str|object=None, age:int=0) -> None:
    super().__init__()
    self.name = name
    self.age = age if isinstance(age, int) else 0
    
  # 객체를 문자열로 나타냄
  def __str__(self) -> str:
    return str(self.name)
  
  # 객체의 공식적인 문자열을 반환하며, 리턴되는 문자열값이 eval함수등에서 표현이 가능해야 함
  # __str__이 구현되지 않은 경우 __str__을 대신함
  def __repr__(self) -> str:    
    return f'Person(name={self.name}, age={self.age})'
  
  # format() 내장 함수(built-in function)를 지원함
  def __format__(self, __format_spec: str) -> str:
    if __format_spec==None:
      return ""
    
    if __format_spec=="name":
      return f"{self.name}"
    
    if __format_spec=="age":
      return f"{self.age}"
    
    return ""
  
  # 객체들간의 비교를 위해 == 연산자를 지원하기 위해 구현한다
  # __eq__와 반대로 __ne__ 가 있다
  # __gt__, __ge__, __lt__, __le__
  def __eq__(self, __value: object) -> bool:
    if not isinstance(__value, Person):
      raise TypeError(f"{type(__value)} 은(는) Person 클래스 또는 그 서브 클래스가 아닙니다.")
    
    return self.age == __value.age
  
  # 객체를 함수처럼 사용할 수 있게 해주는 메소드
  # *는 리스트 타입이며, **는 dict 타입이다.   ex) kim(5), lee(10) 
  def __call__(self, *args: Any, **kwds: Any) -> Any:
    self.age += args[0]
    return self.age
  
  # def hi(self) -> str:
  #   return f'안녕하세요, 저는 {self.name}이고 나이는 {self.age}살 입니다.'   
  
  # hi라는 메소드가 속성(멤버변수)처럼 활용됨
  @property
  def hi(self) ->str:
    return f'안녕하세요, 저는 {self.name}이고 나이는 {self.age}살 입니다.'
  
  # 주어진 속성을 삭제함
  def __delattr__(self, __name: str) -> None:
    print(f"{__name} 속성을 삭제합니다!!!")  
    super().__delattr__(__name)
    
  # 주어진 속성에 접근을 시도할때 자동으로 호출됨, 일종의 객체의 속성 접근을 후킹하는 것임
  # def __getattribute__(self, __name: str) -> Any:
  #   print(f'{__name} 속성에 접근을 시도함!!!')
  #   return super().__getattribute__(__name)
    
  # hash()함수를 지원하기 위한 메소드이며, 
  # 객체의 무결성을 보장하기 위해 hash() 지원 여부를 결정한다.
  def __hash__(self) -> int:
    return hash((self.name, self.age))
  
  # __init__ 보다 먼저 호출되는 메소드
  # __new__를 이용하여 Singleton 객체를 생성할 수 있으나...
  # 어디까지나 개념적인것으로, 여전히 헛점이 존해한다.
  def __new__(cls, obj:str=None, age:int=0):
    return super().__new__(cls)    
  
  # 서브클래스가 상속을 받을때 호출됨
  def __init_subclass__(cls) -> None:
    print(cls)
    cls.subclasses += 1     # 여기서 cls:class는 Student class임에 주의!!!
    return super().__init_subclass__()
  
  @classmethod
  def getSubClassCount(cls) -> int:
    return cls.subclasses
  

  
    
class Student(Person):
  '''
  Student 클래스입니다. name, age, grade 멤버 변수를 갖습니다
  '''
  
  def __init__(self, name: str = None, age:int=0, grade:int=1) -> None:
    super().__init__(name)
    self.grade = 1
    
  def setGrade(self, grade:int=1) -> None:
    self.grade = grade
    
  # 속성(멤버 변수)값에 접근하기 전에 수행되는 메소드
  def __setattr__(self, __name: str, __value: Any) -> None:
    if __name=='grade' and isinstance(__value, int):
      self.age = __value + 7
    super().__setattr__(__name, __value)
    
  def __sizeof__(self) -> int:
    return super().__sizeof__()
  
  # 데이터 Serializing을 지원하기 위한 메소드
  def __reduce__(self) -> str | tuple[Any, ...]:
    return (self.__class__, (self.name, self.age, self.grade))
  
  def __reduce_ex__(self, __protocol: SupportsIndex) -> str | tuple[Any, ...]:
    return (self.__class__, (self.name, self.age, self.grade))
  
  def __new__(cls, obj:str=None, age:int=0, grade:int=1):
    return super().__new__(cls)      
  
  # 잘못된 정보를 줄 수 있음에 유의!!!
  def __sizeof__(self) -> int:
    # return 1
    return super().__sizeof__()
  
  # isinstance()를 지원하기 위한 메소드
  def __instancecheck__(self, __instance: Any) -> bool:
    return super().__instancecheck__(__instance)
  
  def __subclasscheck__(self, __subclass: type) -> bool:
    return super().__subclasscheck__(__subclass)
  
  # int 타입을 파라미터로 받으면 int타입을 반환하도록...
  def __add__(self, val:int) -> int:
    return self.age + val
  
  def __radd__(self, val:int) -> int:
    self.age += val
    return self.age
    

    
print()
print("클래스의 특별한 멤버 변수와 메소드들!!!")

kim = Person()
lee = Person("Lee")
park = Student("Park")
choi = Student()
jung = Student(100)
song = Student({"banana":"바나나"})

print(kim)  # __str__ 메소드가 구현되어 있으면 __str__메소드의 반환값으로, 아니면 __repr__메소드의 반환값으로 표현됨
print(lee)
print(park)
print(choi)
print(jung)
print(song)

print(park.__doc__) # 클래스의 docstring이 없으면 아무값도 갖고 있지 않음
print(kim.__doc__)  # 클래스의 docstring을 출력
print(dir(kim))     # kim 객체의 멤버 변수들과 메소드들을 모두 반환

# __repr__의 활용
yoo = eval('Person(\'유재석\', 10)')
print(yoo)

# __format__ 메소드의 활용
print(format(yoo, 'name'))
print(format(yoo, 'age'))

# __eq__ 메소드의 활용
print(lee==park)
print(lee==yoo)

# __call__
print(yoo(5))
print(song.hi)
print(song(10))
print(song.hi)

# del song.name
# print(song)   # name 속성값이 삭제되어 런타임 에러가 발생함

print(hash(yoo))
print(song.setGrade.__qualname__)   # 소유권을 표현한 이름
song.setGrade()
print(song.hi)

# Serialize
data = pickle.dumps(song)
print(data)

# Unserialize
new_song = pickle.loads(data)
print(new_song.name)
print(new_song.age)
print(new_song.grade)
print()

print(f'Student Class의 상속 횟수 : {Student.getSubClassCount()}')

print(song.__sizeof__())

# __add__ 메소드 오버라이딩
sum_val = song + 1
print(f'sum_val = song + 1 의 결과 : {sum_val}')

a = 0
a += song
print(a)

# 이런게 가능하므로 싱글톤의 의미가 없어진다.
# 파이썬은 문화적(?)으로 OOP를 지향한다. 
# del kim.__class__.instances
# print(yoo.__class__.instances)