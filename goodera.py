import pandas as pd


df = pd.read_excel(r'R:\Code\New folder (2)\Assignment_Excel.xlsx')  
print(df)  #prints the current value 


df['a'] = df['a'].str.lstrip()
df['a'] = df['a'].str.capitalize()


print(df) #prints the new input value 
#df.to_excel("answer.xlsx")   #saves a new filw with updated input values
