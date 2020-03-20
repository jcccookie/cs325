from graph import Graph


def isBipartite(n, marks, graph, i):
    queue = []
    queue.append(i)
    
    while queue:
        u = queue.pop(0)
        
        for v in range(n):
            if graph.adjMatrix[u][u] == 1:
                return False
            
            if graph.adjMatrix[u][v] == 1 and marks[v] == -1:
                marks[v] = 1 - marks[u]
                queue.append(v)
                
            elif graph.adjMatrix[u][v] == 1 and marks[v] == marks[u]:
                return False
    return True


def main():
    # Dictionary to store key-value pairs
    # vertices = {
    #     "Ace": 0,
    #     "Duke": 1,
    #     "Jax": 2,
    #     .
    #     .
    # }
    vertices = {}
    
    with open("wrestler3.txt") as f:
        n = int(f.readline()) # number of vertices
        cnt = 0
        # Read vertices
        for x in range(1, n+1):
            line = next(f)
            word = line.replace('\r', '').replace('\n', '')
            vertices[word] = cnt
            cnt += 1
        
        graph = Graph(n) # Create a empty graph with n vertices
        
        # Number of pairs
        r = int(next(f))
        
        # Read pairs
        for y in range(n+2, (n+2)+r):
            line = next(f)
            modifiedLine = line.replace('\n', '').replace('\r', '')
            wordsList = [word for word in modifiedLine.split(' ')]
            
            # Connect vertices with edges
            graph.addEdge(vertices[wordsList[0]], vertices[wordsList[1]])
    
    # Check rivalry
    # Color marks for each vertex  
    # -1: Unchecked
    #  0: Blue
    #  1: Red
    marks = [-1 for i in range(n)]
    bipartite = True
    
    for i in range(n):
        if marks[i] == -1:
            # If unmarked, assign color
            marks[i] = 0
            
            # Check bipartite
            bipartite = isBipartite(n, marks, graph, i)
            # Instantly exit loop when it's false
            if not bipartite:
                break
    
    # Invert vertice's key and value
    # invertedVertices = {
    #     0: 'Bear',
    #     1: 'Maxxx',
    #     2: 'Killer',
    #     .
    #     .
    # }
    invertedVertices = dict((int(y), x) for x, y in vertices.items())
    babyfaces = []
    heels = []
    
    for i, mark in enumerate(marks):
        if mark == 0:
            babyfaces.append(invertedVertices[i])
        else:
            heels.append(invertedVertices[i])
    
    # Print out result
    if bipartite:
        print("Yes,")
        print("Babyfaces: " + " ".join(babyfaces))
        print("Heels    : " + " ".join(heels))
    else:
        print("No.")
            

if __name__ == '__main__':
   main()
   
   
   