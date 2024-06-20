import pywhatkit as pw
text = '''Python has a simple syntax similar to the English language. Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. 
This means that prototyping can be very quick.'''

pw.text_to_handwriting(text, 'handwriting.png',[0,0,138])
print('Converted !!!')