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

def heuristic(dis_map, node, end): 
    return dis_map[node][end]

def best_first_search(dis_map, time_map, start, end):
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
    pq=[(heuristic(dis_map, start, end), start)]
    visited=set()
    node_before={}
    while pq: 
        _, current = heapq.heappop(pq)
        if current in visited: 
            continue 
        visited.add(current)
        if current==end: 
            return list(visited), find_path(node_before, start, end)
        for neighbor in expand(current, time_map): 
            if neighbor not in visited and neighbor not in node_before: 
                heapq.heappush(pq, (heuristic(dis_map, neighbor, end), neighbor))
                node_before[neighbor]=current 


def a_star_search(dis_map, time_map, start, end):
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

    entered=0 
    pq=[(0 + heuristic(dis_map, start, end), heuristic(dis_map, start, end), entered, start)]
    entered+=1 
    g_score={start: 0}
    node_before={}
    while pq: 
        _, _, _, current=heapq.heappop(pq)
        if current==end: 
            return list(g_score.keys()), find_path(node_before, start, end)
        for neighbor in expand(current, time_map): 
            new_g = g_score[current] + time_map[current][neighbor]
            new_h = heuristic(dis_map, neighbor, end)
            new_f = new_g + new_h
            if neighbor not in g_score or new_g<g_score[neighbor]: 
                g_score[neighbor]=new_g
                heapq.heappush(pq, (new_f, new_h, entered, neighbor))
                entered+=1 
                node_before[neighbor]=current





