#!/usr/bin/python
"""
Given a friend list of youngsters as input.
Find out the at-risk youth from the list.
For complete problem definition ref MR practice questions doc
"""

def mapper(key, value):
    person, friend_status = value.split("->")
    friend, is_criminal = friend_status.split(",")
    yield friend, is_criminal
    yield person, "map:" + friend_status

def reducer(key, values):
    total_records = 0
    criminal_count = 0
    self_criminal = 0
    for record in values:
        if record.startswith("map"):
            record = record.split(":")[1]
            person, is_criminal = record.split(",")
            if is_criminal == 'yes':
                criminal_count += 1
            total_records += 1
        else:
            if record == 'yes':
                self_criminal = 1

    if not self_criminal:
        if float(criminal_count)/total_records >= 0.5:
            yield key,1

if __name__ == '__main__':
    import dumbo
    dumbo.run(mapper, reducer)
