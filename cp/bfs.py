 def bfsOfGraph(self, V, adj):
        visited=[0]*V
        ans=[0]
        de.appendleft(0)
        visited[0]=1
        while de:
            x=de.pop()
            for i in range(len(adj[x])):
                if visited[adj[x][i]]==0:
                    visited[adj[x][i]]=1
                    ans.append(adj[x][i])
                    de.appendleft(adj[x][i])
        return ans
                    