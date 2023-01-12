import sys 

class MinStack:

    def __init__(self):

        self.stack = []               
        

    def push(self, val: int) -> None:         

        if not self.stack:
             self.stack.append((val, val)) 
        else:
            _, last_min = self.stack[-1]
            curr_min = min(last_min, val)
            self.stack.append((val, curr_min))  


    def pop(self) -> None:

        if not self.stack:
            raise Exception("There is no element on the stack.")        
        
        self.stack.pop()       

        

    def top(self) -> int:

        if not self.stack:
            raise Exception("There is no element on the stack.")
        
        top_element, _ = self.stack[-1]
        return top_element
        

    def getMin(self) -> int:

        _, min = self.stack[-1]

        return min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()