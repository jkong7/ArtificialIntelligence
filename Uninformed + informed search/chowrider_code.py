from expand import expand
from collections import deque
import heapq 


def find_path(node_before, start, end): 
    path=[]
    current=end 
    while current!=start: 
        path.append(current)
        current=node_before[current]
    path.append(current)
    return path[::-1]

def breadth_first_search(time_map, start, end):
    """
    Breadth-first Search

    Args:
        time_map (dict): A map containing travel times between connected nodes (places or intersections), where every
        node is a dictionary key, and every value is an inner dictionary whose keys are the children of that node and
        values are travel times. Travel times are "null" for nodes that are not connected.
        start (str): The name of the node from where to start traversal
        end (str): The name of the node from where to start traversal

    Returns:
        visited (list): A list of visited nodes in the order in which they were visited
        path (list): The final path found by the search algorithm
    """

    visited=set()
    node_before={}
    q=deque([start])
    while q: 
        current=q.popleft()
        if current in visited: 
            continue 
        visited.add(current)
        if current==end: 
            return list(visited), find_path(node_before, start, end)
        for neighbor in expand(current, time_map): 
            if neighbor not in visited and neighbor and neighbor not in node_before: 
                q.append(neighbor)
                node_before[neighbor]=current 

def depth_first_search(time_map, start, end):
    """
    Depth-first Search

    Args:
        time_map (dict): A map containing travel times between connected nodes (places or intersections), where every
        node is a dictionary key, and every value is an inner dictionary whose keys are the children of that node and
        values are travel times. Travel times are "null" for nodes that are not connected.
        start (str): The name of the node from where to start traversal
        end (str): The name of the node from where to start traversal

    Returns:
        visited (list): A list of visited nodes in the order in which they were visited
        path (list): The final path found by the search algorithm
    """

    stack=[start]
    visited=set()
    node_before={}
    while stack: 
        current=stack.pop()
        if current in visited: 
            continue 
        visited.add(current)
        if current==end: 
            return list(visited), find_path(node_before, start, end)
        for neighbor in expand(current, time_map): 
            if neighbor not in visited and neighbor not in node_before: 
                stack.append(neighbor)
                node_before[neighbor]=current 

                
# TO DO: Implement Greedy Best-first Search.
def best_first_search(time_map, dis_map, start, end):
    """
    Greedy Best-first Search

    Args:
        time_map (dict): A map containing travel times between connected nodes (places or intersections), where every
        node is a dictionary key, and every value is an inner dictionary whose keys are the children of that node and
        values are travel times. Travel times are "null" for nodes that are not connected.
        dis_map (dict): A map containing straight-line (Euclidean) distances between every pair of nodes (places or
        intersections, connected or not), where every node is a dictionary key, and every value is an inner dictionary whose keys are the
        children of that node and values are straight-line distances.
        start (str): The name of the node from where to start traversal
        end (str): The name of the node from where to start traversal

    Returns:
        visited (list): A list of visited nodes in the order in which they were visited
        path (list): The final path found by the search algorithm
    """

    pass

# TO DO: Implement A* Search.
def a_star_search(time_map, dis_map, start, end):
    """
    A* Search

    Args:
        time_map (dict): A map containing travel times between connected nodes (places or intersections), where every
        node is a dictionary key, and every value is an inner dictionary whose keys are the children of that node and
        values are travel times. Travel times are "null" for nodes that are not connected.
        dis_map (dict): A map containing straight-line (Euclidean) distances between every pair of nodes (places or
        intersections, connected or not), where every node is a dictionary key, and every value is an inner dictionary whose keys are the
        children of that node and values are straight-line distances.
        start (str): The name of the node from where to start traversal
        end (str): The name of the node from where to start traversal

    Returns:
        visited (list): A list of visited nodes in the order in which they were visited
        path (list): The final path found by the search algorithm
    """

    pass
