class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True

    elif p1 == "{" and p2 == "}":
        return True

    elif p1 == "[" and p2 == "]":
        return True

    else:
        return False


def is_paren_balanced(paren_str):
    s = Stack() 
    is_balanced = True 
    index = 0 
    paren_str = paren_str.replace(" ", "") 


    while index < len(paren_str) and is_balanced:
        paren = paren_str[index]       
        if paren in "({[":
            s.push(paren)

        elif paren in ")}]":
            if s.isEmpty():
                is_balanced = False

            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False

        index += 1

    if s.isEmpty() and is_balanced:
        print("Balanced")  

    else:
        print("Unbalanced")

          

