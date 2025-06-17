Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\Acer\Desktop\EDA 1.py
     Pregnancies  Glucose  ...  Age  Outcome
0            6.0      148  ...   50      1.0
1            1.0       85  ...   31      0.0
2            8.0      183  ...   32      1.0
3            1.0       89  ...   21      0.0
4            0.0      137  ...   33      1.0
..           ...      ...  ...  ...      ...
763         10.0      101  ...   63      0.0
764          2.0      122  ...   27      0.0
765          5.0      121  ...   30      0.0
766          1.0      126  ...   47      1.0
767          1.0       93  ...   23      0.0

[768 rows x 9 columns]
#Summary of dataset:By dafault shows top 5 records, to see 'n' top records, enter 'n' in the function as parameter.
data.head()
   Pregnancies  Glucose  BloodPressure  ...  DiabetesPedigreeFunction  Age  Outcome
0          6.0      148           72.0  ...                     0.627   50      1.0
1          1.0       85           66.0  ...                     0.351   31      0.0
2          8.0      183           64.0  ...                     0.672   32      1.0
3          1.0       89           66.0  ...                     0.167   21      0.0
4          0.0      137           40.0  ...                     2.288   33      1.0

[5 rows x 9 columns]
#top implies, 5 records from the starting of the dataset.

#Similarly to see 5 last records of the dataset, data.tail() is the function.
data.tail()
     Pregnancies  Glucose  ...  Age  Outcome
763         10.0      101  ...   63      0.0
764          2.0      122  ...   27      0.0
765          5.0      121  ...   30      0.0
766          1.0      126  ...   47      1.0
767          1.0       93  ...   23      0.0

[5 rows x 9 columns]
# Data Summarisation via Statistics results. data.describe()
data.describe()
       Pregnancies     Glucose  ...         Age     Outcome
count   765.000000  768.000000  ...  768.000000  767.000000
mean      3.828758  120.894531  ...   33.240885    0.349413
std       3.364927   31.972618  ...   11.760232    0.477096
min       0.000000    0.000000  ...   21.000000    0.000000
25%       1.000000   99.000000  ...   24.000000    0.000000
50%       3.000000  117.000000  ...   29.000000    0.000000
75%       6.000000  140.250000  ...   41.000000    1.000000
max      17.000000  199.000000  ...   81.000000    1.000000

[8 rows x 9 columns]
# (VVIP)Handling null/missing values,duplicate data,outliers: Handling Data Inconsistency.
# Finding number of null/missing values across each columns.

#isna()-> is not a number or null value
data.isna().sum()
Pregnancies                 3
Glucose                     0
BloodPressure               5
SkinThickness               5
Insulin                     1
BMI                         3
DiabetesPedigreeFunction    1
Age                         0
Outcome                     1
dtype: int64
# This was the sum of all null values of all 9 columns, across 768 records.

# dropna()-> drop not a number, is a method of handling null values, which may cause inconsistency in data mining, by removing such records(noe the column value!).
filtered_data=data.dropna()

filtered_data
     Pregnancies  Glucose  ...  Age  Outcome
0            6.0      148  ...   50      1.0
1            1.0       85  ...   31      0.0
2            8.0      183  ...   32      1.0
3            1.0       89  ...   21      0.0
4            0.0      137  ...   33      1.0
..           ...      ...  ...  ...      ...
763         10.0      101  ...   63      0.0
764          2.0      122  ...   27      0.0
765          5.0      121  ...   30      0.0
766          1.0      126  ...   47      1.0
767          1.0       93  ...   23      0.0

[753 rows x 9 columns]
#5 records consisting null values deleted.

filtered_data.isna().sum()
Pregnancies                 0
Glucose                     0
BloodPressure               0
SkinThickness               0
Insulin                     0
BMI                         0
DiabetesPedigreeFunction    0
Age                         0
Outcome                     0
dtype: int64


