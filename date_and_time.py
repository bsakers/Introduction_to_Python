from datetime import datetime

#.now() will pull the current date and time
now= datetime.now()
print now

#can call year, month, and day
print now.year
print now.month
print now.day

#can use string concat to grant the date format you want. Example:
print '%s/%s/%s' %(now.month, now.day, now.year)

#can call second, minute, and hour as well
print '%s:%s:%s' %(now.hour, now.minute, now.second)

#putting it all together:
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
