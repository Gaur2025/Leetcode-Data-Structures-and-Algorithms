class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # return t as ans
        t = 0
        
        # create a dictionary to store the edges
        edges = collections.defaultdict(list)

        # populating the edges
        for u, v, w in times:
            edges[u].append((v, w))

        # creating a min Heap
        minHeap = [(0, k)]   # as k node is starting node, so it is at a distance of 0

        # visited set so that we don't get stuck inside a cycle
        visited = set()

        # until we go to each node we have to find the distance
        while minHeap:
            # get the minimum path from minHeap (log(n) operation)
            w1, n1 = heapq.heappop(minHeap)

            # if n1 is already visited, go to next node
            if n1 in visited:
                continue

            # else we add it to visited set
            visited.add(n1)

            t = max(t, w1)

            # now going to each connected node to n1
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    # add it to the minHeap
                    heapq.heappush(minHeap, (w1 + w2, n2))


        # as there could be disconnected components as well in the graph. 
        return t if len(visited) == n else -1

        