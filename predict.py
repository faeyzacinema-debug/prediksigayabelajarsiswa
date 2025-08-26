import streamlit as st
import pickle
from web_function import predict


# (This duplicate app function should be removed to avoid redefinition)

def app(df, x, y):
    st.title("🔮 Halaman Prediksi Gaya Belajar")

    st.markdown("""
        <p style="font-size: 18px;">
        Silakan pilih data berikut sesuai dengan preferensi kamu, dan sistem akan memprediksi gaya belajar terbaik: 
        </p>
    """, unsafe_allow_html=True)

    # Ambil daftar pilihan dari encoder
def app(df, x, y):
    st.title("🔮 Halaman Prediksi Gaya Belajar")

    # Load encoders
    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)

    le_hobi = encoders["hobi"]
    le_pelajaran = encoders["pelajaran"]
    le_metode = encoders["metode"]

    st.markdown("""
        <p style="font-size: 18px;">
        Silakan pilih data berikut sesuai dengan preferensi kamu, dan sistem akan memprediksi gaya belajar terbaik: 
        </p>
    """, unsafe_allow_html=True)
    hobi_options = le_hobi.classes_.tolist()
    pelajaran_options = le_pelajaran.classes_.tolist()
    metode_options = le_metode.classes_.tolist()

    # Tambahkan input widget untuk user
    Hobi = st.selectbox("Apa Hobimu?", hobi_options)
    Pelajaran_Suka = st.selectbox("Pelajaran yang kamu sukai?", pelajaran_options)
    Metode_belajar = st.selectbox("Metode Belajar yang kamu pilih?", metode_options)

    if st.button("Prediksi"):
        try:
            # Validasi input sebelum transformasi
            if Hobi not in le_hobi.classes_:
                st.error("Hobi yang dipilih tidak dikenali. Silakan pilih dari daftar yang tersedia.")
                return
            if Pelajaran_Suka not in le_pelajaran.classes_:
                st.error("Pelajaran yang dipilih tidak dikenali. Silakan pilih dari daftar yang tersedia.")
                return
            if Metode_belajar not in le_metode.classes_:
                st.error("Metode belajar yang dipilih tidak dikenali. Silakan pilih dari daftar yang tersedia.")
                return

            # Encode input user dengan LabelEncoder
            hobi_encoded = le_hobi.transform([Hobi])[0]
            pelajaran_encoded = le_pelajaran.transform([Pelajaran_Suka])[0]
            metode_encoded = le_metode.transform([Metode_belajar])[0]

            features = [hobi_encoded, pelajaran_encoded, metode_encoded]

            prediction, score = predict(x, y, features)

            st.info("Prediksi Sukses")

            if prediction == 0:
                st.success("Siswa memiliki gaya belajar Visual")
            elif prediction == 1:
                st.success("Siswa memiliki gaya belajar Auditory")
            else:
                st.success("Siswa memiliki gaya belajar Kinestetik")

            st.write("Prediksi memiliki tingkat akurasi ", round(score * 100, 2), "%")
        except ValueError:
            st.error("Input tidak dikenali oleh model. Pastikan sesuai data saat training.")