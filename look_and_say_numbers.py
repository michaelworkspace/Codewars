"""
There exists a sequence of numbers that follows the pattern

          1
         11
         21
        1211
       111221
       312211
      13112221
     1113213211
          .
          .
          .
Starting with "1" the following lines are produced by "saying what you see", so that line two is "one one", line three is "two one(s)", line four is "one two one one".

Write a function that given a starting value as a string, returns the appropriate sequence as a list. The starting value can have any number of digits. The termination condition is a defined by the maximum number of iterations, also supplied as an argument.
"""

def look_and_say(data='1', maxlen=5):
    prev = data[0]
    count = 1
    res = ''
    
    for i in range(1, len(data)):
        if prev != data[i]:
            res += str(count) + prev
            prev = data[i]
            count = 1
        else:
            count += 1
    res += str(count) + prev
    if maxlen == 1:
        return [res]
        
    return [res] + look_and_say(res, maxlen-1)
