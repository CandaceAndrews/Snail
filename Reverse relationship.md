### Reverse relationship

* new_record = record_form.save(commit=False)

commit=False tells Django not to save the record_form object to the database immediately after it's validated, which allows us to perform additional actions on the form data before saving it to the database.
In this case, the form data is used to create a new Record object with a foreign key to the corresponding Habit object. So we first set the habit attribute of the new Record object to the habit object we retrieved using get_object_or_404(Habit, pk=habit_pk) earlier, and then save the new Record object to the database using new_record.save().
This way, we can modify the form data or add additional information to the new Record object before saving it to the database with the correct foreign key reference to the corresponding Habit object.
