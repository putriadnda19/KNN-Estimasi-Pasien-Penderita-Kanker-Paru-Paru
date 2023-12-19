import pickle
import streamlit as st

model = pickle.load(open('estimasi_paru-paru.sav', 'rb'))

st.title('Estimasi Pasien Yang Terkena Penyakit Kanker Paru-Paru')

AGE = st.number_input('Input Usia Pasien')
SMOKING = st.number_input('Input Pasien Merokok atau Tidak')
YELLOW_FINGERS = st.number_input('Input Jumlah Gula')
ANXIETY = st.number_input('Input Jumlah Kolestrol')
PEER_PRESSURE = st.number_input('Input Jumlah Sodium')
CHRONIC_DISEASE = st.number_input('Input Jumlah Kalori')
WHEEZING = st.number_input('Input Jumlah Karbohidrat')
ALCOHOL_CONSUMING = st.number_input('Input Jumlah Karbohidrat')
COUGHING = st.number_input('Input Jumlah Karbohidrat')
SHORTNESS_OF_BREATH = st.number_input('Input Jumlah Karbohidrat')
SWALLOWING_DIFFICULTY = st.number_input('Input Jumlah Karbohidrat')
CHEST_PAIN = st.number_input('Input Jumlah Karbohidrat')

predict = ''

if st.button('Estimasi: '):
    predict = model.predict(
        [[AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]]
    )
    st.write('Estimasi Apakah Pasien Terkena Penyakit Kanker Paru-Paru? : ', predict)