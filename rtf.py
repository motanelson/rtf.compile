import os
import zlib

def save_compile(filename, data):
    comp = zlib.compress(data, level=9)
    with open(filename, "wb") as f:
        f.write(comp)

def load_compile(filename):
    with open(filename, "rb") as f:
        comp = f.read()
    return zlib.decompress(comp)

print("\033c\033[47;31m")
print("Give me a data .rtf to compile?")
a = input().strip()

if not os.path.isfile(a):
    print("File not found.")
    exit()

c = os.path.splitext(a)[0] + ".rtfcx"

# Lê o bitmap em modo binário
with open(a, "rb") as f:
    data = f.read()

save_compile(c, data)

print("compile:", c)

# Teste
data2 = load_compile(c)

if data == data2:
    print("compile OK")
else:
    print("compile failed")