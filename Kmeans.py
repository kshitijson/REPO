import math

data_set = [2, 4, 10, 12, 3, 20, 30, 11, 25]
m1 = data_set[0]
m2 = data_set[1]

cluster1 = [0] * len(data_set)
cluster2 = [0] * len(data_set)
itter_count = 0
flag = False

while not flag:
    sum1 = 0
    sum2 = 0
    itter_count += 1
    cluster1 = [0] * len(data_set)
    cluster2 = [0] * len(data_set)

    k = 0
    j = 0
    for i in range(0 ,len(data_set)):
        if(abs(data_set[i] - m1) <= abs(data_set[i] - m2)):
            cluster1[k] = data_set[i]
            k += 1
        else:
            cluster2[j] = data_set[i]
            j += 1
    
    for i in range(0, len(cluster1) - 1):
        sum1 += cluster1[i]
    
    for i in range(0, len(cluster2) - 1):
        sum2 += cluster2[i]


    print(f"\n\n************* Iteration {itter_count} *************")
    a = m1
    b = m2
    m1 = math.ceil(sum1 / k)
    m2 = math.ceil(sum2 / j)
    flag = (a == m1 and b == m2)

    print(f'\n mean1 = {a}, mean2 = {b}')
    print(f'Cluster 1 -----> {cluster1}')
    print(f'Cluster 2 -----> {cluster2}')


print('\n\n***************************************************************')
print(f'\nFinal Cluster 1 -----> {cluster1}')
print(f'Final Cluster 2 -----> {cluster2}')