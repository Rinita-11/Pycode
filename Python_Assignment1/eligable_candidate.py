# Number of students
num_students = int(input("Enter the number of students: "))

# Loop through each student
for i in range(num_students):
    print(f"\nEnter marks for student {i + 1}:")
    maths = float(input("Mathematics: "))
    physics = float(input("Physics: "))
    chemistry = float(input("Chemistry: "))
    
    # Calculate total
    total = maths + physics + chemistry
    
    # Check eligibility
    if (maths >= 60 and physics >= 50 and chemistry >= 40 and total >= 200) or (maths + physics >= 150):
        print(f"Student {i + 1} is eligible.")
    else:
        print(f"Student {i + 1} is not eligible.")
