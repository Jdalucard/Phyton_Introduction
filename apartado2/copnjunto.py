conjunct = set(["lucas", "dalton", 10000000])
# combine
conjunct2 = frozenset(["not parent's", "sin parent's"] + list(conjunct))

conjunct3 = {conjunct2, "dato3"}

# result
result = conjunct3.issuperset(conjunct2)
result2 = conjunct3.isdisjoint(conjunct2)
print(result)
print(result2)
