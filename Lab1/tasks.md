 ### Problem
Given two points represented as x1,y1,x2,y2 .
Return the (float) distance between them considering the following
distance equation.
Hint
math.sqrt() could be a useful function.
 ### Problem 2
Given a list of numbers, create a function that returns a list where all similar
elements have been reduced to a single element.
So [1, 2, 2, 3, 2] returns [1, 2, 3].
 ### Problem 3
Consider dividing a string into two halves.
Case 1:
The length is even, the front and back halves are the same length.
Case 2:
The length is odd, we'll say that the extra char goes in the front half.
e.g. 'abcde', the front half is 'abc', the back half 'de'.
Given 2 strings, a and b, return a string of the form :
(a-front + b-front) + (a-back + b-back)
 ### Problem 4
The program takes a command line argument. This argument is the name of
a text file. The program reads all the text, split them and calculate the 20
Most used words in the file and then write them to a file called
“popular_words.txt”.
Implementation hint:
my_str.split() #returns a List of my_str content by default separated by
space.
We can change the delimiter by passing it to split method
Example:
my_str.split(‘,’) #split by comma. ### Problem 5
The program takes a string and remove the vowels character from it then
print its new version
Implementation hint:
So, “Mobile” becomes “Mbl”
 ### Problem 6
The program takes a string and a character and returns a list with all the
locations that character was found in the given string.
Implementation hint:
String “Google” char ‘o’
Outoupt: [1,2]