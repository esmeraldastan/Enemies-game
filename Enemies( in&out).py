class Enemy(object):
    
    def __init__(self, name, health, damage):
        self.name = name 
        self.health = health 
        self.damage = damage 
        
class infecteds(Enemy):
    def __init__(self, name = "Infected", health = 500, damage = 10):
        super(infecteds, self).__init__(name = "Infected", health = 50 , damage = 10)
        
        
    def race(self):
        print "Run!!! %s are right behind you" % self.name 
        
class zombie(Enemy):
    def __init__(self, name = "Zombie", health = 1000, damage = 25):
        super(zombie, self).__init__( name = "Zombie", health = 1000, damage = 25)
        
    def run(self):
        print "%s are much faster and cause more damage." % self.name
        
        
command = raw_input('>')
print ' do you want to restore health. Type restore'        
class player(object):
    
    def __init__(self, name, health):
        self.name = name 
        self.health = health 
        
class single_player(player):
    def __init__(self, name, health = 50000):
        super(single_player, self).__init__(name, health = 50000)
        

        


class Item(object):
    def __init__(self, name):
        self.name = name
        
class Consumable(Item):
    
    def __init__(self, name, health):
        super(Consumable, self).__init__(name)
        self.health = health
        
class health_potion(Consumable):
    def __init__(self, name, health = 200):
        super(health_potion, self).__init__(name, health = 200)
        

a = health_potion('Blue potion', 3000)
b = single_player('Billy Bob')        
 
if command == 'restore':
    new_health = a.health + b.health
    print new_health
        

    