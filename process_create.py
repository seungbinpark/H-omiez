#!C:\Users\박승빈\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)
print()
