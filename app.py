import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient(model="stabilityai/stable-diffusion-2-1")
cap_client = InferenceClient(model="gpt2")

st.title("Image generation with caption")

st.sidebar.title("Social Media")

if "selected_platform" not in st.session_state:
    st.session_state.selected_platform = None

if st.sidebar.button("Facebook"):
    st.session_state.selected_platform = "Facebook"

if st.session_state.selected_platform == "Facebook":
    base_prompt = "Generate a powerful and inspiring Facebook post about "
    user_prompt = st.text_area("Describe additional details:", "")

    cap_prompt = "the length of prompt should not be greater than 100 words. The post is about "

    full_prompt = base_prompt + user_prompt
    full_cap_prompt = cap_prompt + user_prompt

    if st.button("Generate Image"):
        if user_prompt:
            with st.spinner("Generating image..."):
                try:
                    image = client.text_to_image(full_prompt, guidance_scale=7.5)
                    
                    st.image(image, caption="Generated Image")
                    
                    with st.spinner("Generating caption"):
                        try:
                            caption = cap_client.text_generation(full_cap_prompt,max_new_tokens=100,temperature=0.7)
                            st.subheader("Generated Caption")
                            st.write(caption)
                        except Exception as e:
                            st.error(f"An error occurred while generating caption: {e}")
                except Exception as e:
                    st.error(f"An error occurred while generating image: {e}")
        else:
            st.warning("Please enter a prompt.")