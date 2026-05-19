def insertion_sort(l:list):
    """Algorithm insertion_sort:\n
    Sorted input massive\n
    Example: input: [5,2,4,6,1,3] —> output: [1, 2, 3, 4, 5, 6]
    """
    for j in range(1, len(l)):
        x = l[j]
        i = j-1
        while i>=0 and l[i]>x:
            l[i+1] = l[i]
            i-=1
        l[i + 1] = x