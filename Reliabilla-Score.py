def calculate_reliability_score(total_reviews, five_star_reviews, severity):
    """
    Calculate a reliability score based on the number of total reviews,
    the number of 5-star reviews, and the severity of the issue.

    Parameters:
    - total_reviews (int): The total number of reviews.
    - five_star_reviews (int): The number of 5-star reviews.
    - severity (float): The severity of the issue on a scale of 0 to 1.

    Returns:
    - float: The calculated reliability score.
    """
    
    # Validate inputs
    if total_reviews < 0 or five_star_reviews < 0 or not (0 <= severity <= 1):
        return "Invalid input values"
    
    # Constants (You can adjust these based on your specific needs)
    TOTAL_REVIEW_WEIGHT = 0.4
    FIVE_STAR_REVIEW_WEIGHT = 0.5
    SEVERITY_WEIGHT = 0.1
    
    # Normalizing the number of 5-star reviews
    if total_reviews != 0:
        normalized_five_star = five_star_reviews / total_reviews
    else:
        normalized_five_star = 0
    
    # Calculate the reliability score
    reliability_score = (
        (TOTAL_REVIEW_WEIGHT * total_reviews) +
        (FIVE_STAR_REVIEW_WEIGHT * normalized_five_star) +
        (SEVERITY_WEIGHT * severity)
    )
    
    return reliability_score

# Test the function
print(calculate_reliability_score(100, 80, 0.2))  # Output should be a float representing the reliability score
