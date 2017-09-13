import string
s = "string. With. Punctuation?" # Sample string
out = s.translate(None, string.punctuation)
print(out)
