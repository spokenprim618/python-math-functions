import math
import numpy as np

def angle(a,b,c):
    
    part1A = b**2 + c**2;
    part1B = a**2 + c**2;
    part1C = b**2 + a**2;
    
    part2C = -2*(b * a);
    part2A = -2*(b * c);
    part2B = -2*(c * a);
    
    part3A = a**2 - part1A;
    part3B = b**2 - part1B;
    part3C = c**2 - part1C;
    
    part4A = part3A / part2A;
    part4B = part3B / part2B;
    part4C = part3C / part2C;
    
    angleA = math.acos(part4A);
    angleB = math.acos(part4B);
    angleC = math.acos(part4C);

    return [
    round(math.degrees(angleA),1),
    round(math.degrees(angleB),1),
    round(math.degrees(angleC),1)]

print(angle(4.3,5,6))

def sides(a=0,b=0,c=0, A=0,B=0,C=0):
    sideA = (b**2+c**2)+((-2*b*c)*
    (np.cos((46 * np.pi)/180)))
    
    sideB = (a**2+c**2)+((-2*a*c)*
    (np.cos((46 * np.pi)/180)))
    
    sideC = (b**2+a**2)+((-2*b*a)*
    (np.cos((46 * np.pi)/180)))
    
    return [math.sqrt(sideA),math.sqrt(sideB),math.sqrt(sideC)]

print(sides(A=46,b=5,c=6))
    
