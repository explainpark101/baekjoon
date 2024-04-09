import sys
from typing import List, Optional, Union, Set, Tuple
import json

input = sys.stdin.readline

class Tree:
    parent:'Tree' = None
    __children: list['Tree'] = []
    number:int
    cost:int
    
    def __init__(self, num:int, parent:Union[None,'Tree']=None, children:Union[List['Tree'], None]=[], costMap:dict={}) -> None:
        self.number = num
        self.parent = parent
        self.children = children
        self.cost = costMap.get(num)
    
    @property
    def children(self):
        return self.__children
    
    @children.setter
    def children(self, values:Union[List[Union['Tree', int]], None]):
        if values is None:
            self.__children = None
            return 
        
        self.__children = [
            (Tree(v, self, None) if isinstance(v, int) else v) 
            for v in values
        ]
    
    def iter_children(self, buildings, costMap) -> 'Tree':
        if self.children is None:
            return self
        for child in self.children:
            child.children = buildings.get(child.number)
            if child.cost is None:
                child.cost = costMap.get(child.number)
                
            child.iter_children(buildings, costMap)
        return self
    
    @property
    def total_cost(self) -> Tuple[int, Set[int]]:
        if self.children is None:
            return self.cost, set()
        completed_numbers:Set[int] = set()
        
        cost = self.cost
        next_children:List[Tree] = []
        for child in self.children:
            if child.children is not None:
                next_children += child.children
            cost += child.cost
            completed_numbers.add(child.number)


        return cost, completed_numbers
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        if self.children is None:
            return f"{self.number}"
        return f"""{{ {self.number} -> {self.children} }}"""
    
    def print(self) -> None:
        ...
        
    
    @property
    def is_end(self): return self.children is None

def main():
    for _ in range(int(input())): #Test count
        buildings = {}
        건물개수, 건물순서규칙개수 = list(map(int, input().split(" ")))
        costMap = dict(((idx+1, cost) for idx, cost in enumerate(map(int, input().split(" ")))))
        건물순서목록 = (list(map(int, input().split(" "))) for _ in range(건물순서규칙개수))
        
        for start, target in 건물순서목록:
            if buildings.get(target):
                buildings[target].append(start)
            else: buildings[target] = [ start ]
            
        goal = int(input())
        tree_head = Tree(goal, None, buildings.get(goal), costMap)
        total_cost, completed = tree_head.iter_children(buildings, costMap).total_cost
        print(total_cost, completed, tree_head)
        
        

    
main()