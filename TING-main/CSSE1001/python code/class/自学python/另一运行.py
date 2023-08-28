def rotate(xs:list[int],k:int)->list:
    '''
    rotate ([1,2,3,4,5],2)
    [3,4,5,6,1,2]
    '''
    a = xs[k:] + xs[:k]
    return a
result = rotate([1,2,3,4,5],2)
print(result)