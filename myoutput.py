#!/usr/bin/python

import sys 
from pymongo import MongoClient
import ListAccessObject
import cgi, cgitb

connection = MongoClient()
db = connection.lists

lists = ListAccessObject.ListAccessObject(db)

output = lists.find_items()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print '''
<head>
<style>
table {
    width:100%;
}
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
    text-align: left;
}
table#t01 tr:nth-child(even) {
    background-color: #eee;
}
table#t01 tr:nth-child(odd) {
   background-color:#fff;
}
table#t01 th	{
    background-color: black;
    color: white;
}
</style>
</head>
<body>

'''

print '<table id="t01">'
print '<tr> <th> List Name </th> <th> Item </th> </tr>'
for item in output:
  print '<tr><td>'
  print item['list']
  print '</td><td>'
  print item['item']
  print '</td></tr>'
  #print item
#  print '<br />'
'''
  print '  <tr><td>'
  print '    </td><td>'.join(item)
  print '  </td></tr>'
'''
print '</body>'
print '</table>'
print "</html>"

