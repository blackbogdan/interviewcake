def is_polyndrome(str):
    result = True
    for i in range(0, int(len(str)/2)):
        print str[i], str[len(str)-i-1]
        if str[i]!=str[len(str)-i-1]:
            result = False
            break
    return result
def is_palindrome(str):
    return str==str[::-1]
str = "poop"
print is_polyndrome(str)
print is_palindrome(str)



def is_palindrome(str):
    result = True
    for i in range((len(str)-1)//2):
        if str[i]!=str[len(str)-i-1]:
            result = False
            break
    return result

print "yoooooooooooooo", is_palindrome(str)