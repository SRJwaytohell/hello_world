li = []
D = float('-inf')
f = open("a_input.txt", "r")
for x in f:
    li.append(x.split(' ').ignore('\n'))
print(li)
    #D = x[0]
    #I = x[2]
    #S = x[4]
    #V = x[6]
    #F = x[8]
    #print(x)    

dgraph = {'0': [['1',2,0,'g'],['2',]],       #id, waiting_car,moving_car,r/g,
             '1': ['2'],
             '2': ['0','3'],
             '3': ['0']
          }
print(dgraph)
def find_path(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return path
    res = []
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: 
                 res.append(newpath)
    return res        
print(find_path(dgraph,'2','1'))
