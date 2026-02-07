# 解題思路

題目中的腐爛橘子會讓四周的新鮮橘子腐爛，第一直覺想到可以用dfs解
但多個腐爛橘子會同時讓周遭的新鮮橘子腐爛，並計算讓所有橘子腐爛要花多少時間，所以要使用bfs

會需要三個變數，分別記錄
- 目前新鮮橘子的個數
- 所花費的時間
- 哪些地方有腐爛橘子

先跑一個雙層回圈記錄腐爛橘子
```python
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 2:
            queue.append((r, c))
        elif grid[r][c] == 1:
            fresh += 1
```

當queue裡面有腐爛橘子，並且新鮮橘子個數大於0時，腐爛橘子就會繼續蔓延，而我們要計算時間
```python
while queue and fresh > 0:
    for _ in range(len(queue)):
        r, c = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc))
```

遍歷queue，找到腐爛橘子局子的位子，找到其四周，如果是新鮮橘子就改marked 為2，同時更新新鮮橘子的數量
並且剛腐爛的橘子也要加進queue中
每個while 回圈就是一次腐爛過程，所以是在while loop層級中加上花費時間
```python
while queue and fresh > 0:
    for _ in range(len(queue)):
        r, c = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc))
                
    minutes += 1
```

最後，如果新鮮橘子個數為0，便回傳花費時間
若個數大於1，根據題意，則回傳-1
```python
return minutes if fresh == 0 else -1
```

Time Complexity: O(m * n) m=rows, n=cols，等於需要遍歷的格數
Space Complexity: O(m*n) 最差的情況下，所有格子都是腐爛橘子，每個格子的橘子都要加入道queue中
