#a string that displays four raw vars aka the true form of whatevers
#passed into it
formatter = "%r %r %r %r"

# prints 1 2 3 4
print formatter % (1, 2, 3, 4)
# prints one two three four
print formatter % ("one", "two", "three", "four")
#prints True False False True
print formatter % (True, False, False, True)
#prints the raw value of the formatter four times oof
print formatter % (formatter, formatter, formatter, formatter)
#prints a haiku with multiple lines that shows up as a single line
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
