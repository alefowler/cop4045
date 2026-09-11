#pythagorean triplets

def find_pythagorean(n):
    triples = []
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(b, n+1):
                if a**2 + b**2 == c**2:
                    triples.append((a, b, c))

    return triples 
n=int(input("Enter a number: "))
print(find_pythagorean(n))