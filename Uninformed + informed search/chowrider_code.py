from expand import expand

# TO DO: Implement Breadth-first Search.
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

    pass

# TO DO: Implement Depth-first Search.
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

    pass

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
