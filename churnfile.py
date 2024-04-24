
import streamlit as st
import pandas as pd
import joblib

# Load the trained Random Forest model
model = joblib.load("churn__model.pkl")

# Define the main function for the Streamlit app
def main():
    st.title("Employee Attrition Prediction")

    # Create input fields for user input
    name = st.text_input("Name")
    
    # Define a select box for the department
    department_options = ["Admin", "Engineering", "Finance", "IT", "Logistic", "Sales", "Marketing", "Operations", "Support", "Retail"]
    department = st.selectbox("Department", department_options)
    
    promoted_options = {"Yes": 1, "No": 0}
    promoted = st.selectbox("Promoted (Yes or No)", options=list(promoted_options.keys()))

    review = st.number_input("Review Score", min_value=1, max_value=5, value=3)
    projects = st.number_input("Number of Projects", min_value=1, max_value=10, value=5)
    salary = st.selectbox("Salary Category", ["Low", "Medium", "High"])
    tenure = st.number_input("Tenure (Years)", min_value=1, max_value=10, value=3)
    satisfaction = st.number_input("Satisfaction Level", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    
    bonus_options = {"Yes": 1, "No": 0}
    bonus = st.selectbox("Bonus (Yes or No)", options=list(bonus_options.keys()))

    avg_hrs = st.number_input("Average Hours Worked per Month", value=0)

    # Define a button to trigger predictions
    if st.button("Predict"):
        # Convert salary category to numerical representation
        salary_mapping = {"Low": 1, "Medium": 2, "High": 3}
        salary_numeric = salary_mapping[salary]

        # Map promoted option to numeric value
        promoted_numeric = promoted_options[promoted]
        
        # Map bonus option to numeric value
        bonus_numeric = bonus_options[bonus]

        # Create a DataFrame with the input data
        data = {
            "name": [name],
            "department": [department],
            "promoted": [promoted_numeric],
            "review": [review],
            "projects": [projects],
            "salary": [salary_numeric],
            "tenure": [tenure],
            "satisfaction": [satisfaction],
            "bonus": [bonus_numeric],
            "avg_hrs_month": [avg_hrs]
        }
        df = pd.DataFrame(data)

        # Drop name and department columns
        df = df.drop(columns=["name"])
        df = df.drop(columns=["department"])

        # Make predictions
        prediction = model.predict(df)

        # Interpret predictions
        if prediction[0] == 1:
            prediction_text = "Employee will leave the company"
        else:
            prediction_text = "Employee will not leave the company"

        # Display the prediction
        st.subheader("Prediction")
        st.write(prediction_text)

    # Add a footer with the specified text
    st.markdown("<hr style='border: none; border-top: 2px solid #eee;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Developed by Rajyug IT Solutions</p>", unsafe_allow_html=True)

# Run the main function
if __name__ == "__main__":
    main()
