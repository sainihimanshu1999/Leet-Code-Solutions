def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        temp = head
        while(temp):
            if(temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False
        