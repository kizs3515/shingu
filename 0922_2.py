import urllib
file=urllib.urlopen('http://www.korea.ac.kr')
htmlcontents = file.read()
print htmlcontents
