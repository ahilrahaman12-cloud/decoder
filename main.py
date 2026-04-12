import base64
x = input("Enter to decode\n")
y = base64.b64decode(x)
z = y.decode('utf-8')
print(z)