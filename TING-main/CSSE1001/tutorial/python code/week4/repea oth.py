def is_dna(xox):
    if len(xox) %3 !=0:
        return False
    for x in xox:
        if x not in ('A','T','C','G'):
            return False
        else: return True


def reverse_complement(xox):
    if not is_dna(xox):
          return None
    
    complement = ' ' 
    for x in xox:
        if x == 'A':
            complement += 'T'
        if x == 'T':
            complement += 'A'
        if x == 'c':
            complement +='G'
        if x == 'G':
            complement +='C'
    return complement [::-1]
a = reverse_complement('ATCGGG')
print(a)
            
        
          
