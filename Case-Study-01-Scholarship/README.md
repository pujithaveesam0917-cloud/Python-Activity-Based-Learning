Case Study 01: University Scholarship Allocation

1. Problem Statement

Develop a Python program to evaluate scholarship applicants using aggregate marks, subject-wise minimum marks, attendance, and family income. The program identifies eligible applicants and ranks them according to predefined rules.

2. Objectives

- Calculate aggregate marks for each applicant.
- Check subject-wise minimum marks.
- Verify attendance and family income requirements.
- Identify eligible applicants.
- Rank eligible applicants using tie-breaking rules.

3. Assumptions

The following rules are assumed for this demonstration because the assignment does not provide exact scholarship thresholds:

- Each applicant has marks in three subjects, each out of 100.
- Each subject requires at least 40 marks.
- Aggregate marks must be at least 75%.
- Attendance must be at least 75%.
- Annual family income must not exceed ₹2,50,000.
- Applicants are ranked by aggregate percentage in descending order.
- If aggregate percentages are equal, higher attendance ranks first.
- If attendance is also equal, lower family income ranks first.
- If all three values are equal, names are arranged alphabetically.

4. Algorithm

1. Start.
2. Input the number of applicants.
3. For each applicant, input the name, three subject marks, attendance, and annual family income.
4. Calculate the aggregate percentage.
5. Check subject-wise marks, aggregate percentage, attendance, and income.
6. Add eligible applicants to a list.
7. Rank eligible applicants using the specified tie-breaking rules.
8. Display the eligible applicants and their ranks.
9. Stop.

5. Flowchart

flowchart TD
    A([Start]) --> B[Input applicant details]
    B --> C[Calculate aggregate percentage]
    C --> D{All eligibility conditions satisfied?}
    D -- Yes --> E[Add applicant to eligible list]
    D -- No --> F[Mark applicant as ineligible]
    E --> G{More applicants?}
    F --> G
    G -- Yes --> B
    G -- No --> H[Rank eligible applicants]
    H --> I[Display results]
    I --> J([Stop])

6. Pseudocode

START
INPUT number of applicants

FOR each applicant
    INPUT name, three subject marks, attendance, income
    CALCULATE aggregate percentage

    IF every subject mark >= 40
       AND aggregate percentage >= 75
       AND attendance >= 75
       AND income <= 250000
        ADD applicant to eligible list
    ELSE
        DISPLAY applicant is ineligible
    END IF
END FOR

SORT eligible applicants by:
    aggregate percentage descending
    attendance descending
    income ascending
    name alphabetically

DISPLAY ranked eligible applicants
STOP

7. Python Source Code

The complete Python program will be stored separately in "scholarship.py" in this folder.

8. Test Cases

Applicant| Subject Marks| Attendance| Annual Income| Expected Result
Anu| 80, 85, 90| 90%| ₹2,00,000| Eligible
Balu| 90, 90, 90| 80%| ₹2,00,000| Eligible
Chandu| 90, 35, 95| 95%| ₹1,50,000| Ineligible: subject mark below minimum
Divya| 80, 80, 80| 70%| ₹1,50,000| Ineligible: attendance below minimum
Esha| 80, 80, 80| 85%| ₹3,00,000| Ineligible: income exceeds limit

9. Output Screenshots

Screenshots of the program execution and its results will be added after running and testing "scholarship.py".

10. Conclusion

This case study demonstrates how Python variables, data types, conditional statements, loops, lists, and comparison operators can be used to evaluate scholarship eligibility and rank applicants systematically.
#Case Study 01: University Scholarship Allocation
