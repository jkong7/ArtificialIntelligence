from expand import expand
from collections import deque, defaultdict
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
            if neighbor not in visited and neighbor not in node_before: 
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
            if neighbor not in visited: 
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
            if neighbor not in visited: 
                heapq.heappush(pq, (heuristic(dis_map, neighbor, end), neighbor))
                node_before[neighbor] = current


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

    pq=[(heuristic(dis_map, start, end), 0, 0, start)]
    g_score=defaultdict(lambda: float('inf'))
    g_score[start]=0
    node_before={}
    visited=set()
    entered=1
    while pq:
        _, current_g, _, current=heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current==end:
            return list(visited), find_path(node_before, start, end)
        
        for neighbor in expand(current, time_map):
            tentative_g=current_g+time_map[current][neighbor]

            if tentative_g<g_score[neighbor]:
                g_score[neighbor]=tentative_g
                heapq.heappush(pq, (tentative_g+heuristic(dis_map, neighbor, end), tentative_g, entered, neighbor))
                entered+=1
                node_before[neighbor]=current
