import math
from linkedPack import LinkedList, Node

# Initialize history storage
cosines_history = LinkedList()

def calculate_sides(a, b, c, A, B, C):
    """Calculate missing sides using Law of Cosines"""
    sideA = sideB = sideC = 0
    
    if b and c and A:
        sideA = round(math.sqrt(b**2 + c**2 - (2 * b * c * math.cos(math.radians(A)))), 1)
    
    if a and c and B:
        sideB = round(math.sqrt(a**2 + c**2 - (2 * a * c * math.cos(math.radians(B)))), 1)
    
    if a and b and C:
        sideC = round(math.sqrt(a**2 + b**2 - (2 * a * b * math.cos(math.radians(C)))), 1)
    
    result = (sideA, sideB, sideC)
    cosines_history.append({
        'type': 'calculate_sides',
        'inputs': {'a': a, 'b': b, 'c': c, 'A': A, 'B': B, 'C': C},
        'result': result
    })
    return result

def calculate_angles(a, b, c):
    """Calculate all angles using Law of Cosines"""
    if not (a and b and c):
        return (0, 0, 0)
    
    try:
        angleA = round(math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))), 1)
        angleB = round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))), 1)
        angleC = round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b))), 1)
        result = (angleA, angleB, angleC)
        cosines_history.append({
            'type': 'calculate_angles',
            'inputs': {'a': a, 'b': b, 'c': c},
            'result': result
        })
        return result
    except ValueError:
        return (None, None, None)

def get_history():
    """Return all history items"""
    return cosines_history.get_all()

def add_to_history(calc_type, inputs, result):
    """Add a custom history entry"""
    cosines_history.append({
        'type': calc_type,
        'inputs': inputs,
        'result': result
    })

def delete_from_history(index):
    """Remove a history item by index"""
    cosines_history.delete(index)