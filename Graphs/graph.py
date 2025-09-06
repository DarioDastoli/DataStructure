from LinkedLists.singly_linked_list import SinglyLinkedList
from Queues.queue import Queue
from Stacks.stack import Stack
from typing import Any

class Graph:
    class Vertex:
        def __init__(self, key):
            self.id = key
            self.adj_list = SinglyLinkedList()

        def has_edge_to(self, destination_vertex):
            return self.adj_list.search(destination_vertex) is not None
        
        def add_edge_to(self, destination_vertex):
            if self.has_edge_to(destination_vertex):
                raise ValueError(f'Edge already exists.')
            self.adj_list.insert_in_front(destination_vertex)

        def delete_edge_to(self, destination_vertex: 'Graph.Vertex'):
            self.adj_list.delete(destination_vertex)
        
        def outgoing_edges(self):
            return [(self.id, v.id) for v in self._adj_list]

    def __init__(self):
        self._adj = {}

    def _get_vertex(self, key) -> Vertex:
        if key not in self._adj:
            raise ValueError(f'Vertex {key} does not exist!')
        return self._adj[key]
    
    def insert_vertex(self, key):
        if key in self._adj:
            raise ValueError(f'Vertex {key} already exists!')
        self._adj[key] = Graph.Vertex(key)

    def vertex_count(self) -> int:
        return len(self._adj)

    def insert_edge(self, key1, key2):
        v1 = self._get_vertex(key1) 
        v2 = self._get_vertex(key2) 
        v1.add_edge_to(v2)


    def delete_edge(self, key1, key2):
        v1 = self._get_vertex(key1) 
        v2 = self._get_vertex(key2) 
        v1.delete_edge_to(v2)

    def delete_vertex(self, key):
        vertex = self._get_vertex(key)

        for u in self._adj.values():
            if u != vertex and u.has_edge_to(vertex):
                u.remove_edge_to(vertex)
        del self._adj[key]
        

    def bfs(self, start_vertex, target_vertex):
        
        def reconstruct_path(pred: dict[Any, Any], target: Any) -> list[Any]:
            # Reconstruct the path from start to target by going back until it finds a vertex
            # without predecessor: That can only be the start vertex
            path = []
            while target:
                path.append(target)
                target = pred[target]
            return path[::-1]

        
        distance = {v: float('inf') for v in self._adj} #This line creates a dictionary where each key is a vertex in the graph
        predecessor = {v: None for v in self._adj}
        queue = Queue(self.vertex_count())
        # Initially, we add the start vertex to the queue
        queue.enqueue(start_vertex)
        distance[start_vertex] = 0
        while not queue.is_empty():
            u = queue.dequeue()
            if u == target_vertex:
                # We have found the shortest path to the target
                return reconstruct_path(predecessor, target_vertex)
            
            # For each of u's neighbors, we check if there was already a shorter path to them
            for (_, v) in self._get_vertex(u).outgoing_edges():
                if distance[v] == float('inf'):
                    distance[v] = distance[u] + 1
                    predecessor[v] = u
                    queue.enqueue(v)

        #At this point, we know there is no path from the start to the target vertex
        return None
            

    def dfs(self, start_vertex, color=None):
        if color is None:
            color = {v: 'white' for v in self._adj}
            acyclic = True
            stack = Stack()
            stack.Push((False, start_vertex))
            while not stack.is_empty():
                (mark_as_black, v) = stack.Pop()
                col = color.get(v, 'white')
                if mark_as_black:
                    color[v] = 'black'
                elif col == 'grey':
                    color[v] = 'grey'
                    acyclic = False
                elif col == 'white':
                    color[v] = 'grey'
                    stack.Push((True, v))
                    for(_, w) in self._get_vertex(v).outgoing_edges():
                        stack.Push((False, w))
            return acyclic, color
