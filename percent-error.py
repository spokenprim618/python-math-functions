# def percentError(actual, experimental):
#     first= experimental - actual
#     second= abs(first)
#     third= second/ actual
#     fourth= third *100
#     fifth = round(fourth,1)
#     return fifth
# print(percentError(10.9,11.6))
def percentError(actual, experimental):
    return round(((abs(experimental - actual))/actual)*100, 1)
print(percentError(10.9,11.6))
