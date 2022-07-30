import collections

def getImportance(self, employees, id: int) -> int:
    # Put the employee with id on queue
    
    hash_map = {}
    for emp in employees:
        hash_map[emp.id] = emp
    
    q = collections.deque([hash_map[id]])
    total_imp = 0
    
    while q:
        node = q.popleft()
        total_imp += node.importance
        for subid in node.subordinates:
            q.append(hash_map[subid])
    
    return total_imp
        