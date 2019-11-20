
#import the library
import textwrap
"""
#Function which will have all the execution of code
#Setting the width with the paragraph
#Wrap() will return the paragraph in list with width
#for loop
#print the paragraph output as expected
"""
def paragraph_func(paragraph):

    paragraph_width = textwrap.TextWrapper(width=20)
    paragraph_string = paragraph_width.wrap(text=paragraph)
    count=0
    for element in paragraph_string:
        count+=1
        print('Array [{}] = "{}"'.format(count, element))

paragraph1 = "This is a sample text but a complicated problem to be solved," \
            "so we are adding more text to see that it actually works."

#excecuting the function
paragraph_func(paragraph1)

print("\n")

paragraph2 = "One of the main promises Apple is making with its new 16-inch MacBook Pro is that the keyboard " \
            "— after years of easily broken butterfly-switch mechanisms — is finally switching back to the more " \
            "reliable scissor-style switches it’s used in the past. And iFixit’s teardown of the new laptop confirms " \
            "that promise, with Apple using scissor switches that appear to be virtually identical the ones it uses in " \
            "its Magic Keyboards, first introduced in 2015."

paragraph_func(paragraph2)
