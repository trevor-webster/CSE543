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

def die(str):
    print "Content-Type: text/html"
    print ""
    print """<html>
  <head>
    <title>Password Storage</title>
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
if form.has_key("username"):
    username = form["username"].value;
else:
    username = ""
if form.has_key("password"):
    password = form["password"].value;
else:
    password = ""
if form.has_key("admin"):
    admin = form["admin"].value;
else:
    admin = "0"

debug = False
if debug:
    id = "foo1337"
    site = "www.bar.com"
    username = "john"
    password = "pazzword"
    admin = "1"

if (id == "" or site == "" or username == "" or password == ""):
    die("<p>Missing parameters.</p>")

if id.isalnum() == False:
    die("<p>Bad id.</p>")

if admin == "1":
    try:
        blacklist = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])['blacklist'].value
    except Exception, e:
        die("<p>Malformed cookie or missing blacklist name</p>")
    if blacklist.isalnum() == False:
        die("<p>Bad blacklist name. It must be alphanumeric.</p>")
    try:
        f = open(blacklist, "r")
        m = f.read()
        f.close()
    except Exception, e:
        die("<p>Cannot open blacklist file %s: %s</p>" % (blacklist, str(e)))

    die("<p>Blacklist:</p><pre>%s</pre>" % m)

try:
    f = open("/tmp/level05/" + id, "a+")
    f.write("%s:%s:%s\n" % (site, username, password))
    f.close()
except Exception, e:
    die("<p>Something went horriby wrong (%s). Contact the admin.</p>" % str(e))

die("<p>Password saved.</p>")

</pre>
  </body>
</html>