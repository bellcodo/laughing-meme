# import the magic random picker
import random, urllib2

# list of things to pick from
url_for_list = "https://raw.githubusercontent.com/bellcodo/laughing-meme/master/typing_options.lst"
raw_typing_options = urllib2.urlopen(url_for_list)
list_of_options = raw_typing_options.read()
#print "DEBUG - raw typing options is %s, %s" % (raw_typing_options, list_of_options)
typing_options = ['abc','def', 'ghi']

# find a way to pick something
typing_choice = random.choice(typing_options)

# a way to tell the user what to do
print typing_choice
