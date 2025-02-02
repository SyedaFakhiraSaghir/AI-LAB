class environment:
 def __init__(self,n):
   self.tasks={}
   import random
   for i in range(n):
     self.tasks[i]=random.choice(["Completed","Failed"])


 def get_percept(self):
   return self.tasks


class BackupManagementAgent:
 def __init__(self):
   pass
  
 def retryFailedTasks(self, env):
   for i in range(len(env.tasks)):
     if env.tasks[i] == "Failed":
       env.tasks[i] = "Completed"
       print(f"Task {i} is completed ✅")
     else:
       print(f"Task {i} is already completed ❕")


def runAgent(agent, env):
 print(f"tasks before retrying \n{env.tasks}\n")
 agent.retryFailedTasks(env)
 print(f"tasks after retrying \n{env.tasks}\n")


env=environment(10)
agent=BackupManagementAgent()
runAgent(agent,env)
