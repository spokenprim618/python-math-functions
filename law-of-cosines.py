import math
import numpy as np
# for some reason b is c and c is b
def sides(a=0,b=0,c=0, 
          A=0,B=0,C=0):
   
    sideA = (b**2+c**2)+((-2*b*c)*
    (np.cos((A * np.pi)/180)));
    
    sideB = (a**2+c**2)+((-2*a*c)*
    (np.cos((B * np.pi)/180)));
    
    sideC = (b**2+a**2)+((-2*b*a)*
    (np.cos((C * np.pi)/180)));
    
    return [
    round(math.sqrt(sideA),1),
    round(math.sqrt(sideB),1),
    round(math.sqrt(sideC),1),
    ]

print(sides(A=36,B=0,C=0, 
            a=0,b=5,c=7));

def angle(
    a1=sides(A=36,b=7,c=5)[0],
    b1=sides(A=36,b=7,c=5)[1],
    c1=sides(A=36,b=7,c=5)[2]
    ):
        
    part1A = b1**2 + c1**2;
    part1B = a1**2 + c1**2;
    part1C = b1**2 + a1**2;
    
    part2C = -2*(b1 * a1);
    part2A = -2*(b1 * c1);
    part2B = -2*(c1 * a1);
    
    part3A = a1**2 - part1A;
    part3B = b1**2 - part1B;
    part3C = c1**2 - part1C;
    
    part4A = part3A / part2A;
    part4B = part3B / part2B;
    part4C = part3C / part2C;
    
    angleA = math.acos(part4A);
    angleB = math.acos(part4B);
    angleC = math.acos(part4C);
    
    return [
    round(math.degrees(angleA),0),
    round(math.degrees(angleB),0),
    round(math.degrees(angleC),0)
    ]
print(angle())
