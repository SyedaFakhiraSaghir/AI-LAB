class Environment:
 def displayEnvironment(self):
     for i in range(len(self.components)):
       if self.vulnerability[i]=='Safe':
         print(f'{self.components[i]} : safe ✔' )
       elif self.vulnerability[i]=='Low Risk Vulnerable':
         print(f'{self.components[i]} : Low Risk Vulnerable ⚠')
       else:
         print(f'{self.components[i]} : High Risk Vulnerable ❌')
 def __init__(self):
   # components are a part of the environment
   import random
   # 0 VULNERABLE 1 SAFE
   # critical components
   self.components=['A','B','C','D','E','F','G','H','I']
   self.vulnerability={}
   for i in range(len(self.components)):
     self.vulnerability[i]=random.choice(['Safe', 'Low Risk Vulnerable', "High Risk Vulnerable"])
   self.displayEnvironment()




class SecurityAgent:
 def __init__(self):
   self.patch_list=[]
   pass


 def scanComponent(self,env):
   for i in range(len(env.components)):
       if env.vulnerability[i]=='Safe':
         print(f'success {env.components[i]} is safe ✅' )
       elif env.vulnerability[i]=='Low Risk Vulnerable':
         print(f'warning!! component {env.components[i]} is Low Risk Vulnerable ⚠')
         self.patch_list.append(env.components[i])
       else:
         print(f'WARNING!!!! component {env.components[i]} is High Risk Vulnerable ❌')
         self.patch_list.append(env.components[i])


 def patchComponents(self, env):
   for i in range(len(env.components)):
       if env.vulnerability[i]=='Low Risk Vulnerable':
         print(f'patching {env.components[i]} \n patched {env.components[i]}')
         env.vulnerability[i]=='Safe'
       else:
         print(f'premium service needed to patch {env.components[i]}')


 def final_check(self,env):
   for i in range(len(env.components)):
       if env.vulnerability[i]=='Safe':
         print(f'{env.components[i]} is safe ✅' )
       elif env.vulnerability[i]=='Low Risk Vulnerable':
         print(f'component {env.components[i]} is Low Risk Vulnerable and has not been patched')


       else:
         print(f'WARNING!!!! component {env.components[i]} needs premiun service')




def runAgent(agent, env):
 for i in range(len(env.components)):
   agent.scanComponent(env)
 agent.patchComponents(env)


agent = SecurityAgent()
env=  Environment()
runAgent(agent,env)
for i in range(len(env.components)):
 if env.vulnerability[i]==1:
   print(f'component {env.components[i]} is unsafe ⚠')
 else:
   print(f'component {env.components[i]} is safe ✔')
