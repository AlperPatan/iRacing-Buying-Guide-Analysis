import re
import os
import pypdf
import pandas as pd

# 1. SPORTS CAR KATEGORİSİNDEKİ TEMEL SERİLER
# Bu liste iRacing'in popüler Sports Car serilerini kapsar.
SPORTS_CAR_SERIES = {
    'Global Mazda': 'Global Mazda MX-5 Cup',
    'GR86': 'Toyota GR86 Cup',
    'Falken Tyre': 'GT4 Falken Tyre Challenge', 
    'iRacing Porsche Cup': 'Porsche Cup',
    'GT Sprint': 'GT Sprint',
    'GT Endurance': 'GT Endurance',
    'GT3 Fanatec': 'GT3 Fanatec Challenge',
    'IMSA iRacing': 'IMSA iRacing Series',
    'IMSA Michelin': 'IMSA Michelin Pilot Challenge',
    'Production Car': 'Production Car Sim-Lab Challenge',
    'LMP3 Trophy':'LMP3',
    'Global Endurance Tour':'Global Endurance (6Hr)',
    'LMP2 Challenge':'LMP2 Challenge',
    'Prototype Challenge' : 'Prototype Challenge',
    'iRacing GT3': 'iRacing GT3 - Regionals'

    #'Ring Meister': 'Ring Meister'
}

# 2. PİST İSİMLERİNİ TEMİZLEME HARİTASI
NORM_MAP = {
    'Spa': 'Spa',
    'Nürburgring Nordschleife': 'Nürburgring Nords','Nürburgring Grand-Prix-Strecke':'Nürburgring GP',
    'Nürburgring Combined': 'Nürburgring Combined','Daytona': 'Daytona',
    'Sebring': 'Sebring', 'Mount Panorama': 'Bathurst', 'Watkins Glen': 'Watkins Glen',
    'Road America': 'Road America', 'Road Atlanta': 'Road Atlanta', 'Monza': 'Monza',
    'Interlagos': 'Interlagos', 'Red Bull Ring': 'Red Bull Ring', 'Okayama': 'Okayama',
    'Oulton Park': 'Oulton Park', 'Laguna Seca': 'Laguna Seca', 'Silverstone': 'Silverstone',
    'Suzuka': 'Suzuka', 'Brands Hatch': 'Brands Hatch', 'Zandvoort': 'Zandvoort',
    'Imola': 'Imola', 'Virginia International': 'VIR', 'Charlotte Motor': 'Charlotte',
    'Le Mans': 'Le Mans', 'Hungaroring': 'Hungaroring', 'Mugello': 'Mugello',
    'MotorLand Aragón': 'Aragon', 'Gilles Villeneuve': 'Montreal', 'Sonoma': 'Sonoma',
    'Portimão': 'Portimao', 'Algarve': 'Portimao', 'Misano': 'Misano', 'Fuji': 'Fuji'
}

def create_datasets():
    all_data = []
    week_pattern = re.compile(r'Week\s+(\d+)\s+\(\d{4}-\d{2}-\d{2}\)')
    
    
    season_pattern = re.compile(r'202\d Season \d')
    
    files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    if not files:
        print("Hata: Klasörde PDF bulunamadı!")
        return

    print("DataSet Oluşturuluyor\n")

    for filename in files:
        season_name = filename.replace('.pdf', '').replace('.PDF', '')
        
        try:
            reader = pypdf.PdfReader(filename)
            current_series = None
            
            for page in reader.pages:
                lines = page.extract_text().split('\n')
                
                for line in lines:
                    
                    if season_pattern.search(line):
                        current_series = None 
                        for pdf_name, custom_name in SPORTS_CAR_SERIES.items():
                            if pdf_name.lower() in line.lower():
                                current_series = custom_name
                                break
                    
                    if current_series:
                        match = week_pattern.search(line)
                        if match:
                            week_num = match.group(1) 
                            
                            track_str = week_pattern.sub('', line).strip()
                            track_str = re.sub(r'\[.*?\]', '', track_str) 
                            track_str = track_str.split(' - ')[0].strip() 
                            
                            for k, v in NORM_MAP.items():
                                if k.lower() in track_str.lower():
                                    track_str = v
                                    break
                                    
                            if len(track_str) > 2:
                                row = {
                                    'Sezon': season_name,
                                    'Seri': current_series,
                                    'Hafta': int(week_num),
                                    'Pist': track_str
                                }
                                all_data.append(row)
                                
        except Exception as e:
            print(f"!!! {filename} okunamadı: {e}")

    df_all = pd.DataFrame(all_data)
    
    if df_all.empty:
        print("Hiç veri çıkarılamadı.")
        return

    df_all.to_csv('Tum_SportsCar_Dataset.csv', index=False, encoding='utf-8-sig')
    print("-> Ana Veritabanı oluşturuldu: Tum_SportsCar_Dataset.csv")

    for series in df_all['Seri'].unique():
        df_series = df_all[df_all['Seri'] == series]
        safe_filename = series.replace(" ", "_") + "_Dataset.csv"
        df_series = df_series.sort_values(by=['Sezon', 'Hafta'])
        df_series.to_csv(safe_filename, index=False, encoding='utf-8-sig')
    
    print("\nİşlem başarılı!.")

if __name__ == "__main__":
    create_datasets()