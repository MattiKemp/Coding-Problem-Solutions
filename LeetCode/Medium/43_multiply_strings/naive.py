class Solution(object):
    def multiply(self, num1, num2):
        arr = ['0']*(len(num1)+len(num2))
        def multiplyDigit(digi1, digi2):
            return str(int(digi1) * int(digi2))
        def addDigit(digi1, digi2):
            return str(int(digi1) + int(digi2))
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[-1-i-j] = addDigit(arr[-1-i-j], multiplyDigit(num1[-i-1], num2[-j-1]))
        print(arr)
        for i in range(len(arr)-1):
            if len(arr[-i-1]) > 1:
                arr[-i-2] = addDigit(arr[-i-2], arr[-i-1][0:-1])
                arr[-i-1] = arr[-i-1][-1]
        non_zero = len(arr)-1
        for i in range(len(arr)):
            if arr[i] != '0':
                non_zero = i
                break

        print(arr)
        #print(''.join(arr))
        print(''.join(arr[non_zero:]))
        return ''.join(arr[non_zero:])



def main():
    Solution().multiply("123","456")

if __name__ == '__main__':
    main()

