def gcd(a,b):
    return b if a%b ==0 else gcd(b , a%b)

class Fraction:
    def __init__(self,a,b):
        self.num = a // gcd(a,b)
        self.den = b // gcd(a,b)
    
    def __add__(self,other):
        return Fraction(self.num * other.den + other.num * self.den,self.den * other.den)
    
    def __mul__(self, other):
        return Fraction(self.num * other.den , self.den * other.den)
    
    def __iadd__(self, other):
        return self + other

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return "{} / {}".format(self.num,self.den)    


obj1 = Fraction(4,8)
obj2 = Fraction(4,8)

print(obj1 + obj2)