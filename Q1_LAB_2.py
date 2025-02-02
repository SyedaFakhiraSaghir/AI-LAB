class Environment:
 def __init__(self):
   # components are a part of the environment
   import random
   # 0 VULNERABLE 1 SAFE
   # critical components
   self.components=['A','B','C','D','E','F','G','H','I']
   self.vulnerability=[]
   for i in range(len(self.components)):
     self.vulnerability.append(random.randint(0,1))
     if self.vulnerability[i]==1:
       print(f'component {self.components[i]} is safe ✔' )
     else :
       print(f'component {self.components[i]} is vulnerable ⚠')


class SecurityAgent:
 def __init__(self):
   self.patch_list=[]
   pass


 def scanComponent(self,percept,component):
   if percept == 1:
     print("warning! vulnerable component detected ⚠")
     self.patch_list.append(component)
   else:
     print("success! component is safe ✔")


 def patchComponents(self, Env):
   for component in self.patch_list:
     print(f'patching {component}')
     index = env.components.index(component)
     env.vulnerability[index] = 0 
     print(f'patched {component}')


def run_agent(agent, env):
 for i in range(len(env.components)):
   agent.scanComponent(env.vulnerability[i],env.components[i])
 agent.patchComponents(env)


agent = SecurityAgent()
env=  Environment()
run_agent(agent,env)
for i in range(len(env.components)):
 if env.vulnerability[i]==1:
   print(f'component {env.components[i]} is unsafe ⚠')
 else:
   print(f'component {env.components[i]} is safe ✔')
