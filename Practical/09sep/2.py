import pandas as pd
data = {  
'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Mar', 'Mar', 'Mar', 'Apr', 'Apr', 'Apr', 'May', 'May', 'May', 'Jun', 
'Jun', 'Jun', 'Jul', 'Jul', 'Jul', 'Aug', 'Aug', 'Aug', 'Sep', 'Sep', 'Sep', 'Oct', 'Oct', 'Oct', 'Nov', 'Nov', 'Nov', 'Dec', 
'Dec', 'Dec'],  
 
'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 
'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'], 
 
'Sales': [100, 150, 120, 200, 180, 160, 300, 250, 240, 350, 300, 280, 400, 380, 360, 450, 400, 380, 500, 450, 
430, 550, 500, 480, 600, 550, 520, 650, 600, 570, 700, 650, 620, 750, 700, 680]}

df = pd.DataFrame(data)
newdf = pd.pivot_table(df, index="Month",columns="Product", values="Sales", sort=False, aggfunc="sum")
print(newdf)

print(newdf.transpose())