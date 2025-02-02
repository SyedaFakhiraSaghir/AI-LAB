class Environment:
 def update_servers(self):
   for i in range(len(self.tasks)):
     if self.tasks[i] <= 4:
       self.servers[i]="Underloaded"
     elif self.tasks[i]>=6:
       self.servers[i]="Overloaded"
     else:
       self.servers[i]="Balanced"


 def __init__(self, n):
   self.tasks={}
   self.servers = {}
   import random
   for i in range(n):
     self.tasks[i]=random.randint(0,10)
   self.update_servers()


 def get_percept(self):
   return self.servers


class LoadBalancerAgent:
 def __init__(self):
   pass


 def balanceLoad(self, env):
       for i in range(len(env.servers)):
           if env.servers[i] == "Overloaded":
               balanced = False
               for j in range(len(env.servers)):
                   if env.servers[j] == "Underloaded" and i != j:
                       transfer = min(env.tasks[i] - 6, 4 - env.tasks[j])+1
                       if transfer > 0:
                           env.tasks[i] -= transfer
                           env.tasks[j] += transfer
                           env.update_servers()
                           print(f"{transfer} tasks are transferred from server {i} to server {j}")
                           balanced = True
                       if env.servers[i] != "Overloaded":
                           break
               if not balanced:
                   print(f"Balancing not possible at the moment for server {i}")


def runAgent(agent, env):
 print(f"servers before balancing \n{env.servers}\n")
 print(f"tasks before balancing \n{env.tasks}\n")
 agent.balanceLoad(env)
 print(env.servers)
 print(f"servers after balancing \n{env.servers}\n")
 print(f"tasks after balancing \n{env.tasks}\n")


env = Environment(5)
agent = LoadBalancerAgent()
runAgent(agent, env)
