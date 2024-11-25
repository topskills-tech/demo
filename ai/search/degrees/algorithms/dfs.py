from search.degrees.util import neighbors_for_person


def dfs_shortest_path(source, target):
    """
    Find the shortest path between two actors using DFS.
    Args:
        source: ID of the starting actor.
        target: ID of the target actor.
    Returns:
        A list of (movie_id, actor_id) tuples representing the shortest path,
        or None if no path is found.
    """

    stack = [(source, [])] #initialise stack with the source actor and path
    visited = set() #track visited node

    while stack:
        #pop the next actor and the path if the stack is not empty
        current_actor, path = stack.pop()

        if current_actor in visited:
            continue #skip actor if already visited

        visited.add(current_actor) # track actor as visited

        #check all neighbours of current actor
        for movie_id, co_star_id in neighbors_for_person(current_actor):
            new_path = path + [movie_id, co_star_id]

            if co_star_id == target: # we found the connection
                return new_path

            if co_star_id not in visited: # we haven't visited this node
                stack.append((co_star_id, new_path))

    return None


