from collections import defaultdict 

NOT_POSSIBLE = -1

class Solution:

    def build_graph(self, equations, values):

        graph = defaultdict(dict)

        for i in range(len(equations)):

            node_one, node_two = equations[i]
            weight = values[i]

            graph[node_one][node_two] = weight
            graph[node_two][node_one] = 1 / weight
        
        return graph 

    def get_query_responses(self, graph, visited, source, dest, weight):

        #base case   
            
        
        #process node
        if source == dest:
            print(source, dest, weight)
            return weight 
        
        visited.add(source)

        #get neighbors
        neighbors = graph[source]
        for neighbor in neighbors:

            if neighbor in visited:
                continue 
            
            weight_to_this_neighbor = graph[source][neighbor] 
            division_result = self.get_query_responses(graph, visited, neighbor, dest, weight * weight_to_this_neighbor)

            if division_result == NOT_POSSIBLE:
                continue 
            
            return division_result



        return NOT_POSSIBLE 


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        query_answers = []             

        graph = self.build_graph(equations, values)

        for source, dest in queries:

            if source not in graph or dest not in graph:
                query_answers.append(NOT_POSSIBLE)
                continue 
            
            if dest in graph[source]:
                query_answers.append(graph[source][dest])
                continue

            visited = set()

            weight = 1

            

            query_answers.append(self.get_query_responses(graph, visited, source, dest, weight))
        
        return query_answers