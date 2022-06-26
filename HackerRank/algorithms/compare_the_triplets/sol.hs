compareTriplets a b = do
    Data.List.foldr(\x acc -> 
        if a !! x > b !! x 
            then [acc !! 0 + 1, acc !! 1] 
        else if a !! x < b !! x 
            then [acc !! 0, acc !! 1 + 1] 
        else acc) [0,0] [0,1,2]
