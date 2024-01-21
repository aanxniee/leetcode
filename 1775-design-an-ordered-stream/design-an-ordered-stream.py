class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.data = [None]*n
        self.ptr = 0


    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """

        self.data[idKey-1] = value # insert value

        # ptr hasn't reached insertion value
        if self.ptr < idKey - 1:
            return []

        # move ptr if a value has been inserted at the ptr
        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr +=1

        return self.data[idKey-1:self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)