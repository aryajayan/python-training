# rewrite yesterday's programs to use f-strings wherever applicable

d={"name": "python", "ext": "py", "creator": "guido"}

for key, value in d.items():
    print(f"{key} {value}") 

# --output--
# name python
# ext py
# creator guido


d={"name":"abc", "age":18, "country":"India"}

for key, value in d.items():
    print(f"{value} belongs to {key}")


# --output--
# abc belongs to name
# 18 belongs to age
# India belongs to country