import re
# use this to remove duplicate character from text preserving the order.
# Example: remove_duplicate_char('testacoba') -> tesacob 
def remove_duplicate_char(text):
    return "".join(dict.fromkeys(text))

# use this to remove character from text.
# Example: remove_char('test', 't') -> es 
def remove_char(text, char):
    return text.replace(char, '')

# sanitize will remove space, number, and puctuation from given text
def sanitize(text):
    return re.sub('[^A-Za-z]+', '', text)

# use this to replace a character with another character.
# Example: replace_char('test', 't', 'b') -> besb 
def replace_char(text, old_char, new_char):
    return text.replace(old_char, new_char)

# return order of given character in alphabetical rank, start from 0
# Example: char_to_order('a') -> 0, char_to_order('k') -> 10
def char_to_order(char):
    return ord(char.lower()) - ord('a')

# return lowercase character of given order in alphabetical rank, start from 0
# Example: order_to_char('0') -> a, order_to_char('10') -> k, order_to_char('26') -> a
def order_to_char(order):
    while order >= 26:
        order -= 26
    
    while order < 0:
        order += 26

    return chr(order + ord('a'))    

# create square matrix with given length from given array. 
# Matrix will be filled with priority from left to right then top to bottom.
def create_square(arr, length):
    rows, cols = (length, length) 
    square = [] 
    idx = 0
    for i in range(cols): 
        col = [] 
        for j in range(rows): 
            col.append(arr[idx])
            idx += 1 
        square.append(col)
    return square

# X that satisfy aX = 1 mod m
def mod_inverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

