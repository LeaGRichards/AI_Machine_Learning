########  Learning Python ########

## Some basic principles
  # The article called at the end of a script will be shown (nothing before)
  # When running a segment of code, will assume ALL changes done in whole code even if the change has not ran itself

## Create a STRING -> can use both double and single quotation marks
  msg = 'hello'
  msg = "hello"

## Create a LIST
  # can be made of different types of variables
  # Use square brackets for list [ ]

  l = [2, 3.14, 'hello']
  l.append(42) # Adds 42 to the previous list
  l
    # Reports : [2, 3.14, 'hello', 42]

  # OR call the article with print()
  print(l)
    # Reports : [2, 3.14, 'hello', 42]

## Create a TUPPLE
  # Use double parenthesis ()
  # Only ONE type of variable
  # Cannot append new parts to an existing tupple, you have to create a new one

  t = tuple((3, 2, 1)) # this creates a tupple of the content of the inner parenthesis
    # Reports : (3, 2, 1)

  # OR (same) 
  t = tuple([3, 2, 1]) # this converts a list in [] into a tupple
    # Reports : (3, 2, 1)

  # OR (same)
  t = (1, 2, 3)
  t
    # Reports : (3, 2, 1)

## Create a DICTIONNARY
  # Basically a value defined by a key
  # like 1 define by the key as A and 2 defined by the key as B
  # Made with fancy brackets { } 
  
  d = {
    'name': 'Nico',
    'age': 32
  }
  d
    # Reports : {'name': 'Nico', 'age': 32}

## Create a FORLOOP
  # A range : starts from 0 and end 1 number before, 
    # Range(10) is from 0 to 9
  # for -> the function for forloops
  # then give the name of something, can be a letter or a word (ex : j or monkey)
  # 

  for j in range(4):
    print(j)
    # Reports : 
       # 0
       # 1
       # 2
       # 3

## TABULATION in forloops
  # tab means the code written is about the above forloop 
  # enumerate function returns a tupple that you can unfold
  # Will loop the first loop (i) for the values of the second loop (j)
  # Then create a table with the first loop (1) asociated with the second loop (j)

for i in range(4):
  for j in range(2):
    print(i, j)
    # Reports : 
      # 0 0
      # 0 1
      # 1 0
      # 1 1
      # 2 0
      # 2 1
      # 3 0
      # 3 1

## Forloop variation

for i, li in enumerate(l):
    print(i, li)
    # Reports : 
      # 0 2
      # 1 3.14
      # 2 hello
      # 3 42

## Create a list and associate each value to another value manually

l2 = [2, 3, 4] # List of 3
len(l2) # If number of variables is unknown then use len() function
  Reports : 3

a, b, c = l2 # associate a, b and c to the 3 values of the list l2
a
  Reports : 2

# Play witht the list
a, *_ = l2 
  # a is associated with 2;  3 and 4 are ignore (but technically encompassed in *_
  # * means the rest of the variables beyond
_
