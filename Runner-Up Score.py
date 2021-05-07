if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    

maxx=max(arr)
newlist=[]
for i in range(n):
    if arr[i]!=maxx:
        newlist.append(arr[i])

        
print(max(newlist)) 
