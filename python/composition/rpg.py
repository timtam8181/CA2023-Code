class Character:
    def __init__(self, name, race, health, attack):
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
        self.inv = Inventory([], 0, 0, 0)

    def battle(self, other):
        print(f'{self.name} attacks {other.name}!')
      
    
class Chest: 
    def __init__(self, items, gold, silver, copper):
        self.inv = Inventory(items, gold, silver, copper)

class Inventory: 
    def __init__(self, items, gold, silver, copper):
        self.items = items # list
        self.set_currency(gold, silver, copper) # Delegation
        
    # from_inv and to_inv are instrances of Inventory
    def transfer(self , to_inv):
        # Add all the items from from_inv to to_inv
        to_inv.items.extend(self.items)
        # Delete all the items from from_inv
        self.items = []
        # Add the currency from from_inv to to_inv
        to_inv.copper += self.copper
        # Set currency of from_inv to 0
        self.copper = 0

    # Setter
    def set_currency(self, gold, silver, copper):
        self.copper = gold * 10000 + silver * 100 + copper

    # Getter
    def get_currency(self):
        gold = self.copper // 10000
        silver = (self.copper % 10000) // 100
        copper = self.copper % 100
        return gold, silver, copper
    

class Ranger(Character):
    def battle(self, other):
        print(f'{self.name} casts a wicked spell at {other.name}!')

class Mage(Character):
    def __init__(self, name, race, health, attack):
        # Call the superclass constructor
        super().__init__(self, name, race, health, attack)
        self.mana = 100

    def battle(self, other):
        print(f'{self.name} casts a wicked spell at {other.name}!')
        self.mana -=20  
            
class Burglar(Character):
    def battle(self, other):
        print(f'{self.name} sneaks in a stealth attack on {other.name}!')

class Wizard(Character):
    def battle(self, other):
        print(f'{self.name} summons an orc minion, which attacks {other.name}!')          