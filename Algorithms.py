import numpy as np
import sort_algorithms as sa
from test import time_test as tt

if __name__=="__main__":
    A = np.random.randint(-10**5,10**5,10**7)
    # tt(sa.ins_sort, A)
    tt(sa.merge_sorted, A)