'''
try...except...finally
'''

class calculator:
  def __init__(self) -> None: ...
  @staticmethod
  def sum(li:object) -> int:
    tot = 0
    # 아래와 같이 하면 li가 iterable이 아닌경우 런타임 에러가 발생함
    # for i in li:
    #   tot += i
    # return tot      
    try:
      for i in li:
        tot += i
    # except:
    #   print("argument is not iterable")
    #   return 0
    
    # except TypeError:
    #   print("TypeError가 발생함 : object is not iterable")
    #   return 0   
    except TypeError as e:
      print(f"에러발생 : {str(e)}")
      return 0  
    
    return tot
  
  @staticmethod
  def divide2(num1:int, num2:int) -> tuple:
    if num2==0:
      raise ZeroDivisionError("나눌 수는 0이 될 수 없습니다!!!")
    
    mok = 0
    nam = 0
    mok = num1 // num2
    nam = num1 % num2
    
    return (mok, nam)
  
  @staticmethod
  def divide(num1:int, num2:int) -> tuple:
    try:
      mok = 0
      nam = 0
      mok = num1 // num2
      nam = num1 % num2
    except ZeroDivisionError as e:
      print(f"에러발생 : {str(e)}")
      # return (0,0)
    except TypeError as e:
      print(f"에러발생 : {str(e)}")
      # return (0,0)
    except:
      print("알 수 없는 에러발생!!!")
      # return (0,0)
    finally:
      return (mok, nam)
    
class Person:
  def __init__(self) -> None:
    self.__name:str = "Unknown"
    

# kim = Person()
# print(kim.__name)

try:
  tp = calculator.divide2(10, 0)
except ZeroDivisionError as e:
  print(str(e))

  
  
# li = [i for i in range(1,11)]
# tot = calculator.sum(li)
# print(tot)

# num = 1
# tot = calculator.sum(num)
# print(tot)    
    
# str1 = "test"
# tot = calculator.sum(str1)
# print(tot)  

# tp = calculator.divide(10, 3)
# print(tp)

# tp = calculator.divide(2, 3)
# print(tp)

# tp = calculator.divide(2.3, 3.1)
# print(tp)

# tp = calculator.divide(0, 3)
# print(tp)

# tp = calculator.divide(3, 0)
# print(tp)

# tp = calculator.divide("str", "st")
# print(tp)