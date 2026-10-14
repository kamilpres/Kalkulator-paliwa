import streamlit as st

st.title("🚗 Kalkulator paliwa")

dystans = st.number_input("Dystans w km", min_value=0.0)
spalanie = st.number_input("Spalanie l/100 km", min_value=0.0)
cena = st.number_input("Cena paliwa zł/l", min_value=0.0)

litry = (dystans / 100) * spalanie
koszt = litry * cena

st.success(f"Koszt podróży: {koszt:.2f} zł")
st.write(f"Zużycie paliwa: {litry:.2f} litrów")