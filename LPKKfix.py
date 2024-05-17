import streamlit as st
import requests
import base64
import pandas as pd

from streamlit_lottie import st_lottie  

def img_to_base64(image_path):
    """Convert image to base64"""
    with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    
    # Import gambar & konversi ke base64
img_path = "imgs/icon_aka.png"  
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" style="width: 100%; height: auto;">',
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
st.sidebar.header("~~~ PROJECT LPK ~~~")

# Pilihan konten menggunakan selection box
selected_content = st.sidebar.radio(
        "Pilih yukk 👐:",
        ["Home", "Konfigurasi Elektron", "Periode & Golongan", "Our Group"],
    )

    # Tampilkan konten terkait
if selected_content == "Home":
    st.title ("Aplikasi Konfigurasi Elektron")

    # Pembuatan 2 kolom
    col1, col2 = st.columns([2, 1])

    with col1 :
    # file json format (File path)
        lottie_url = "https://lottie.host/71414735-9c10-46df-933d-79b410ef1f45/JsDJjvFBb3.json"

    # Fungsi untuk memproses lottie url
    def load_lottie_url(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Memproses animasi lottie
    lottie_json = load_lottie_url(lottie_url)

    # Menampilkan animasi lottie
    with col2 :
        if lottie_json is not None:
            st_lottie(lottie_json)
        else:
            st.write("Failed to load Lottie animation.")

    with col1 :
        st.write("Konfigurasi elektron adalah susunan atau gambaran yang menunjukan penempatan elektron dalam suatu atom. Susunan elektron-elektron tersebut berdasarkan kulit atau orbital. Melalui Konfigurasi Elektron kita dapat mengetahui golongan dan periode dari suatu atom. Golongan tersebut ditunjukkan oleh jumlah elektron terluar (elektron valensi), dan periode ditunjukkan oleh nomor kulit terbesar pada isi elektron (kulit terluar). Adapun jenis konfigurasi elektron subkulit(kuantum), bersifat lebih kompleks dibandingkan konfigurasi elektron kulit. Konfigurasi ini menekankan pada kebolehjadian ditemukan elektron pada tingkat subkulit atom. Di tingkat subkulit, terdapat orbital yaitu tempat yang mungkin ditempati oleh elektron. Orbital dibagi menjadi empat, yaitu orbital s, p, d, dan f.")

if selected_content == "Konfigurasi Elektron":
    # Electron configuration for atoms
    electron_config = {
        "Hidrogen[H]": "1s1",
        "Helium[He]": "1s2",
        "Lithium[Li]": "1s2 2s1",
        "Berilium[Be]": "1s2 2s2",
        "Boron[B]": "1s2 2s2 2p1",
        "Karbon[C]": "1s2 2s2 2p2",
        "Nitrogen[Ni]": "1s2 2s2 2p3",
        "Oksigen[O]": "1s2 2s2 2p4",
        "Fluorin[F]": "1s2 2s2 2p5",
        "Neon[Ne]":"1s2 2s2 2p6",
        "Natrium[Na]":"1s2 2s2 2p6 3s1",
        "Magnesium[Mg]":"1s2 2s2 2p6 3s2",
        "Aluminium[Al]":"1s2 2s2 2p6 3s2 3p1",
        "Silikon[Si]":"1s2 2s2 2p6 3s2 3p2",
        "Fosforus[P] ":"1s2 2s2 2p6 3s2 3p3",
        "Belerang[S]": "1s2	2s2	2p6	3s2	3p4",
        "Klorin[Cl]":"1s2 2s2 2p6 3s2 3p5",
        "Argon[Ar]":"1s2 2s2 2p6 3s2 3p6",
        "Kalium[K]":"1s2 2s2 2p6 3s2 3p6 4s1",
        "Kalsium[Ca]":"1s2 2s2 2p6 3s2 3p6 4s2",
        "Skandium[Sc]":"1s2	2s2	2p6	3s2	3p6 3d1 4s2",
        "Titanium[Ti]":"1s2	2s2	2p6	3s2	3p6	3d2	4s2",
        "Vanadium[V]":"1s2 2s2 2p6 3s2 3p6 3d3 4s2",
        "Kromium[Cr]":"1s2 2s2 2p6 3s2 3p6 3d5 4s1",
        "Mangan[Mn]":"1s2 2s2 2p6 3s2 3p6 3d5 4s2",
        "Besi[Fe]":"1s2 2s2	2p6	3s2	3p6	3d6	4s2",
        "Kobalt[Co]":"1s2 2s2 2p6 3s2 3p6 3d7 4s2",
        "Nikel[Ni]":"1s2 2s2 2p6 3s2 3p6 3d8 4s2",
        "Tembaga[Cu]":"1s2 2s2 2p6 3s2 3p6 3d10 4s1",
        "Seng[Zn]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2",
        "Galium[Ga]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2	4p1",
        "Germanium[Ge]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p2",
        "Arsenik[As]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p3",
        "Selenium[Se]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p4",
        "Bromin[Br]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p5",
        "Kripton[Kr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
        "Rubidium[Rb]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 5s1",
        "Stronsium[Sr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s2",
        "Ittrium[Y]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d1 5s2",
        "Zirkonium[Zr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d2 5s2",
        "Niobium[Nb]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d4 5s1",
        "Molibdenum[Mo]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1",
        "Teknisium[Tc]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s2",
        "Rutenium[Ru]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d7 5s1",
        "Rodium[Rh]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d8 5s1",
        "Paladium[Pd]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10",
        "Perak[Ag]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s1",
        "Kadmium[Cd]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2",
        "Indium[In]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p1",
        "Timah[Sn]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p2",
        "Antimon[Sn]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 5s2 5p3",
        "Telurium[Te]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 5s2 5p4",
        "Iodin[I]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 5s2 5p5",
        "Xenon[Xe]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6",
        "Cesium[Cs]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2	5p6 6s1",
        "Barium[Ba]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2	5p6 6s2",
        "Lantanum[La]":"1s2 2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 5s2 5p6 5d1 6s2",
        "Cerium[Ce]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f1	5s2	5p6	5d1 6s2",
        "Praseodymium[Pr]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f3 5s2 5p6 6s2",
        "Neodymium[Nd]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f4 5s2 5p6 6s2",
        "Promotium[Pm]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f5 5s2 5p6 6s2",
        "Samarium[Sm]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f6 5s2 5p6 6s2",
        "Europium[Eu]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f7 5s2 5p6 6s2",
        "Gadolinium[Gd]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f7 5s2 5p6 5d1 6s2",
        "Terbium[Tb]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f9 5s2 5p6 6s2",
        "Dysprosium[Dy]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f10 5s2 5p6 6s2",
        "Holmium[Ho]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f11 5s2 5p6 6s2",
        "Erbium[Er]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f12 5s2 5p6 6s2",
        "Thulium[Tm]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f13 5s2 5p6 6s2",
        "Ytterbium[Yb]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6 6s2",
        "Lutesium[Lu]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d1 6s2",
        "Hafnium[Hf]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d2 6s2",
        "Tantalum[Ta]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d3 6s2",
        "Wolfram[W]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d4 6s2",
        "Rhenium[Re]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d5 6s2",
        "Osmium[Os]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d6 6s2",
        "Iridium[Ir]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d7 6s2",
        "Platina[Pt]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d9 6s1",
        "Emas[Au]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	6s1",
        "Raksa[Hg]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 6s2",
        "Talium[Tl]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 6s2 6p1",
        "Timbal[Pb]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 6s2 6p2",
        "Bismut[Bi]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 6s2 6p3",
        "Polonium[Po]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	6s2	6p4",
        "Astatin[At]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	6s2	6p5",
        "Radon[Rn]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 6s2 6p6",
        "Fransium[Fr]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	6s2	6p6	7s1",
        "Radium[Ra]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 6s2 6p6 7s2",
        "Aktinium[Ac]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2	6p6	6d1	7s2",
        "Torium[Th]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 6s2 6p6 6d2 7s2",
        "Protaktinium[Pa]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	5f2	6s2	6p6	6d1	7s2	",
        "Uranium[U]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 5f3 6s2 6p6 6d1 7s2",
        "Neptunium[Np]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 5f4 6s2 6p6 6d1 7s2",
        "Plutonium[Pu]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f6 6s2 6p6 7s2",
        "Americium[Am]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 5f7 6s2 6p6 7s2",
        "Curium[Cm]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 5f7 6s2 6p6 6d1 7s2",
        "Berkelium[Bk]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 5f9 6s2 6p6 7s2",
        "Californium[Cf]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d10 5f10	6s2	6p6	7s2",
        "Einsteinium[Es]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f11 6s2 6p6 7s2",
        "Fermium[Fm]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d10 5f12 6s2	6p6 7s2",
        "Mendelevium[Md]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d10 5f13 6s2	6p6 7s2",
        "Nobelium[No]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	5f14 6s2 6p6 7s2",
        "Lawrencium[Lr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 5f14 6s2 6p6 7s2 7p1",
        "Rutherfordium[Rf]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 5f14 6s2 6p6 6d2 7s2",
        "Dubnium[Db]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d10 5f14 6s2	6p6	6d3 7s2",
        "Seaborgium[Sg]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d4 7s2",
        "Bohrium[Bh]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d10 5f14 6s2	6p6	6d5	7s2",
        "Hassium[Hs]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d10 5f14 6s2	6p6	6d6 7s2",
        "Meitnerium[Mt]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d7 7s2",
        "Darmstadtium[Ds]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	5f14 6s2 6p6 6d8 7s2",
        "Roentgenium[Rg]":"1s2 2s2 2p6 3s2 3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	5f14 6s2 6p6 6d9 7s2",
        "Copernicium[Cn]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d10 5f14 6s2	6p6	6d10 7s2",
        "Nihonium[Uut]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 5f14 6s2 6p6 6d10 7s2 7p1",
        "Flerovium[Fl]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 5f14 6s2 6p6 6d10 7s2 7p2",
        "Moskovium[Uup]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10	4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2	7p3",
        "Livermorium[Lv]":"1s2 2s2 2p6 3s2 3p6 3d10	4s2	4p6	4d10 4f14 5s2 5p6 5d10 5f14 6s2	6p6	6d10 7s2 7p4",
        "Tenesis[Uus]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10	5f14 6s2 6p6 6d10 7s2 7p5",
        "Oganeson[Uuo]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14	5s2	5p6	5d10 5f14 6s2 6p6 6d10 7s2 7p6",
    }

    st.title("Electron Configuration")
    st.write("Select an atomic number:")

    atomic_number = st.selectbox("Atomic Name", list(electron_config.keys()))

    if st.button("Kirim"):
        st.write("Electron Configuration :", electron_config[atomic_number])
        
        
if selected_content == "Periode & Golongan":
    
        # Load atomic data from CSV
    atomic_df = pd.read_csv("Data_atom.csv", index_col="name")

    def search_atomic_data(atomic_name):
        """Search for atomic data based on atomic name."""
        return atomic_df.loc[atomic_name] if atomic_name in atomic_df.index else None

    # Streamlit app
    def main():
        st.title("Atomic Data Search")

        # Selectbox for atomic names
        search_name = st.selectbox("Select an atomic name:", atomic_df.index.tolist())

        # Search for atomic data
        result = search_atomic_data(search_name)

        # Display result if found
        if st.button("Search"):
            if result is not None:
                st.success(f"Atomic Name : {search_name}")
                st.success(f"Periode : {result['periode']}")
                st.success(f"Golongan : {result['golongan']}")
            elif search_name:
                st.error("Atomic name not found in the database.")

    if __name__ == "__main__":
        main()

    st.image('imgs/atomic_table.jpeg', width=None)

if selected_content == "Our Group":
    st.title("""Halooo!!🙋‍♀️""")
    st.header("Kenalan dulu yuk") 
    
    
    st.write("""Disusun oleh Kelompok 4 (1A)
1. Anggun Salsa Erista (2360070)
2. Difta Ayu Fazriatami (2360108)
3. Nurul Hasanah (2360220)
4. Raissa Mutiara Dewi (2360232)
5. Salma Aulia Putri (2360254)""")