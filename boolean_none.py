"""
Return Value from bool()

The bool() returns:

False if the value is omitted or false True if the value is true

The following values are considered false in Python:

None

False

Zero of any numeric type. For example, 0, 0.0, 0j

Empty sequence. For example, (), [], ''.

Empty mapping. For example, {}

objects of Classes which has bool() or len() method which returns 0 or False

All other values except these values are considered true.

"""



n = 3
while n:
    print(n)
    n -= 1