import RestaurantGen as rg
import streamlit as st
import difflib

st.title("Foodie Navigator")

with st.sidebar:
    user_destination_country = st.selectbox("Which country are you traveling to?✨",
                                                ("Germany", "Switzerland", "Japan", "Italy", "Greece", "Seychelles", "France", "Spain", "Thailand", "Mexico", "Brazil", "UAE"))
    
    user_output_language = st.sidebar.selectbox(
    "What is your desired translation language?",
    ("French", "Polish", "English", "Ukrainian", "German", "Spanish", "Italian", "Greek", "Japanese", "Thai", "Chinese", "Portuguese", "Arabic"))

food_suggestions = ["Sushi", "Pizza", "Croissant", "Tacos", "Paella", "Pasta Carbonara", "Ramen", "Biryani", "Pho", "Moussaka", "Baguette", "Peking Duck", "Spaghetti", "Dumplings"]

def automplete_food(input_text, food_list):
    if not input_text:
        return []
    matches = difflib.get_close_matches(input_text, food_list, n=3, cutoff=0.3)
    return matches

# Get user food input
user_food = st.text_input("What food delicacy would you like to try?😊")
suggested_foods = automplete_food(user_food, food_suggestions)

if suggested_foods:
    st.info(f"Did you mean: **{', '.join(suggested_foods)}**?")

with st.form("Food_form"):
    user_phrase = st.text_area(label="What phrase would you like to translate?")
    submit_button = st.form_submit_button("Send")

if submit_button:
    if (user_destination_country and user_food) or (user_output_language and user_phrase):
        response = rg.restaurant_recommendations(user_destination_country, user_food, user_output_language, user_phrase)
        st.write(response)
    else:
        st.warning("Please provide all details before submitting")
