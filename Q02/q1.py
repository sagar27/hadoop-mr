#!/usr/bin/python
"""
select * from incomeTable where sex='Male';
"""

def mapper(key,value):
    name,age,sex,occupation,incomelevel = value.split(",")
    key = "-".join([name,age,sex,occupation,incomelevel])
    if sex == 'Male':
        yield key,sex

if __name__ == '__main__':
    import dumbo
    dumbo.run(mapper)
