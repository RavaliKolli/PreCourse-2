# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes on VSCODE
# Any problem you faced while coding this : No

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data = data 
        self.next = None
        
class LinkedList: 
  
    def __init__(self):
        self.head = None
        
    def push(self, new_data): 
        newNode = Node(new_data)
        if self.head == None:
            self.head = newNode
            return
        else:
            curr = self.head
            while (curr.next) != None:
                curr = curr.next
            curr.next = newNode
        
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow = self.head
        fast = self.head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        return slow.data


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
print(list1.printMiddle())
