import streamlit as st

def main():
    st.title("Weekly Check-In Form")
    st.write("""
    Please fill out the form with all the requested information.
    """)

    # Form Container
    with st.form(key='fitness_form'):
        
        # Question 1: Email
        email = st.text_input("Email", key="email")
        
        # Question 2: Cardio sessions details
        cardio_sessions = st.text_area(
            "How many cardio sessions did you do, what kind and duration and speed level? Put the cardio type,(Ex: stairs, incline treadmill, jump rope) length of time you did each workout and the speed level: Final Product should look like this (Ex: 5 total: 4 stairs, 20 mins, lvl 6 the first 10 mins and lvl 5 the last 10 mins, and 2 mile walk around my neighborhood )",
            key="cardio_sessions"
        )
        
        # Question 3: Average daily steps
        daily_steps = st.text_input("Average daily steps?", key="daily_steps", placeholder="Found in the Health app if you have an iPhone.")
        
        # Question 4: Exercise you hate or want removed / Macro changes
        exercise_hate_or_macro = st.text_area(
            "Any exercise you hate and want it removed? And why? OR what macro do you feel you want more of?",
            placeholder="Please explain both why you hate the exercise and/or why you want more of a specific macro.",
            key="exercise_hate_or_macro"
        )
        
        # Question 5: First/Last Name
        full_name = st.text_input("What is your first/last name?", key="full_name")
        
        # Question 6: Macros from the Weekly View (Protein/Carbs/Fats)
        macros_weekly = st.text_input(
            "Macros from the Weekly View (Protein/Carbs/Fats) and what your target was supposed to be. Please write it like this (Target pro 200/carbs 130/fats 100 / Actual pro 199/carbs 129/fats 120)",
            key="macros_weekly"
        )
        
        # Question 7: Weekly Calories
        weekly_calories = st.text_input(
            "Avg Weekly Calories. Please write it like this (Target calories: 2350 / Actual calories: 2442)",
            key="weekly_calories"
        )
        
        # Question 8: Waist and Bicep Measurements
        waist_bicep_measurements = st.text_input(
            "Waist Relaxed/Flexed Measurements. Bicep Flexed Measurements.",
            key="waist_bicep_measurements"
        )
        
        # Question 9: Anything you want to discuss with coach
        discuss_with_coach = st.text_area(
            "Is there anything you want to bring up or discuss with me right away?",
            key="discuss_with_coach"
        )
        
        # Question 10: Compliance to Meal Plan
        compliance = st.slider(
            "On a scale of 1-10, what was the level of your compliance to the meal plan/macros last week? 10 means perfect adherence",
            min_value=1, max_value=10, key="compliance"
        )
        
        # Question 11: Subtle Improvement
        subtle_improvement = st.text_area("What is a subtle improvement you have found on your body that you're proud of?", key="subtle_improvement")
        
        # Question 12: Missed workouts
        missed_workouts = st.text_area("Did you miss any workouts last week? If so, how many, what body part days, and why?", key="missed_workouts")
        
        # Question 13: Proud moments
        proud_moments = st.text_area("Tell me something you're PROUD that you did this week! And your biggest win, both fitness and a non-fitness aspect of your life win.", key="proud_moments")
        
        # Question 14: Improvement Goal
        improvement_goal = st.text_area("What is something you want to improve on this week?", key="improvement_goal")
        
        # Question 15: Hunger Level
        hunger_level = st.slider("On a scale of 1-10, what was your hunger level this week? 10 being starving, 1 meaning you could have easily fasted.", min_value=1, max_value=10, key="hunger_level")
        
        # Question 16: Water Intake
        water_intake = st.text_input("How much water did you drink this week on average each day? Always aim for a gallon BARE MINIMUM. Optimal would be 1.5-2 gals and curbs hunger and helps your body metabolize fat.", key="water_intake")
        
        # Question 17: Sleep hours
        sleep_hours = st.text_input("How many hours of sleep did you get per night this week on average?", key="sleep_hours")
        
        # Question 18: Previous and Current Weight
        weight = st.text_input("What was your previous and current weight this week?", key="weight")
        
        # Question 19: Goal and Accomplishment
        goal_accomplishment = st.text_area("What was your goal last week and did you accomplish it?", key="goal_accomplishment")
        
        # Question 20: Goal and Game Plan for This Week
        weekly_goal_game_plan = st.text_area("What is your goal this week and what is your game plan to accomplish it? Be specific with actionable targets to hit that I'll be holding you accountable to.", key="weekly_goal_game_plan")
        
        # Question 21: How can coach serve you better
        coach_feedback = st.text_area("Is there anything I can do as your coach to serve you better? Please put the date below as well!", key="coach_feedback")
        
        # Question 22: Upload Image
        uploaded_image = st.file_uploader("Weekly Check-In Images", type=["jpg", "jpeg", "png"], key="uploaded_image")
        
        # Submit button
        submit_button = st.form_submit_button("Submit")

    # Form submission
    if submit_button:
        st.write("### Form Submitted!")
        
        # Display all the collected responses
        form_data = {
            "Email": email,
            "Cardio Sessions": cardio_sessions,
            "Average Daily Steps": daily_steps,
            "Exercise Hate/Macro Preference": exercise_hate_or_macro,
            "Name": full_name,
            "Macros (Weekly View)": macros_weekly,
            "Weekly Calories": weekly_calories,
            "Waist/Bicep Measurements": waist_bicep_measurements,
            "Discussion with Coach": discuss_with_coach,
            "Compliance to Meal Plan": compliance,
            "Subtle Improvement": subtle_improvement,
            "Missed Workouts": missed_workouts,
            "Proud Moments": proud_moments,
            "Improvement Goal": improvement_goal,
            "Hunger Level": hunger_level,
            "Water Intake": water_intake,
            "Sleep Hours": sleep_hours,
            "Weight": weight,
            "Goal Accomplishment": goal_accomplishment,
            "Weekly Goal & Game Plan": weekly_goal_game_plan,
            "Coach Feedback": coach_feedback
        }
        
        # Display the responses for the user to review (or store them somewhere)
        for key, value in form_data.items():
            st.write(f"**{key}:** {value}")
        
        # Display the uploaded image if there is one
        if uploaded_image is not None:
            st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

if __name__ == "__main__":
    main()
