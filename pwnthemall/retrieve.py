<html>
  <head>
    <title>Password Storage</title>
  </head>
  <body>
<p>Blacklist:</p><pre>#!/usr/bin/env python2
import sys
import cgi
import random
import os
import tempfile
import Cookie
#debugging
#import cgitb; cgitb.enable()

STORAGE = "/tmp/level05/"


def die(str):
    print "Content-Type: text/html"
    print ""
    print """<html>
  <head>
    <title>Password Retrieval</title>
  </head>
  <body>
%s
  </body>
</html>""" % str
    sys.exit(0)

form = cgi.FieldStorage()

if form.has_key("id"):
    id = form["id"].value;
else:
    id = ""
if form.has_key("site"):
    site = form["site"].value;
else:
    site = ""
if form.has_key("admin"):
    admin = form["admin"].value;
else:
    admin = "0"

debug = False
if debug:
    id = "foo1337"
    site = "bar.com"
    admin = "1"

if (id == "" or site == ""):
    die("<p>Missing parameters.</p>")

if id.isalnum() == False:
    die("<p>Bad id.</p>")

res = list()

if admin == "1":
    try:
        site = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])['site'].value
        password = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])['password'].value
    except Exception as ex:
        die("<p>Malformed cookie or missing site/password.</p>")

    if password != 'terriblechoice':
        die("<p>Wrong password.</p>")

    for filename in os.listdir(STORAGE):
        fullpath = "%s%s" % (STORAGE, filename)
        if os.path.isfile(fullpath):
            f = open(fullpath, "r")
            for l in f:
                if site in l:
                    res.append(l)
            f.close()

    die("<pre>" + '\n'.join(res) + "</pre>")


try:
    f = open(STORAGE + id, "r")
    for l in f:
        if site in l:
            res.append(l)
    f.close()
except Exception, e:
    die("<p>Cannot retrieve the password. Wrong id?</p>")

die("<pre>" + '\n'.join(res) + "</pre>")












</pre>
  </body>
</html>