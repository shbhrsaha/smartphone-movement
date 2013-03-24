#!/usr/bin/env python

import cgi

print "Content-Type: text/html"
print
print 'Hello World'

form = cgi.FieldStorage()

# prints alpha, beta, gamma to a file
output = ""
output += form["ax"].value + "\n"
output += form["ay"].value + "\n"
output += form["az"].value + "\n"
output += form["ai"].value + "\n"
output += form["alpha"].value + "\n"
output += form["beta"].value + "\n"
output += form["gamma"].value + "\n"

with open("livedata.txt", "w") as text_file:
    text_file.write(output)