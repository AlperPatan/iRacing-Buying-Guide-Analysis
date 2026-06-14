import pandas as pd
import matplotlib.pyplot as plt

# Dev datamızı okuyoruz
df = pd.read_csv('Tum_SportsCar_Dataset.csv')

# Pistleri saydırıyoruz (Ring Meister içindeki Nürburgring'ler de dahil olacak!)
pist_sayilari = df['Pist'].value_counts().head(50)

print("--- YENİ TOP 10  ---")
print(pist_sayilari)

# Grafiğe dök
plt.style.use('ggplot')
plt.figure(figsize=(12, 8))
bars = plt.barh(pist_sayilari.index[::-1], pist_sayilari.values[::-1], color='#e31b23')
plt.title('iRacing Sports Car Kategori: En Popüler 10 Pist ', fontsize=16)
plt.xlabel('Takvimde Toplam Görülme Sayısı', fontsize=12)

for bar in bars:
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
             f'{int(bar.get_width())}', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('Final_Pist_Siralama.png', dpi=300)
plt.show()