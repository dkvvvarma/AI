def water_jug_dfs(capacity_a, capacity_b, target):
    def dfs(a, b, visited):
        if (a, b) in visited:
            return False
        
        visited.add((a, b))
        
        if a == target or b == target:
            return True
      
        if dfs(capacity_a, b, visited):
            return True
        
        if dfs(a, capacity_b, visited):
            return True
        
        if dfs(0, b, visited):
            return True
        
        if dfs(a, 0, visited):
            return True
        
        pour = min(a, capacity_b - b)
        if dfs(a - pour, b + pour, visited):
            return True
        
        pour = min(b, capacity_a - a)
        if dfs(a + pour, b - pour, visited):
            return True
        
        return False
    
    visited = set()
    return dfs(0, 0, visited)

capacity_a = int(input("Enter amount of water(lit) in jug 1: "))
capacity_b = int(input("Enter amount of water(lit) in jug 2: "))
target = int(input("Enter total target amount of water(lit) : "))

if water_jug_dfs(capacity_a, capacity_b, target):
    print(f"Target {target} liters can be measured.")
else:
    print(f"Target {target} liters cannot be measured.")