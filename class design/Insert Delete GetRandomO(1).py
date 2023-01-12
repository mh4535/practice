class RandomizedSet:

    def __init__(self):
        
        self.map_of_val_to_list_index = {}      
        self.list_of_values = []
        

    def insert(self, val: int) -> bool:

        if not self.map_of_val_to_list_index:
            
            initial_index = 0
            self.map_of_val_to_list_index[val] = initial_index 
            self.list_of_values.append(val)        
            
            return True 

        
        if val in self.map_of_val_to_list_index:
            return False
        
        self.list_of_values.append(val)
        self.map_of_val_to_list_index[val] = len(self.list_of_values) - 1
        
        return True 

            
    '''    
    map =  {5:0,
            6:1,
            200:3,
            35:2
    }       

        35
    [0,1,2,3]

    '''

    def swap_and_update_map(self, list_index_to_swap_into):

        last_element = self.list_of_values[len(self.list_of_values) - 1]
        self.list_of_values[list_index_to_swap_into] = last_element
        self.list_of_values.pop()

        self.map_of_val_to_list_index[last_element] = list_index_to_swap_into



    def remove(self, val: int) -> bool:

        if not self.map_of_val_to_list_index or val not in self.map_of_val_to_list_index:

            return False         
        
        list_index_to_swap_into = self.map_of_val_to_list_index[val] 
        del self.map_of_val_to_list_index[val]

        is_item_at_last_position_in_list = list_index_to_swap_into == len(self.list_of_values) -1

        if is_item_at_last_position_in_list:           

            self.list_of_values.pop()
            return True

        self.swap_and_update_map(list_index_to_swap_into)    
        

        return True 

        

    def getRandom(self) -> int:

        random_element = random.choice(self.list_of_values)

        return random_element 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

