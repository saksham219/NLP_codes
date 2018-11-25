import numpy as np

def Levenshtein_dist(s1,s2):

    # get lengths
    N = len(s1)
    M = len(s2)

    # initialisation
    dist_mat = np.zeros((N+1,M+1), dtype='int')

    dist_mat[1:N+1, 0] = list(range(1,N+1))
    dist_mat[0, 1:M+1] = list(range(1,M+1))

    # recurrence calculation
    for i in range(1,N+1):
        for j in range(1,M+1):
            ins_cost = dist_mat[i,j-1] + 1  # deletion
            del_cost = dist_mat[i-1,j] + 1  # insetion
            sub_cost = dist_mat[i-1,j-1] + 2 if s1[i-1] != s2[j-1] else dist_mat[i-1,j-1]   # substitution

            min_cost = min(ins_cost, del_cost, sub_cost)

            dist_mat[i,j] = min_cost

    # termination
    print(dist_mat)
    return dist_mat[N, M]

