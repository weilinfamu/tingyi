#对于两个集合collection 之间的对比，可以用 any(piece <= existing_piece_value for piece in cross_pieces):
any(x <= y for x in 'collection' for y in 'collection')
#对于两个集合collection 之间的对比，可以用 all(piece <= existing_piece_value for piece in cross_pieces):
range 返回的是一个数字序列但是不是tuple，如果需要tuple，需要用tuple(range(1,10))
startswith 检查字符串是否以指定的子字符串开头
 f-string（格式化字符串），它是一种在字符串中插入变量值或表达式的方式
 
 enumerate() 是一个内置函数，在循环迭代时可以为每个元素提供索引（序号）以及对应的值