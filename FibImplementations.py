
import timeit
# this is a program written to demonstrate how dynamic programming can optimize the efficiency of our
# algorithms via reducing or eliminating repetitive recursive calls via caching local return values of the recursive
# stack
# @Author: John Miller


class FibImplementations(object):

    # complexity: O(2^n). This is because our each increment of the input index, which we will call
    # n in this case, will require another branch on the recursion tree, increment
    # explanation: the call to recurse on the two indices less than index then make two additional recursive calls, forming a
    # recursion tree that is growing at a rate of 2 to the power of the number index is, roughly, with eah operation in this being a
    # constant time operation
    def SimpleFibCalc(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index == 0:
            return 0  # base case
        if index == 1 or index == 2:
            return 1  # base case
        else:
            # recurse on both index - 1 and index - 2 to find the previous two Fibonacci nums to sum
            return self.SimpleFibCalc(index - 1) + self.SimpleFibCalc(index - 2)

    # complexity = O(2n + 1). Because after the initial recursion occurs, the else branch of the helper function
    # will only execute n times, and then in that execution, there will be at most another 2 recursive calls, therefore,
    # with all the other operations in this function being O(1) linear time, the function has a O(2n + 1)
    # complexity, which can be simplified to O(n) for simplicity as imput size grows
    # reasoning: we call this function 1 time, plus the n times that
    def MemoizeFibCalculation(self, index):
        """
        :type index: int
        :rtype: int
        """
        # First, set up an array to cache the fibonacci numbers at the indices before the end index
        optimizationArray = [0]*(index + 2)
        optimizationArray[0] = 0  # base case
        optimizationArray[1] = 1  # base case
        return self.MemoizeFibKerner(index, optimizationArray)

    def MemoizeFibKerner(self, index, optimizationArr):
        """
        :type index: int
        :type optimizationArr: List[int]
        :rtype: int
        """
        # if index is a base case, or we have already cached the value in our optimization array, return that index of the array
        if index == 0 or index == 1 or optimizationArr[index] != 0:
            return optimizationArr[index]
        # else, recurse on the two lesser indices than our index variable and cache the value into our memoize array. This branch will only execute at
        # most n times, as the values will be stored in our optimization array.
        else:
            cachedValue = self.MemoizeFibKerner(
                index - 1, optimizationArr) + self.MemoizeFibKerner(index - 2, optimizationArr)
            optimizationArr[index] = cachedValue
            return cachedValue

    # iterativeFibCalculator uses the same idea as MemoizeFibKernel, but, instead, it uses iteration instead
    # of recursion to build its optimization array.
    def iterativeFibCalc(self, index):
        """
        :type index: int
        :rtype: int
        """
        # if we are at a base case where the index is already the value of the fibonacci number, return the index
        if index == 0 or index == 1:
            return index
        # Else, use a while loop to start from the bottom/least index, and ue what we know initially to build our way up to the
        # resulting in us eventually finding the fibonacci number at the desired index
        else:
            efficiencyArray = [0] * (index + 1)
            efficiencyArray[0] = 0
            efficiencyArray[1] = 1
            indexer = 2
            while indexer < (index + 1):
                efficiencyArray[indexer] = efficiencyArray[indexer -
                                                           1] + efficiencyArray[indexer - 2]
                indexer += 1
            return efficiencyArray[index]


# testing the efficiencies of our algorithms
obj = FibImplementations()
for num in range(30, 38):
    print("\nfor fibonacci num at index " + str(num))
    print("memoized loading:")
    print("\nthe memoized Solution is " + str(obj.MemoizeFibCalculation(num)))
    print("iterative loading:")
    print("\nthe iterative Solution is " + str(obj.iterativeFibCalc(num)))
    print("simpleFibCalc loading:")
    print("\n  the simpleFibCalc Solution is " + str(obj.SimpleFibCalc(num)))
