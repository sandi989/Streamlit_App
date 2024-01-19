import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.write(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    """,
    unsafe_allow_html=True
)

PAGE_TITLE = "CV | Sandi Hendrawan"
NAMA = 'SANDI HENDRAWAN'
DESKRIPSI = 'Perkenalkan saya Sandi Hendrawan, saya merupakan lulusan dari Universitas Atma Jaya Yogyakarta program studi Informatika yang memiliki kemampuan dalam query pada database, data science, dan PHP.'
EMAIL = 'sandi898hendrawan'
SOCIAL_MEDIA = {
    'LinkedIn' : 'https://www.linkedin.com/in/sandi-hendrawan-290041216/',
    'GitHub' : 'https://github.com/sandi989',
    'Instagram': 'https://www.instagram.com/sandi898/',
}
KONTAK= ''' 
    - Jl. Bromantakan no.16, Punggawan, Surakarta
    - sandi898hendrawan@gmail.com
    - sandi898
    '''
PENDIDIKAN  = {
    'SMA Regina Pacis Surakarta' : 2017,
    'Universitas ATMA JAYA Yogyakarta' : 2018-2023
}
SKILL = {'SQL', 'Python', 'PHP', 'Javascript', 'Visualization', 'Power BI '}

col1, col2 = st.columns([1,2], gap="small")

with col1:
    st.image("image.png", width=230)

with col2:
    st.title(NAMA)
    st.markdown(DESKRIPSI)
    st.divider()

with st.container():
    st.write('#')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

with st.container():
    st.write('#')
    st.subheader('CONTACT')
    col0, col1,col2= st.columns([1, 1, 20])

    col1.write('<i class="fa fa-home"></i>', unsafe_allow_html=True)
    col2.write('Jl. Bromantakan no.16, Punggawan, Surakarta')

    col1.write('<i class="fa fa-whatsapp"></i>', unsafe_allow_html=True)
    col2.write('082136228481')

    col1.write('<i class="fa fa-envelope"></i>', unsafe_allow_html=True)
    col2.write('sandi898hendrawan@gmail.com')

    col1.write('<i class="fa fa-instagram"></i>', unsafe_allow_html=True)
    col2.write('@sandi898')

# st.write('#')
st.divider()


with st.container():
    st.subheader('PENDIDIKAN')
    with st.container():
        col0,col1,col2, col3 = st.columns([1, 1, 6,20])
        col1.text('✔')
        col2.text('2017')
        col3.text('SMA Regina Pacis Surakarta')

    with st.container():
        col0,col1,col2, col3 = st.columns([1,1,6,20])
        col1.text('✔')
        col2.text('2018 - 2023')
        col3.text('Universitas ATMA JAYA Yogyakarta')

# st.write('#')
st.divider()

with st.container():
    st.subheader('SKILL')
    col1, col2 = st.columns([1, 20]) 
    with col2:
        for i in SKILL:
            st.text(f'➤ {i}')

# st.write('#')
st.divider()
with st.container():
    st.subheader('PENGALAMAN ORGANISASI')
    with st.container():
        col1,col2 = st.columns([1, 20])
        col2.text('➤ Anggota Kelompok Studi Linux UAJY Tahun Periode 2018/2019')
        col2.text('➤ Pengurus Kelompok Studi Linux UAJY Tahun Periode 2019/2020')



