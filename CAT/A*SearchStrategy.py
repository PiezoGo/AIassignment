import heapq
from typing import Dict, List, Tuple, Optional


def astar_search(
    graph: Dict[str, List[Tuple[str, int]]],
    heuristics: Dict[str, int],
    start: str,
    goal: str
) -> Tuple[Optional[List[str]], float]:
    """
    Performs A* Search on a weighted graph.
    
    f(n) = g(n) + h(n)
    • g(n) = actual cost from start to node n
    • h(n) = heuristic estimate from node n to goal
    
    Parameters:
        graph: dict {node: [(neighbor, cost), ...]}
        heuristics: dict {node: estimated_cost_to_goal}
        start: starting node
        goal: goal node
        
    Returns:
        (path, total_cost) if path found, else (None, float('inf'))
    """
    # Priority queue: (f_cost, g_cost, node, path)
    # Using counter to break ties consistently
    counter = 0
    open_list = []
    heapq.heappush(open_list, (heuristics.get(start, 0), 0, counter, start, [start]))
    
    # Best known g-cost for each node
    best_g = {}
    
    while open_list:
        f_cost, g_cost, _, current, path = heapq.heappop(open_list)
        
        # Skip if we found a better path already
        if current in best_g and best_g[current] <= g_cost:
            continue
            
        best_g[current] = g_cost
        
        # Optional: clean debug output
        print(f"→ Visited: {current:>2} | g={g_cost:>2} | f={f_cost:>2} | h={heuristics.get(current, 0):>2}")
        
        # Goal check
        if current == goal:
            return path, g_cost
        
        # Expand neighbors
        for neighbor, step_cost in graph.get(current, []):
            new_g = g_cost + step_cost
            new_h = heuristics.get(neighbor, 0)
            new_f = new_g + new_h
            
            # Only add to open list if promising
            if neighbor not in best_g or new_g < best_g[neighbor]:
                counter += 1
                heapq.heappush(open_list, (new_f, new_g, counter, neighbor, path + [neighbor]))
    
    # No path found
    return None, float('inf')


# ============================
# Example Usage
# ============================

if __name__ == "__main__":
    # Graph: cities with travel costs
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1), ('E', 3)],
        'D': [('E', 1)],
        'E': []
    }
    
    # Admissible heuristic (straight-line distance estimate)
    heuristics = {
        'A': 7,
        'B': 6,
        'C': 4,
        'D': 2,
        'E': 0
    }
    
    print("A* Search Traversal:\n")
    path, cost = astar_search(graph, heuristics, start='A', goal='E')
    print("\n" + "="*50)
    
    if path:
        print(f"Optimal Path : {' → '.join(path)}")
        print(f"Total Cost   : {cost}")
    else:
        print("No path found.")