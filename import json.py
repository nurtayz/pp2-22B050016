import json

with open("sample.json", "r") as file:
    data = json.load(file)

print("Interface status")
print("=" * 74)
print("DN", " " * 40, "Description ", " " * 8,  "speed", " " * 4, "MTU")
print("-" * 42, "-" * 20, " ", "-" * 7, "\t", "-" * 4)
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t","\t", " " * 16, imdata[i][j]["speed"] ,"\t" , imdata[i][j]["mtu"])