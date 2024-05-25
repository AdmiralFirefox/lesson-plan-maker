import streamlit as st

async def app():
  # Initialize unit_topics list
  if "unit_topics" not in st.session_state:
      st.session_state.unit_topics = []

  st.title("Lesson Plan Maker")
  st.write("Developed by: James Joseph L. Cuadra, BSCS 3B AI")
  st.text("")
  st.write("This is a lesson plan maker... yap yap yap")
  st.text("")
  st.text("")

  # Simple Options
  subject_name = st.text_input("Enter subject name:")
  st.text("")

  subject_description = st.text_area("Brief description of the subject:")
  st.text("")

  subject_unit = st.slider("How many units does your subject have?", 1, 12, 3)
  st.text("")

  # Advance Options
  advance_options = st.checkbox("Specify Topics")
  if advance_options:
      unit_topics = []
      for i in range(1, subject_unit + 1):
          unit_topic = st.text_input(f"Enter Topic for Unit {i}:")
          unit_topics.append(unit_topic) 

      # Update session state with unit_topics
      st.session_state.unit_topics = unit_topics

      # Check for empty topics and display error if any
      if any(topic.strip() == "" for topic in st.session_state.unit_topics):
          st.info("Fill out topics for each unit.")
  else:
      st.session_state.unit_topics = []
        
  st.text("")
  st.text("")
  if st.button("Generate Response"):
    if subject_name and subject_description and subject_unit:
        if advance_options and any(topic.strip() == "" for topic in st.session_state.unit_topics):
            st.error("Fill out all the needed fields.")
        else:
            st.write(f"The name of the subject is: {subject_name}")
            st.write(f"Description: {subject_description}")
            st.write(f"Number of units: {subject_unit}")

            if st.session_state.unit_topics:
                st.write("")
                st.write("Topics:")
                for topic in st.session_state.unit_topics:
                    st.write(topic)
    else:
        st.error("Fill out all the needed fields.")

#run the app
if __name__ == "__main__":
  import asyncio
  asyncio.run(app())
