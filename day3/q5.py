# Loop over a dict and print the value and key in the format value belongs to key.

d={"name":"abc", "age":18, "country":"India"}

for key, value in d.items():
    print(value , " belongs to ", key)