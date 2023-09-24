from random import randint
randint(1,6)

import random
random.randint(1,6)

def foo() -> None:
    """print the result of six sided dice until a six is rolled 
    """
    while roll != 6:
    # roll a dice 
        roll = randint (1,6)
        
        #print its value
        print(roll)
        
    #check if it is six, and exit if it is 
    if roll == 6:  # comparison operation vs assignment operation#
        return 
        
        
        
        
        def foo() -> None:
    """print the result of six sided dice until a six is rolled 
    """
   
        roll = randint(1,6)
        #print its value
        print(roll)
        
        
         while roll != 6:
    # roll a dice 
            roll = randint (1,6)
            print(roll)
        return  
    ---------------------------------------------
    type("hello world")
    <class 'str'>
    
--------------------------------------------
    hello world 
    syntaxerror invalid SyntaxError
    ---------------------------------------------]
    
    hello
name error  
------------------------------------------------
type(" ")
<class 'str'>
------------------------------------
eg. "hello" + space + "world"
hello world 
----------------------------------------------------------------
3 * "Hello world!"
''
-------------------------------------------------------------------------------
"a" < "b"
True
-----------
ord("a"), ord("b") 
(97,98)
chr(97)
'a'
----
'Z' <'a'
=--------
"a","aa"
TRUE
-------
"b" > "aa"
--------
"aba">"ab"
-----------
"aZ" < "aa"
True
--------empty != space 
len('') != len(' ')
empty is less than anything
-----------------------
'b' > 'aa'
-----------------------
len('n')   1  
----------------------
print("hello\weorld")
hello
world
-------------------------------------
when it comes to tab
"hello\t world"
'hello\tworld'
----------------
print("hello\tworld")
hello world
----------------------
int("3.14")
ValueError
-------------
float("123.456")
123.456
-------------------
int(" \t \n \n 235 \t")
235
-----------------------
using string formatter 

x = 1
y = 'two'
z= f"x={x} y={y}"
print(z)
x=1 y=two
----------------
x=3
print(f"{x=}")
x+3
-----------------
len has distributive property
len(cs+"world") == len(cs) + len("world")
----------------
substring
"h" in "hellp world"
True
------------------
string is ordered 
cs = "hello world"
cs[0]
'h'
cs[1]
e
cs[2]
l
cs[len(cs)]
error
--------------------
cs = "hello world"
cs[-1]
'd'
cs[-2]
'l'
---------------------
string slicing
cs = "012345689"
cs[1:4]   #依然要从0开始数#
'123'  #stop at 4, so it not output 4#
cs[0:9]
'0123455678'
cs[0:]  #omit and the difault#
'0123456789'
-------------------------
cs = "0123456789"
cs[-1] == cs[len(cs)-1]
True
cs[3:-1]
'345678'
cs[:-1]  #omit left-endpoint default to 0 
'012345678'
cs[:]
'0123456789'
cs[-7:]
'3456789'



-----------------------
cs = "0123456789"
cs[::2]      #increment by two from zero inclusive to ten exclusive中文从包括零到不包括十，以每次增加两个的方式递增
'02468'
cs[::-1]      # decrease by 1 from ten inclusive to zero exclusive
'9876543210'
cs[1:-3:3]       #1: This is the starting index of the slice. It starts from the second character (index 1) of the string.
                  #-3: This is the stopping index of the slice. It stops before the third-to-last character (index -3) of the string.
                 #3: This is the step or stride value. It means every third character will be included in the slice.
'14'
cs[0:10:-4]    #can't start at 0 and then backwards 
''
cs[10:0:-4]    #!!!重点 
'951'
cs[::-4]
'951'

----------------------------
immutability of strings 

cs = "hello"
cs[0] = 'H'
Error
------------------------------
strings as booleans 

bool('')
False

bool('Hello')
True

''<'A'
True    # !!!
bool(" ")
True 
------------------
strings are ordered sequences of characters
-----------------------
loop 
for loop


for <name. in <iterator>
<code>
eg.
for x in 'abcd':
    print(x)
a
b
c 
d 
    x
---------    ----------------------------
nesting for loops 

