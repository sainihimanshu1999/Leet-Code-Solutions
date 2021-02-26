def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
    pascal = [1]*(rowIndex+1)
    for i in range(2,rowIndex+1):
        for j in range(i-1,0,-1):
            pascal[j] += pascal[j-1]
    return pascal