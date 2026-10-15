
import streamlit as st
from PIL import Image

# Configure the browser tab title, icon, and page layout
st.set_page_config(
    page_title="AgriSwasthya AI",
    page_icon="🌱",
    layout="centered"
)

# Display the main heading of our application
st.title("🌱 AgriSwasthya AI")

# Display a smaller heading below the main title
st.subheader("Your Smart Crop Health Assistant")

# Explain the purpose of the application to the farmer
st.write(
    "Upload a crop leaf image to begin your crop health assessment."
)

# Create a dropdown so the farmer can select the crop
# This information can later help the AI analyze the correct crop
crop = st.selectbox(
    "Select your crop",
    ["Tomato", "Potato", "Rice", "Wheat"]
)

# Create a dropdown to select the preferred language
# We will use this choice later to display guidance in that language
language = st.selectbox(
    "Choose your language",
    ["English", "Hindi"]
)

# Allow the farmer to upload an image from their device
# Only JPG, JPEG, and PNG image formats are accepted
uploaded_file = st.file_uploader(
    "Upload a leaf photograph",
    type=["jpg", "jpeg", "png"]
)

# Check whether the farmer has uploaded an image
# This prevents us from trying to process an empty upload
if uploaded_file is not None:

    # Open the uploaded image using Pillow (PIL)
    # The image object can later be passed to an AI model
    image = Image.open(uploaded_file)

    # Display the uploaded image so the farmer can verify it
    st.image(
        image,
        caption="Uploaded crop image",
        use_container_width=True
    )

    # Display the farmer's current selections
    st.write(f"Selected crop: {crop}")
    st.write(f"Selected language: {language}")

    # Create a button to start the crop analysis process
    if st.button("Analyze Crop"):

        # For now, this is only a placeholder message
        # We still need to integrate a real crop-disease AI model
        st.info(
            "Image received! AI model integration is our next step."
        )

else:
    # Ask the farmer to upload an image before proceeding
    st.info("Please upload a leaf image to get started.")