(digits, alphas) = ("012", "xy")
for d in digits:
    for a in alphas: #  loops resolves themselves from inside out 
        print(d+a)
        0x
        0y 
        1x
        1y
        2x
        2y
----------- --------------------
(digits, alphas) = ("012", "ab")
for d in digits:
    for a in alphas:
        pass     (python disallows empty for-loops)
    print(d+a)
    0b             # 这一行打印了当前数字 d 和当前字母 a 的连接。由于 a 始终为 "b"，而 d 是 "0"、"1" 或 "2"，结果为 "0b"、"1b" 和 "2b"。

    1b
    2b
    
        ------------
(digits, alphas) = ("012", "xy")
    for d in digits:
        for a in alphas: 
            pass
        print(d+a)
        2b        because of pass
-------------------------------------
accumulator 

acc = ""
for x in "abcd"
    acc = acc + x
    print(acc)
a
ab
abc 
abcd 
-------------------  
acc = ""
for x in "abcd"
    acc = x + acc 
    print(acc)
a 
ba 
cba 
dcba 
----------------
while loop = for 
eg. 
for x in xs:
is code-equivalent to 
k=o
while k < len(xs)
k+=1
----------------=====
###第二次


def remove(c:str, cs:str)->str:
    """
    precondition: len(c) == 1
    
    >> remove('b', 'bluey')
    """
    answer = ''
    for x in cs:
        if c == x:
            pass
        else:
            answer += x
            
    return answer
----------------------
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
      ===================================
      return = store 
        ===================================
def remove(c:str, cs:str)->str:
    ans = ''
    for x in cs:
        if c!=x:
          ans += x
          
    return ans
print(remove('b','berry'))
==============================
def cap(cs: str)->str:
    """
    >>> cap('hello')
    'Hello'
    """
    ans = ''
    for x in cs:
        if 'a' <= x <= 'z':
            ans += chr(ord(x)- ord('a') - ord('A'))
        else:
            ans += x
    return ans
--------------------------
tuple (immutable)
xs = (0,1,2,3)
ys = ('a','b','c','d')

concatenation 
xs+ys 
(0,1,2,3,'a','b','c','d')
-------------------------
roundbrace  ()  是一个 function default evaluation
(1) + (2)
3
(1) + (2,3)
type error
tyep((1,)) 注意有无comma 的区别  有就是tuple 没有就是int
-------------------------
两个tuple 相加
(1,) + (2,)
(1,2)
-------------------------
tuple in for loop 
for x in (1,2,3):
    print(x)    
-------------------------
tuple comparing 
(1,2,3) == (1,2,3)
True 
-------------------------
(1,2,3) < (1,2,4)
tuple 跟comparing strings 一样

-------------------------
（1,2,3） < (1,2)
False
-------------------------
(1,2) < (1,2,3)
True
(1,1,3)<(1,2,1)   stops at the second element and concludes
-------------------------
lists   mutable 
xs = [0,1,2,3]   xs means x's, which is plural 
type(xs)   
<class 'list'>

-------------------------
still list  
xs = [0,1,2,3]
xs[0]
1
-------------------------
cuz list is mutable 
xs[0] = 2 * xs[1]
2
-------------------------
xs = ['a',2, 'b', 3']
[1,2,3,4,5,6,7,8,9,10] <[2] point-wise comparison.
-------------------------
Menbership  
i in [1,2,3]
True
-------------------------
123 in [1,2,3]
False
-------------------------
[1] in [1,2,3]
false 
-------------------------
[1] in [[1[,2],3]]]]
True 
-------------------------
.append()  #add to the end of the li st
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
-------------------------
xs = [1,2,3]
xs = xs + [4]
function sorted 
xs = [6,4 2 1 3 5]
sorted(xs)
[1,2,3,4,5,6]
-------------------------
another way to sort
[6,4 2 1 3 5]
xs.sort()    object-oriented type of philosophy
xs
[1,2,3,4,5,6]
-------------------------
xs = [6,4 2 1 3 5]
xs.append(9)
xs
[6,4 2 1 3 5,9]
-------------------------
xs = [6,4 2 1 3 5]
xs.append([4,5])  put a list in the end 
xs 
[6,4 2 1 3 5,[4,5]]
-------------------------
Extend   用法
xs = [1,2,3]
xs.extend([4,5])
xs
[1,2,3,4,5]
code similar to  \ xs = xs + [4,5]
-------------------------
List Aliasiing 
xs = [1,2,3]
ys = xs # ys is a name which is getting the value that stored in xs 