#Dropping unnecessary columns, via, drop():remove/drop unnecessary columns.
filtered_data_1=filtered_data.drop(columns=['Insulin','BMI','DiabetesPedegreeFunction','Age'],axis=1) #Note:The way of writing formula.
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    filtered_data_1=filtered_data.drop(columns=['Insulin','BMI','DiabetesPedegreeFunction','Age'],axis=1) #Note:The way of writing formula.
  File "C:\Users\Acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\frame.py", line 5581, in drop
    return super().drop(
  File "C:\Users\Acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 4788, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\Acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 4830, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\Acer\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\indexes\base.py", line 7070, in drop
    raise KeyError(f"{labels[mask].tolist()} not found in axis")
KeyError: "['DiabetesPedegreeFunction'] not found in axis"
filtered_data_1=filtered_data.drop(columns=['Insulin','BMI','DiabetesPedigreeFunction','Age'],axis=1) #Note:The way of writing formula. Axis defines that the data is being dropped along 1 axis only.
filtered_data_1
     Pregnancies  Glucose  BloodPressure  SkinThickness  Outcome
0            6.0      148           72.0           35.0      1.0
1            1.0       85           66.0           29.0      0.0
2            8.0      183           64.0            0.0      1.0
3            1.0       89           66.0           23.0      0.0
4            0.0      137           40.0           35.0      1.0
..           ...      ...            ...            ...      ...
763         10.0      101           76.0           48.0      0.0
764          2.0      122           70.0           27.0      0.0
765          5.0      121           72.0           23.0      0.0
766          1.0      126           60.0            0.0      1.0
767          1.0       93           70.0           31.0      0.0

[753 rows x 5 columns]


#Replacing(filling the space of) null values, with some valid numbers, is another method to deal with Null Value Data Inconsistency. fillna




#fillna()-> fill not a number will fill up the null values, with PROVIDED user values.
data_filtered_2=data.fillna(0)
data_filtered.isna().sum()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    data_filtered.isna().sum()
NameError: name 'data_filtered' is not defined. Did you mean: 'data_filtered_2'?
data_filtered_2.isna().sum()
Pregnancies                 0
Glucose                     0
BloodPressure               0
SkinThickness               0
Insulin                     0
BMI                         0
DiabetesPedigreeFunction    0
Age                         0
Outcome                     0
dtype: int64
# We generally replace null values with mean,median, or modeof the data.
  
print(x=round(data['Glucose'].mean))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(x=round(data['Glucose'].mean))
TypeError: type method doesn't define __round__ method
print(x=round(data['Glucose'].mean()))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(x=round(data['Glucose'].mean()))
TypeError: 'x' is an invalid keyword argument for print()
x=round(data['Glucose'].mean())
x
121
data_filtered_3=data.fillna(x)
data_filtered_3.isna().sum()
Pregnancies                 0
Glucose                     0
BloodPressure               0
SkinThickness               0
Insulin                     0
BMI                         0
DiabetesPedigreeFunction    0
Age                         0
Outcome                     0
dtype: int64
#correlation matrix: Matrix, with same saet of record labels as the set of column labels, signifiying relation b/w them.    .corr()
data
     Pregnancies  Glucose  ...  Age  Outcome
0            6.0      148  ...   50      1.0
1            1.0       85  ...   31      0.0
2            8.0      183  ...   32      1.0
3            1.0       89  ...   21      0.0
4            0.0      137  ...   33      1.0
..           ...      ...  ...  ...      ...
763         10.0      101  ...   63      0.0
764          2.0      122  ...   27      0.0
765          5.0      121  ...   30      0.0
766          1.0      126  ...   47      1.0
767          1.0       93  ...   23      0.0

[768 rows x 9 columns]
>>> 
>>> 
>>> data
     Pregnancies  Glucose  ...  Age  Outcome
0            6.0      148  ...   50      1.0
1            1.0       85  ...   31      0.0
2            8.0      183  ...   32      1.0
3            1.0       89  ...   21      0.0
4            0.0      137  ...   33      1.0
..           ...      ...  ...  ...      ...
763         10.0      101  ...   63      0.0
764          2.0      122  ...   27      0.0
765          5.0      121  ...   30      0.0
766          1.0      126  ...   47      1.0
767          1.0       93  ...   23      0.0

[768 rows x 9 columns]
>>> data_filtered_3.corr()
                          Pregnancies   Glucose  ...       Age   Outcome
Pregnancies                  1.000000  0.086717  ...  0.274974  0.532347
Glucose                      0.086717  1.000000  ...  0.263514  0.083602
BloodPressure                0.066613  0.149455  ...  0.239555  0.000625
SkinThickness                0.084185  0.052957  ... -0.095734  0.052060
Insulin                     -0.013961  0.331358  ... -0.042117  0.096176
BMI                          0.003751  0.196458  ...  0.013794  0.034576
DiabetesPedigreeFunction    -0.006537  0.077144  ... -0.019670 -0.000703
Age                          0.274974  0.263514  ...  1.000000  0.052786
Outcome                      0.532347  0.083602  ...  0.052786  1.000000

[9 rows x 9 columns]
>>> 
>>> 
>>> # Data Visualisation Tool
>>> import seaborn as sns

... 
... i
>>> import matplotlib.pyplot as plt
>>> 
>>> sns.heatmap(data_filtered_3[:10], annot=True)# Graphical format to represent correlation data of first ten rows(Less data: more visibility,less complex).
<Axes: >
>>> plt.show
<function show at 0x0000027770007B00>
>>> plt.show()
