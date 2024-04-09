import sys
from typing import List, Set, Union
input = lambda :sys.stdin.readline().strip()

class Node:
    required_time:int
    index:int
    requirements:Set['Node']
    derivations:Set['Node']
    
    start_time:int = 0
    
    def __hash__(self): return hash(self.index)
    def __eq__(self, x) -> bool: return x.index == self.index
    def __ne__(self, x) -> bool: return x.index != self.index
    
    def __lt__(self, x:'Node') -> bool: return self.required_time < x.required_time
    def __gt__(self, x:'Node') -> bool: return self.required_time > x.required_time
    def __radd__(self, x) -> int: return self.required_time + int(x)
    def __add__(self, x) -> int: return self.required_time + int(x)
    
    def __iter__(self): return self
    
    def __init__(self, cost, index) -> None:
        self.required_time = cost
        self.index = index
        self.requirements = set()
        self.derivations = set()
    
    def __repr__(self) -> str:
        return f"{self.index}"

    def completed(self, elapsed_time:int):
        return self.start_time + self.required_time < elapsed_time



def get_roots(node:Node) -> Set[Node]:
    last_nodes = node.requirements
    root_nodes = set()
    if len(last_nodes) == 0:
        return {node}
    for requirement in last_nodes:
        requirement.derivations.add(node)
        root_nodes |= get_roots(requirement)
    return root_nodes
    
    

def eta(goal:Node) -> List[Set[Node]]:
    if len(goal.requirements) == 0:
        return goal.required_time
    
    elapsed_time = 0
    roots = get_roots(goal)
    currents = list(roots)
    derivations = set().union([n.derivations for n in currents])

        
    return elapsed_time    

def main() -> None:
    testCount = int(input())
    for _ in range(testCount):
        건물개수, 건물순서규칙개수 = list(map(int, input().split(" ")))
        nodeMap:dict[str, Node] = dict(((idx+1, Node(required_time, idx+1)) for idx, required_time in enumerate(map(int, input().split(" ")))))
        adjMat = [list(map(int, input().split(" "))) for _ in range(건물순서규칙개수)]
        for start, target in adjMat:
            nodeMap[target].requirements.add(nodeMap[start])
        goal = int(input())
        
        get_roots(nodeMap[goal])
        


main()