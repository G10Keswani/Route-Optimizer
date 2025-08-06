def optimize_route(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True

    for _ in range(n - 1):
        last = route[-1]
        next_city = min((i for i in range(n) if not visited[i]), key=lambda i: distance_matrix[last][i])
        route.append(next_city)
        visited[next_city] = True

    return route
