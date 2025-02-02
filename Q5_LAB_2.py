import random


class Environment:
   def __init__(self):
       self.locations = ['Corridor', 'Medicine Storage', 'Nurse Station', 'room_1', 'room_2', 'room_3']
       self.patients = {
           'room_1': {'id': 'P1', 'medicine': 'panadol', 'schedule': '1:00 AM'},
           'room_2': {'id': 'P2', 'medicine': 'Arinac', 'schedule': '2:00 PM'},
           'room_3': {'id': 'P3', 'medicine': 'Softin', 'schedule': '11:00 AM'}
       }
       self.staffAvaliability = random.choice([True, False])


   def getInfo(self, roomKey):
       return self.patients.get(roomKey)


class Agent:
   def __init__(self):
       self.location = 'Medicine Storage'
       self.medicineToDeliver = None


   def move(self, destination):
       print(f"moving from {self.location.replace('_', ' ')} to {destination.replace('_', ' ')}")
       self.location = destination


   def collectMedicine(self, medicine):
       if self.location == 'Medicine Storage':
           self.medicineToDeliver = medicine
           print(f"collected {medicine}.")
       else:
           print("medicine unavailable. go to medicine storage.")


   def verifyPatient(self, expectedId):
       print(f"scanned patient id: {expectedId}.")
       return True  # assuming successful verification for now


   def deliverMedicine(self, room, patientInfo):
       if self.location == room:
           if self.verifyPatient(patientInfo['id']):
               if self.medicineToDeliver == patientInfo['medicine']:
                   print(f"successfully delivered {self.medicineToDeliver} to {self.location.replace('_', ' ')} ✅")
                   self.medicineToDeliver = None
               else:
                   print(f"carrying the wrong medicine. expected {patientInfo['medicine']} ❌")
           else:
               print("id mismatch! 🚫")
       else:
           print("wrong room ⛔")


def runAgent(agent, env):
   for room, patientInfo in env.patients.items():
       agent.move('Medicine Storage')
       agent.collectMedicine(patientInfo['medicine'])
       agent.move(room)
       if not env.staffAvaliability:
           print("alert! assistance required from medical staff ⚠")
       agent.deliverMedicine(room, env.getInfo(room))


env = Environment()
agent = Agent()
runAgent(agent, env)
