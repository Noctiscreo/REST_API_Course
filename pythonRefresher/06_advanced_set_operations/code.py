# <start with this element>.difference(<remove this element>)

baseSet = {"Bob", "Rolf", "Anne"}
removeSet = {"Bob", "Anne"}

# '.difference' removes 'removeSet' elements from 'baseSet'.
remainder = baseSet.difference(removeSet)

print(remainder)

# reverse the above and end up with an empty set, because you're taking 'Bob' and 'Anne' (and 'Rolf,' which isn't there anyway) from 'Bob' and 'Anne,' leaving nothing:
remainder = removeSet.difference(baseSet)

print(remainder)

# .symmetric_difference returns EVERY value which does not feature in BOTH collections:

set1 = {1, 2, 3, 4, 5, "Sally"}
set2 = {1, 2, 3, 4, 5, "Bob"}

set3 = set1.symmetric_difference(set2)
# The above line returns the same as the below line, where '|' = .union:
set4 = set1.difference(set2) | set2.difference(set1)

print(set3)
print(set4)

# Combine two sets together with .union:
baseSet = {"Rolf"}
additionalSet = {"Bob", "Anne"}

# '.union' combines 'baseSet' elements with 'additionalSet' elements:
union = baseSet.union(additionalSet)

print(union)

# Which students study ART only?

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

artOnly = art.difference(science)

print(artOnly)

# Which students study SCIENCE only?

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

scienceOnly = science.difference(art)

print(scienceOnly)

# Which students study BOTH subjects? Use .intersection:

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

bothSubjects = art.intersection(science)

print(bothSubjects)
