import pandas as pd
# קריאה של הקובץ csv
# cs ="r" + input("enter the csv addres ")
df = pd.read_csv(r"C:\Users\gmth0\OneDrive\Pictures\Screenshots\PlayTennis.csv")


# יצירת שתי טבלאות חדשות אחד לכן אחד ללא
mask_yes =df['PlayTennis']== "Yes"
filterd_yes=df[mask_yes].copy()
filterd_yes.drop('PlayTennis', axis=1, inplace=True)

unique_vals = filterd_yes['Outlook'].unique().tolist()
print(unique_vals)

mask_no=df['PlayTennis']== "No"
filterd_no=df[mask_no].copy()
filterd_no.drop('PlayTennis', axis=1, inplace=True)
print(filterd_yes,"\n",filterd_no)


# יצירת שךוש משתנים אחד לכמות כללי אחד לכן ואחד ללא
amount_of_rows=df.shape[0]
amount_of_yes=filterd_yes.shape[0]
amount_of_no=filterd_no.shape[0]

#יצירת שתי מילונים ולהכניס לתוכם את שמות של העמודות המתאימות
d_yes = {}
d_no = {}

for col in filterd_yes.columns:
    d_yes[col] = {}
    for j in df[col].unique().tolist():
        d_yes[col][j] = 1 / (amount_of_yes + 1)
print(d_yes)
for col in filterd_no.columns:
    d_no[col] = {}
    for j in df[col].unique().tolist():
        d_no[col][j] = 1 / (amount_of_no + 1)
print(d_no)
#הכנסה של הכמות פעמים שיש כל אפשרות ביחס לבחירה לתוך המילון

for col in filterd_yes.columns:
    d_yes[col].update(
        {k: v / amount_of_yes for k, v in filterd_yes[col].value_counts().items()}
    )
for col in filterd_no.columns:
    d_no[col].update({k: v / amount_of_no for k, v in filterd_no[col].value_counts().items()})
print(d_yes)
print(d_no)

#הכנסה של נתונים מהמשתמש
d_input={}
print("enter plese the details")
i_outlook = input("what is the outlook? {Sunny,Riny,Overcast} ").strip()
i_temperature = input("what is the temperature? {Hot,Mild,Cold} ").strip()
i_humidity = input("what is the humidity? {High,Normal} ").strip()
i_windy = input("isit windy? {True,False} ").strip()
i_windy = i_windy == 'True'

#חישוב הסטיסטיקה
yes = d_yes['Outlook'][i_outlook] * d_yes['Temperature'][i_temperature] * d_yes['Humidity'][i_humidity] * d_yes['Windy'][i_windy]
no = d_no['Outlook'][i_outlook] * d_no['Temperature'][i_temperature] * d_no['Humidity'][i_humidity] * d_no['Windy'][i_windy]

yes *=  amount_of_yes/amount_of_rows
no *=  amount_of_no/amount_of_rows
if yes > no:
    print("yes")
else:
    print("no")