# This problem is a really easy one so the optimial solution isn't too complicated.
# The arrays can be treated as continious strings by use two pointers for each array.
# The first pointer keeps track of where you are in the current string and the second 
# pointer keeps track of which string you are currently on. If the first pointer is to large
# then just increment the second pointer to move onto the next string. So now we can just
# compare each spot in each array as if we are just looping through two strings.
# Ex: word1 = ["a", "cb"], pointer1 will start off at 0 and spot1 will start off at 0.
# so word1[spot1][pointer1] = word1[0][0] = 'a'. 
# We increment pointer1 which is now larger than word1[spot1]
# so we move onto the next string by incrementing spot1: spot1=1 and setting pointer1 to 0.
# so word1[spot1][pointer1] = word1[1][0] = 'c' and so on till we iterate through the entire array.
# Runtime O(n), where n is the total size of all the characters in the smallest array, space O(1)
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        pointer1=0
        spot1=0
        pointer2=0
        spot2=0
        found = False
        while(spot1 < len(word1) and spot2 < len(word2)):
            if(pointer1 >= len(word1[spot1])):
                pointer1 = 0
                spot1+=1
                found = True
            if(pointer2 >= len(word2[spot2])):
                pointer2 = 0
                spot2+=1
                found = True
            if(not found):
                if(word1[spot1][pointer1] != word2[spot2][pointer2]):
                    return False
                pointer1+=1
                pointer2+=1
            found = False
        
        if(spot1 != len(word1) or spot2 != len(word2)):
            return False
        return True


def main():
    print('----Main----')

if __name__ == '__main__':
    main()
