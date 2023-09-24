1.__str__ is for class to string
2.Not Overriding is_blocking: The is_blocking method is not overridden in the Floor class because it seems that for Floor objects, you want them to be non-blocking, just like the base Tile class. In this case, there's no need to override it because the behavior is the same.
3.

4.Reusing Code: The reason for providing implementations of get_type and __str__ in both the base class and the subclass is to reuse code when the behavior is the same. If you want Floor objects to have a different string representation or type compared to other Tile objects, you override those methods. However, if the behavior is the same, you can choose to either override and reuse the base class implementation (as in is_blocking), or not override it if the behavior doesn't need to change.
5.
def get_type(self) -> str:
    return "Abstract Tile"	

def __str__(self) -> str:
   return self.get_type()
The get_type method returns the string "Abstract Tile". So, when you call the __str__ method on an instance of this class, it calls get_type() and returns "Abstract Tile" as the result. So, the return value of str(tile) (assuming tile is an instance of this class) would be "Abstract Tile".
6.The __repr__ method in Python is used to define a string representation of an object. It's intended to be an unambiguous representation of the object, and it's often used for debugging and development purposes. When you call the built-in repr() function on an object, it should return a string that, when passed to the Python interpreter, creates an object with the same state.
eval() is indeed primarily used for evaluating and executing Python expressions or code dynamically. It takes a string containing a Python expression or statement, parses it, and executes it within the current context. Here's a basic example of how eval() works:
pythonCopy code
x = 10
expression = "x * 2"
result = eval(expression)  # This will calculate 10 * 2print(result)  # Output: 20

10class Person: 
def __init__(self, name, age): 
self.name = name 
self.age = age
Person is a class.
self.name and self.age are attributes of the Person class.
self refers to the instance of the class. It's a convention in Python to name this parameter self, but you could technically name it something else (although it's not recommended). When you create an instance of the Person class, such as person1 = Person("Alice", 30), self inside the __init__ method refers to person1, and self.name and self.age are attributes specific to that instance.

13.In the context of the __repr__ method:
pythonCopy code
return f"Person('{self.name}', {self.age})"
Person is the name of the class.
self.name and self.age are attributes of an instance of the Person class, which are specific to each object created from the class.
You don't need to use {} around Person because Person is the name of the class, not an attribute of an instance. However, you do need {} around self.name and {self.age} because those are the attributes of the instance, and you want to include their values in the string representation.

14.=============
15. # Check if the character is alphabetic
     if char.isalpha():
16.The 
 If the key exists, it returns the associated value; otherwise, it returns a default value specified as the second argument to .get() (or None if no default is provided).

python
Copy code
my_dict = {'a': 1, 'b': 2}
value = my_dict.get('a', 0)  # Returns 1 (key 'a' exists)
value = my_dict.get('c', 0)  # Returns 0 (key 'c' does not exist)
17.  if char.isalpha():
18.message = message.lower()
19.
append: Adds an element to the end of a list.
python
Copy code
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

extend: Appends the elements of an iterable (e.g., another list) to the end of the current list.
python
Copy code
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
19
pop: Removes and returns the last element from the list (by default). You can specify an index to remove an element at that position.
python
Copy code
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop()  # Removes and returns the last element
print(popped_element)  # Output: 5
print(my_list)  # Output: [1, 2, 3, 4]

20.Parentheses ():

Function Calls: You use parentheses to call a function and pass arguments to it. Example: my_function(argument)

Method Calls: Parentheses are used to call methods on objects. Example: my_object.method()

Creating Tuples: Parentheses are used to create tuples. Example: my_tuple = (1, 2, 3)

Grouping Expressions: Parentheses are used to group expressions to control the order of operations. Example: (x + y) * z

Square Brackets []:

Lists: You use square brackets to create and access lists. Example: my_list = [1, 2, 3]

Indexing: To access elements in a list or other iterable, you use square brackets with an index. Example: my_list[0]

