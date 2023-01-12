class Logger:

    def __init__(self):

        self.message_to_time_map = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.message_to_time_map:

            self.message_to_time_map[message] = timestamp
            return True

        last_timestamp = self.message_to_time_map[message]
        diff_in_timestamps = abs(timestamp - last_timestamp)        
        
        if diff_in_timestamps >= 10:
            self.message_to_time_map[message] = timestamp
            return True
        
        return False 
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)