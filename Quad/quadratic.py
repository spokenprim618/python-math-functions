import math
from pyscript import document

class Quad():

    def orientation(event): 
        a1 = document.querySelector("#orientation")
        a1 =float(a1.value)
        val = "has a minimum" 
        if a1>0: 
            output_div = document.querySelector("#output-quad")
            output_div.innerText = "This {}".format(val)
        else:   
            val = "has a maximum"
            output_div = document.querySelector("#output-quad")
            output_div.innerText = "This {}".format(val)
            
            
        document.getElementById("orientation").style.display = "none";
        document.getElementById("orientation-butt").style.display = "none";
        
        document.getElementById("TermMinMax2nd").style.display = "block";
        document.getElementById("TermMinMax1st").style.display = "block";
        document.getElementById("minMax-butt").style.display = "block";
        text_h2 = document.querySelector("#change")
        text_h2.innerText = "What is the vertex."
        
    def minMax(event):
        
        b2 = document.querySelector("#TermMinMax2nd")
        a2 = document.querySelector("#TermMinMax1st")
        
        a2 = float(a2.value)
        b2 = float(b2.value)
        
        minMax = -(b2/(2*a2))
        
        output_div = document.querySelector("#output-quad")
        output_div.innerText = "The vertex is {}".format(minMax)
        
        document.getElementById("TermMinMax2nd").style.display = "none";
        document.getElementById("TermMinMax1st").style.display = "none";
        document.getElementById("minMax-butt").style.display = "none";
        
        document.getElementById("TermEquation1st").style.display = "block";
        document.getElementById("TermEquation2nd").style.display = "block";
        document.getElementById("TermEquation3st").style.display = "block";
        document.getElementById("xEquation").style.display = "block";
        document.getElementById("equation-butt").style.display = "block";
        
        text_h2 = document.querySelector("#change")
        text_h2.innerText = "What is the output of the equation."
    
    def equation(event):
        
        a3 = document.querySelector("#TermEquation1st")
        b3 = document.querySelector("#TermEquation2nd")
        c3 = document.querySelector("#TermEquation3st")
        x = document.querySelector("#xEquation")
        a3 = float(a3.value)
        b3 = float(b3.value)
        c3 = float(c3.value)
        x = float(x.value)
        equation = a3*(x**2) + b3*x + c3

        output_div = document.querySelector("#output-quad")
        output_div.innerText = "The equation is {}".format(equation)
        
        document.getElementById("TermEquation1st").style.display = "none";
        document.getElementById("TermEquation2nd").style.display = "none";
        document.getElementById("TermEquation3st").style.display = "none";
        document.getElementById("xEquation").style.display = "none";
        document.getElementById("equation-butt").style.display = "none";
        
        document.getElementById("TermXNeg1st").style.display = "block";
        document.getElementById("TermXNeg2nd").style.display = "block";
        document.getElementById("TermXNeg3rd").style.display = "block";
        document.getElementById("x_intNeg-butt").style.display = "block";
        text_h2 = document.querySelector("#change")
        text_h2.innerText = "What is the quadratic equation with a negative."
        
    def x_intNeg(event):
        a4 = document.querySelector("#TermXNeg1st")
        b4 = document.querySelector("#TermXNeg2nd")
        c4 = document.querySelector("#TermXNeg3rd")
        a4 = float(a4.value)
        b4 = float(b4.value)
        c4 = float(c4.value)
        try:
           squared = math.sqrt((b4**2)-(4*a4*c4))
        except (UnboundLocalError,ValueError):
            output_div = document.querySelector("#output-quad")
            output_div.innerText = "An error occurred"
            
        if isinstance(squared,float)==True:
            try:
                squared = (b4**2)-4*a4*c4
               
            except (UnboundLocalError,ValueError):
                output_div = document.querySelector("#output-quad")
                output_div.innerText = "there is no value"

        try:           
            rest = (-b4-squared)/(2*a4)
        except (UnboundLocalError,ValueError):
            output_div = document.querySelector("#output-quad")
            output_div.innerText = "there is no value"
        else:
            output_div = document.querySelector("#output-quad")
            output_div.innerText = "This is the squared portion {} and this is the rest {}".format(squared,rest)

        document.getElementById("TermXNeg1st").style.display = "none";
        document.getElementById("TermXNeg2nd").style.display = "none";
        document.getElementById("TermXNeg3rd").style.display = "none";
        document.getElementById("x_intNeg-butt").style.display = "none";
        
        document.getElementById("TermXPos1st").style.display = "block";
        document.getElementById("TermXPos2nd").style.display = "block";
        document.getElementById("TermXPos3rd").style.display = "block";
        document.getElementById("x_intPos-butt").style.display = "block";
        text_h2 = document.querySelector("#change")
        text_h2.innerText = "What is the quadratic equation with a positive."

    def x_intPos(event):
        a5 = document.querySelector("#TermXPos1st")
        b5 = document.querySelector("#TermXPos2nd")
        c5 = document.querySelector("#TermXPos3rd")
        a5 = float(a5.value)
        b5 = float(b5.value)
        c5 = float(c5.value)
        try:
            squared = math.sqrt((b5**2)-(4*a5*c5))
            
        except (UnboundLocalError,ValueError):
            output_div = document.querySelector("#output-quad")
            output_div.innerText = "there is no value"
        if isinstance(squared,float)==True:
            try:
                squared = (b5**2)-4*a5*c5
               
            except (UnboundLocalError,ValueError):
                output_div = document.querySelector("#output-quad")
                output_div.innerText = "there is no value"
        try:           
            rest = (-b5+squared)/(2*a5)
        except (UnboundLocalError,ValueError):
            output_div = document.querySelector("#output-quad")
            output_div.innerText = "there is no value"
        else:
            output_div = document.querySelector("#output-quad")
            output_div.innerText = "This is the squared portion {} and this is the rest {}".format(squared,rest)
            