# Essay Generator

import streamlit as st
from openai import GPT3
import autocorrect
from apa import Citations

col1, col2 = st.columns([2,4])

with col1:
    st.image("logo_kent.png")

with col2:
    st.markdown("""
                <h1 class = title1>
                    Kent Jym B. Katigbak
                </h1>
                <h4 class = subtitle1>
                    Industrial Engineer, CLSSYB, SO2, PMFC, CIFC, DSFC, Data Analyst, Python Programmer
                </h4>
                <style>
                    .title1 {
                    padding-bottom: 0rem;
                }
                    .subtitle1 {
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.write("______________________________________")

# Initialize GPT-3 model and citations object
model = GPT3(model="text-davinci-002")
citations = Citations()

# Define function to generate text
def generate_text(topic, num_words):
    response = model.generate(
        prompt=topic,
        n=num_words,
        temperature=0.5,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0,
        fine_tuning=True
    )
    # Correct grammar and spelling
    response = autocorrect.spell(response)
    
    # Extract citations from text and format them in APA style
    references = citations.extract(response)
    citations_apa = citations.format(references, "apa")
    return response, citations_apa

# Create Streamlit user interface
st.title("Essay Generator")
st.text("Enter a topic and the desired number of words:")
topic = st.text_input("Topic:")
num_words = st.number_input("Number of words:")

# Generate and display text and citations
generated_text, citations_apa = generate_text(topic, num_words)
st.text(generated_text)
st.text("Citations:")
st.text(citations_apa)


st.write("______________________________________")
st.title("Let's Connect!")

fb, linkedin, instagram, twitter = st.columns([2,2,2,2])

with fb:
    st.write("[Facebook](https://www.facebook.com/kntktgbk/)")

with linkedin:
    st.write("[LinkedIn](https://www.linkedin.com/in/kentjk/)")

with instagram:
    st.write("[Instagram](https://www.instagram.com/kentjk_/)")

with twitter:
    st.write("[Twitter](https://twitter.com/kentjk_)")
