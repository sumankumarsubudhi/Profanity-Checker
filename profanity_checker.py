import urllib

def file_read():
    with open('quotes.txt') as file:
        file_text = file.read()
        profanity_checker(file_text)

def profanity_checker(some_text):
    website = urllib.urlopen('http://www.wdylike.appspot.com/?q='+some_text)
    profanity_value = website.read()
    website.close()
    if "true" in profanity_value:
        print("Profanity Alert!!")
    elif "false" in profanity_value:
        print("Congrats!! The file don't contain any curse words.")
    else:
        print('There was some problem in loading the file.')

file_read()
