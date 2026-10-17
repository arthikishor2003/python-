# Naive Bayes Probability Program

p_study_pass = 0.9
p_study_fail = 0.2

p_pass = 0.8
p_fail = 0.2

# Calculate total probability
p_study = (p_study_pass * p_pass) + (p_study_fail * p_fail)

# Calculate conditional probabilities
p_pass_given_study = (p_study_pass * p_pass) / p_study
p_fail_given_study = (p_study_fail * p_fail) / p_study

# Display output
print("Probability of pass =", round(p_pass_given_study, 4))
print("Probability of fail =", round(p_fail_given_study, 4))

if p_pass_given_study > p_fail_given_study:
    print("Predicted result: Pass")
else:
    print("Predicted result: Fail")