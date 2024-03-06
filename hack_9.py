"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""


def fn_hack_9():
    result = [1, 2, 3]
    i = 0
    x = 1
    while i < 3:
        result.insert(x, "@")
        i += 1
        x += 2
    return result
