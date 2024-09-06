# String manipulations

import re
lk = "Arihant is don"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(bool(x))