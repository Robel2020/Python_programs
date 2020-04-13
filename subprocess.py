import datetime
import subprocess, os

import re
# current = datetime.datetime.now()
# print(current.strftime("%a"))
# print(current.strftime("%H"))
# print(current.strftime("%M"))
# string = "07/09/76,"
# print(string)
# string= string[0:8]
# print(string)

txt = " The most important thing is programming "

x = re.findall("he", txt)
x = re.findall( 'mo', txt)