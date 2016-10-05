Susannah Go
CSCI 8920
Week 6 Problem Set

1. The file is problem6_1.py. Input files must be hard-coded (lines 21-22). This is similar code to the week 5's
assignment, with the exception of a random prefix and then adjusting for this during decryption. My plan
had originally been to calculate the prefix length based on the offset, (how many dummy bytes I have to give the oracle
before I see repeated blocks), chop this many bytes off the front of the output string, and then
use the program from last week. However my program is doing a weird thing where it gives different offsets for different
runs using the same prefix lengths. I'm not sure why this is happening, but I was still able to complete the assignment
with a not-so-pretty work around.

2. The file is problem6_2.py. There are two ways that a string can fail to have valid PKCS7 padding. First, the string
may not have the correct number of repeated bytes (e.g. it only has 2 copies of \x03). The second way is if the string
still has unprintable characters after being stripped according to PKCS7 rules. In doing this problem I realized that
my PKCS7 chopping function from week 5 is incorrect for any padding with more than one byte, so hopefully your test
cases didn't pick up on that!
