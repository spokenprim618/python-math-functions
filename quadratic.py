import math
def quad():

    def orientation(a): 
        val = "has a minimum" 
        if a>0: 
            return val
        else:   
            val = "has a maximum"
            return val
             
    def minMax(a,b):
        minMax = -(b/(2*a))
        return minMax
    
    def equation(a,x,b,c):
        return a*(x**2) + b*x + c
        
    def x_intNeg(a,b,c):
        try:
           squared = math.sqrt((b**2)-(4*a*c))
        except:
            print ("An error occurred")
        if isinstance(squared,float)==True:
            try:
                squared = (b**2)-4*a*c
               
            except UnboundLocalError:
                return ("there is no value")

        try:           
            rest = (-b-squared)/(2*a)
        except UnboundLocalError:
            return ("there is no value")
        else:
            return [squared, rest]
  

    def x_intPos(a,b,c):
        try:
            squared = math.sqrt((b**2)-(4*a*c))
            
        except:
            print ("An error occurred")
        if isinstance(squared,float)==True:
            try:
                squared = (b**2)-4*a*c
               
            except UnboundLocalError:
                return ("there is no value")
        try:           
            rest = (-b+squared)/(2*a)
        except UnboundLocalError:
            return ("there is no value")
        else:
            return [squared, rest]
    
    return [orientation(1),
            minMax(1,-3),
            equation(
                1,
                minMax(1,-3),
                -3,
                -4),
            x_intPos(1,-3,-4),
            x_intNeg(1,-3,-4),
            equation(
                1,
                0,
                -3,
                -4)]
print(quad())
