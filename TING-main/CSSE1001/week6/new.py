
def read_config(filename):
    config = {}
    with open(filename) as fin:
        for line in fin:
            line = line.strip()
            if line.startswith('[') and \
                line.endswith(']'):
                #heading line
                heading = line[1:-1]
                config[heading] = {}
            elif line.count('=') == 1\
            and heading is not None:
                attr, _, value = line.partition('=')
                config[heading][attr] = value
            else:
                raise ValueError('Invalid config file')
               
    return config


result = read_config('D:/use for code/tingyi/TING-main/CSSE1001/week6/week06_config.txt')



def get_value(config, setting):
    heading, _, attr = setting.partition('.')
    print(config[heading][attr])




config = read_config('D:/use for code/tingyi/TING-main/CSSE1001/week6/week06_config.txt')
get_value(config, 'user.mobile')