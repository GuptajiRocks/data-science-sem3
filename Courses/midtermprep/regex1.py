import re
# phone = '+91-2333876589 my phone number'
# num = re.sub(r'\D','',phone)
# print(num)

string = 'PQPPPPPRPPPD'
res = re.findall('P{1,2}', string)
print(res, len(res))