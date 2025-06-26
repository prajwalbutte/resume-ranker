print("Resume Ranker - Applicant Tracking System Python Project\n\n")


#Input
job_description = input("Paste Job Description:\n").lower()
resume = input("Paste Resume Here:\n").lower()


#Processing Input
jd_words = job_description.split()
resume_words = resume.split()

#Finding matching words
match = 0
for word in jd_words:
    if word in resume_words:
        match += 1 

#Score Calculating
score = int((match/len(set(jd_words)))*100)

#Outputs
print(f"\nYour resume match score is:{score}%")

if score >= 75 :
    print("Strong match,Your resume files the job well.")
elif score >= 40 :
    print("Average match,Try improving your resume.")
else:
    print("Weak match..!Customize your resume better.")


print("Thank You..!\n")