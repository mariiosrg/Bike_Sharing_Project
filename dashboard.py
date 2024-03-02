import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu
from babel.numbers import format_currency
sns.set(style='dark')

def create_mean_season_total_df(df):
    mean_season_total_df = df.groupby('season_label')['total_count_day'].mean().reset_index().sort_values("total_count_day",ascending=False)
    return mean_season_total_df

def create_mean_month_total_df(df):
    mean_month_total_df = df.groupby('month_label')['total_count_day'].mean().reset_index().sort_values("total_count_day",ascending=False)
    return mean_month_total_df

def create_mean_hour_total_df(df):
    mean_hour_total_df = df[df['season_label'] == 'musim_dingin'].groupby('hour')['total_count_hour'].mean().reset_index().sort_values("hour",ascending=False)
    return mean_hour_total_df

all_df = pd.read_csv("data/df_bike_cln.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://images.unsplash.com/photo-1645260820321-b9d5a513ad71?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    Selected = option_menu("Hasil Analisis Data pada df_bike",
    ["1. Bagaimana hubungan rata rata perental dengan kondisi musim ?",
    "2. Pada bulan apa rata rata kenaikan perental sepeda tertinggi dan terendah ?",
    "3. Bagaimana kenaikan rata rata perental berdasarkan jam pada musim dingin, pada jam berapa rata rata perental naik signifikan ?"])

mean_season_total_df = create_mean_season_total_df(all_df)
mean_month_total_df = create_mean_month_total_df(all_df)
mean_hour_total_df = create_mean_hour_total_df(all_df)

st.title('BIKE SHARING DASHBOARD :sparkles:')
if(Selected == "1. Bagaimana hubungan rata rata perental dengan kondisi musim ?"):
    st.subheader('Bagaimana hubungan rata rata perental dengan kondisi musim ?', divider="blue")

    
    #Membuat barchart menggunakan seaborn
    fig, ax = plt.subplots(figsize=(10, 5))

    colors = ['#72BCD4', '#d0d6c9', '#d0d6c9', '#d0d6c9']

    ax = sns.barplot(y="total_count_day", x="season_label", data=mean_season_total_df, palette = colors)
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    ax.bar_label(ax.containers[2])
    ax.bar_label(ax.containers[3])


    plt.title("Data Rata-rata rental sepeda berdasarkan musim", fontsize=15)
    plt.ylabel("Jumlah Perental")
    plt.xlabel('Jenis Musim')
    plt.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)

    st.subheader("Kesimpulan Hasil Analisis")
    st.write("""
        Hubungan antara perental sepeda dengan kondisi musim 
        sangat berpengaruh dikarenakan pada hasil analisis 
        terlihat bahwa musim gugur memiliki nilai tertinggi 
        dan musim semi terendah. dengan demikian musim dapat 
        mempengaruhi rata rata perental sepeda karena faktor suhu 
        dan udara yang dapat mempengaruhi kenyamanan seorang berkendara sepeda diluar.
    """)

if(Selected == "2. Pada bulan apa rata rata kenaikan perental sepeda tertinggi dan terendah ?"):
    st.subheader('Pada bulan apa rata rata kenaikan perental sepeda tertinggi dan terendah ?', divider="red")

    
    #Membuat barchart menggunakan seaborn
    fig, ax = plt.subplots(figsize=(15,6))

    ax = sns.barplot(x='month_label', y='total_count_day', data= mean_month_total_df)
    ax.bar_label(ax.containers[0])

    plt.xlabel("Bulan")
    plt.ylabel("Rata - Rata")
    plt.title("Data Rata-rata rental sepeda (Bulan)")

    st.pyplot(fig)

    st.subheader("Kesimpulan Hasil Analisis")
    st.write("""Bulan june, september, dan agustus menjadi 
    bulan dengan rata rata perental yang tertinggi dibandingkan 
    dengan bulan januari, februari, dan desember. ini dipengaruhi 
    oleh suhu dan udara. dan juga merupakan bulan transisi musim
    """)

if(Selected == "3. Bagaimana kenaikan rata rata perental berdasarkan jam pada musim dingin, pada jam berapa rata rata perental naik signifikan ?"):
    st.subheader('Bagaimana kenaikan rata rata perental berdasarkan jam pada musim dingin, pada jam berapa rata rata perental naik signifikan ?', divider="violet")

    
    #Membuat barchart menggunakan seaborn
    fig, ax = plt.subplots(figsize=(20, 6)) 
    plt.plot(mean_hour_total_df["hour"], mean_hour_total_df["total_count_hour"], marker='o', linewidth=2, color="#72BCD4") 
    plt.title("Data Rata-rata rental sepeda untuk setiap jam pada musim dingin", fontsize=15)
    plt.ylabel("Jumlah Perental")
    plt.xlabel('Jam')
    plt.xticks(fontsize=10) 
    plt.yticks(fontsize=10) 
    plt.xticks(range(24), [f'{h:02d}:00' for h in range(24)])
    st.pyplot(fig)

    st.subheader("Kesimpulan Hasil Analisis")
    st.write("""Kenaikan terjadi diantara jam 06.00 hingga jam 08.00 pagi, 
    lalu pada sore harinya terlihat kenaikan pada jam 15.00 hingga jam 17.00 sore. 
    ini terjadi dikarenakan pada jam tersebut bukan jam bekerja sehingga banyak warga 
    yang menyewakan sepeda untuk menikmati alam sebelum atau sesudah mereka bekerja dan 
    tak lain juga karena suhu dan kenyamanan berkendara
    """)


