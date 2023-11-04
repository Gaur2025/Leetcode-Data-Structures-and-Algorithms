class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # we need to create a hashset to store the edges, a hashmap to store the neighbors
        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        visited = set()    # to track the cities we have visited

        changes = 0      # this will be returned as the answer.

        # populating the neighbors
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # creating our dfs function i.e., findChanges
        def findChanges(city):
            # get our defined variables
            nonlocal edges, neighbors, visited, changes

            # we need to go to each neighbor of the city
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                # check if the neighbor can visit 0.
                if (neighbor, city) not in edges:
                    changes += 1

                # add this to visited
                visited.add(neighbor)
                # call dfs on its neighbors now
                findChanges(neighbor)
            

        # at this point we have our mapping of each city
        # we need to reach 0 city
        visited.add(0)
        findChanges(0)   # dfs → this function will return me changes
        return changes

        