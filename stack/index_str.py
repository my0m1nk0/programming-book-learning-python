def matches(opens, clos):
    opensText = "([{"
    closes = ")]}"

    return opensText.index(opens) == closes.index(clos)

opens_txt = "([{"
close = ")]}"
str_words = 'Hello World Hi AI'

res = matches("{","}")
print(res)
print(opens_txt.index('{'))
print(opens_txt.index('['))
print(opens_txt.index('('))

print(close.index(")"))
print(close.index("]"))
print(close.index("}"))

print(str_words.index("A"))
