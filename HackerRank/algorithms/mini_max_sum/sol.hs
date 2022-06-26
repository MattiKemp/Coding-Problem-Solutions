miniMaxSum arr = do
    let sum = Data.List.foldr (+) 0 arr
    let min = Data.List.foldr (\x acc -> if sum-x < acc then sum-x else acc) sum arr
    let max = Data.List.foldr (\x acc -> if sum-x > acc then sum-x else acc) 0 arr
    print $ Data.List.intercalate " " (Data.List.map show [min, max])

lstrip = Data.Text.unpack . Data.Text.stripStart . Data.Text.pack
rstrip = Data.Text.unpack . Data.Text.stripEnd . Data.Text.pac
