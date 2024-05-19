Name: Necula Mihail <br>
Group: 313CAa

## Readme Project PCLP3

***A. TASK 1***

Reads the dataset and store it in a dataframe using the function read_csv from <br>
the module "panda". After:
- verify if the dataset has duplicate rows
- find the number of missing values from every column
- find the type of the values from every column

***B. TASK 2***

Process the columns "Survived", "Pclass" and "Sex". For every processed column <br>
is made a graphic of type pie. The operation of proessing a column includes the <br>
next steps:
- find all the options / values from the column
- find of how many times every options appears in the column

***C. TASK 3***

Process the columns which have just numerical values. For every processed <br>
column is made a histogram.

***D. TASK 4***

Find the number of missing values from every column. For every column which <br>
has holes, is printed on the screen how many they are and the percentage of <br>
holes from all values which should be. <br>
After, find the numbers of characteristics / values which are missing for the <br>
persons which survived, respectively for the people that died. On the screen, <br>
we print the percetage of missing values from all values which should be <br>
for every class from the category "Survived". <br>

***E. TASK 5***

Create a list which conatins the category of age for every person. The categories <br>
of age are:
- [0, 21) years -> category 0
- [21, 41) years -> category 1
- [41, 61) years -> category 2
-  over 61 years -> category 3

This list is added in the dataframe as a new column. After we do this, we count <br>
the number of persons from every category of age and make a graphic which <br>
contains these informations.

***F. TASK 6***

Add the column "Category of age" in dataframe and count how many male survived <br>
and died in every category of age. Print the number of male survivors on screen, <br> 
for every category, and make a graphic with this informations.

***G. TASK 7***

Find the number of children (< 18 years) and adults which survived and died.  <br>
Calculate the percentege of children from the ship and print the result on <br>
screen. After, we do a graphic of type pie which conatins the informations <br>
about the adults and their existence after Titanic. We do, the same thing <br>
for children.

***H. TASK 8***

We fill up the holes from the dataframe. We have 3 columns with missing <br>
values: "Age", "Cabin", "Embarked". <br>

Age - We caclulte the medium age for a survivor and for a person who died. <br>
If a person survived, but we don't know his age, we put the medium age of <br>
a survivor. The same thing is done and for a person who died, but have <br>
hasn't the age known.

Cabin, Embarked - Because these columns have string values, we must work <br>
a little differently . For every column, firstly we determinate the most <br>
frequent option of survivors and fill the survivors's holes from the collum. <br>
Secondly, we do the same thing for the person which, unfortunately, died. 

***I. TASK 9***

Split the column "Name" to do a column with the titles of the people. We do <br>
3 lists: one with the titles for men, another with the titles for women, and the <br>
last with the neutral titles. We go throught the column of "Title" and "Sex" <br>
and count the number of worng and right pairs / titles. We plot the results.

***J. TASK 10***

Take first 100 persons from the dataset and do a graphic with the columns: <br>
"Survived", "Pclass" and "Fare". The purpose of this graphic is to analyze <br>
how the class and the fare influnenced the life of the persons.

