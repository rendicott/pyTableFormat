# pyTableFormat

Helper utility classes for taking existing Python class objects and easily displaying them
in table and csv format for debugging and export purposes.

## Usage

Take one of your existing objects and inherit TableFormat

```python
from pyTableFormat import TableFormat, Table_Formattable_Object

class MyPeopleObject(Table_Formattable_Object):
    def __init__(self):
        self.name = 'bob'
        self.gender = 'm'
        self.age = '15'

# create some objects
mypeoples = []
for i in range(5):
    m = MyPeopleObject()
    m.name = 'person-' + str(i)
    m.gender = 'm'
    m.age = str(int(m.age) + i)
    mypeoples.append(m)

# use the dumpself_tableformat_header method to print a header based on object property names
print(mypeoples[1].dumpself_tableformat_header())
# now loop through the list anc call the dumpself_tableformat method.
for person in mypeoples:
    print(person.dumpself_tableformat())

```

### Fixing Column Widths

If you run the above sample you'll see that this works but the name column is truncated.

```
C:\source\rendicott-github\pyTableFormat>python sample.py
age  gender  name
15   m       pers
16   m       pers
17   m       pers
18   m       pers
19   m       pers
```

This is because by default the TableFormat helper class will just take the column width from the
length of the property name string. This can be adjusted however by overriding the inherited
dict_extend_values property like so:

```python
class MyPeopleObject(Table_Formattable_Object):
    def __init__(self):
        self.name = 'bob'
        self.gender = 'm'
        self.age = '15'
        self.dict_extend_values = {'name': 15}

```

Now when you run it the column widths are better. 

```
C:\source\rendicott-github\pyTableFormat>python sample.py
age  gender  name
15   m       person-0
16   m       person-1
17   m       person-2
18   m       person-3
19   m       person-4
```

### Filtering Properties from Table Output
The dump_ignore_attrs property is pretty straighforward. If you want to ignore certain properties 
just add them to the list like so

```python
class MyPeopleObject(Table_Formattable_Object):
    def __init__(self):
        self.name = 'bob'
        self.gender = 'm'
        self.age = '15'
        self.dict_extend_values = {'name': 15}
        self.dump_ignore_attrs = ['gender']
```

Now when you run it gender won't show up in the table 

```
C:\source\rendicott-github\pyTableFormat>python sample.py
age  name
15   person-0
16   person-1
17   person-2
18   person-3
19   person-4
```

### Dumping to CSV

Dumping to csv is similar and straighforward. It simply uses different methods.

```python
# now dump some csv to screen (or file)
print(mypeoples[1].dumpself_csv_header())
# now loop through the list anc call the dumpself_csv method.
for person in mypeoples:
    print(person.dumpself_csv())
```

Output looks like this:
```
age,gender,name,

"15","m","person-0",

"16","m","person-1",

"17","m","person-2",

"18","m","person-3",

"19","m","person-4",
```

## License
MIT