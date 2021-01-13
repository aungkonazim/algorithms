from collections import defaultdict
def findItinerary(tickets):
    outdeg={}
    graph=defaultdict(list)
    for a,b in tickets:
        graph[a].append(b)
        if a not in outdeg:
            outdeg[a]=1
        else:
            outdeg[a]+=1
        if b not in outdeg:
            outdeg[b]=0
    for i in graph:
        graph[i]=sorted(graph[i])
    path=[]
    def DFS(at):
        print(outdeg,at)
        while outdeg[at]!=0:
            # print(graph[at],-outdeg[at])
            nex=graph[at][-outdeg[at]]
            outdeg[at]-=1
            DFS(nex)
        print(path)
        path.append(at)
    print(graph,outdeg)
    DFS("JFK")
    return path[::-1]
input_ = [["MUC","LHR"],["JFK","MUC"],["LHR","JFK"],["JFK","CCC"],["CCC","JFK"]]
input_ = [['JFK','CCC'],['CCC','JFK'],['BBB','JFK'],['JFK','BBB'],['JFK','AAA']]
print(findItinerary(input_))