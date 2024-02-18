import math
from pyscript import document

def quad():

    def orientation(event): 
        a1 = document.querySelector("#orientation")

        val = "has a minimum" 
        if a1>0: 
            return val
        else:   
            val = "has a maximum"
            return val
             
    def minMax(event):
        a2 = document.querySelector("#2ndTermMinMax")
        b2 = document.querySelector("#1stTermMinMax")

        minMax = -(b2/(2*a2))
        return minMax
    
    def equation(event):
        a3 = document.querySelector("#1stTermEquation")
        b3 = document.querySelector("#2ndTermEquation")
        c3 = document.querySelector("#3stTermEquation")
        x = document.querySelector("#xEquation")

        return a3*(x**2) + b3*x + c3
        
    def x_intNeg(event):
        a4 = document.querySelector("#1stTermXNeg")
        b4 = document.querySelector("#2ndTermXNeg")
        c4 = document.querySelector("#3rdTermXNeg")

        try:
           squared = math.sqrt((b4**2)-(4*a4*c4))
        except:
            print ("An error occurred")
        if isinstance(squared,float)==True:
            try:
                squared = (b4**2)-4*a4*c4
               
            except UnboundLocalError:
                return ("there is no value")

        try:           
            rest = (-b4-squared)/(2*a4)
        except UnboundLocalError:
            return ("there is no value")
        else:
            return [squared, rest]
  

    def x_intPos(event):
        a5 = document.querySelector("#1stTermXPos")
        b5 = document.querySelector("#2ndTermXPos")
        c5 = document.querySelector("#3rdTermXPos")

        try:
            squared = math.sqrt((b5**2)-(4*a5*c5))
            
        except:
            print ("An error occurred")
        if isinstance(squared,float)==True:
            try:
                squared = (b5**2)-4*a5*c5
               
            except UnboundLocalError:
                return ("there is no value")
        try:           
            rest = (-b5+squared)/(2*a5)
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
