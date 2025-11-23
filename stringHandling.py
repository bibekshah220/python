# string handling

a= "hello, world"

print(a)

print(len(a))      # print the length of strings, returns no of characters in string
print (a[1])      # returns the character of given index no.

print(a[2:5])  # returns the substring with  start index no and end index no
print (a.split(","))     #seperates the string with given delimeter

b= "As per survey its 62 percentage battery with live instructor"
print (b.split(" "))

c = "  hello  "
print(c.strip())  # remove perfix and postfix whitespaces

print(c.replace("h","y"))    #replaces the old char with new char







