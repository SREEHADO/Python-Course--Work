'''s='python programming'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.casefold())

s.center(100, " ")
print(s.center(100, "+"))

s.center(100, " ")
print(s.center(50, "%"))

print(s.ljust(100, '*'))

print(s.rjust(59, '-'))

s='300'
print(s.zfill(9))

s='xyz'
print(s.zfill(0))

s='full stack python programming power'
print(s.find('o'))
print(s.rfind('p'))
print(s.index('p'))
print(s.rindex('p'))
print(s.count('g'))

s='Dhanush Sree harsha Abhinov'
print(s.replace('h','*' ))

s='Dhanush Sree Harsha Abhinov'
print(s.replace('rs','^' ))

s='Dhanush Sree Harsha Abhinov'
print(s.replace('a','*' ))

s="python programming"
print(len(s))

print(chr(128578))

print(chr(158578))

print(chr(98578))

print(chr(128520))

print(sorted(s))

print(sorted(s, reverse=True))

s='python programming'
print(s.split())

s='python programming'
print(s.split('r'))

s='artificial intelligence'
print(s.split())

s='artificial intelligence is good and also bad technology'
print(s.split('l'))

s='artificial intelligence is good and also bad technology'
print(s.split('i', 4))

print(s.split())
s='sreeharshasingsverygood'
print(s.splitlines())

print(s.split())
s='sree harsha sings very good'
print(s.rsplit(':'))

print(s.split())
s='sree harsha sings very good'
print(s.partition('*'))

print(s.split())
s='sree harsha sings very good'
print(s.rpartition('.'))

s=['sree'  'harsha'  'sings'  'very'  'good']
print(' '.join(s))

s='  perplexity    ai    bot '
print(s.strip(''))

s='        perplexity    ai    bot '
print(s.lstrip(''))

s=' perplexity    ai    bot     '
print(s.rstrip())

text= 'hello,😈'
print(text.encode())

# Original text
text = 'hello,😈'

# Encode the string into bytes (default UTF-8)
encoded_bytes = text.encode()  # same as text.encode('utf-8')
print("Encoded bytes:", encoded_bytes)

# Decode the bytes back into a string
try:
    decoded_text = encoded_bytes.decode('utf-8')  # specify encoding explicitly
    print("Decoded text:", decoded_text)
except UnicodeDecodeError as e:
    print("Decoding failed:", e)

h='java developer'
print(h.isupper())

h='SAP-ABAP'
print(h.islower())

h='sreeharsha'
print(h.isalpha())

h='789'
print(h.isalnum())

h=''
print(h.isstartswith())

h=''
print(h.isendswith())'''