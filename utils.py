import numpy as np
import pandas as pd



class VeriYasamDongusu:
  """Veri İşleme ve Analiz Yaşam Döngüsünü (Lifecycle) yöneten sınıf."""

  @staticmethod
  def asama_1_veri_uret(satir_sayisi: int, sutun_sayisi: int) -> pd.DataFrame:
    """Yaşam Döngüsü Aşama 1: Veri Üretimi (Ingestion Lifecycle)."""
    # Guard Clause / Escape Check: Geçersiz parametre kontrolü
    if satir_sayisi <= 0 or sutun_sayisi <= 0:
      raise ValueError(
          "[Hata] Satır ve sütun sayıları sıfırdan büyük olmalıdır."
      )

    try:
      ham_veri = np.random.randn(satir_sayisi, sutun_sayisi)
      sutun_isimleri = [f"Öznitelik {i+1}" for i in range(sutun_sayisi)]
      return pd.DataFrame(ham_veri, columns=sutun_isimleri)
    except Exception as e:
      # Beklenmeyen durumlarda güvenli çıkış (Escape / Exception handling)
      raise RuntimeError(f"Veri üretimi sırasında kritik hata: {e}")

  @staticmethod
  def asama_2_veri_isle_ve_analiz_et(df: pd.DataFrame) -> pd.DataFrame:
    """Yaşam Döngüsü Aşama 2 & 3: Dönüştürme ve İstatistiksel Analiz (Processing &

    Analysis).
    """
    # Guard Clause: Boş veri kontrolü (Erken kaçış)
    if df is None or df.empty:
      raise ValueError(
          "[Hata] Analiz edilecek aktif veri akışı (DataFrame) bulunamadı."
      )

    # Pandas ile temel istatistiksel yaşam döngüsü özeti
    ozet_tablo = df.describe()
    return ozet_tablo


