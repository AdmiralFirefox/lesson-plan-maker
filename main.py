import streamlit as st

def first_reponse_test():
   text = "First Reponse"

   return text

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
    response = first_reponse_test()
    st.write(response)

    # After the first prompt has been generated
    if response:
      st.text("")
      st.text("")
      subject_unit = st.slider("How many units does your subject have?", 1, 10, 3)

      # Inputs for Unit Description
      st.text("")
      specify_topics = st.checkbox("Specify Topics")
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
                st.write(f"The name of the subject is: {subject_name}")
                st.write(f"The student's year level are: {student_year_level}")
                st.write(f"Description: {subject_description}")
                st.write(f"Number of units: {subject_unit}")

                if st.session_state.unit_topics:
                    st.write("")
                    st.write("Topics:")
                    for i, topic in enumerate(st.session_state.unit_topics, start=1):
                        st.write(f"Topic for Unit {i}: {topic}")
        else:
            st.error("Fill out all the needed fields.")
    

#run the app
if __name__ == "__main__":
  import asyncio
  asyncio.run(app())
