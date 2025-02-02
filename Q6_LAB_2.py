import random


class Environment:
 def __init__(self):
   self.rooms={}
   self.status={}


 def initialize(self):
   charr='a'
   print("++++++++++++++ initial state of rooms ++++++++++++++\n")
   for i in range(3):
     self.rooms[i] = {}
     self.status[i]={}
     for j in range(3):
       self.rooms[i][j]= charr
       if self.rooms[i][j] in ('a', 'b', 'd', 'f', 'g', 'h'):
         self.status[i][j]='safe'
       else:
         self.status[i][j]='fire'
       print(charr + ' '+ self.status[i][j]+ '\n')
      
       charr=chr(ord(charr)+1)
  def displayEnvironment(self):
   print("++++++++++++++___ Displaying Environment ___++++++++++++++\n")
   for i in range(3):
     for j in range(3):
       print('\n',self.status[i][j], self.rooms[i][j] , end=' ')
     print()


 def get_percept(self):
   return self.rooms, self.status


class Agent:
 def __init__(self):
   pass
  def put_out_fire(self, env):
   for i in range(3):
     for j in range(3):
       if env.status[i][j]=='fire':
         print(f'fire in room {env.rooms[i][j]} 🔥❗ extinguishing fire now 🧯')
         env.status[i][j]='safe'
       else:
         print(f'no fire in room {env.rooms[i][j]} ✅')
       env.displayEnvironment()


def runAgent(agent, env):
   env.initialize()
   agent.put_out_fire(env)
  
env= Environment()
agent=Agent()
runAgent(agent,env)
