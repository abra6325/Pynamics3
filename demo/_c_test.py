import cik_core

print(cik_core.CikObject)

x = cik_core.CikObject()

y = cik_core.CikObject()

print(x.parent)
print(x.children)

x.add_child(y)

print(x.children)