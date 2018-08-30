#Q.1
import re
EMAIL=input('Enter Email-ID:')
m=re.fullmatch('^[a-zA-Z][_a-zA-z0-9.]*(@)(gmail.com|yahoo.com)',EMAIL)
if m:
    print('EMAIL IS VALID')
else:
    print('EMAIL IS NOT VALID')
  
#Q.2
import re
a=input('Enter Indian Phone number:')

m=re.fullmatch('(\+91-)[6-9][0-9]{9}',a)
if m:
    print('NUMBER IS VALID')
else:
    print('NUMBER IS NOT VALID')
