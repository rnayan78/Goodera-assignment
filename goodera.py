import pandas as pd

df = pd.read_excel(r'R:\Code\New folder (2)\Assignment_Excel.xlsx')  
print(df)  #prints the current value 
           

df = df.assign(a=df['Output String'])  #changed the name of input string to 'a'

print(df) #prints the new input value which is identical to output value
df.to_excel("answer.xlsx")  #saves a new file in which input string identical to output