def remove(c: str , cs:str) -> str:
    """
    precondition:len(c) == 1
    >>>remove('b', 'bluey')
    'luey'
    """
    ans = ''
    for x in cs:   #character in cs
        if c == x:
            pass
        else:
            ans += x
    return ans 
print(remove('b' , 'bluey'))
    ------------------------