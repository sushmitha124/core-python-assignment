def calculate_positive_feedback(ratings):
    positive_count = sum(1 for rating in ratings if rating >= 4)
    if len(ratings) == 0:
        return 0.0
    positive_percentage = (positive_count / len(ratings)) * 100

    return positive_percentage
ratings = eval(input("Enter ratings"))
positive_feedback_percentage = calculate_positive_feedback(ratings)
print(f"Positive Feedback: {positive_feedback_percentage:.2f}%")
