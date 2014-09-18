#!/usr/bin/python
"""
Calculates user median session length
"""
def mapper(key,value):
    user,session_length = value.split()
    yield user,int(session_length)

def reducer(key, values):
    length = 0
    session_lengths = []
    for value in values:
        session_lengths.append(value)
    length = len(session_lengths)
    median = 0
    session_lengths.sort()
    middle_length = length/2
    if length % 2:    #Odd number of values
        median = session_lengths[middle_length]
    else:
        median = float(session_lengths[middle_length-1] + session_lengths[middle_length])/2
    yield key,median

if __name__ == '__main__':
    import dumbo
    dumbo.run(mapper,reducer)
