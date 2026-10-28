Bulut Tabanlı Otomatik Veri Analiz ve 
Görselleştirme Aracı 
Bu proje, Python programlama dili kullanılarak geliştirilmiş; Pandas ve NumPy 
kütüphaneleriyle veri işleme, Streamlit ile interaktif web arayüzü sunma ve bulut bilişim 
prensipleriyle PaaS (Platform as a Service) ortamında yayınlama süreçlerini içeren 
uçtan uca bir yazılım geliştirme çalışmasıdır. 
Kullanılan Teknolojiler ve Bağımlılıklar (requirements.txt) 
Projenin kararlı bir şekilde çalışması için gerekli kütüphaneler ve görevleri şunlardır: 
streamlit>=1.30.0 \rightarrow Web arayüzünü ve kullanıcı etkileşim katmanını ayağa 
kaldırmak için kullanılır. 
pandas>=2.0.0 \rightarrow Veri setlerini okumak, tabloya dönüştürmek ve istatistiksel 
özetler çıkarmak için kullanılır. 
numpy>=1.24.0 \rightarrow Simülasyon verisi üretmek ve matris tabanlı matematiksel 
işlemler yapmak için kullanılır. 
openpyxl>=3.1.0 \rightarrow Kullanıcıların .xlsx (Excel) formatında dosya yüklediğinde 
Pandas'ın bunu okuyabilmesi için arka planda çalışan motor/bağımlılıktır. 
Mimari ve Yazılım Yaşam Döngüsü (SDLC) 
Proje, yazılım mühendisliği prensiplerinden Sorumlulukların Ayrılması (Separation of 
Concerns) ilkesine sadık kalınarak modüler bir yapıda tasarlanmıştır: 
Arayüz Katmanı (app.py): Kullanıcı etkileşimlerini, dosya yükleme (file_uploader) 
işlemlerini ve grafik çıktılarının sunulmasını yönetir. 
İş Mantığı Katmanı (utils.py): Veri yaşam döngüsünü (Veri Üretimi \rightarrow 
Dönüştürme \rightarrow Analiz) yöneten sınıfları ve fonksiyonları barındırır. 
Bellek Yönetimi (RAM): Proje, ek bir veritabanı maliyetine gerek duymadan, 
yüklenen veya üretilen verileri geçici bellek (RAM) üzerinde anlık olarak işleyip optimize 
bir performans sunar. 
Kurulum ve Yerelde Çalıştırma 
Projeyi kendi bilgisayarınızda test etmek için terminal üzerinde sırasıyla şu 
adımları izleyebilirsiniz: 
1.Projeyi klonlayın veya indirin. 
2.Gerekli kütüphaneleri yükleyin. 
pip install -r requirements.txt 
3.Uygulamayı yerelde başlatın: 
streamlit run app.py 
Deployment (Bulut Üzerinde Yayınlama)
​Bu uygulama, ek bir sunucu yönetimi, AWS, Ubuntu veya benzeri harici altyapı gerektirmeden Streamlit Community Cloud platformunda GitHub entegrasyonu ile doğrudan Platform as a Service (PaaS) mimarisine bağlanmıştır. Kodlar GitHub reposuna gönderildiği an bulut ortamında otomatik olarak derlenir ve canlıya alınır.