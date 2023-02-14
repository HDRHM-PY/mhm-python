"""
We are going to implement linear search method below:
@Args value, items
@Return target index in list
"""


def search(List : int, tr : int):
    
    i = 0
    while i < len(List):
        if List[i] == tr:
            return True
        i = i + 1
        
    return False



List1 = [1, 3, 6, 9, 4, 8, 7, 5, 2]

tr1 = 10

if search(List1, tr1):
    print("found")
else :
    print("not found")
