from linkedPack import LinkedList, Node

# Initialize history storage
percent_history = LinkedList()

def calculate(experimental, actual):
    """Calculate percent error"""
    if actual == 0:
        return None  # Avoid division by zero
    
    result = round((abs(experimental - actual) / actual) * 100, 2)
    percent_history.append({
        'type': 'percent_error',
        'inputs': {'experimental': experimental, 'actual': actual},
        'result': result
    })
    return result

def get_history():
    """Return all history items"""
    return percent_history.get_all()

def add_to_history(experimental, actual, result):
    """Add a manual history entry"""
    percent_history.append({
        'type': 'percent_error',
        'inputs': {'experimental': experimental, 'actual': actual},
        'result': result
    })

def delete_from_history(index):
    """Remove a history item by index"""
    percent_history.delete(index)