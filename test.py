def incascade(n):
    grow(n)
    print(n)
    shrink(n)

def grow(n):
    n = n // 10
    if 0 < n < 10:
        print(n)
    else:
        grow(n)
        print(n)

def shrink(n):
    n = n // 10
    if 0 < n < 10:
        print(n)
    else:
        print(n)
        shrink(n)

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    
class Kangaroo:
    def __init__(self):
        self.pouch_contents = []
        
    def pun_in_pouch(self,string):
        if string in self.pouch_contents:
            print('object already in pouch')
        else:
            self.pouch_contents.append(string)
    
    def __str__(self):
        if self.pouch_contents == []:
            return "The kangaroo's pouch is empty"
        else:
            return "The kangaroo's pouch contains: {0}".format(str(self.pouch_contents))
        
        

def fast_oerlap(s, t):
    
    """
    >>> fats_overlap([3, 4, 6, 7, 9, 10], [1, 3, 5, 7, 8])
    2
    """
    i, j, count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count

