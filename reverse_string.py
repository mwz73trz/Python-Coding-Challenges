def reverse_string(str):
    words = str.split(" ")
    print(words)
    reverse_string = " ".join(reversed(words))
    return reverse_string

print(reverse_string("I love Python"))