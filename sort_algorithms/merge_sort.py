from math import ceil
def merge_sort(A:list, reverse=False):
    d = len(A)
    if d<=1:
        return A
    else:
        mid = ceil(d/2)
        return merge(merge_sort(A[mid:], reverse),merge_sort(A[:mid],reverse), reverse)


def merge(L:list, R:list, reverse=False):
    r = []
    i,j = 0, 0
    if not(reverse):
        while i < len(L) and j < len(R):
            if  L[i]<=R[j]:
                r.append(L[i])
                i+=1
            else:
                r.append(R[j])
                j+=1
    else:
        while i < len(L) and j < len(R):
            if  L[i]<=R[j]:
                r.append(R[j])
                j+=1
            else:
                r.append(L[i])
                i+=1
    r.extend(L[i:])
    r.extend(R[j:])
    return r