Slicing: Square brackets are used for slicing to extract a portion of a sequence. Example: my_list[1:3]

Dictionary Access: To access values in a dictionary, you use square brackets with the key. Example: my_dict['key']

List Comprehensions: When creating lists using comprehensions, square brackets are used. Example: [x for x in range(10)]

List Methods: Some list methods use square brackets, like append, extend, and pop.

Remember that the choice between parentheses and square brackets depends on the specific context and the data structure or operation you are working with.


21.In Python dictionaries, keys are typically stored as strings unless specified otherwise，when you access a dictionary using a key, it's treated as a string even if you didn't include quotes when you originally created the dictionary.
22.freqs.items(): This part of the expression is used to iterate through all the key-value pairs (items) in the freqs dictionary.
23.for letter, count in ...: This is a "destructuring assignment" feature in Python. It allows you to unpack the elements of each tuple in the iterable returned by freqs.items() into the variables letter and count.
24..value     It is often used when you want to work with the values of a dictionary separately from its keys.
25.freqs.items() returns a view object containing the key-value pairs as tuples. In this case, it would return something like [('A', 3), ('B', 2), ('C', 3), ('D', 1)].
26..values(): This method returns a view of all the values in the dictionary. It does not return keys or key-value pairs, only the values.
27.
28.Example:
29.
30.python
31.Copy code
32.my_dict = {'a': 1, 'b': 2, 'c': 3}
33.values = my_dict.values()
34.print(values)  # Output: dict_values([1, 2, 3])
35..items(): This method returns a view of all key-value pairs (tuples) in the dictionary. It provides both the keys and their corresponding values.
36.
37.Example:
38.
39.python
40.Copy code
41.my_dict = {'a': 1, 'b': 2, 'c': 3}
42.items = my_dict.items()
43.print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
44. [letter for letter, count in freqs.items() if count == max_count]   for letter, count  if count -- max_count return letter?  
45.ChatGPT
46.Yes, you're correct. This line of code:
47.
48.python
49.Copy code
50.[letter for letter, count in freqs.items() if count == max_count]
51.is a list comprehension that iterates over the items (key-value pairs) in the freqs dictionary. For each item, it unpacks the letter and count from the item and checks if count is equal to max_count. If the condition is met, it includes letter in the resulting list.
52.还有它这里为啥要用[]?  The square brackets [] in the list comprehension are used to create a new list.
53.mixed_list = [1, 'two', (3, 4), [5, 6]]
54.my_list = [1, 2, 'hello', 3, 'world']
55.max_count = max(freqs.values())
56.max_letters = [char for char, count in freqs.items() if count == max_count]    By default, Python's max() function returns only one maximum value, and if there are multiple elements with the same maximum value, it returns the first one encountered.
57.
58.In the example I provided, where max_count is assigned the result of max(freqs.values()), it would return 3, which is the first maximum value it finds. If there are multiple elements with the same maximum value, the max() function doesn't provide a straightforward way to get all of them directly. You would need to iterate through the data and collect the elements with the maximum value manually, as shown in the code snippet I provided earlier.
59.n = len(str(num)): 这一行代码用于确定输入数字 num 有多少位数，即它的长度。这是为了确定要将每个位数的数字提升到的幂次方 n
60.digit = temp % 10: 这一行代码用于提取 temp 的最后一位数字，并将其存储在变量 digit 中。temp % 10 的操作会返回 temp 的最后一位数字。
61.The // operator can be combined with = to create the //= operator, which is used for floor division with assignment.
62.
63.For example, if you have a variable x and you want to divide it by 2 using floor division and update the value of x with the result, you can use //= like this:
64.
65.python
66.Copy code
67.x = 7
68.x //= 2
69.After this code, x will be updated to 3 because 7 // 2 is 3, and x //= 2 assigns this result back to x.
70.
71.So, //= is a shorthand for performing floor division and updating the variable in place. It's a common way to modify variables when you want to perform an operation and store the result back in the same variable.It calculates the quotient (the result of the division) without considering any remainder.   It rounds the quotient down to the nearest integer if necessary. This means that if the result is not a whole number, it truncates the fractional part to obtain an integer.   4 rather than 4.0

