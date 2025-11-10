

# Function to calculate BMI
def bmi_calc(weight: float, height: float) -> float {
    # BMI = weight(kg) / (height(m))^2
    return weight / (height * height);
}

# Function to determine BMI category
def categorybmi(bmi: float) -> str {
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
        weight = 120;    # weight in kg
        height = 1.8;  # height in meters
        
        # Calculate BMI
        bmi = bmi_calc(weight, height);
        category = categorybmi(bmi);
        
        # Report results
        report("BMI Calculator Results:");
        report("------------------");
        report(f"Weight: {weight} kg");
        report(f"Height: {height} m");
        report(f"BMI: {bmi:.1f}");
        report(f"Category: {category}");
    }
}
    
