import streamlit as st

# Main function to run the Streamlit app
def main():
    st.title("Weekly Check-In Form")

    # Create the form
    with st.form(key='health_metrics_form'):
        st.write("Question 1:")
        
        # 1a. Date
        date = st.date_input("1a. Date")
        
        # 1b. Current Weight
        current_weight = st.number_input("1b. Current Weight (lbs)", min_value=0, step=1)

        # 1c. Previous Weight
        previous_weight = st.number_input("1c. Previous Weight (lbs)", min_value=0, step=1)

        # 1d. Waist Relaxed
        waist_relaxed = st.number_input("1d. Waist Relaxed (in)", min_value=0, step=1)
        
        # 1e. Waist Flexed
        waist_flexed = st.number_input("1e. Waist Flexed (in)", min_value=0, step=1)
        
        # 1f. Bicep Flexed
        bicep_flexed = st.number_input("1f. Bicep Flexed (in)", min_value=0, step=1)
        
        st.write("Question 2:")
        
        # 2a. Target Calories
        target_calories = st.number_input("2a. Target Calories", min_value=0, step=1)
        
        # 2b. Actual Calories
        actual_calories = st.number_input("2b. Actual Calories", min_value=0, step=1)
        
        st.write("Question 3:")
        
        # 3a. Target Protein
        target_protein = st.number_input("3a. Target Protein (g)", min_value=0, step=1)
        
        # 3b. Target Carbs
        target_carbs = st.number_input("3b. Target Carbs (g)", min_value=0, step=1)
        
        # 3c. Target Fats
        target_fats = st.number_input("3c. Target Fats (g)", min_value=0, step=1)
        
        # 3d. Actual Protein
        actual_protein = st.number_input("3d. Actual Protein (g)", min_value=0, step=1)
        
        # 3e. Actual Carbs
        actual_carbs = st.number_input("3e. Actual Carbs (g)", min_value=0, step=1)
        
        # 3f. Actual Fats
        actual_fats = st.number_input("3f. Actual Fats (g)", min_value=0, step=1)
        
        st.write("Question 4:")
        
        # 4a. Upload Image
        uploaded_image = st.file_uploader("4a. Upload Image", type=["jpg", "jpeg", "png"])
        
        # Submit button
        submit_button = st.form_submit_button(label='Submit')
    
    # Display the input data
    if submit_button:
        st.write("### Submitted Data")
        st.write(f"**Date:** {date}")
        st.write(f"**Current Weight:** {current_weight} lbs")
        st.write(f"**Previous Weight:** {previous_weight} lbs")
        st.write(f"**Waist Relaxed:** {waist_relaxed} in")
        st.write(f"**Waist Flexed:** {waist_flexed} in")
        st.write(f"**Bicep Flexed:** {bicep_flexed} in")
        st.write(f"**Target Calories:** {target_calories}")
        st.write(f"**Actual Calories:** {actual_calories}")
        st.write(f"**Target Protein:** {target_protein} g")
        st.write(f"**Target Carbs:** {target_carbs} g")
        st.write(f"**Target Fats:** {target_fats} g")
        st.write(f"**Actual Protein:** {actual_protein} g")
        st.write(f"**Actual Carbs:** {actual_carbs} g")
        st.write(f"**Actual Fats:** {actual_fats} g")
        
        if uploaded_image is not None:
            st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

if __name__ == "__main__":
    main()
