#!/usr/bin/python
"""
Given a friend list from a social networking website.Display a list of common friends.
A->B,C,D
B->A,C,D,E
C->A,B,D,E
D->A,B,C,E
E->B,C,D
"""

import sys
import copy
def mapper(key, value):
   person, friendlist = value.split("->")
   friends = friendlist.split(",")
   for friend in friends:
      friends_copy = copy.copy(friends)
      friends_copy.remove(friend)
      if person < friend:
         yield person+friend, set(friends_copy)
      else:
         yield friend+person, set(friends_copy)

def reducer(key, values):
   friendlist = []
   for friends in values:
       friendlist.append(friends)
   yield key, list(friendlist[0].intersection(friendlist[1]))

if __name__ == '__main__':
   import dumbo
   dumbo.run(mapper, reducer)
