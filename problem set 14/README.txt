Susannah Go
CSCI 8920
Week 14 Problem Set

File problem14a.py generates the table. The dimensions (number of chains, chain length, length of password) are hard-coded in line 64. The output is a file called rainbow_table.txt. The time it takes to generate the table is printed to the console.

File problem14b.py uses the rainbow table file to try and crack the password. The dimensions are hard-coded in lines 14-16 and must match those in problem14a.py (sorry! I couldn't think of a better way to do this). The program prints out all password candidates to the console, as well how long the program took to run.

I've included a rainbow table for you. The program should be able to find the password "182" using this table.

This assignment is incomplete. I am able to crack numeric passwords of length 3 using 400 chains of length 40,000. This happens fairly quickly (about 60s to generate the table, 9s to crack the password). However I was never able to generate a table large enough to even crack a password of length 4. The largest table I tried was 1000 chains of length 400,000 (25 min to generate the table, 6 min to unsuccessfully attempt to crack the password). I also only did this for MD5 hash and not the LM hash.

For your viewing pleasure, here are the stats for cracking "182" using 10 different rainbow tables of 400 chains, each with length 40,000. The first time is for table generation; the second time is for password cracking; then I indicate the results:

1. 56.18s; 07.99s; found "182" and "457"
2. 56.02s; 10.04s; found "457"
3. 60.15s; 10.03s; found "182"
4. 64.74s; 09.73s; found "182" and "457"
5. 56.24s; 10.28s; found "182"
6. 52.73s; 08.97s; no passwords found
7. 57.75s; 08.60s; found "182" and "457"
8. 55.37s; 09.02s; found "182"
9. 59.32s; 9.20s; no passwords found
10. 54.62s; 07.53s; found "182"

So this table size worked 70% of the time for password "182"
