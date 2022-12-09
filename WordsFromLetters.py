import streamlit as st
from itertools import permutations

st.title("Word Generator from Input Letters")
st.subheader("Simply type all the letters in lower case. There should be no space, comma, or any unnecessary symbols.")

def get_words(letters):
    # Create a list of all possible permutations of the letters
    perms = [''.join(p) for p in permutations(letters)]

    # Open the dictionary file and read all words into a list
    with open('dictionary.txt') as f:
        words = [line.strip() for line in f]

    # Filter the list of permutations to only include words that are in the dictionary
    return [perm for perm in perms if perm in words]

st.title('English Word Generator')

# Get the letters from the user
letters = st.text_input('Enter the letters:')

# If the user entered any letters, generate the words and display them
if letters:
    words = get_words(letters)
    st.write(words)
