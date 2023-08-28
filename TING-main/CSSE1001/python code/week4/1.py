def is_dna(sequence):
    if len(sequence) % 3 != 0:
        return False
    
    for i in sequence:
        if i not in ('A','C','G','T'):
            return False
    return True
        
def print_codons(dna):
    if not is_dna(dna):
        print("无效的 DNA 序列")
  #  x=0
  #  while x < len(dna):
  #      print(dna[x:x+3])
   #     x += 3
    for x in range(0,len(dna),3):
       print(dna[x:x+3])
       
print_codons('AAAAAAA')



#3

    
        
    
    
    