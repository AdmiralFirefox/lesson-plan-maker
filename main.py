import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() 

# Configure API Keys
genai.configure(api_key=os.getenv("API_KEY"))

# Generate course description prompt for the Gemini API
def generate_course_description(subject_name, student_year_level, subject_description):
  prompt = f"""
    Generate A Course Description 

    The name of the subject is {subject_name}

    The students are {student_year_level} level

    What I want to learn my students for this subject:
    {subject_description}

    Generate goals/objectives on what the students expect at the end of this course.
  """

  return prompt

# Generate Unit Description prompt for the Gemini API
def generate_unit_description(first_prompt, subject_unit, subject_topics):
   prompt = f"""
    Based on the following course description:
    {first_prompt}

    The subject will have {subject_unit} units only.

    The topics for each unit are {subject_topics}


    Structure your overall response into the following:

    Course Name: 

    Course Description:

    Course Goals:

    Course Structure:

    Target Audience:

    Unit 1: Topic Title
    - What are the things that needed to be discussed on this unit?
    - Create a simple activity to test the student's learning on this unit

    Unit 2: Topic Title
    - What are the things that needed to be discussed on this unit?
    - Create a simple activity to test the student's learning on this unit

    And so on. 
   """

   return prompt

def generate_unit_description_auto(first_prompt, subject_unit):
   prompt = f"""
    Based on the following course description:
    {first_prompt}

    The subject will have {subject_unit} units only.


    Structure your overall response into the following:

    Course Name: 

    Course Description:

    Course Goals:

    Course Structure:

    Target Audience:

    Unit 1: Topic Title
    - What are the things that needed to be discussed on this unit?
    - Create a simple activity to test the student's learning on this unit

    Unit 2: Topic Title
    - What are the things that needed to be discussed on this unit?
    - Create a simple activity to test the student's learning on this unit

    And so on. 
   """

   return prompt

@st.cache_data
def generate_first_response(subject_name, student_year_level, subject_description):
    # Initialize model and its configurations
    model = genai.GenerativeModel("gemini-1.5-flash")
    model.temperature = 0.8
    model.top_k = 20
    model.top_p = 0.7
    model.max_output_tokens = 500

    # Provide a prompt for generation
    prompt = generate_course_description(subject_name, student_year_level, subject_description)

    # Generate content
    response = model.generate_content([prompt])

    return response.text

@st.cache_data
def generate_second_response(specify_topics, first_prompt, subject_unit, subject_topics):
    # Initialize model and its configurations
    model = genai.GenerativeModel("gemini-1.5-flash")
    model.temperature = 0.8
    model.top_k = 20
    model.top_p = 0.7
    model.max_output_tokens = 1000

    # Provide a prompt for generation
    prompt = generate_unit_description(first_prompt, subject_unit, subject_topics) if specify_topics else  generate_unit_description_auto(first_prompt, subject_unit)

    # Generate content
    response = model.generate_content([prompt])

    return response.text


async def app():
  # Initialize states
  if "unit_topics" not in st.session_state:
      st.session_state.unit_topics = []
  
  if "generate_first_prompt" not in st.session_state:
     st.session_state.generate_first_prompt = False

  st.title("Lesson Plan Maker")
  st.write("Developed by: James Joseph L. Cuadra, BSCS 3B AI")
  st.text("")
  st.write("This is a lesson plan maker")
  st.text("")
  st.text("")

  # Inputs for course description
  subject_name = st.text_input("Enter subject name:")
  st.text("")

  student_year_level = st.selectbox(
    "What year level are your students?",
    ("1st Year", "2nd Year", "3rd Year", "4th Year"),
    index=None, placeholder="Choose year level")
  st.text("")

  subject_description = st.text_area("What do you want your students to learn on this subject:")
  st.text("")
        
  # Generate Course Description
  st.text("")
  if st.button("Generate Course Description"):
    if subject_name and student_year_level and subject_description:
        st.session_state.generate_first_prompt = True
    else:
        st.error("Fill out all the needed fields.")

  
  st.text("")
  if st.session_state.generate_first_prompt:
    first_response = generate_first_response(subject_name, student_year_level, subject_description)
    st.write(first_response)

    # After the first prompt has been generated
    if first_response:
      st.text("")
      st.text("")
      subject_unit = st.slider("How many units does your subject have?", 1, 10, 3)

      # Inputs for Unit Description
      st.text("")
      specify_topics = st.checkbox("Specify Topics (topics will be auto-generated if leaved unchecked)")
      if specify_topics:
          unit_topics = []
          for i in range(1, subject_unit + 1):
              unit_topic = st.text_input(f"Enter Topic for Unit {i}:")
              unit_topics.append(unit_topic) 

          # Update session state with unit_topics
          st.session_state.unit_topics = unit_topics

          # Check for empty topics and display info if any
          if any(topic.strip() == "" for topic in st.session_state.unit_topics):
              st.info("Fill out topics for each unit.")
      else:
          st.session_state.unit_topics = []

      # Generate Lesson Plan
      st.text("")
      if st.button("Generate Lesson Plan"):
        if subject_name and student_year_level and subject_description and subject_unit:
            if specify_topics and any(topic.strip() == "" for topic in st.session_state.unit_topics):
                st.error("Fill out all the needed fields.")
            else:
                second_response = generate_second_response(specify_topics, first_response, subject_unit, ", ".join(st.session_state.unit_topics))
                st.write(second_response)
        else:
            st.error("Fill out all the needed fields.")
    
    st.write("")
    if st.button("Clear All and Generate Another"):
        st.cache_data.clear()
        streamlit_js_eval(js_expressions="parent.window.location.reload()")


#run the app
if __name__ == "__main__":
  import asyncio
  asyncio.run(app())
