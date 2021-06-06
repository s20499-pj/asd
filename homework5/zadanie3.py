"""
Mając do dyspozycji funkcje:
• głowa(A) - dla tablicy / łańcucha A zwraca pierwszy element
• ogon(A) - dla tablicy / łańcucha A zwraca taką samą tablicę bez pierwszego elementu
• jestPusta(A) - dla tablicy / łańcucha A zwraca informację o tym czy tablica/ łancuch
jest pusty
napisz w rekurencyjne funkcje, które (każda za 3 pkt)(UWAGA: nie można używać pętli.):
• wypiszą na ekranie część wspólną dwóch posortowanych tablic
• wypiszą na ekranie rewers słowa
"""

ar= [1,2,3,4,5,6,8,17,20]
arra = [1,2,5,7,8,19,20]
string = "ala ma kota"

def head(a):
    return a[0]

def tail(a):
    return a[1::]

def isEmpty(a):
    if a: return False
    else: return True

def commonPart(a,b):
    if not (isEmpty(a) or isEmpty(b)):
        if head(a) == head(b):
            print(head(a), end = ' ')
            commonPart(tail(a), tail(b))
        elif head(a) > head(b):
            commonPart(a, tail(b))
        else:
            commonPart(tail(a), b)
            
"""
# bez rekursji
def reverse(a):
    print(a[::-1])
"""

def reverse(s):
    if not isEmpty(s):
        reverse(tail(s))
        print(head(s), end = '')



commonPart(ar, arra)
print("\n"+ string)
reverse(string)
print()
