# add your get_student_with_more_classes function here!
# if students have same number of classes, return first student.
def get_student_with_more_classes(student1, student2):
    if student1.get_num_classes() >= student2.get_num_classes():
        return student1
    return student2