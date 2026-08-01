# 1
# python --version

#2
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3//4)
print(3**4)

#3
print("Kush")
print("Kai")
print("India")
print("Yes")

#4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['A', 'B', 'C']))
print(type("Kush"))
print(type("India"))

# ex Lvl 3
print(5)
print(5.5)
print(5+5j)

print("Kush") # string
print(True)
print(False)

print(["Apple", "Mango", "Banana", "Strawberry"]) # list
print({"Kush", "Mango", "Apple"}) # tuple
print((1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9)) # set
print({
    'First': 1,
    "Second": 2,
    "Third": 3,
    "Forth": 4,
    "Five": 5,
})


# Euclidean distance of - (2, 3) and (10, 8)

#horizontal diff
diff = 2 - 3
print(diff)

#vertical diff
vdiff = 10 - 8
print(vdiff)

# square both
diffSqr = diff * diff
vdiffSqr = vdiff * vdiff

# add squares
newSqr = diffSqr + vdiffSqr

# take square root - exponentiation with 0.5
res = newSqr ** 0.5
print(res)