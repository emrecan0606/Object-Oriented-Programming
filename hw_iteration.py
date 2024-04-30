
class DistanceIterator:

    def __init__(self,numbers):
      self.n=[] 
      self.num=numbers
      
      
      
    
    def __iter__(self):
       return self
    
    def __next__(self):
       
       if self.n <= self.num :
             result=self.n
             
             return result
          
       else:
          raise StopIteration
       
       
    
    
# empty number list
assert [n for n in DistanceIterator([])] == []

# one number in list --> also no distances
assert [n for n in DistanceIterator([4])] == []

# some examples
assert [n for n in DistanceIterator([4,2,-2])] == [2,6,4]
assert [n for n in DistanceIterator([3,3,3,8])] == [0, 0, 5, 0, 5, 5]
assert [n for n in DistanceIterator([-1,20,23,-5,8])] == [21, 24, 4, 9, 3, 25, 12, 28, 15, 13]    


