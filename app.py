# import streamlit as st
# import chat
#
# st.title("Serry Bot")
# st.subheader("Travel Planner for travelers")
#
# if 'generated' not in st.session_state:
#     st.session_state['generated'] = []
#
# if 'past' not in st.session_state:
#     st.session_state['past'] = []
#
#
# def main():
#     days = st.number_input("Enter the number of days", min_value=1, value=1)
#     start = st.text_input("Enter the start location")
#     end = st.text_input("Enter the end location")
#
#     mode_options = ["Planned Transportation", "Unplanned Transportation"]
#     mode = st.selectbox("Select Transportation Mode", mode_options)
#
#     theme_options = ["Chilling", "Devotional"]
#     theme = st.selectbox("Select Theme", theme_options)
#
#     output = chat.answer(days, start, end, mode, theme)
#     user_input = f"{days} days trip from {start} to {end} with {mode} transportation and theme: {theme}"
#
#     if user_input:
#         st.session_state.past.append(user_input)
#         st.session_state.generated.append(output)
#
#     if st.session_state['generated']:
#         for i in range(len(st.session_state['generated'])-1, -1, -1):
#             message(st.session_state["generated"][i], key=str(i))
#             message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
#
#
# @st.cache_resource
# def message(msg, is_user=False, key=None):
#     if is_user:
#         st.write(f"User: {msg}")
#     else:
#         st.write(f"Serry Bot: {msg}")
#
#
# if __name__ == "__main__":
#     main()
import streamlit as st
import chat
import time
st.set_page_config(layout="wide")
st.title("Less Go :)")
st.subheader("Travel Planner for travelers")
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
col1, col2 = st.columns(2)
with col1:
    with st.form(key='user_input_form', clear_on_submit=True):
        st.subheader("Hey!! Just Try")
        days = st.number_input("Number of Days", min_value=1, value=1)
        start = st.text_input("Start Location")
        end = st.text_input("End Location")
        mode_options = ["Public Transportation", "Private Transportation"]
        mode = st.selectbox("Transportation Mode", mode_options)
        submit_button = st.form_submit_button(label='Submit')
# Generate response and display in the scrollable section
with col2:
    response_section = st.empty()
    if submit_button:
        with st.spinner("Generating response..."):
            output = chat.answer(days, start, end, mode)
        styled_responses = ""
        styled_responses += f"<div style='margin-left: 20px;'>{output}</div>"
        styled_responses += "<hr/>"
        border_style_col2 = "border: 2px solid #ddd; border-radius: 8px; padding: 10px; max-height: 480px; overflow-y: scroll;"
        response_html = f"<div style='{border_style_col2}'>{styled_responses}</div>"
        st.markdown(response_html, unsafe_allow_html=True)
css = '''
<style>
section.main > div:has(~ footer ) {
    padding-bottom: 1px;
}
</style>
'''
st.markdown(css, unsafe_allow_html=True)
