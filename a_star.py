from graph import Graph
from queue import PriorityQueue


def a_star(graph, start_vertex, target):
    # Create the priority queue for open vertices.
    vertices_pq = PriorityQueue()

    start_vertex.cost = start_vertex.h

    # Adds the start vertex to the priority queue.
    print(f'Visiting/queueing vertex {start_vertex.entity}')
    vertices_pq.put(start_vertex)
    print('Prioritized vertices (v, cost(v)):',
          *((vert.entity, vert.cost) for vert in vertices_pq.queue), end=2 * '\n')

    # The starting vertex is visited first and has no leading edges.
    # If we did not put it into 'visited' in the first iteration,
    # it would end up in 'visited' during the second iteration, pointed to
    # by one of its children vertices as a previously unvisited vertex.
    visited[start_vertex] = None

    # Loops until the priority list gets empty.
    while not vertices_pq.empty():
        # Gets the vertex with the lowest cost.
        vertex = vertices_pq.get()
        # If the vertex being explored is a target vertex, ends the algorithm.
        print(f'Exploring vertex {vertex.entity}')
        if vertex.entity == target:
            return vertex
        # Examines each non-visited adjoining edge/vertex.
        for edge in graph.adjacent_edges(vertex):
            # Gets the second endpoint.
            v_2nd_endpoint = edge.opposite(vertex)

            # Skips the explored vertices.
            if v_2nd_endpoint in explored:
                continue

            # Checks if the endpoint has a weight and is the weight the cheapest one.
            if v_2nd_endpoint.cost is None \
                    or vertex.cost - vertex.h + edge.weight < v_2nd_endpoint.cost - v_2nd_endpoint.h:
                # Adds the second endpoint to 'visited' and maps
                # the leading edge for the search path reconstruction.
                v_2nd_endpoint.cost = vertex.cost - vertex.h + edge.weight + v_2nd_endpoint.h
                # Prevents reinsertion to the priority queue. The
                # endpoint distance value will be updated.
                if v_2nd_endpoint not in visited:
                    print(f'Visiting/queueing vertex {v_2nd_endpoint.entity}')
                    vertices_pq.put(v_2nd_endpoint)
                # Forces the priority queue to recalculate in case of an
                # inner vertex update resulting with the highest priority
                vertices_pq.put(vertices_pq.get())
                # Replaces the previous vertex' ancestor with a cheaper one.
                visited[v_2nd_endpoint] = edge
        print('Prioritized vertices (v, cost(v)):',
              *((vert.entity, vert.cost) for vert in vertices_pq.queue), end=2 * '\n')
        # The vertex is used for update and put aside.
        explored.append(vertex)
    return None

