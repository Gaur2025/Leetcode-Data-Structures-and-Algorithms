class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        This function is responsible for returning the order in which courses are to be taken.
        Approach:
            a. A DFS approach can be used.
            b. We can start with a 0-th node. Check for its neighbors in prereq hashmap.
            c. If a neighbor exists we run dfs on it.
            d. If any neighbor doesn't exist, then we add that node's value to our output.
            e. To track whether we have visited a node or not, we can use a hashset.
            *f. If it is impossible to find any prerequisite node/course, we return an empty list.
            TC = O(numCourses + numPrerequisites)
        """
        # creating hashmap, output list, and visit and cycle sets.
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites: 
            prereq[crs].append(pre)

        output = []

        visit, cycle = set(), set()

        # creating our DFS function
        def dfs(crs):
            # if a cycle is made
            if crs in cycle:
                return False

            # if the course is already visited
            if crs in visit:
                return True

            # if the course graph is making any cycle
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)

            # if the course is neither visited, nor a start of any cycle in graph. 
            # we add it to our visit set and save the result in the output.
            visit.add(crs)
            output.append(crs)
            return True

        # dfs on each course node
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output

        