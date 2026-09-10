def find_dup_str(s,n):
    
    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        for j in range(i + n, len(s) - n + 1):
            if s[j:j+n] == sub:
                return sub
    return ""

s= input("Enter a string: ")
n= int(input("Enter the lenght wanted: "))
print(find_dup_str(s,n))

def find_max_dup(s):
    for n in range(len(s)//2,0,-1):
        sub = find_dup_str(s,n)
        if sub != "":
           return sub
    return ""

s2= input("Enter a string: ")
print(find_max_dup(s2))
