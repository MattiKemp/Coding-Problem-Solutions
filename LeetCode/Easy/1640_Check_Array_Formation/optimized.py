# optimized version that stores the indicies of arrays in pieces
# instead of pointers to the arrays in pieces 
def canFormArray(arr, pieces):
    # Construct hashmap that maps the first element in each array in pieces to the index of its array
    piecesDict = {pieces[piece][0]:piece for piece in range(len(pieces))}
    spot = 0
    while(spot < len(arr)):
        # pieces array first element has been found
        # this must be changed as index 0 will be stored which
        # python could get confused with being False
        if(piecesDict.get(arr[spot])!=None):
            # check each element in the pieces array
            for k in pieces[piecesDict.get(arr[spot])]:
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
