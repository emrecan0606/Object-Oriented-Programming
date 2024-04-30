from typing import Tuple






class Entity:

    def __init__(self, name: str, coords: Tuple[int, int], hit_points: int) -> None:
         
        self.name=name
        self.coords=coords
        self.hit_points=hit_points
        
    
        
    def take_damage(self, damage_amount: int) -> None:
            
        
        raise NotImplementedError
    
        
    def is_alive(self) -> bool:
        if self.hit_points>0:
            return True
        else:
            return False
        
    def get_distance(self, other_coords: tuple[int, int]) -> int:
        distance=abs(self.coords[0]-other_coords[0]+abs(self.coords[1]-other_coords[1]))
        return distance

        # method to count distance to other object
        # for calculation of distance use Taxicab/Manhattan metric: https://en.wikipedia.org/wiki/Taxicab_geometry
        # returns the distance

     

class Rock(Entity):
    
  
   
    
    def take_damage(self, damage_amount: int) -> None:
        
        if damage_amount>10:
            self.hit_points=hit_points-1
        else:
            return False   
        
        
       
        



class Furniture(Entity):
    def take_damage(self, damage_amount: int) -> None:
        
        self.hit_points=damage_amount     
   
       
    
class LivingEntity(Entity):
    
    def __init__(self, name: str, coords: tuple[int, int], hit_points: int, level: int, damage: int, attack_range: int):
        
        super().__init__(name,coords,hit_points)
        self.level=level
        self.damage=damage
        self.attack_range=attack_range  
    
    
    def level_up(self,plus):
        self.level += 1

    def take_damage(self, damage_amount: int) -> None:
        self.hit_points=damage_amount 
        
        
        # method to apply damage on this entity
        # the whole damage_amount is applied to hitpoints       
    
       
    def hit(self, other_entity: Entity) -> None:
        
        
        # method to hit other entity to cause them to take damage
        # this is abstract method, just keep it as it is
        raise NotImplementedError("This method is abstract. Please implement it")  # in the child, not here :-)
    
    def move(self, vector: Tuple[int, int]) -> None:
        list1=list(self.coords)
        list2=list(vector)
        list1[0]=list1[0]+list2[0]
        self.coords=tuple(list1)
        vector=tuple(list2)
        # method to make entity move on the board
        # it expects vector of steps in x and y directions, the vector is represented as tuple (x, y)
        # the move is executed by editing coordinates by the vector elements
        # x is editing x axis and y is editing y axis
        # +x, -x, +y, -y define also direction of move

        

    def in_range(self, other_entity: Entity) -> bool:
        
    if self.get_distance(other_entity.coords)<=self.attack_range:
        return True
    else:
        return False
    
    
        # method to check if other entity is in range
        # return True if get_distance to other entity <= self.range
        # return False if get_distance to other entity > self.range
        

class Warrior(LivingEntity):
    
    def hit(self, other_entity: Entity) -> None:
        
        if self.get_distance(other_entity.take_damage)self.hit_points:
            return True
        else:
            return False
         
         
        #implement hit to another entity
        #if other entity is in range make it to take damage with it's own method take_damage
        #damage_amount applied to other entity is equal to damage of attacking entity
  
        
    def take_damage(self, damage_amount: int) -> None:
        
        if damage_amount>10:
         self.hit_points=hit_points-1
        else:
            return False   
            
        # method to apply damage on this entity
        # Warrior is taking damage only when the damage_amount is bigger then his level
        #   If damage is bigger than level Warrior takes the difference as a damage_amount
        #   Else Warrior takes no damage
        

    def level_up(self) -> None:
        self.level += 1
    
        # this method should increase the level according to parent; use call to parent's method
        # also increase damage by 1 and hit_points by 2
        


class Archer(LivingEntity):

    def hit(self, other_entity: Entity) -> None:
        
        if self.get_distance(other_entity.take_damage)self.hit_points:
            return True
        else:
            return False
        
        
        
        # implement hit to another entity
        # if other entity is in range make it to take damage with it's own method take_damage
        # damage_amount applied to other entity is equal to damage of attacking entity
        

    def level_up(self) -> None:
        self.level += 1
         
        # this method should increase the level according to parent; use call to parent's method
        # also increase damage by 2 and hit_points by 1
        
            


    
   
    
   
        
    
   


      

    
 
        


       
        
   

    
        
    
    
        
        
    
   































