To solve this problem, we need to create a subroutine that detects the start-of-packet marker in a data stream. The marker is a sequence of four characters that are all different.

We can do this by keeping track of the last four characters received in the data stream, and checking if they are all different. If they are, we have found a start-of-packet marker and can return the number of characters processed so far.

Here is one possible implementation of this subroutine in Python:

```
def find_start_of_packet(data):
  last_four = []
  for i in range(len(data)):
    last_four.append(data[i])
    if len(last_four) > 4:
      last_four.pop(0)
    if len(set(last_four)) == 4:
      return i + 1
  return -1
```

This subroutine takes a data stream as input, and returns the number of characters processed before the first start-of-packet marker is found. If no marker is found, it returns -1.

To solve part 1 of the problem, we can use this subroutine to find the first start-of-packet marker in the given data stream. For example, for the data stream mjqjpqmgbljsphdztnvjfqwrcgsmlb, the subroutine would return 7, because the first start-of-packet marker is complete after the seventh character is processed.

To solve part 2 of the problem, we just need to modify the subroutine to look for a start-of-message marker instead of a start-of-packet marker. The start-of-message marker is the same as the start-of-packet marker, but it consists of 14 characters instead of 4. We can do this by changing the length of the last_four list and the value of the len(set(last_four)) check in the subroutine.

Here is the modified subroutine that solves part 2 of the problem:

```
def find_start_of_message(data):
  last_fourteen = []
  for i in range(len(data)):
    last_fourteen.append(data[i])
    if len(last_fourteen) > 14:
      last_fourteen.pop(0)
    if len(set(last_fourteen)) == 14:
      return i + 1
  return -1

Using this subroutine, we can find the first start-of-message marker in the given data stream. For example, for the data stream mjqjpqmgbljsphdztnvjfqwrcgsmlb, the subroutine would return 19, because the first start-of-message marker is complete after the 19th character is processed.



Try again
