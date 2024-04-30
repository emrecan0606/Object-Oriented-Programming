from math import gcd

def gcd(m,n):
    while m%n !=0:
        oldm=m
        oldn=n

        m=oldm
        n=oldm%oldn
    return n    
    
class Fraction:
    
   

    def __init__(self, num, den):
        
        self.top=num
        self.bottom=den

    def __repr__(self):
        return str(self.top)+ "/"+ str(self.bottom)
    
    def normalize(self):
        return Fraction(2*self.top,self.bottom)

    def __eq__(self, other):
        return (self.top*other.bottom==other.top*self.bottom)
    
    def __lt__(self,other):
        return (self.top*other.bottom<other.top*self.bottom)
    
    def __le__(self, other):
            return (self.top*other.bottom<=other.top*self.bottom)
    

    def __add__(self,other):
        newtop=self.top*other.bottom+other.top*self.bottom
        newbottom=self.bottom*other.bottom
        return Fraction(newtop,newbottom)
        x=gcd(newtop,newbottom)
        return Fraction(newtop//x,newbottom//x)
    
     
    def __sub__(self,other):
        newtop=self.top*other.bottom-other.top*self.bottom
        newbottom=self.bottom*other.bottom
        return Fraction(newtop,newbottom)
        x=gcd(newtop,newbottom)
        return Fraction(newtop//x,newbottom//x)
    
    def __mul__(self,other):
        newtop=self.top*other.bottom*other.top*self.bottom
        newbottom=self.bottom*other.bottom
        return Fraction(newtop,newbottom)
        x=gcd(newtop,newbottom)
        return Fraction(newtop//x,newbottom//x)
    
    def __truediv__(self,other):
        newtop=self.top*other.bottom/other.top*self.bottom
        newbottom=self.bottom*other.bottom
        return Fraction(newtop,newbottom)
        x=gcd(newtop,newbottom)
        return Fraction(newtop//x,newbottom//x)
    
    





  
"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


# constructor
assert Fraction(1, 2).num == 1 and Fraction(1, 2).den == 2

# repr
assert f"{Fraction(1, 2)}" == "1/2"

# normalization
assert Fraction(3, 6).normalize().num == 1 \
       and Fraction(3, 6).normalize().den == 2 \
       and type(Fraction(3, 6).normalize().num) is int \
       and type(Fraction(3, 6).normalize().den) is int

# comparison magic
assert Fraction(1, 3) == Fraction(2, 6)
assert not(Fraction(1, 3) == Fraction(3, 1))
assert Fraction(1, 3) <= Fraction(1, 2)
assert Fraction(1, 3) < Fraction(1, 2)


# operation methods
assert Fraction(1, 2).add(Fraction(1, 3)) == Fraction(5, 6)
assert Fraction(1, 2).sub(Fraction(1, 3)) == Fraction(1, 6)
assert Fraction(2, 2).mul(Fraction(1, 3)) == Fraction(1, 3)
assert Fraction(1, 2).div(Fraction(1, 3)) == Fraction(3, 2)

# operators magic
assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)
assert Fraction(1, 2) * Fraction(1, 3) == Fraction(1, 6)
assert Fraction(1, 2) / Fraction(1, 3) == Fraction(3, 2)