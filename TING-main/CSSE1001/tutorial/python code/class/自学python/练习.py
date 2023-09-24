# if 
可以条件嵌套  built-in  (if 里面加if)


elif 
==================
from random import randint 
======================
循环结构
for- in 循环
a = (1, 2, 3, 4, 5)
x = sum(a)
for x in range(1,100):
sum += 1
print (sum)
=====
ranage(1,100,2)

x%2 == 0
===================
break 指的是跳出本次的循环
continue 直接继续
==========================
while 循环
while True:：



===================
for i in range (1,10)
    for j in range (1,i+1)
        print (i,'*',j,'=',i*j,end='\t')
    print()
=====================
    
for i in range (1,10):
    for j in range (1,i+1):
        print (i,'*',j,'=',i*j,end='\t')
    print()
    
===========    =========================================

找（100,1000）水仙花数     153 = 1**3 + 5**3 + 3**3

for i in range(100,1000):
    low = i % 10
    mid = i // 10
    high = i // 100
    if i == low **3 + mid **3 + high **3:
        print(i)
        

====================
def factorial(num):
    ”“”
    求阶乘
    “”“
    result = 1
    for i in range(1, num+1):
        result *= i 
    return result
=======================
正确的求阶乘
def factorial(num):
    """
    求阶乘
    """
    result = n
    for i in range (n,0,-1):
        result *= i 
    return result
    =====================
m = int(input(''))
===============================
def factorial(n):
    """
    Calculate the factorial of a number.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Prompt the user to input values for 'm' and 'n'
m = int(input('m='))
n = int(input('n='))

# Calculate factorials for 'm', 'n', and 'm - n'
fm = factorial(m)
fn = factorial(n)
fmn = factorial(m - n)

# Calculate the combination formula C(M, N)
combination = fm // (fn * fmn)

# Print the result
print(f"C({m}, {n}) = {combination}"   #还是不理解
      ==============================
      需要再字符中插入变量的值，可以使用 f-string
      f"{变量名}"
x = 123
print (f"{x} {x}的值是123")
花括号中的值是变量
==============================
成员运算
'x' in 'xz123'
print('x' in 'xz123')
------------------------
'x' not in 'xz123'
========================
'abc' *'xyz'
'abc' +'xyz'
print('abc'*33)
------------------------
切片操作
s[i] 
s[i:j:k]
------------------------
'xyzxyzxyz'.count('xyz')
3
------------------------
'xyzxyzxyz'.count('a')
0
------------------------
'xyzxyzxyz'.isalnum()
True
------------------------
'xyzxyzxyz'.isalpha()
True
------------------------
','.join('abcdef')  #join是连接的意思
'a,b,c,d,e,f'
------------------------
"abcd".split(',')
['a', 'b', 'c', 'd']
-
'xyz'.startswith('x')
True
------------------------
print(int(123.456))
123  #取整不会是四舍五入，直接取整  123.456
------------------------
使用type()函数可以查看变量的类型
------------------------
python 强类型编程语言
------------------------
abc = 123
prnt(type(abc))
<class 'int'>
------------------------
python 必须是显示改变类型，不会因为算力的改变而改变
------------------------
字符串--- 统计，语义分析
数字----计算
------------------------
字符串是比较第一个字符
‘456’ > '1234'
True
------------------------
num1 = input('num1:')
num2 = input('num2:')
sum = eval(num1) + eval(num2)   #eval()函数用来执行一个字符串表达式，并返回表达式的值  sum = eval(f'{num1} + {num2}')  \
    f'{}' 是Python中的一种格式化字符串的方式
print(sum)

------------------------
#计算器
num1 = input('num1:')
num2 = input('num2:')
op = input('请输入运算符号’）
sum = eva(f'{num1} {op} {num2}')
print(sum)
------------------------

           






   


            
        

