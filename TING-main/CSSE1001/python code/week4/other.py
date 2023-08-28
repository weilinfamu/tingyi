def is_dna(string):
    if len(string) % 3 != 0:
      return False
    for i in string:
        if i not in ('A', 'T', 'C', 'G'):
            return False 
        else:
            return True

def reverse_complement(dna):
    if not is_dna(dna):
        return None
    
    compliment = ' '
    for c in dna:
        if c == 'A':
            compliment += 'T'
        if c == 'T':
            compliment += 'A'
        if c == 'C':
            compliment += 'G'
        if c == 'G':
            compliment += 'C'
    return compliment
a = reverse_complement('ATCGGG')
print(a)

            
        
    