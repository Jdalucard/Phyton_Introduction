def phrase(name, lastname, adjective="tonto"):
    return f"{name} {lastname} es muy {adjective}"


phrase_result = phrase("Juan", "Scott", adjective="Intelligent")
print(phrase_result)
