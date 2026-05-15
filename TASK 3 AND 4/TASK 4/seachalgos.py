# =============================================
# TASK FOUR – SEARCH AND OPTIMIZATION
# Breadth First Search (BFS) and Depth First Search (DFS)
# =============================================

from collections import deque

# ==================== GRAPH DEFINITION ====================
# Using Adjacency List representation

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# ==================== BFS IMPLEMENTATION ====================
def breadth_first_search(start, goal):
    print("=== BREADTH FIRST SEARCH (BFS) ===")
    print(f"Starting from: {start}  →  Goal: {goal}\n")
    
    queue = deque([(start, [start])])      # (current_node, path)
    visited = set()
    
    print("Exploration Order:")
    while queue:
        current, path = queue.popleft()
        
        if current in visited:
            continue
            
        visited.add(current)
        print(f"Visited: {current} | Path: {path}")
        
        if current == goal:
            print("\n GOAL FOUND!")
            print(f"Shortest Path (BFS): {' → '.join(path)}")
            return path
        
        # Add neighbors to queue
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    print(" Goal not found!")
    return None


# ==================== DFS IMPLEMENTATION ====================
def depth_first_search(start, goal):
    print("\n\n=== DEPTH FIRST SEARCH (DFS) ===")
    print(f"Starting from: {start}  →  Goal: {goal}\n")
    
    stack = [(start, [start])]          # (current_node, path)
    visited = set()
    
    print("Exploration Order:")
    while stack:
        current, path = stack.pop()     # Pop from end (Stack behavior)
        
        if current in visited:
            continue
            
        visited.add(current)
        print(f"Visited: {current} | Path: {path}")
        
        if current == goal:
            print("GOAL FOUND!")
            print(f"Path Found (DFS): {' → '.join(path)}")
            return path
        
        # Add neighbors to stack (in reverse to maintain left-to-right order)
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    
    print("Goal not found!")
    return None


# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    print("GRAPH USED FOR SEARCH:")
    for node in graph:
        print(f"  {node} → {graph[node]}")
    print("-" * 50)
    
    # Run BFS
    bfs_path = breadth_first_search('A', 'G')
    
    # Run DFS
    dfs_path = depth_first_search('A', 'G')
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"BFS Path:   {' → '.join(bfs_path) if bfs_path else 'None'}")
    print(f"DFS Path:   {' → '.join(dfs_path) if dfs_path else 'None'}")
    print("\nNote: BFS finds the shortest path in an unweighted graph.")