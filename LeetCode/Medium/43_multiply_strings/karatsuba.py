class Solution(object):
    def multiply(self, num1, num2):
        # modify the naive solution to perform recursive Karatsuba's algorithm.
        # the below code isn't super optimal.
        def multiplyDigit(digi1, digi2):
            return str(int(digi1) * int(digi2))
        def addDigit(digi1, digi2):
            return str(int(digi1) + int(digi2))
        def minusDigit(digi1, digi2):
            if digi1[0] == '-':
                return '-' + addDigit(digi1[1:], digi2)
            return str(int(digi1) - int(digi2))

        def addNums(num1, num2):
            arr = ['0']*(max(len(num1),len(num2))+1)
            for i in range(len(num1)):
                arr[-i-1] = num1[-i-1]
            for i in range(len(num2)):
                arr[-i-1] = addDigit(arr[-i-1], num2[-i-1])
            for i in range(len(arr)-1):
                if len(arr[-i-1]) > 1:
                    arr[-i-2] = addDigit(arr[-i-2], arr[-i-1][0:-1])
                    arr[-i-1] = arr[-i-1][-1]
            non_zero = len(arr)-1
            for i in range(len(arr)):
                if arr[i] != '0':
                    non_zero = i
                    break
            return ''.join(arr[non_zero:])

        def minusNums(num1, num2):
            arr = []
            if len(num1) > len(num2) or (len(num1)==len(num2) and num1 > num2):
                arr = [i for i in num1]
                for i in range(len(num2)):
                    arr[-i-1] = minusDigit(arr[-i-1], num2[-i-1])
            else:
                arr = [i for i in num2]
                for i in range(len(num1)):
                    arr[-i-1] = minusDigit(arr[-i-1], num1[-i-1])
            for i in range(len(arr)-1):
                if arr[-i-1][0] == '-':
                    arr[-i-2] = minusDigit(arr[-i-2], '1')
                    arr[-i-1] = minusDigit('10',arr[-i-1][1:])
            non_zero = len(arr)-1
            for i in range(len(arr)):
                if arr[i] != '0':
                    non_zero = i
                    break
            return ''.join(arr[non_zero:])
            
        def naive(num1, num2): 
            arr = ['0']*(len(num1)+len(num2))
            for i in range(len(num1)):
                for j in range(len(num2)):
                    arr[-1-i-j] = addDigit(arr[-1-i-j], multiplyDigit(num1[-i-1], num2[-j-1]))
            for i in range(len(arr)-1):
                if len(arr[-i-1]) > 1:
                    arr[-i-2] = addDigit(arr[-i-2], arr[-i-1][0:-1])
                    arr[-i-1] = arr[-i-1][-1]
            non_zero = len(arr)-1
            for i in range(len(arr)):
                if arr[i] != '0':
                    non_zero = i
                    break
            return ''.join(arr[non_zero:])
        if len(num1) < 200 or len(num2) < 200:
            return naive(num1, num2)
        b = 10
        m = len(num1)-1
        if len(num2) < len(num1):
            m = len(num2)-1
        x1 = num1[:-m]
        x0 = num1[-m:]
        y1 = num2[:-m]
        y0 = num2[-m:]
        # calculate z2
        z2 = self.multiply(x1,y1)
        z0 = self.multiply(x0,y0)
        z1 = minusNums(self.multiply(addNums(x1,x0),addNums(y1,y0)), addNums(z2, z0))
        arr = ['0']*(len(num1)+len(num2))
        arr[-2*m-1] = z2
        arr[-m-1] = z1
        arr[-1] = z0
        for i in range(len(arr)-1):
            if len(arr[-i-1]) > 1:
                arr[-i-2] = addDigit(arr[-i-2], arr[-i-1][0:-1])
                arr[-i-1] = arr[-i-1][-1]
        non_zero = len(arr)-1
        for i in range(len(arr)):
            if arr[i] != '0':
                non_zero = i
                break
        return ''.join(arr[non_zero:])


def main():
    print(Solution().multiply("123","456"))
    print(Solution().multiply("999","999"))
    print(Solution().multiply("881095803","61"))
    a="721983712982189371289473920702391139020391290237092389023790123749230149012379056429015623965912365789156124397239473012948902629056231856249857239578707213490712490721497123493127590126924652391563920462394623904603926564563489562398563428956213472332472039479123890123792310293823904213900123929130239019672901672198339284136482364829562481962389723897432895287568237643278463829756289756248976238976231986231896238976923872389749238792378589756239846231876123793274902374098376487321582356802967891246832146380256824975837924682316408174601289481237568912741923864203876238956328175123906390164230185613298712389731294123784123876102391238946091640129756190460129886213476012369012"
    b="92817389452365012650237846893256945124632870831246523146523942380462387468912382364892365902356902365897214802364802365234089236409632984623894802356802368037180123038264083264803274608234627856238046320469256239236419823892364892374698325689326523894603256892737846923816923876238974623918683792589274645378582374538275623896439287928364892749823569832648237489127489127489724682354923848279812381273238916423894291377921739821368796482642381648923768236482374892378723682136587236587231498231648971648971648937568927138927169374879125981235893124682356923865123895238914537891458127453789452389157623179619234612384681274891234812346873"
    print("len of a: " + str(len(a)))
    print("len of b: " + str(len(b)))
    print(Solution().multiply(a,b))

if __name__ == '__main__':
    main()

