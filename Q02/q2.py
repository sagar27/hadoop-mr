#!/usr/bin/python
"""
select name,occupation from incomeTable;
"""

def mapper(key,value):
    name,age,sex,occupation,incomelevel = value.split(",")
    key = "-".join([name,occupation])
    yield key,1

if __name__ == '__main__':
    import dumbo
    dumbo.run(mapper)
