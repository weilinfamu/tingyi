
def is_dna(sequence):
    if len(sequence) % 3 !=0:
        return False

    for i in sequence:
        if i not in ('A','C','G','T'):
            return False
    return True
print(is_dna('ATG'))  
##2     

    
#     if not is_dna(dna):
#         return None
#     complement_dic = {'A':'T','T':'A','C':'G','G':'C'}
#     complement = []
#     for i in dna:
#         if i in complement_dic:
#             complement.append(complement_dic[i])
#     reverse_complement =''.join(complement[::-1])
#     return reverse_complement
# print(reverse_complement('ATCGGG'))
#     complement = []
def reverse_complement(dna):
    if not is_dna(dna):
      return None
    complement = []
    for i in dna:
        if i == 'A':
          complement += 'T'
        elif i == 'T':
           complement+= 'A'
        elif i == 'C':
            complement += 'G'
        elif i == 'G':
            complement+= 'C'
    
    reverse_complement =''.join(complement[::-1])

    return reverse_complement
print(reverse_complement('ATCGGG'))

#3
def print_codons(dna):
    if not is_dna(dna):
        print('无效的DNA序列')
        pass
    else:
        for i in range(0,len(dna),3):    #range(0,len(dna),3)
            print(dna[i:i+3])
print_codons('ATCGGG')

# #4
# num1 = input('请输入第一个数字：')
# num2 = input('请输入第二个数字：')
# op = input('请输入运算符：')
# sum = eval(f'{num1}{op}{num2}')
# print(sum)

##
def generate_codons(dna):
    if not is_dna(dna):
        return None
    codons = []
    for i in range(0,len(dna),3):
        codons.append(dna[i:i+3])
    return codons
def print_codons(codons):  #接着的是这个codons
    for i in codons:
        print(i)
        

print_codons(generate_codons("AAAAAAAAA"))   #调用函数之后，后面必须打印下来，不然没有输出
    


              