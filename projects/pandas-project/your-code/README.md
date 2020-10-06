Panda Project.

The first step is to read the csv archive.
The we take a quick look at the dataframe, and look for the null values with isna() function.
Sometimes we have entire columns with invalid values.
After that we search for duplicates and drop them.
That´s the first part of the cleaning, we´ll call it the general cleaning.
We have a specific cleaning after the las phase, wher we analyze the elements of the columns to decide wich values need to be changed in order to make sense.
After the cells are transformed into logical data, we make a final evaluation and print the file.
After the cleaning the dataframe we analyze the data with charflows that explain the general statistics of the dataframe.

To perform this project there are several tools involved:

Python.
Pandas library.
Jupyter notebook.
Regex.
CSV.
Others.
