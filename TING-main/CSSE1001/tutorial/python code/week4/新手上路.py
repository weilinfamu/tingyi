def is_dna(string):
    if len(string) % 3 != 0:
        return False

    for i in string:
        if i not in('A', 'T', 'C', 'G'):
            return False
    return True
a = is_dna('ATCGG')
print(a)
    

        

