'''
Thread와 공유 자원,
Thread의 종료
'''
import threading
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
    self.thread = threading.Thread(target=self.__run)
    self.thread.start()    
    
  @property
  def id(self) -> str:
    return f'ThreadWrapper : {self.__id}'
  
  def __run(self) -> any: pass
  

class Tickekter(ThreadWrapper):
  def __init__(self) -> None:
    super().__init__()
    self.pub_tickets = None
    self.prv_tickets = []
    # print(Tickekter.__dir__)
  
  def __str__(self) -> str:
    return str(self.prv_tickets)
    
  def setTicketCount(self, liTicket:list) -> None:
    self.pub_tickets = liTicket
    
  def startGetTicket(self):
    self.start()
    
  def __run(self) -> any:
    index = 0
    while True:
      if len(self.pub_tickets) <= 0:
        break
      
      self.prv_tickets.append(self.pub_tickets.pop())
       
    return super().__run()
  
if __name__ == '__main__':
  tickets = ['ticket1', 'ticket2', 'ticket3']
  th = Tickekter()
  th.setTicketCount(tickets)
  th.start()
  print(dir(th))
  print(th.__class__)
  print(type(th))
  
  
  
# tickets = ['ticket1', 'ticket2', 'ticket3']
# ts = []
# for i in range(3):
#   t = Tickekter()
#   t.setTicketCount(tickets)
#   ts.append(t)
  
# for t in ts:
#   t.startGetTicket()
  
# for t in ts:
#   print(t)
