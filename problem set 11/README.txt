Susannah Go
CSCI 8920
Week 11 Problem Set

#1: The file is problem11_1.py. Upon execution the program executes two tests: one generating a shared key for p = 101 and g = 53, and one generated a shared key for the NIST prime and g = 2. Interestingly, I started out by using math.pow for the exponents, and this was giving me inaccurate results for large values of p and g. The ** operator seems to work fine though. This file contains a function that uses number theory tricks for quick exponentiation. This function is used again in problems 2 and 3. 

#2: The file is problem11_2.py. I created a class for the Server, and upon execution the program performs a successful login. It can be shown that changing the values of either the username (line 79) or password (line 92) on the client side results in an unsuccessful attempt.

#3: The file is problem11_3.py. The weakness I exploited was that the server doesn't check that A != 0. If A = 0, then any login attempt with a valid username is successful regardless of the password. This attack could easily be prevented if the server checked that A != 0. More details about the changes I made to the program are in the comments for this file. Upon execution the program does a successful login with a fake password (given in line 22). This password can be changed to anything, and will still result in a successful login. I also provided commented code that would prevent this attack.
