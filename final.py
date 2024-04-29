import streamlit as st
import os
import pandas as pd

st.set_page_config(
    page_title="CSE 6431 final",
    page_icon="📊",
    layout="wide",
)

st.title("MacBook Pro I/O Device Obsolescence")

sales_data = {
    "Product": ["Apple 60W MagSafe 2 Power Adapter", "Apple 85W MagSafe 2 Power Adapter", "Apple USB SuperDrive", "Apple USB-C to SD Card Reader", "SUM"],
    "Sales": ["116,591", "281,241", "29,621", "40,875", "468,328"]
}

df = pd.DataFrame(sales_data)

st.header("Sales Data for Apple Accessories on Amazon")
st.markdown(df.to_html(index=False, justify='left'), unsafe_allow_html=True)
st.title("")
option_to_images = {
    "Apple USB SuperDrive": ["superdrive.png", "Apple_USB_SuperDrive.png"],
    "Apple USB Ethernet Adapter": ["ethernet_adapter.png"],
    "Apple USB-C to SD Card Reader": ["sd_card_reader.png", "Apple_USB-C_to_SD_Card_Reader.png"],
    "Apple MagSafe 2 Power Adapter": ["magsafe_power_adapter.png", "Apple_60W_MagSafe_2_PowerAdapter.png", "Apple_85W_MagSafe_2_PowerAdapter.png", "Apple_MagSafe_2_Power_Adapter_2lines.png", "Apple_MagSafe_2_Power_Adapter_comb.png"]
}
st.header("Apple Accessories that will become obsolete")
selected_option = st.selectbox('Select the I/O device', list(option_to_images.keys()))

image_filenames = option_to_images[selected_option]

col1, col2 = st.columns(2)

with col1:
    st.header("I/O device Information")
    image_path_1 = os.path.join('pic', image_filenames[0])
    if os.path.exists(image_path_1):
        st.image(image_path_1, caption=selected_option)
    else:
        st.write(f"Picture {image_filenames[0]} not found.")

with col2:
    st.header("Sales History")
    for i, image_filename in enumerate(image_filenames[1:]):
        image_path = os.path.join('pic', image_filename)
        if os.path.exists(image_path):
            st.image(image_path, caption=None)
        else:
            st.write(f"Picture {image_filename} not found.")
    if len(image_filenames) == 1:
        st.write(f"There is no data for the product.")