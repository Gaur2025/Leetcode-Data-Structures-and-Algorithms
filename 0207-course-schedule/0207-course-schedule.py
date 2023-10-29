class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        This function is responsible to check whether we can finish all the courses given.
        Approach: DFS (We can perform DFS to visit each course node)
                    a. A hashmap can be used to store the prerequisites of every course.
                    b. A visitSet can also be maintained to have a track of visited course node.
                    c. We perform dfs to visit each course node.
                    d. Then check if it has prerequisite nodes.
                    e. If no prerequisites ⇒ return True, else False
        """
        
        # Map each course to a prerequisite list.
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet ⇒ to track all courses along the current DFS path
        visitSet = set()

        def dfs(crs):
            # to handle the cyclic edge cases (pre = [[1, 2], [1, 3], [2, 3]])
            # we need to store the course nodes into a visitSet
            if crs in visitSet:
                return False

            # if there is no prerequisite
            if preMap[crs] == []:
                return True

            # Now visiting a course node
            visitSet.add(crs)

            # check if it has prerequisite
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # after visiting
            visitSet.remove(crs)

            # if all prerequisites are visited
            preMap[crs] = []
            return True

        # Now calling dfs for all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        