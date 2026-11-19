
import streamlit as st
from deep_translator import GoogleTranslator

# Page configuration
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# Application title
st.title("🌍 AI Language Translation Tool")
st.write("Translate text between multiple languages easily!")

st.divider()

# Available languages
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

# Language selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

# Text input
text = st.text_area(
    "Enter text to translate:",
    placeholder="Type your text here...",
    height=150
)

# Translation button
if st.button("🌐 Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text!")

    elif source_language == target_language:
        st.warning("Please select two different languages!")

    else:
        try:
            with st.spinner("Translating..."):
                translator = GoogleTranslator(
                    source=languages[source_language],
                    target=languages[target_language]
                )

                translated_text = translator.translate(text)

            st.success("Translation completed!")

            st.subheader("Translated Text")

            st.text_area(
                "Your translation:",
                value=translated_text,
                height=150
            )

        except Exception as e:
            st.error(f"Translation failed: {e}")

st.divider()

st.caption("Developed as part of the CodeAlpha AI Internship")
