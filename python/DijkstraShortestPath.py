def build_graph(filename):
    g = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    lines = [line.rstrip().split('\t') for line in lines]
    for line in lines:
        v, edge_and_weights = int(line[0]), line[1:]
        _ = [t.split(',') for t in edge_and_weights]
        edges = {int(edge): int(weight) for edge, weight in _}
        g.append((v, edges))
        
    return {node[0]: node[1] for node in g}

def dijkstra(graph, source=1, DIST=1000000):
    '''
    A function to compute the shortest path between two nodes 
    using the Dijkstra algorithm algorithm
    '''
    # Initilize distance to all nodes except tthe source node to DIST 
    distances = {n : DIST if n != source else 0 for n in graph.keys()}

    # Defining sets to store processed and unprocessed nodes
    processed = set([])
    to_process = {n for n in graph.keys()}

    while len(to_process) > 0:
        min_dis = DIST
        curr_node = -1
        for v in to_process:
            dis = distances[v]
            if dis < min_dis:
                min_dis = dis
                curr_node = v

        processed.add(curr_node)
        to_process.remove(curr_node)

        for neighbor, weight in graph[curr_node].items():
            d = distances[curr_node] + weight
            if distances[neighbor] > d:
                distances[neighbor] = d

    return distances

if __name__ == '__main__':
    graph = build_graph('tests/dijkstra.txt')
    distances = dijkstra(graph)
    node_indices = '7,37,59,82,99,115,133,165,188,197'
    ans = ','.join([ str(distances[int(node)]) for node in node_indices.split(',') ])
    print(ans)





















































