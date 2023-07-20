users = {
    "id" : "1",
    "name" : "Leanne Garaham",
    "username" : "Bret",
    "email" : "Sincere@april.biz",
    "address" : {
        "street" : "Kulas light",
        "suite" : "Apt. 556",
        "city" : "Gwenborough",
        "zipcode" : "92998-3874",
        "geo" : {
            "lat" : "-37.3159",
            "lng" : "81.1496"
        }
    }
}
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print(users)
# mengetahui kelas dengan cara mem-print di bawah ini:
print(type(users))
# -MENGUBAH PYTHON DICTIONARY KE JSON-
print("\nUbah Dictionary ke JSON")
import json
result = json.dumps(users)
print(type(result))
print(result)

# -MENGUBAH JSON KE PYTHON DICTIONARY-

# MENULIS HASIL KE FILE
with open("result.json", "w") as file:
    json.dump(users, file)
