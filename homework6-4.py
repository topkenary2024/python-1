glossary = {
    'string': "A series of characters that can be printed as plain text.",
    'integer': "A non-decimal whole number.",
    'float': "A number with a decimal point.",
    'list': "A collection of items in a particular order.",
    'dictionary': "A collection of key-value pairs.",
    'loop': "A sequence of instructions that is repeated until a specific condition is met.",
    'function': "A block of code designed to perform a specific task.",
    'boolean': "A data type with two possible values: True or False.",
    'conditional statement': "An expression that evaluates to True or False and determines which block of code to execute.",
    'f-string': "A type of formatted string literal that allows you to embed expressions directly inside the string."
}

# Loop through the glossary and print each term and definition
for word, definition in glossary.items():
  print(f"\n{word.title()}: {definition}")
