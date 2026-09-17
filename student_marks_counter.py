# student marks counter and avarage marks
student = [57,67,85,95,78,66]
def student_marks_counter(marks):
    total = sum(marks) #total marks
    average = total/len(marks) # avarage marks
    hig = max(marks) # highest marks
    low = min(marks) # lowest marks
    # student RESULTS
    print("-"*5,"RESULT","-"*5)
    print("total ",total,sep="= ")
    print(f"average = {average:.2f}")
    print("highest ",hig,sep="= ")
    print("lowest ",low,sep="= ")
    # pass or fail condition
    if average >= 40:
        print("status: pass")
    else:
        print("status: fail")
student_marks_counter(student)