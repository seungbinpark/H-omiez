#!C:\Users\박승빈\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print()
