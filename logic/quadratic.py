import math
from linkedPack import LinkedList, Node

# Initialize history storage
quad_history = LinkedList()

class QuadraticCalculator:
    @staticmethod
    def get_orientation(a):
        """Determine if parabola opens up or down"""
        try:
            a = float(a)
            result = "has a minimum" if a > 0 else "has a maximum"
            quad_history.append({
                'type': 'orientation',
                'inputs': {'a': a},
                'result': result
            })
            return result
        except (ValueError, TypeError):
            return "Invalid input for orientation calculation"

    @staticmethod
    def find_vertex(a, b):
        """Calculate vertex of parabola"""
        try:
            a = float(a)
            b = float(b)
            if a == 0:
                return None  # Avoid division by zero
            result = round(-(b / (2 * a)), 2)
            quad_history.append({
                'type': 'vertex',
                'inputs': {'a': a, 'b': b},
                'result': result
            })
            return result
        except (ValueError, TypeError):
            return None

    @staticmethod
    def evaluate_equation(a, b, c, x):
        """Evaluate quadratic equation at specific x value"""
        try:
            a = float(a)
            b = float(b)
            c = float(c)
            x = float(x)
            result = round(a * (x**2) + b * x + c, 2)
            quad_history.append({
                'type': 'evaluation',
                'inputs': {'a': a, 'b': b, 'c': c, 'x': x},
                'result': result
            })
            return result
        except (ValueError, TypeError):
            return None

    @staticmethod
    def solve_quadratic(a, b, c):
        """Find roots of quadratic equation"""
        try:
            a = float(a)
            b = float(b)
            c = float(c)
            
            if a == 0:
                return None, None  # Not a quadratic equation

            try:
                squared = math.sqrt((b**2) - (4 * a * c))
                if isinstance(squared, float):
                    root1 = (-b - squared) / (2 * a)
                    root2 = (-b + squared) / (2 * a)
                    result = (round(root1, 2), round(root2, 2))
                    quad_history.append({
                        'type': 'solution',
                        'inputs': {'a': a, 'b': b, 'c': c},
                        'result': result
                    })
                    return result
            except ValueError:
                squared = (b**2) - (4 * a * c)
                result = (f"Discriminant: {squared} (no real roots)", None)
                quad_history.append({
                    'type': 'solution',
                    'inputs': {'a': a, 'b': b, 'c': c},
                    'result': result
                })
                return result
        except Exception:
            return "Invalid input values", None

def get_history():
    """Return all history items"""
    return quad_history.get_all()

def add_to_history(calculation_type, inputs, result):
    """Add a custom history entry"""
    quad_history.append({
        'type': calculation_type,
        'inputs': inputs,
        'result': result
    })

def delete_from_history(index):
    """Remove a history item by index"""
    quad_history.delete(index)