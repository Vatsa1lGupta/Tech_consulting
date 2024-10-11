# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:55:58 2024

@author: vatsa
"""

import streamlit as st
import pandas as pd
#from openai import OpenAI
  # For AI-generated course previews and summaries
import random
import pdfplumber



import google.generativeai as genai
genai.configure(api_key="AIzaSyAr5RPuvqHfe8OHSmo2vqKHITudPIeEhhs")

model = genai.GenerativeModel("gemini-1.5-flash")



# Sample data for learners
learner_data = [
    {"name": "Vatsal Gupta", "progress": 43, "completed": 10, "total": 23},
    {"name": "Mounika", "progress": 77, "completed": 20, "total": 23},
    {"name": "Akshit", "progress": 43, "completed": 10, "total": 23},
    {"name": "Priyavrat", "progress": 23, "completed": 1, "total": 23}]

learner_reactions = {
    "angry": 0,
    "sad": 0,
    "neutral": 32,
    "happy": 86,
    "love": 144
}

latest_feedback = [
    {"name": "Andrii Zarypov", "feedback": "I have a few comments about the content. It might be improved with real cases."}
]

files = ["05 06 Reading 02 The Pyramid Principle.pdf",
         "05 06 Reading 03 Writing Clarifies Thinking.pdf",
         ]
api_key = 'AIzaSyAr5RPuvqHfe8OHSmo2vqKHITudPIeEhhs'  # Replace with your OpenAI API key


# Set up OpenAI API key
engine = "GPT-3.5"
# Function to generate AI course previews and summaries



def extract_text_from_pdf():
    texts = ""
    for file in files:
        print(file)
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                texts += page.extract_text()
    return texts
    

def generate_course_summary(course_name):
    prompt = f"Generate a brief summary for the course {course_name}, focusing on the key learning objectives."
    print("prompt", prompt)
    
    return user_name

# Function to generate personalized study materials
def generate_study_materials(user_name):
    prompt = f"Generate a personalized study guide for {user_name}, focusing on their progress and learning gaps."
    
    return user_name


# Function to provide AI-driven learning pathway
def generate_learning_pathway(user_name):
    prompt = f"Create an adaptive learning pathway for {user_name} based on their progress and future goals."
    
    return user_name
state = st.session_state


texts = extract_text_from_pdf()
#print(texts)
chat = model.start_chat(history=[])


def generate_adaptive_quiz():
    prompt = f"{texts} \n ok, read the above given text. I want you to generate an adaptive quiz of 10 questions on it . you will pass each question one by one and pass 4 options for each and capture response from the quiz taker after each question. if the answer entered is right then ask a slightly difficult question for the next one"
    print("=========================================", prompt)
    
    
    
    
    response = chat.send_message(prompt, stream=True)
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    for chunk in response:
        if chunk.text:
          st.write(chunk.text)
    
    
    
    i=1 
    prompt1 = st.chat_input("your answer:", key=i)
    with st.chat_message("quiz"):
        
        if prompt1:
            st.session_state.messages.append({"role": "user", "content": prompt1})
            with st.chat_message("user"):
               st.markdown(prompt)
            #if (prompt1 == "exit"):
            #    break
            stream = chat.send_message(prompt1, stream=True)
            
            response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
            #for chunk in response:
            #    if chunk.text:
            #      st.write(chunk.text)
        
















# Set page configuration
st.set_page_config(page_title="LMS Dashboard", layout="wide")

# Header
st.title("Ekosh LMS 2.0: Personalized AI-Driven Learning")

# Sidebar: User selection
st.sidebar.header("Student Profile")

user_name = st.sidebar.selectbox("Select Student", [learner['name'] for learner in learner_data])

page = st.sidebar.radio(
    "Navigation",
    ("Faculty Dashboard", "Learners","Program", "Calendar", "Files", "Instructors", "Assignments", "Score", "Feedback", "General", "Custom links", "Integrations", "Quick start")
)

# Display based on the selected page
if page == "Faculty Dashboard":
    st.title("Faculty Dashboard")
    
    # Columns for 'On Track' and 'Need Reminder' metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="On track", value="215", delta="Active last 3 days")
    with col2:
        st.metric(label="Need reminder", value="26", delta="Not active last 3 days")

    # Learner Progress
    st.subheader("Learner Progress")
    for learner in learner_data:
        st.write(f"{learner['name']} - {learner['progress']}% ({learner['completed']}/{learner['total']})")
    
    # Satisfaction Rate
    st.subheader("Satisfaction Rate")
    satisfaction_rate = 85
    st.metric(label="Satisfaction Rate", value=f"{satisfaction_rate}%")

elif page == "Program":
    st.title("Program Overview")
    st.write("Here you will see the course program details.")

elif page == "Calendar":
    st.title("Calendar")
    st.write("Here you will see the course calendar.")

elif page == "Files":
    st.title("Files")
    st.write("Here you will see the course files.")

elif page == "Learners":
    st.title("Learners")
    st.write("Here you will see a list of learners.")

elif page == "Instructors":
    st.title("Instructors")
    st.write("Here you will see a list of instructors.")

elif page == "Assignments":
    st.title("Assignments")
    st.write("Here you will see assignment progress.")
    # Example assignment progress
    st.write("John Doe: In Review")
    st.write("Andrii Zarypov: Submitted")
    st.write("Roman Shauk: In Review")

elif page == "Score":
    st.title("Scores")
    st.write("Here you will see the scores of learners.")

elif page == "Feedback":
    st.title("Feedback")
    st.write("Here you will see feedback from learners.")

elif page == "General":
    st.title("General Settings")
    st.write("Here you can manage general settings.")

elif page == "Custom links":
    st.title("Custom Links")
    st.write("Here you can manage custom links.")

elif page == "Integrations":
    st.title("Integrations")
    st.write("Here you can manage integrations.")

elif page == "Quick start":
    st.title("Quick Start Guide")
    st.write("Here you will see the quick start guide for learners.")






if page == "Faculty Dashboard":

    # Fetch user data
    user = next((learner for learner in learner_data if learner["name"] == user_name), None)
    
    # Columns for 'On Track' and 'Need Reminder' metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="On track", value="215", delta="Active last 3 days")
    with col2:
        st.metric(label="Need reminder", value="26", delta="Not active last 3 days")
    
    # Columns for Learner Reactions
    st.subheader("Learner Reactions")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("😡", learner_reactions["angry"], "Angry")
    col2.metric("😟", learner_reactions["sad"], "Sad")
    col3.metric("😐", learner_reactions["neutral"], "Neutral")
    col4.metric("😊", learner_reactions["happy"], "Happy")
    col5.metric("😍", learner_reactions["love"], "Love")
    
    # Learner Progress and Satisfaction Rate
    st.subheader("Learner Progress and Satisfaction")
    col1, col2 = st.columns([2, 1])
    
    # Learner Progress
    with col1:
        st.write("### Learner Progress")
        st.write(f"{user_name}'s Progress: {user['progress']}% ({user['completed']}/{user['total']} completed)")
    
    # Satisfaction Rate
    with col2:
        st.write("### Satisfaction Rate")
        satisfaction_rate = 85
        st.metric(label="Satisfaction Rate", value=f"{satisfaction_rate}%", delta="All time")
if page == "Learners":
    
    # AI-Generated Course Summary
    st.subheader("AI-Generated Course Summary")
    course_name = st.text_input("Enter the course name for summary generation:", "Google Analytics Course")
    if st.button("Generate Course Summary"):
        course_summary = generate_course_summary(course_name)
        st.write(course_summary)
    
    # Adaptive Quizzes
    st.subheader("Adaptive Quiz")
    if st.button("Generate Adaptive Quiz"):
        adaptive_quiz = generate_adaptive_quiz()
        st.write(f"Quiz Question: {adaptive_quiz['question']} (Difficulty: {adaptive_quiz['difficulty']})")
    
    # Personalized Study Materials
    st.subheader("Personalized Study Materials")
    if st.button("Generate Study Materials"):
        study_materials = generate_study_materials(user_name)
        st.write(study_materials)
    
    # Dynamic Learning Pathways
    st.subheader("AI-Driven Quick Cheat sheet")
    if st.button("Generate Cheat Sheet"):
        learning_pathway = generate_learning_pathway(user_name)
        st.write(learning_pathway)
    
    # Feedback Section
    st.subheader("Latest Feedback")
    for feedback in latest_feedback:
        st.write(f"{feedback['name']}: {feedback['feedback']}")
    
    # Footer
    st.write("---")
    st.write("Dashboard for tracking learner progress, adaptive learning, and personalized study materials in an AI-powered LMS.")
