
import streamlit as st
import joblib
import numpy as np

# Load model AI
model = joblib.load('house_model.pkl')

# =========================
# GIAO DIỆN
# =========================

st.title("🏠 DỰ ĐOÁN GIÁ NHÀ")

st.write("Nhập thông tin căn nhà bên dưới")

# =========================
# INPUT
# =========================

dien_tich = st.number_input("📏 Diện tích")

phong_ngu = st.number_input("🛏️ Số phòng ngủ")

phong_tam = st.number_input("🚿 Số phòng tắm")

so_tang = st.number_input("🏢 Số tầng")

cho_dau_xe = st.number_input("🚗 Chỗ đậu xe")

duong_chinh = st.selectbox(
    "🛣️ Gần đường chính",
    ["Có", "Không"]
)

phong_khach = st.selectbox(
    "🛋️ Có phòng khách",
    ["Có", "Không"]
)

tang_ham = st.selectbox(
    "🏚️ Có tầng hầm",
    ["Có", "Không"]
)

nuoc_nong = st.selectbox(
    "♨️ Có nước nóng",
    ["Có", "Không"]
)

may_lanh = st.selectbox(
    "❄️ Có máy lạnh",
    ["Có", "Không"]
)

khu_vuc_dep = st.selectbox(
    "🌆 Khu vực đẹp",
    ["Có", "Không"]
)

noi_that = st.selectbox(
    "🪑 Nội thất",
    [
        "Đầy đủ",
        "Bán đầy đủ",
        "Không có"
    ]
)

# =========================
# CHUYỂN ĐỔI DỮ LIỆU
# =========================

def chuyen_doi(value):
    return 1 if value == "Có" else 0

duong_chinh = chuyen_doi(duong_chinh)
phong_khach = chuyen_doi(phong_khach)
tang_ham = chuyen_doi(tang_ham)
nuoc_nong = chuyen_doi(nuoc_nong)
may_lanh = chuyen_doi(may_lanh)
khu_vuc_dep = chuyen_doi(khu_vuc_dep)

day_du = 0
ban_day_du = 0

if noi_that == "Đầy đủ":
    day_du = 1

elif noi_that == "Bán đầy đủ":
    ban_day_du = 1

# =========================
# DỰ ĐOÁN
# =========================

if st.button("🔍 DỰ ĐOÁN GIÁ NHÀ"):

    data = np.array([[
        dien_tich,
        phong_ngu,
        phong_tam,
        so_tang,
        duong_chinh,
        phong_khach,
        tang_ham,
        nuoc_nong,
        may_lanh,
        cho_dau_xe,
        khu_vuc_dep,
        day_du,
        ban_day_du
    ]])

    prediction = model.predict(data)

    st.success(
        f"💰 Giá dự đoán: {prediction[0]:,.0f} VNĐ"
    )
