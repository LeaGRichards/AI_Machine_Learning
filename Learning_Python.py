########  Learning Python ########

# The article called at the end of a script will be shown (nothing before)

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
  # for i in range(10):
  # A range : starts from 0 and end 1 number before, in this case 0 to 9
  # for is the function for forloops
  # give the name of something, can be a letter or a word (j or monkey)
  # 

  for j in range(4):
    print(i, j)

## Tabulation
  # tab means the code is about the top forloop; to explain...; enumerate function returns a tupple that you can unfold

