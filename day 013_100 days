print("Exam grade calculator")
print()

exam = input("Name of exam: ")
total_score = int(input("Score: "))
your_score = int(input("Your score: "))
print()

number_score = float(your_score / total_score)
final_number = round(number_score*100, 2)
final_perc = round(float(your_score / total_score) * 100, 2)

print("You got", final_perc, "%")

if final_number >= 90:
  grade = "A+"
  print("You got", final_number, "which is a", grade)
elif final_number >= 80 and final_number <= 89:
  grade = "A"
  print("You got", final_number, "which is a", grade)
elif final_number >= 70 and final_number <= 79:
  grade = "B"
  print("You got", final_number, "which is a", grade)
elif final_number >= 60 and final_number <= 69:
  grade = "C"
  print("You got", final_number, "which is a", grade)
elif final_number >= 50 and final_number <= 59:
  grade = "D"
  print("You got", final_number, "which is a", grade)
elif final_number <= 49:
  grade = "U"
  print("You got", final_number, "which is a", grade)
else:
  print("Error, please try again.")
