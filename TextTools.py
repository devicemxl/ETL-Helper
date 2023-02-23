def decimalToBinary(n):
    return ''.join(format(ord(i), '08b') for i in n)
#
# Jaccard Distance
# By David Ochoa
def JaccardDistance(A,B):
    a=set(A.lower())
    b=set(B.lower())
    d = (float(len(a.intersection(b))) / len(a.union(b)))
    return d
#
# Hamming Distance
# By David Ochoa
def HammingDistance(x, y):
    x=x.lower()
    y=y.lower()
    d= float((sum(xi != yi for xi, yi in zip(x, y))+0.00000001))
    return d

# Longest common substring recursion
# Original code by Ryuga

def lcs(i,j,X,Y,count):
    if (i == 0 or j == 0):
        return count
    if (X[i - 1] == Y[j - 1]):
        count = lcs(i - 1, j - 1,X,Y, count + 1)
    count = max(count, max(lcs(i, j - 1,X,Y, 0), lcs(i - 1, j,X,Y, 0)))
    return count
