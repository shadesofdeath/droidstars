import os

# Dosyaları taramak için dizin yolunu belirtin
directory = '.'

# Tüm html dosyalarını tarayın
for filename in os.listdir(directory):
  if filename.endswith('.html'):
    # Dosyayı açın ve satırlarını okuyun
    with open(filename) as f:
      lines = f.readlines()
    # 27. satırdaki <a> etiketini <button> etiketine çevirin
    lines[26] = lines[26].replace('cornflowerblue', 'white')
    # Dosyayı tekrar yazın
    with open(filename, 'w') as f:
      f.write(''.join(lines))
