

# Function to calculate BMI
def calculate_bmi(weight: float, height: float) -> float {
    # BMI = weight(kg) / (height(m))^2
    return weight / (height * height);
}

# Function to determine BMI category
def get_bmi_category(bmi: float) -> str {
    if (bmi < 18.5) {
        return "Underweight";
    } elif (bmi < 25) {
        return "Normal weight";
    } elif (bmi < 30) {
        return "Overweight";
    } else {
        return "Obese";
    }
}

# Main walker
walker init {
    with entry {
        # Sample values (you can modify these)
        weight = 70;    # weight in kg
        height = 1.75;  # height in meters
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height);
        category = get_bmi_category(bmi);
        
        # Report results
        report("BMI Calculator Results:");
        report("------------------");
        report(f"Weight: {weight} kg");
        report(f"Height: {height} m");
        report(f"BMI: {bmi:.1f}");
        report(f"Category: {category}");
    }
}
    
