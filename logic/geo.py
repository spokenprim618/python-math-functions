from linkedPack import LinkedList, Node

# Initialize history storage
geo_history = LinkedList()

def calculate(n1, n2, nth):
    """Calculate geometric sequence term"""
    r = n2 / n1
    result = round(n1 * (r ** (nth - 1)), 3)
    
    geo_history.append({
        'type': 'geometric_sequence',
        'inputs': {
            'first_term': n1,
            'second_term': n2,
            'term_number': nth,
            'common_ratio': r
        },
        'result': result,
        'formula_used': 'aₙ = a₁ × rⁿ⁻¹',
        'rounded_to': 3
    })
    return result

def get_history():
    """Return all history items with detailed metadata"""
    return geo_history.get_all()

def add_to_history(calculation_type, inputs, result):
    """Add a custom history entry"""
    geo_history.append({
        'type': calculation_type,
        'inputs': inputs,
        'result': result
    })

def delete_from_history(index):
    """Remove a history item by index"""
    geo_history.delete(index)