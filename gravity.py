import pandas as pd
#read csv file
df = pd.read_csv("final_data.csv")
print(df.columns)
df.drop(['Unnamed: 0'],axis=1,inplace=True)
#df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', ''))
#df['Radius']=df['Radius'].astype('float')
radius = df['Radius'].to_list()
mass= df['Mass'].to_list()
gravity = []
def converttosi(r,m):
    for i in range(0,len(r)-1):
        radius[i]=r[i]*6.957e+8
        mass[i]=m[i]*1.989e+30
#converttosi(radius,mass)
def gravitycalc(r,m):
    G=6.674e-11
    for i in range(0,len(m)):
        g=m[i]*G/((r[i])**2)
        gravity.append(g)
gravitycalc(radius,mass)
df["gravity"]=gravity
df.to_csv("stars_with_gravity.csv")