'''
class polymorphism(다형성)
메소드 오버라이딩
'''

class GameUnit:
  game_id = 1
  def __init__(self) -> None:
    self.name = "Undefined"
    self.hp = 100
    self.position = []
    self.speed = []
    self.power = 1
    self.id = GameUnit.game_id
    GameUnit.game_id += 1
    
  def __str__(self) -> str:
    return f'{self.name}({self.id}) : hp({self.hp})'
    
  def move(self, pos:list) -> None:
    self.position = pos.copy()
  
  def attack(self, unitTarget) -> None:
    unitTarget.hp -= self.power
  
  
class Scv(GameUnit):
  def __init__(self, pos:list) -> None:
    super().__init__()
    self.name = "SCV"
    self.position = pos.copy()
    self.speed = [2,2]
    
  def attack(self, unitTarget) -> None:
     super().attack(unitTarget)
     print(f"{self.name}이 {unitTarget.name}을 전동드릴로 공격합니다")
    

class Marine(GameUnit):
  def __init__(self, pos:list) -> None:
    super().__init__()
    self.name = "Marine"
    self.hp = 200
    self.power = 5
    self.position = pos.copy()
    self.speed = [3,3]
    
  def attack(self, unitTarget) -> None:
    super().attack(unitTarget)
    print(f"{self.name}이 {unitTarget.name}을 머신건으로 공격합니다")
    
    
scv1 = Scv([1,1])
print(scv1)

scv2 = Scv([2,2])
print(scv2)

marine1 = Marine([3,3])
print(marine1)

marine2 = Marine([3,3])
print(marine2)

enemy_scv = Scv([4,4])
print(enemy_scv)

print()

num = 1

li = [scv1, scv2, num, marine1, marine2]
for unit in li:
  if isinstance(unit, GameUnit):
    unit.attack(enemy_scv)
    print(enemy_scv)
    
  print()
  
  
  