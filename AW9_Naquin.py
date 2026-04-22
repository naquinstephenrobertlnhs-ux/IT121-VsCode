def analyze_scores(score1, score2, score3):
    average = (score1 + score2 + score3) / 3

    print("Average:", average)

    if average >= 90:
        print("Exellent!")
    elif average >= 75:
        print("Good!")
    else:
        print("Needs Improvement")

    analyze_scores(85, 90, 80)