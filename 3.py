print("Create Dict")
agencies = {
    "CBI": "Central Bureau of Investigation",
    "FBI": "Federal Bureau of Investigation",
    "NIA": "National Investigation Agency",
    "SSB": "Service Selection Board",
    "WPA": "Works Progress Administration"
}
print(agencies)
print("**************************************************")
print("Type of Variable")
print(type(agencies))
print("**************************************************")
print("Add the map of acronym BSE 'Bombay Stock Exchange':")
agencies["BSE"] = 'Bombay Stock Exchange'
print(agencies)
print("**************************************************")
print("Change the value of the key SSB to 'Social Security Administration':")
print("Using update() method")
agencies.update({"SSB": "Social Security Administration"})
print(agencies)
print("**************************************************")
print("Remove the (key value) pairs with keys CBI and WPA:")
print("Using del keyword and giving the key as index")
del agencies["CBI"]
print("Dictionary after del: ", agencies)
print("****************************************************")
print("Using pop() method")
agencies.pop("WPA")
print("Dictionary after pop: ", agencies)
