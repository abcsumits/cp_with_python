def dfs(vertex):
    #print(vertex)
    if visited[vertex]==1:
        return
    else:
        visited[vertex]=1
        for i in range(len(gp[vertex])):
            if visited[gp[vertex][i]]==1:
                continue
            else:
                dfs(gp[vertex][i])
        return