import data_set as ds

print("*********** TASK 2 ***********")

# Read the data set.
list = ds.read_data("../titanic/train.csv")
list = ds.eliminate_duplicates(list)

# Do a graphic using the information from  the column
# "Survived".
survivors = ds.extract_column(list, "Survived")
surv_options = ds.eliminate_duplicates(survivors)
surv_counter = ds.count_aparitions(survivors, surv_options)
if surv_options[0] == 0:
	surv_options[0] = "survivors"
	surv_options[1] = "deads"
else:
	surv_options[1] = "survivors"
	surv_options[0] = "deads"
ds.print_graphic_with_percenteges(surv_options, surv_counter, "Survived?")

# Do a graphic using the information from  the column
# "Survived".
pclass = ds.extract_column(list, "Pclass")
class_options = ds.eliminate_duplicates(pclass)
class_counter = ds.count_aparitions(pclass, class_options)
ds.print_graphic_with_percenteges(class_options, class_counter, "Classes")

# Do a graphic using the information from  the column
# "Sex".
sex = ds.extract_column(list, "Sex")
sex_options = ds.eliminate_duplicates(sex)
sex_counter = ds.count_aparitions(sex, sex_options)
ds.print_graphic_with_percenteges(sex_options, sex_counter, "Sex")