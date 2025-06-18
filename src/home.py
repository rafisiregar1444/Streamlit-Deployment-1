import pandas as pd
import streamlit as st # type: ignore

def home():    
    # judul
    st.title("Deteksi Potensi Resign Karyawan Menggunakan Machine Learning")
    st.markdown("---")
    
    # deskripsi
    st.markdown("## Latar Belakang")
    st.markdown(''' 
    Attrition atau pengunduran diri karyawan merupakan tantangan besar bagi banyak perusahaan. Hal ini dapat meningkatkan biaya rekrutmen, hilangnya pengetahuan dan pengalaman, serta dapat menurunkan moral karyawan yang masih bertahan. Oleh karena itu, sangat penting untuk memprediksi potensi resign ini, agar perusahaan dapat melakukan langkah-langkah pencegahan yang tepat, seperti meningkatkan kebijakan retensi dan kepuasan kerja.
    
    Dalam proyek ini, saya sebagai seorang data scientist bertugas untuk membuat model machine learning yang dapat memprediksi apakah seorang karyawan berisiko untuk resign berdasarkan data historis yang ada di perusahaan. Model ini akan digunakan untuk mengidentifikasi karyawan yang berisiko resign dan membantu perusahaan untuk meningkatkan retensi mereka.
    ''')
    st.markdown("---")

    st.markdown("## Rumusan Masalah")
    st.markdown('''           
    Dalam waktu tiga bulan ini, saya harus mengembangkan sebuah model machine learning untuk memprediksi potensi resign karyawan berdasarkan data historis yang ada. Fokus utama adalah pada nilai recall yang tinggi untuk memastikan akurasi dalam memprediksi karyawan yang berisiko resign, dengan tingkat kepercayaan 99%. Hal ini sangat penting karena dalam konteks dunia kerja, akurasi tinggi sangat dibutuhkan agar perusahaan bisa mengambil langkah yang tepat.
    ''')
    
    st.markdown("---")

    # dataset
    st.markdown("## Dataset")
    data_karyawan = pd.read_csv('src/P1M2_rafi_siregar.csv')  # Sesuaikan nama file dataset
    st.dataframe(data_karyawan.head(5))

    st.markdown("---")

    # data overview
    st.markdown("## Data Overview", unsafe_allow_html=True)

    st.markdown("""
        ### Data Overview

        | **Kolom**                | **Penjelasan**                                                                                         |
        |--------------------------|--------------------------------------------------------------------------------------------------------|
        | **Age**                  | Usia karyawan dalam tahun.                                                                              |
        | **Gender**               | Jenis kelamin karyawan: `Male` (Laki-laki), `Female` (Perempuan).                                       |
        | **Years at Company**     | Jumlah tahun yang telah dihabiskan karyawan di perusahaan.                                              |
        | **Monthly Income**       | Pendapatan bulanan karyawan dalam dolar.                                                               |
        | **Job Role**             | Peran atau jabatan yang dijalani karyawan dalam perusahaan.                                            |
        | **Work-Life Balance**    | Penilaian terhadap keseimbangan kerja dan kehidupan pribadi karyawan.                                   |
        | **Job Satisfaction**     | Tingkat kepuasan karyawan terhadap pekerjaan mereka.                                                    |
        | **Performance Rating**   | Penilaian kinerja karyawan oleh perusahaan.                                                            |
        | **Overtime**             | Status apakah karyawan bekerja lembur: `Yes`/`No`.                                                     |
        | **Number of Promotions** | Jumlah promosi yang telah diterima oleh karyawan.                                                      |
        | **Distance from Home**   | Jarak tempat tinggal karyawan dengan tempat kerja dalam mil.                                           |
        | **Education Level**      | Tingkat pendidikan terakhir karyawan.                                                                  |
        | **Marital Status**       | Status pernikahan karyawan: `Married`, `Single`, `Divorced`.                                           |
        | **Number of Dependents** | Jumlah tanggungan yang dimiliki karyawan.                                                              |
        | **Job Level**            | Tingkatan jabatan karyawan di perusahaan: `Mid`, `Entry`, `Senior`.                                    |
        | **Company Size**         | Ukuran perusahaan: `Large`, `Medium`, `Small`.                                                         |
        | **Remote Work**          | Apakah karyawan bekerja dari jarak jauh: `Yes`/`No`.                                                   |
        | **Leadership Opportunities** | Kesempatan untuk memimpin dalam perusahaan: `Yes`/`No`.                                           |
        | **Innovation Opportunities** | Kesempatan untuk berinovasi dalam perusahaan: `Yes`/`No`.                                           |
        | **Company Reputation**   | Reputasi perusahaan di mata karyawan: `Excellent`, `Good`, `Fair`, `Poor`.                             |
        | **Employee Recognition** | Penghargaan yang diberikan kepada karyawan atas pencapaian mereka: `Very High`, `High`, `Medium`, `Low`. |
        | **Attrition**            | Status apakah karyawan tetap bertahan atau mengundurkan diri: `Yes`/`No`.                              |
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Model yang digunakan
    st.markdown("## Algoritma yang Digunakan dalam Pemodelan")
    st.markdown(''' 
                Dalam penelitian ini, algoritma **Gradient Boosting** digunakan karena performanya yang sangat baik dalam mengatasi permasalahan klasifikasi. Dengan nilai recall train sebesar 77%, model ini dapat memprediksi potensi resign karyawan dengan akurasi yang tinggi, membantu perusahaan untuk meningkatkan kebijakan retensi mereka.
                ''')
    
    st.markdown("---")


if __name__ == "__main__":
    home()
