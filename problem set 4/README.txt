Susannah Go
CSCI 8920
Week 4 Problem Set

1: The decryption part seems to be working fine. (After I emailed you about the weird character at the end of the
plaintext it occurred to me that it was probably padding, so I went back and chopped it off.) I implemented the
built-in CBC modes only to evaluate my output.

2: I never got my CBC encryption working properly, therefore my oracle is not working properly either. I'm pretty sure
the issue stems from how I'm implementing PKCS7 padding, but didn't have time to debug it. I used the built-in CBC
encryption mode to try and get more work completed on this part, so I think this may work for if the length of the
plaintext is a multiple of the block size. I ran out of time and didn't get the byte prepend/append functionality
working.

Question: ECB mode may go undetected even if the code is correct if no plaintext blocks are repeated. In this case no
blocks of ciphertext will be repeated either. Since this is our only method of identifying ECB mode, it will go
undetected.
