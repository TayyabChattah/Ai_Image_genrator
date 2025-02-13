import streamlit as st
import gradio_client as gc

st.title("Ai image genrator")




client=gc.Client("black-forest-labs/FLUX.1-dev")

prompt=st.sidebar.text_area("Enter your prompt here: ","")

GenrateImage=st.sidebar.button("Genrate Image")

if GenrateImage:
    if prompt:
        result=client.predict(
            prompt=prompt,
            seed=0,
            randomize_seed=True,
            width=512,
            height=512,
            num_inference_steps=4,
            api_name="/infer"

        )