72.digit = temp % 10: This line calculates the last digit of the current value of temp using the modulo operator (%). For example, if temp is 1234, then digit will be 4. It extracts the rightmost digit.

digit = temp % 10 extracts the last digit for the purpose of calculating the nth power of each digit and adding it to the sum.
temp //= 10 reduces the value of temp by one decimal place, effectively removing the last digit to move on to the next digit in the number.


73.temp //= 10: After extracting the rightmost digit, this line removes that digit from the current value of temp by performing floor division (//) by 10. For example, if temp was 1234, after this line, it becomes 123. This prepares temp for the next iteration of the loop, where the next rightmost digit will be extracted.
74.
75.So, these two lines work together to extract the digits of num one by one, from right to left, and process them in the loop to check if num is an Armstrong number.

76.a = 1
print(type(a))  # <class 'int'> -- 整型
​
b = 1.1
print(type(b))  # <class 'float'> -- 浮点型
​
c = True
print(type(c))  # <class 'bool'> -- 布尔型
​
d = '12345'
print(type(d))  # <class 'str'> -- 字符串
​
e = [10, 20, 30]
print(type(e))  # <class 'list'> -- 列表      [10,20,30]这种数list
​
f = (10, 20, 30)
print(type(f))  # <class 'tuple'> -- 元组   (10,20,30)  这种是元组/   元组的特点是一旦创建，它们的内容是不可变的，但可以包含可变类型的对象，例如列表。
​
h = {10, 20, 30}
print(type(h))  # <class 'set'> -- 集合   {} 集合
​
g = {'name': 'TOM', 'age': 20}   字典
print(type(g))  # <class 'dict'> -- 字典   /  字典允许您存储不同类型的值作为键的值。  ‘name’:’TOM’

77.\n 换行（line feed)
78.print('输出的内容', end="\n")  print 自带换行结束符（print has its own end-of-line character
79.Input（input("提示信息")    imput 接受的输入一般在变量里面
80.Input 会把用户输入的任何信息当string使用
81.Complex(real[,imag])   实部和虚部
82.
repr(x) 是 Python 中的一个内置函数，用于获取对象 x 的“官方”字符串表示形式。它返回一个字符串，通常可以传递给 eval() 函数，以重新创建原始对象。
repr 是 "representation" 的缩写，它表示对象的字符串表示形式，通常是可以直接在代码中使用以创建相同对象的形式。这与 str(x) 不同，后者是对象的用户友好字符串表示形式。
83. = =tuple(s)= =  将序列s转化成一个元组
84.chr(x) is a built-in function in Python that converts an integer x into the corresponding Unicode character. It returns a string representing that character.For example, chr(65) would return the string 'A' because Unicode code point 65 corresponds to the uppercase letter 'A'.
The purpose of this function is to convert an integer into the corresponding character, and it is the opposite operation to ord(), which converts a character into an integer.
85.Bin(x)把整数转换为2进制字符串
86.
复合赋值运算符   （+=  -=  /=(c = c/a)  //=  （ c = c //a 整除 divided evenly
87.C %= a   c = c % a   remainder assignment
88.**=  c **=a  c = c**a
89. If :
age = int(input('请输入您的年龄：'))
if age < 18:
    print(f'您的年龄是{age},童工一枚')
elif (age >= 18) and (age <= 60):
    print(f'您的年龄是{age},合法工龄')
elif age > 60:
print(f'您的年龄是{age},可以退休')
90.random.randint(a, b) 函数用于生成一个指定范围内的随机整数，包括 a 和 b
import random

