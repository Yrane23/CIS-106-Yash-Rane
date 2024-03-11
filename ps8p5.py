with open("data2.txt", 'r') as file:
  lines = file.readlines()

total_tuition = 0.0
student_count = 0
for i in range(0, len(lines), 3):
  last_name = lines[i].strip()
  district_code = lines[i + 1].strip()
  credits = int(lines[i + 2].strip())
  cost_per_credit = 250 if district_code == 'I' else 500
  tuition = credits * cost_per_credit
  total_tuition += tuition
  student_count += 1
  print(f"{last_name} {credits} {tuition}")

print(f"Sum of all tuition owed: ${total_tuition}")
print(f"Number of students: {student_count}")

