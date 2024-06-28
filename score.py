student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

heightest_score = 0
for score in student_scores:
  if score > heightest_score:
    heightest_score = score

print(f"The heighest score in the class is: {heightest_score}")