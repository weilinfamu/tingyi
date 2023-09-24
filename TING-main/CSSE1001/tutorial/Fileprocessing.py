def find_functions(week06_functions):
    with open(week06_functions) as fin:
        for line in fin:
            if line.startswith("def "):  
                print(line)
            