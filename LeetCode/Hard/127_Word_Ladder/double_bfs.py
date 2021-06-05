class Soltuion(object):
    def ladderLength(self, beginWord, endWord, wordList):
        class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        #init adjacency list
        adjList = {k:set() for k in wordList}
        #endWord isn't in wordList so it is unreachable from beginWord
        if(endWord not in adjList.keys()):
            return 0
        #construct adj list
        for k in wordList:
            for j in wordList:
                if(k!=j):
                    found = False
                    for i in range(len(k)):
                        if(k[i]!=j[i]):
                            if(found):
                                found = False
                                break
                            found = True
                    if(found):
                        adjList[k].add(j)
        
        print(adjList)
        # the rest of the dictionary is unreachable from beginWord
        if(len(adjList[beginWord])==0):
            return 0
        
        if(endWord in adjList[beginWord]):
            return 2
        # I will implement the double bfs with two queues
        
        bfsBegin = deque()
        bfsBegin.append(beginWord)
        beginVisited = {beginWord,endWord}
        beginDepth = 1
        beginCurrLevel = 1
        beginNextLevel = 0
        bfsEnd = deque()
        bfsEnd.append(endWord)
        endVisited = {endWord,beginWord}
        endDepth = 1
        endCurrLevel = 1
        endNextLevel = 0
        found = False
        while(len(bfsBegin)>0 and len(bfsEnd)>0):
            beginPopped = bfsBegin.pop()
            for k in adjList[beginPopped]:
                if(k not in beginVisited):
                    bfsBegin.appendleft(k)
                    beginVisited.add(k)
                    #improvement break here since we have found what
                    #we are looking for
                    beginNextLevel += 1
                    if(k in endVisited):
                        found = True
            beginCurrLevel-=1
            if(found):
                break
            if(beginCurrLevel == 0):
                beginDepth += 1
                beginCurrLevel = beginNextLevel
                beginNextLevel = 0
            endPopped = bfsEnd.pop()
            for k in adjList[endPopped]:
                if(k not in endVisited):
                    bfsEnd.appendleft(k)
                    endVisited.add(k)
                    endNextLevel += 1
                    if(k in beginVisited):
                        found = True
            endCurrLevel-=1
            if(endCurrLevel == 0):
                endDepth+=1
                endCurrLevel = endNextLevel
                endNextLevel = 0
            
        print(found)
        print(beginDepth)
        print(endDepth)
        if(found):
            return beginDepth + endDepth
        return 0

def main():
    print('----main----')

if __name__ == '__main__':
    main()
