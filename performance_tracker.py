class Student:
    def calculate_average_marks(students):
        average_marks = {}
        for name,marks in students.items():
            average_marks[name] = round(sum(marks)/len(marks), 2)
        return average_marks

    def find_top_performer(average_marks):
        return max(average_marks,key=average_marks.get)

# Input example
students = eval(input("Enter the student marks"))
obj=Student
# Calculate average marks and top performer
average_marks = obj.calculate_average_marks(students)
top_performer = obj.find_top_performer(average_marks)

# Output results
print("Average Marks:", average_marks)
print("Top Performer:", top_performer)
