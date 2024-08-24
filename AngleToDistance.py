import math as mt
import numpy
import pandas as pd
start=5
end=85
step=5
#Denote length
h1=44.98 # height of testing object
# h2= # height of 
d=50  # length of testing finger
c1=[]
c2=[]
# h=h2-h1
for i in range(start, end, step):
    print("Angle:",i)
    c1.append(i)
    h=mt.cos(mt.radians(i))*d
    h2=h1+h
    print("h2:",h2)
    c2.append(h2)
data ={
    'Angle':c1,
    'h2':c2
}
df = pd.DataFrame(data)

# Xuất DataFrame ra file Excel
output_file = 'Stiffness.xlsx'
df.to_excel(output_file, index=False)

print(f"Dữ liệu đã được lưu vào tệp {output_file}")
