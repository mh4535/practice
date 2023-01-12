from collections import deque

NO_PATH = 0
FIRST_LETTER = ord('a')
LAST_LETTER = ord('z') 

class Solution:

    

    def get_new_word(self, first_substring, last_substring, valid_words):

        new_words = []

        for i in range (FIRST_LETTER, LAST_LETTER + 1):

            char_to_insert = chr(i)

            new_word = first_substring + char_to_insert + last_substring

            if new_word not in valid_words:
                continue

            new_words.append(new_word)

        return new_words


    def get_neighbors(self, valid_words, word):

        neighbors = []

        for i in range(len(word)):
            char = word[i]
            first_substring = word[: i]
            last_substring = word[i + 1: len(word)]

            new_word_list = self.get_new_word(first_substring, last_substring, valid_words)

            for new_word in new_word_list:
                neighbors.append(new_word)

        return neighbors
            

    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:

        valid_words = set(word_list)

        if end_word not in valid_words:
            return NO_PATH
        
        queue = deque()

        initial_distance = 1
        initial_tuple = (begin_word, initial_distance)
        queue.append(initial_tuple)

        visited = set()
        visited.add(begin_word)

        while queue:

            word, distance = queue.popleft()

            if word == end_word:
                return distance
            
            neighbors = self.get_neighbors(valid_words, word)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)

                new_neighbor = (neighbor, distance + 1)
                queue.append(new_neighbor)
        
        return NO_PATH