# 生成一个1到10之间的随机整数
random_number = random.randint(1, 10)
#(1,10) 表示一个范围
print("随机整数:", random_number)                     
.random.choice(sequence): 从序列中随机选择一个元素。
.random.shuffle(sequence): 随机打乱序列中的元素顺序。

91.三元运算符（Ternary Operator），也被称为条件运算符，是一种用于在单行代码中根据条件选择不同值的编程构造。
模板：值1    if条件    else 值2
它通常以 condition ? value_if_true : value_if_false 的形式表示
x = 10
y = 20
max_value = x if x > y else y
print(max_value)  # 输出 20
 
92.While
i = 1
result = 0
while i <= 100:
    result += i  result 是不断积累的数字   循环值
    i += 1   i 是不断往复的数字
​
# 输出5050
print(result)


93.# 方法一：条件判断和2取余数为0则累加计算
i = 1
result = 0
while i <= 100:  循环值
    if i % 2 == 0:    
        result += i    积累值
    i += 1	
​
# 输出2550
print(result)
94.while True:
    print('媳妇儿，我错了')
    response = input('女朋友：还要刷今天晚饭的碗吗？（输入是或否）：')
    if response.lower() == '是':
        print('刷晚饭的碗')
    elif response.lower() == '否':
        break
    else:
        print('请输入是或否来回答女朋友的问题。')    当输入其他无关的话题时

掌握把input赋值给一个变量

95.i = 1 
while i <= 5:
 print('媳妇儿，我错了') i += 1 
print('媳妇儿原谅我了...')  没有indentation
96.i = 1 
while i <= 5: 
print('媳妇儿，我错了') 
i += 1
else: print('媳妇原谅我了...')

97.区别在于有没有 else 子句决定了循环结束后是否执行额外的代码。在第一个循环中，无论如何都会执行循环之外的语句，而在第二个循环中，只有当循环正常结束（不被 break 中断）时才会执行 else 子句。  你可以把带有 else 子句的循环看作是一种特殊情况的处理器。如果循环正常结束，它会执行特定的操作；如果循环被中断，那这个操作就被略过了。这样的设计可以用来处理需要在循环结束后执行一些操作的情况，而又不希望这些操作被 break 中断的情况

注意 如果是有else，break终止了之后，else下方缩进的代码就不会继续执行了。、
continue退出循环后，会执行else下方的缩进的代码
98.

String  我们一般使用’’创建字符串
一般 variables = ‘x’ 这种形式  （General variables = 'x' form）




a = 'hello world'
b = "abcdefg"
print(type(a))
print(type(b))
when using  <class,type>  一般会在type上面加上’’用以enclosed.

比如：<class 'str'>

99.The % operator in Python is used for string formatting. It allows you to create formatted strings by substituting values into a string template.

100.
%s is a placeholder for a string value.
%d is a placeholder for an integer value.
%f is a placeholder for a floating-point value.
% is used to format the string, followed by the values you want to substitute into the string.
name = 'Tom'
age = 30
print('My name is %s and I am %d years old' % (name, age))

The (name, age) part is used to provide the values that will be inserted into these placeholders in the specified order. It's enclosed in parentheses to create a tuple containing the values 'Tom' and 30. The % operator then takes this tuple and substitutes the values into the placeholders in the string.

101.The continue statement is used in Python to skip the rest of the current iteration of a loop and move on to the next iteration.   
for i in range(5):
    if i == 2:
        print("Skipping iteration 2")
        continue  # Skip the rest of this iteration and move to the next
    print("Iteration:", i)

print("Loop finished")
102.Break  
for i in range(5):
    if i == 3:
        print("Breaking at iteration 3")
        break  # Terminate the loop prematurely
    print("Iteration:", i)
else:
    print("Loop completed normally")

print("Loop finished")
In this example, the loop iterates from 0 to 4. When i is equal to 3, the break statement is encountered, which immediately terminates the loop.
103.
