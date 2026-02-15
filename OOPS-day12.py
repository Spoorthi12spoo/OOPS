#Polymorphism(Method overriding)

class RoyalMessenger:
    def deliver(self, message):
        return f"Delivered: {message}"

class UrgentMessenger(RoyalMessenger):
    def deliver(self, message):
        return f"URGENT: Delivered: {message}"

royal = RoyalMessenger()
urgent = UrgentMessenger()
print(royal.deliver("Your taxes are due."))
print(urgent.deliver("Enemy at the gates!"))



class DeliveryBot:
    def status(self):
        return f"Package en route."

class FastDeliveryBot(DeliveryBot):
    def status(self):
        return f"Package arriving in 5 minutes!"

basic = DeliveryBot()
fast = FastDeliveryBot()
print(basic.status())
print(fast.status())


class Robot:
    def communicate(self):
        return "Beep beep."

class ExplorerRobot(Robot):
    def communicate(self):
        return "Exploring new planets!"

r = Robot()
e = ExplorerRobot()
print(r.communicate())
print(e.communicate())



class Creature:
    def battle_cry(self):
        return "For glory!"

class Dragon(Creature):
    def battle_cry(self):
        return "Feel my fiery breath!"

c = Creature()
d = Dragon()
print(c.battle_cry())
print(d.battle_cry())