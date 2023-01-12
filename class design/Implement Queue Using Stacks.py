'''

1   
2   3
3   2
'''

class MyQueue:

    def __init__(self):

        self.main_stack = []
        self.helper_stack = []
        

    def push(self, x: int) -> None:

        self.main_stack.append(x)       

    def pop(self) -> int:

        if len(self.main_stack) == 0:
            raise Exception("Error: stack is empty.")            

        while len(self.main_stack) > 1:

            num = self.main_stack.pop()
            self.helper_stack.append(num)
        
        popped_element = self.main_stack.pop()

        while len(self.helper_stack) > 0:
            
            num = self.helper_stack.pop()
            self.main_stack.append(num)

        return popped_element
        

    def peek(self) -> int:

        return self.main_stack[0]

        
        

    def empty(self) -> bool:

        return len(self.main_stack) == 0

        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()