
import streamlit as st
import joblib
import numpy as np

# LOAD MODEL
model = joblib.load("house_model.pkl")

# TITLE
st.title("🏠 DỰ ĐOÁN GIÁ NHÀ BẰNG AI")

st.write("Nhập thông tin căn nhà để dự đoán giá")

# INPUT

area = st.number_input("Diện tích", min_value=0)

bedrooms = st.number_input("Số phòng ngủ", min_value=0)

bathrooms = st.number_input("Số phòng tắm", min_value=0)

stories = st.number_input("Số tầng", min_value=0)

mainroad = st.selectbox(
    "Gần đường chính",
    [1, 0]
)

guestroom = st.selectbox(
    "Có phòng khách",
    [1, 0]
)

basement = st.selectbox(
    "Có tầng hầm",
    [1, 0]
)

hotwaterheating = st.selectbox(
    "Có nước nóng",
    [1, 0]
)

airconditioning = st.selectbox(
    "Có máy lạnh",
    [1, 0]
)

parking = st.number_input(
    "Số chỗ đậu xe",
    min_value=0
)

prefarea = st.selectbox(
    "Khu vực ưu tiên",
    [1, 0]
)

# NỘI THẤT
furnished = st.selectbox(
    "Full nội thất",
    [1, 0]
)

semi_furnished = st.selectbox(
    "Bán nội thất",
    [1, 0]
)

# PREDICT
if st.button("🔍 DỰ ĐOÁN GIÁ NHÀ"):

    data = [[
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnished,
        semi_furnished
    ]]

    prediction = model.predict(data)

    # Đổi sang tỷ VNĐ
    price_billion = prediction[0] / 1000000

    st.success(
        f"🏠 Giá dự đoán: {price_billion:.2f} tỷ VNĐ"
    )
