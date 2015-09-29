# Oulipo
Fun with maths and letters

## Eodermdrome
http://oulipo.net/fr/contraintes/eodermdrome

Usage : python3 eodermdrome.py [dictfile]

Prints all eodermdrome which are present in the dict file.

The dictfile must be formatted with one word per line, ASCII encoding (python doesn't like accent too much).

At the time of writing the script is able to print out eodermdrome made of two words of respectively 5 and 6 letters.

To reduce the global set of combinations I used a reduced wordlist containing only words of 5 or 6 letters.

This list was obtained using this command on a linux system :

egrep -e "^[a-z]{5,6}$" fulllist > list5or6

then using the list5or6 file as dictfile for the python script.

Current result : found 729 results out of a list of 22533 words of 5 or 6 letters

Special thanks to ABO le tchèque for the design of the main algorithm!