# Simple Entity tests
entity = Entity("E", (0, 0), 10)
# constructor
assert entity.name == "E"
assert entity.coords == (0, 0)
assert entity.hit_points == 10
# is alive check
assert entity.is_alive()
# get distance check
assert entity.get_distance((0, 0)) == 0

# Rock tests
rocky = Rock("Rocky", (0, 1), 5)
# constructor
assert rocky.name == "Rocky"
assert rocky.coords == (0, 1)
assert rocky.hit_points == 5
# is alive check
assert rocky.is_alive()
# get distance check
assert rocky.get_distance((0, 0)) == 1
# damage taking
rocky.take_damage(7)
assert rocky.hit_points == 5
rocky.take_damage(100)
assert rocky.hit_points == 4

# Table tests
table = Furniture("Table", (1, 0), 3)
# constructor
assert table.name == "Table"
assert table.coords == (1, 0)
assert table.hit_points == 3
# is alive check
assert table.is_alive()
# get distance check
assert table.get_distance((0, 0)) == 1
# damage taking
table.take_damage(2)
assert table.hit_points == 1
table.take_damage(2)
assert table.hit_points == -1
assert not table.is_alive()

# LivingEntity tests
tim = LivingEntity("Tim", (-1, 0), 3, 1, 1, 1)
# constructor
assert tim.name == "Tim"
assert tim.coords == (-1, 0)
assert tim.hit_points == 3
assert tim.level == 1
assert tim.damage == 1
assert tim.attack_range == 1
# is alive check
assert tim.is_alive()
# get distance check
assert tim.get_distance((0, 0)) == 1
# level up check
tim.level_up()
assert tim.level == 2
# damage taking
tim.take_damage(1)
assert tim.hit_points == 2
assert tim.is_alive()
# move check
assert tim.in_range(entity)
tim.move((0, -1))
assert not tim.in_range(entity)

# Warrior tests
willy = Warrior("William Wallace", (1, 1), 3, 5, 8, 2)
# constructor
assert willy.name == "William Wallace"
assert willy.coords == (1, 1)
assert willy.hit_points == 3
assert willy.level == 5
assert willy.damage == 8
assert willy.attack_range == 2
# is alive check
assert willy.is_alive()
# get distance check
assert willy.get_distance((0, 0)) == 2
# level up check
willy.level_up()
assert willy.hit_points == 5
assert willy.level == 6
assert willy.damage == 9
# damage taking
willy.take_damage(1)
assert willy.hit_points == 5
willy.take_damage(7)
assert willy.hit_points == 4
# fight checks
rocky = Rock("Rocky", (0, 1), 5)
willy.hit(rocky)
assert rocky.hit_points == 5
table = Furniture("Table", (1, 0), 3)
willy.hit(table)
assert table.hit_points == -6
tim = LivingEntity("Tim", (-1, 0), 3, 1, 1, 1)
willy.hit(tim)
assert tim.hit_points == 3
willy.move((-1, -1))
assert willy.get_distance((0, 0)) == 0
willy.hit(tim)
assert tim.hit_points == -6

# Archer tests
rob = Archer("Robin Hood", (5, 8), 3, 1, 7, 10)
# constructor
assert rob.name == "Robin Hood"
assert rob.coords == (5, 8)
assert rob.hit_points == 3
assert rob.level == 1
assert rob.damage == 7
assert rob.attack_range == 10
# is alive check
assert rob.is_alive()
# get distance check
assert rob.get_distance((0, 0)) == 13
# level up check
rob.level_up()
assert rob.hit_points == 4
assert rob.level == 2
assert rob.damage == 9
# damage taking
rob.take_damage(1)
assert rob.hit_points == 3
# fight checks
willy = Warrior("William Wallace", (1, 1), 3, 5, 8, 2)
rob.hit(willy)
assert willy.hit_points == 3
rob.move((0, -1))
rob.hit(willy)
assert willy.hit_points == -1
assert not willy.is_alive()