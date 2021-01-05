# Naive version which uses the property of pieces having to be in order and pieces being unique elements to 
# determine if arr can be constructed using pieces in O(arr) time, number of elements in arr,
# and O(pieces) space, total number of elements in each array in pieces
def canFormArray(arr, pieces):
    # Construct hashmap that maps the first element in each array in pieces to its array
    # we do this as the order of the elements in pieces arrays must be conserved
    # this means that when 'constructing' arr, if a new element is discovered
    # it must be the first element in a array in pieces, or arr can't be created.
    # If it is the first element in a pieces array, the next elements in arr must be 
    # in the order of the array in pieces.
    piecesDict = {piece[0]:piece for piece in pieces}
    spot = 0
    while(spot < len(arr)):
        # pieces array first element has been found
        if(piecesDict.get(arr[spot])):
            # check each element in the pieces array
            for k in piecesDict.get(arr[spot]):
                # if arr has already been constructed
                if(spot >= len(arr)):
                    return True
                elif(arr[spot]==k):
                    spot+=1
                # pieces ordering is not conserved
                else:
                    return False
        # no element found
        else:
            return False
    # arr has been fully constructed
    return True

def main():
    print(canFormArray([15,88],[[88],[15]]))
    print(canFormArray([15,88],[[88],[1]]))
    print(canFormArray([91,4,64,78],[[78],[4,64],[91]]))
    print(canFormArray([49,18,16],[[16,18,49]]))
    print(canFormArray([1,3,5,7],[[2,4,6,8]]))

if __name__ == '__main__':
    main()
