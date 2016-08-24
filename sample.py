from pyTableFormat import TableFormat, Table_Formattable_Object

class MyPeopleObject(Table_Formattable_Object):
    def __init__(self):
        self.name = 'bob'
        self.gender = 'm'
        self.age = '15'
        self.dict_extend_values = {'name': 15}
        self.dump_ignore_attrs = ['gender']

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


# now dump some csv to screen (or file)
print(mypeoples[1].dumpself_csv_header())
# now loop through the list anc call the dumpself_csv method.
for person in mypeoples:
    print(person.dumpself_csv())