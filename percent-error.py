
def percentError(actual, experimental):
    return round(((abs(experimental - actual))/actual)*100, 1)
print(percentError(10.9,11.6))
