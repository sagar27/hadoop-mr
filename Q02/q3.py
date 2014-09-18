#!/usr/bin/python
"""
Select IncomeLevel, Count(Name) from IncomeTable group by IncomeLevel;
"""

def mapper(key,value):
    name,age,sex,occupation,incomelevel = value.split(",")
    yield incomelevel,1

def reducer(key,values):
    yield key,sum(values)

if __name__ == '__main__':
    import dumbo
    dumbo.run(mapper,reducer)
