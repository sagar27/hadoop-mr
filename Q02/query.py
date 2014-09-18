#!/usr/bin/python
"""
Q1, Q2 and Q3 combined.
Refer MR practice questions doc
"""
def mapper(key, value):
   name,age,sex,occupation,incomelevel = value.split(",")
   record1 = "-".join([name,age,sex,occupation,incomelevel])
   record2 = "-".join([name,occupation])
   if sex == 'Male':
      yield ['q1',[record1, sex]], 1
   yield ['q2',record2], 1
   yield ['q3',incomelevel],1

def reducer(key, values):
   q_type, record = key
   if q_type == 'q3':
      yield record,sum(values)
   else:
      yield record, 1

if __name__ == '__main__':
   import dumbo
   dumbo.run(mapper, reducer)
