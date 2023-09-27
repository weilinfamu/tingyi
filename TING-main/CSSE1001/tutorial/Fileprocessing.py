# def find_functions(filename):
#     with open(filename) as fin,\
#         open('functions.txt', 'w') as fout:
#         for line in fin:
#             line = line.strip()
#             if line.startswith("def "):  
#                fout.write(line)
# find_functions('week06_functions.py')   
                                                                                                                           
def find_functions2(filename):
    with open(filename) as fin:
        for line in fin:
            line = line.strip()
            if line.startswith("def "):         
                _, _, line = line.partition(' ')
                
                name, _, line = line.partition('(')
                
                args,_ , _ = line.partition(')')    
                args_list = []
                for arg in args.split(','):
                    args_list.append(arg.strip())
                print(args_list)
               
                
find_functions2('week06_functions.py')                                                                                                                              


