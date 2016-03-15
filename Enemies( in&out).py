class Enemy(object):
    
    def __init__(self, name, health, damage):
        self.name = name 
        self.health = health 
        self.damage = damage 
        
class infecteds(Enemy):
    def __init__(self, name = "Infected", health = 50, damage = 10):
        super(infecteds, self).__init__(name = "Infected", health = 50 , damage = 10)
        
        
    def race(self):
        print "Run!!! %s are right behind you" % self.name 
        
        
        
class player(object):
    
    def __init__(self, name, health):
        self.name = name 
        self.health = health 
        
class single_player(player):
    def __init__(self, name, health = 50000):
        super(single_player, self).__init__(name, health = 50000)
        
        def 
        
        
bug = Enemy()
human = player()
        
        

    