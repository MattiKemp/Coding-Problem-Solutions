class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Soltuion(object):
    def getTargetCopy(self, original, cloned, target):
        if(original):
            if(original==target):
                return cloned
            # I know this is really nasty to read but I wanted to see if I could do it in 4 lines or less
            #probably could do it in one line if you really wanted to given how ridiculous python is lol
            return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)

def main():
    print('test')

if __name__ == '__main__':
    main()
