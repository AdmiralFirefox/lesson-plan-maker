# Lesson Plan Maker

This project is designed to streamline and enhance the educational experience by leveraging the powerful capabilities of the Gemini API. This project aims to automate the creation of comprehensive and customizable lesson plans, tailored specifically for college-level courses across various disciplines. By integrating the powerful capabilities of the Gemini API, the system can analyze course objectives, learning outcomes, and available resources to generate detailed lesson plans that include lectures, assignments, and assessments. Professors can easily modify and personalize these plans to fit their teaching style and specific course requirements. This not only saves valuable time but also ensures that the educational content is structured, coherent, and aligned with academic standards. The Lesson Plan Maker supports educators in delivering high-quality and effective instruction, contributing to an enriched learning experience for students.

This project utilizes [Gemini API](https://gemini.google.com/) and deployed to [Streamlit.](https://streamlit.io/)

<br />

<div align="center">
    <strong>
        <p><a href="https://leappn-plan-maker-vs69gwzhrwzcwtfpyansry.streamlit.app/">You can view the live site here »</a></p>
    </strong>
    <strong>
        <p>Note: Please ensure fair usage of the prompts. I don't have much tokens left from the Gemini API 😅</p>
    </strong>
</div>

<br />

## Video Demo

https://github.com/AdmiralFirefox/lesson-plan-maker/assets/79429518/554b8df9-8a2a-472d-bfcc-f012df115637

<br />

## Project set-up

Clone the project
```bash
https://github.com/AdmiralFirefox/lesson-plan-maker.git
```

<br />

Install python packages
```bash
pip install -r requirements.txt
```

<br />

Run the streamlit app locally
```bash
streamlit run main.py
```

<br />

## Functionalities
* Generates a course description that provides a foundational overview of the entire course, including its goals and objectives.
* You can specify the number of Units you want to have on the created course. You can specify up to the limit of 10.
* You can specify on what will be the topic on each unit. If you don't want to specify the topic, the topics will be auto-generated. 
* A detailed lesson plan is generated based on the course description and the number of units and their topics prompted by the user. A lesson plan is structured on the following:
  - Course Name
  - Course Description 
  - Course Goals/Objectives (What would students expect when completing the course)
  - Course Structure
  - Target Audience
  - Unit Number: Topic Title
    - Things that needed to be discussed on this unit.
    - A simple activity to assess the student's learning on this unit.

<br />

## Usage Intructions

### Filling up information for Course Description

<img src="https://github.com/AdmiralFirefox/lesson-plan-maker/assets/79429518/cfe60e1c-1553-4e6e-892a-90b1ab3db5ab" alt="" width="100%" height="100%" />

- Fill up the subject name, year level of the students and a short description of what do you want your students to learn on the subject.
- After filling up the needed forms, click the Generate Course Description button.
- After clicking the button, a course description will be generated. It may take some time to generate.

<br />

### Specifying number of units

<img src="https://github.com/AdmiralFirefox/lesson-plan-maker/assets/79429518/dc7d0f65-181f-47d4-8717-e522f398358a" alt="" width="100%" height="100%" />

- Scroll down to the bottom of the generated course description, you will see a slider indicating how many units do you want to have on the subject. You can have the number of units up to the limit  of 10.
- Below the slider, you can check the checkbox if you want to specify a topic for each unit. Leave it unchecked and it will auto-generate the topics for each unit.

<br />

### Filling up the topic for each unit

<img src="https://github.com/AdmiralFirefox/lesson-plan-maker/assets/79429518/09bb83b2-4eb6-4fb8-9244-3a67be05d12d" alt="" width="100%" height="100%" />

- After checking the checkbox, fill up the topic for each unit.
- Once done, click the Generate Lesson Plan button.
- After clicking the button, it will generate a detailed lesson plan. It may take some time to generate.

<br />

### Generating another lesson plan

<img src="https://github.com/AdmiralFirefox/lesson-plan-maker/assets/79429518/bd5f0882-993a-47fc-bee1-a87a84614318" alt="" width="100%" height="100%" />

- If you want to generate another lesson plan, scroll down to the bottom of the generated lesson plan and click the Clear All and Generate Another button.

<br />


