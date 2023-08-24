import streamlit as st
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages


# To hide the sidebar of this page
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
# End of the code to hide the sidebar


show_pages([
    Page("LucidDemoApp1.py","Page1"),
    Page("LucidDemoApp2.py","Page2")
])

if st.button('Next Page'):
    switch_page('Page1')