import streamlit as st

def app(df):
    # Judul halaman
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Aplikasi Rekomendasi Gaya Belajar</h1>", unsafe_allow_html=True)
    
    # Garis pemisah
    st.markdown("<hr style='border: 1px solid #f0f0f0;'>", unsafe_allow_html=True)

    # Deskripsi aplikasi
    st.markdown("""
    <div style="text-align: center; font-size: 18px;">
        Selamat datang di <strong>Aplikasi Rekomendasi Gaya Belajar</strong>! 🎓<br><br>
    </div>
    <div style="text-align: justify; font-size: 18px;">
        Aplikasi ini dirancang untuk membantu siswa atau pengguna memahami <strong>gaya belajar</strong> yang paling cocok untuk mereka — apakah itu <span style="color:#2D9CDB"><strong>Visual</strong></span>, <span style="color:#27AE60"><strong>Auditory</strong></span>, atau <span style="color:#F2994A"><strong>Kinestetik</strong></span>.<br><br>
        Dengan memberikan informasi sederhana seperti <strong>hobi</strong>, <strong>pelajaran yang disukai</strong>, dan <strong>metode belajar favorit</strong>, sistem akan memprediksi gaya belajar terbaik untuk meningkatkan efektivitas dalam proses pembelajaran. 🚀
    </div>
    """, unsafe_allow_html=True)

    # Spacer
    st.markdown("###")

    # Info box
    st.info("Aplikasi ini menggunakan Machine Learning untuk memberikan rekomendasi berdasarkan data historis siswa.")
