from linkedPack import LinkedList, Node

# Initialize history storage
arith_history = LinkedList()

def calculate(n1, n2, nth):
    """Calculate arithmetic sequence term"""
    d = n2 - n1
    result = n1 + (nth - 1) * d
    
    arith_history.append({
        'type': 'arithmetic_sequence',
        'inputs': {
            'first_term': n1,
            'second_term': n2,
            'term_number': nth,
            'common_difference': d
        },
        'result': result,
        'formula_used': 'aₙ = a₁ + (n-1)d'
    })
    return result

def get_history():
    """Return all history items with detailed metadata"""
    return arith_history.get_all()

def add_to_history(calculation_type, inputs, result):
    """Add a custom history entry"""
    arith_history.append({
        'type': calculation_type,
        'inputs': inputs,
        'result': result
    })

def delete_from_history(index):
    """Remove a history item by index"""
    arith_history.delete(index)