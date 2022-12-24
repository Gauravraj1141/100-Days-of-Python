
def optimalPoint(magic, dist):
    # Write your code here
    for i in range(len(magic)):
        magic_level = magic[i]
        for j in range(len(dist)):
          magic_level -= dist[j]
          if magic_level < 0:
            break
          magic_level += magic[(i + j + 1) % len(magic)]
          # print(magic_level)
          print(magic[(i + j + 1) % len(magic)])
          print("hey i is ",i)
        else:
            if i == 0:
                return i
            if i >= 0:
                return 1
    return -1

magic = [10,6,3,8,1]
dist = [1,3,8,4,3]
print(optimalPoint(magic, dist))