'''
Python list
'''

Books=["java","anaconda","FLASK","Codata"]
number = len(Books)
print("Total length of this boooks is:",number)

Books.append("GRE")
print(Books)
Books.insert(2,"LOLO")
print(Books)
Books.pop()
print(Books)
Books.remove("FLASK")
print(Books)
Books.reverse()
print(Books)