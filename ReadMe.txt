@author William Wallace
@date 22/05/2020


EXPLANATION
Etude 7 - Poker Hands reformats, sorts in ascending order of value, and prints valid formats of text input in the form of poker hands,
if it is possible. If no answer is possible for the input, the terminal will print "Invalid: " and the invalid hand.

HOW TO RUN
To run Etude 7, open VSCode or a similar code editor and run by typing "python pokerHandsFinal.py" without quotation marks
while in the directory containing pokerHandsFinal.
To get the answer, the line of input must contain the valid cards separated by spaces, back-slashes, or hyphens. A card consists of a
number from 1 - 13 (inclusive) immediately followed by a letter to indicate suit (c, d, h, s, C, D, H, S). Cards 1, 10, 11, 12, and 13
may alternatively be represented by a letter (a, t, j, q, k, A, T, J, Q, K).

For parsing a txt file with multiple tests, again ensure there is one test case per line.
In a code editor, type "cat <text-filename-here> | python pokerHandsFinal.py" without quotation marks, and replacing the file in the pointy brackets. 

For more information, refer to the PDF outlining "Etude 7 - Poker Hands" in the current folder. 

TEST CASES:

Input:
11h/14c/3d/6s/9c
0h/14c/3d/6s/9c
-1h/14c/3d/6s/9c
1h/-14c/3d/6s/9c
4d-2s-7d-8c-10d-2h
3s 7d 1c 6h 5h
3s/7d/1c/6h/5h
3s  7d    1c   6h      5h
h/s/d/d/s
h
he
hel
hell
hello

 

4d/4s 1c 12d-13h
14/6/5/3/1
QS-Kh-5c-Jh-3h
2c 13S 2h Kd 10C
h/
3s-3d-3c-3d-3h
3s 4d 3c 3d 3h
7d/3s/1h/6h/10h
7d/as/1h/Kh/th
7d.as.1h.Kh.th

Output:
Invalid: 11h/14c/3d/6s/9c
Invalid: 0h/14c/3d/6s/9c
Invalid: -1h/14c/3d/6s/9c
Invalid: 1h/-14c/3d/6s/9c
Invalid: 4d-2s-7d-8c-10d-2h
3S 5H 6H 7D AC
3S 5H 6H 7D AC
Invalid: 3s  7d    1c   6h      5h
Invalid: h/s/d/d/s
Invalid: h
Invalid: he
Invalid: hel
Invalid: hell
Invalid: hello
Invalid:
Invalid:
Invalid:
Invalid: 4d/4s 1c 12d-13h
Invalid: 14/6/5/3/1
3H 5C JH QS KH
2C 2H TC KD KS
Invalid: h/
Invalid: 3s-3d-3c-3d-3h
3C 3D 3H 3S 4D
3S 6H 7D TH AH
7D TH KH AH AS
Invalid: 7d.as.1h.Kh.th