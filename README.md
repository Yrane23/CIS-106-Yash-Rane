# CIS-106-Yash-Rane
ps3p1
#input phase
exam_score_1 = float(input("Enter exam score 1: "))
exam_score_2 = float(input("Enter exam score 2: "))


#process phase
weighted_score_1 = exam_score_1 * 0.6
weighted_score_2 = exam_score_2 * 0.4
total_score = weighted_score_1 + weighted_score_2

#output phase
print("Total score", total_score)

