def display_marks_statement(student):
    print("\n----student marks statement----")
    print(f"name:{student['name']}")
    print(f"roll number:{student['roll number']}")
    print("subject_wise marks:")
    for subject.marks in student['marks'].items():
       print(f"{subject}:{marks}")
        total=sum(student['marks'].values())
        average=total/len(student['marks'])
        print(f"total marks:{total}")
        print(f"average marks:{average:2f}")
        if average>=50:
            print("result:passed")
        else:
            print("result:failed")
student={}
student['name']=input("enter student name:")
student['roll number']=input("enter the student roll number:")
num_subject=int(input("enter the number of subject:"))
student['marks']={}
for _ in range(num_subject):
   subject=input("enter the subject name:")
   marks=int(input(f"enter the marks for{subject}:"))
   student['marks'][subject]=marks
display_marks_statement(student)
                    
                    