ys[-1] = 9  # taking the value of  3 in xs and changing to 9 
ys = [1,2,9]
xs= [1,2,9]  # xs is also changed, multiple reference point to the same object could change
 
-------------------------
[' ' for _ in range(3)]
-------------------------
xs = [1,2,3]
ys = xs.copy()
ys[-1] = 9
ys = [1,2,9]
xs = [1,2,3]

-------------------------
passing list to function
def foo(ys):
    ys[0] = -100
    
    xs = [1,2,3]
    foo(xs)    #由于在 Python 中列表是可变对象，函数内的 ys 参数与 xs 引用同一个列表对象。    
    #在函数内部修改传递给函数的可变对象（如列表）会影响到原始对象，即使这些修改是在函数内部进行的。
    xs
    [-100,2,3]  # xs is changed because ys is changed
    
    -------------------------
 append to the list
 xs = [1,2,3]
 ys = xs 
 xs.append(4)
 ys
[1,2,3,4]
不要用xs = xs + 6
用xs.append
-------------------------
def count(xs:list[int],ys:list[int])->int:
    """
    count([1,2], [1,2,3])
    2
    """
    ans = 0
    
    for y in xs:
        if y in ys:
            ans += 1
    return ans
print(count([1,2],[1,2,3]))     #for 和return 在同一缩进，进行循环，return在for的内部，只进行一次循环。
另一中version  return sum(y in ys for y in xs)

--------------------------------
def foo(xs:list[int])-> list[int]:
    #筛选重复的数字
    ans = []
    for x in xs:
        if x not in xs:
            ans.append(x)
    return ans
-------------------------
练习  
def foo(xs:list[int])-> list[int]:
    #筛选重复的数字
    ans = []
    for x in xs:
        if x not in ans:
            ans.append(x)
    return ans
print(foo (xs = [1,2,2,3,3,4,5,6]))
-------------------------
slicing 
xs = [1,2,3,4,5,6,7,8,9,10]
xs[::3]  #increment by 3 from zero inclusive to ten exclusive
[1,4,7,10]
xs[7:2:-2]  #decrease by 2 from seven inclusive to two exclusive
[6,4,2]
xs[3:6]
[4,5,6]
-------------------------
rotate 

def rotate(xs:list[int],k:int)->list:
    '''
    rotate ([1,2,3,4,5],2)
    [3,4,5,6,1,2]
    '''
    a = xs[k:] + xs[:k]
]   return a
-------------------------
#给爷好好看  You start with the naught_pieces set: set([5, 2, 4]).
You sort the set, resulting in a sorted list: [2, 4, 5].
You convert each integer element of the sorted list into a string: '2', '4', '5'.
The join() method then combines these strings using the separator ", " to create a single string: '2, 4, 5'.
    
    -------------------------    
    用逗号连接起来的两个'2','3'最后print 会变成2 3
    #difference '+' 与 , 的区别
   #When you use the + operator to concatenate strings, they are combined without any automatic addition of spaces.
    # When you use a comma to separate different arguments within the print() function, a space is automatically added between those arguments in the output
    print("O has: " + ", ".join(["2", "3"]))  #join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    -------------------------
    默认情况下，print() 函数会在输出内容的末尾添加一个换行符，将输出移到下一行。通过使用 end=""，我们可以防止在每个元素之间添加换行符，从而保持在同一行输出。
-------------------------
rotate function 

rotate([1,2,3,4,5],100)
kp = k % len(xs)
return xs[kp:] + xs[:kp]
[3,4,5,1,2]
-------------------------
list(range(2,7,-1))
[]
list(range(7,2,-1))
[7,6,5,4,3] #从7开始，每次减1，直到2

-------------------------
if board[row][col] != '':
        old_piece = int(board[row][col]) #Named old_piece_size to existing piece on the board
        if pieces >= old_piece: #2 kinds. there is already existing same piece on the board
            print('Invalid_Size_MESSAGE')
            return None



    







































