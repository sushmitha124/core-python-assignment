def calculate_positive_feedback(ratings):
    # Count the number of positive feedbacks (ratings 4 and 5)
    positive_count = sum(1 for rating in ratings if rating >= 4)

    # Calculate the percentage of positive feedback
    if len(ratings) == 0:
        return 0.0
    positive_percentage = (positive_count / len(ratings)) * 100

    return positive_percentage


# Example input
ratings = eval(input("Enter ratings"))
positive_feedback_percentage = calculate_positive_feedback(ratings)

# Output the result
print(f"Positive Feedback: {positive_feedback_percentage:.2f}%")
