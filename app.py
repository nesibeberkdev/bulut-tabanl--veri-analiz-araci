import pandas as pd
import streamlit as st
from utils import VeriYasamDongusu  # Yazdığımız modüler sınıfı içeri aktarıyoruz

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Bulut Tabanlı Veri Analiz Aracı", page_icon="📊", layout="wide"
)

st.title("📊 Bulut Tabanlı Otomatik Veri Analiz ve Görselleştirme Aracı")
st.write(
    "Bu uygulama, Pandas ve NumPy ile işlenen verileri bulutta anlık olarak"
    " görselleştirir."
)

# --- VERİ ALIM (INGESTION) BÖLÜMÜ ---
st.sidebar.header("📥 Veri Kaynağı Yönetimi")
veri_kaynagi = st.sidebar.radio(
    "Veriyi nereden almak istiyorsunuz?",
    ["Simülasyon Verisi Üret (NumPy)", "Dosya Yükle (CSV / Excel)"],
)

df = None  # Ana veri çerçevemiz

try:
  if veri_kaynagi == "Simülasyon Verisi Üret (NumPy)":
    st.subheader("⚙️ Simülasyon Verisi Yapılandırması")
    col1, col2 = st.columns(2)
    with col1:
      satir = st.slider("Satır Sayısı", min_value=5, max_value=200, value=50)
    with col2:
      sutun = st.slider("Sütun Sayısı", min_value=1, max_value=10, value=3)

    # Yaşam Döngüsü Aşama 1: Veri Üretimi
    df = VeriYasamDongusu.asama_1_veri_uret(satir, sutun)
    st.success("✔ Simülasyon verisi başarıyla üretildi!")

  else:
    st.subheader("📂 Dosya Yükleme Paneli")
    yuklenen_dosya = st.file_uploader(
        "Lütfen bir CSV veya Excel dosyası yükleyin", type=["csv", "xlsx"]
    )

    if yuklenen_dosya is not None:
      # Dosya türüne göre Pandas ile okuma (Veri Alımı)
      if yuklenen_dosya.name.endswith(".csv"):
        df = pd.read_csv(yuklenen_dosya)
      else:
        df = pd.read_excel(yuklenen_dosya)
      st.success(f"✔ '{yuklenen_dosya.name}' başarıyla yüklendi!")
    else:
      st.info(
          "Lütfen sol panelden bir dosya yükleyin veya simülasyon moduna"
          " geçin."
      )

  # --- VERİ GÖRSELLEŞTİRME VE ANALİZ BÖLÜMÜ ---
  if df is not None:
    st.markdown("---")
    st.subheader("📋 Ham Veri Önizlemesi")
    st.dataframe(df.head(10), use_container_width=True)

    # Yaşam Döngüsü Aşama 2 & 3: Analiz
    st.markdown("---")
    st.subheader("📈 İstatistiksel Özet ve Görselleştirme")

    tab1, tab2 = st.tabs(["Grafik Görünümü", "İstatistiksel Analiz"])

    with tab1:
      # Grafik türü seçimi
      grafik_tipi = st.selectbox(
          "Grafik Türü Seçin", ["Çizgi Grafik (Line)", "Çubuk Grafik (Bar)"]
      )
      if grafik_tipi == "Çizgi Grafik (Line)":
        st.line_chart(df.select_dtypes(include="number"))
      else:
        st.bar_chart(df.select_dtypes(include="number"))

    with tab2:
      ozet_df = VeriYasamDongusu.asama_2_veri_isle_ve_analiz_et(df)
      st.dataframe(ozet_df, use_container_width=True)

except Exception as e:
  st.error(f"Bir hata oluştu: {e}")

  #  footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>"
    "Bulut Tabanlı Veri Görselleştirme Aracı © 2026"
    "</div>",
    unsafe_allow_html=True
)