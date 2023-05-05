'''
Thread와 공유 자원,
Thread의 종료
'''
import threading, time
# from sec09 import ThreadWrapper

class ThreadWrapper:
  thread_id = 1
  def __init__(self) -> None:    
    self.thread = None
    self.__id = ThreadWrapper.thread_id
    ThreadWrapper.thread_id += 1
    
  def __str__(self) -> str:
    return f'ThreadWrapper(id={self.id})'
  
  def start(self) -> None:
    self.thread = threading.Thread(target=self.Run)
    self.thread.start()    
    
  @property
  def id(self) -> str:
    return f'ThreadWrapper : {self.__id}'
  
  def Run(self) -> any: pass
  

class Tickekter(ThreadWrapper):
  def __init__(self) -> None:
    super().__init__()
    self.pub_tickets = None
    self.prv_tickets = []
    # print(Tickekter.__dir__)
  
  def __str__(self) -> str:
    return str(self.prv_tickets)
    
  def setTickets(self, liTicket:list=[]) -> None:
    self.pub_tickets = liTicket
    
  def startTicketing(self):
    if len(self.pub_tickets):
      self.start()
    
  def Run(self) -> any:
    index = 0
    while True:
      time.sleep(0.1)
      if len(self.pub_tickets) <= 0:
        break
      
      self.prv_tickets.append(self.pub_tickets.pop())
       
    return super().Run()
  
if __name__ == '__main__':
  tickets = ['ticket1', 'ticket2', 'ticket3']

  ts = []
  for i in range(3):
    t = Tickekter()
    t.setTickets(tickets)
    ts.append(t)

  for t in ts:
    t.startTicketing()
    
  time.sleep(1)
  for t in ts:
    print(t)
    
  print()
  print(tickets)
  
