# BSM Directory Monitor

Bu proje, `/home/yakup/bsm/test` dizinindeki dosya değişikliklerini (oluşturma, silme, değiştirme, taşıma vb.) Python'un **watchdog** kütüphanesiyle izler ve bu değişiklikleri `/home/yakup/bsm/logs/changes.json` dosyasına JSON formatında kaydeder. Ayrıca bir **systemd** servisi (`bsm-monitor.service`) sayesinde sistem yeniden başlatılsa bile otomatik olarak devreye girer.

## Dosyalar

- **monitor.py**: Python scripti. Watchdog ile belirtilen dizini izler.
- **bsm-monitor.service**: `systemd` servisi dosyası. `monitor.py`’yi arka planda çalıştırır.
- **README.md**: Bu döküman.

## Kurulum ve Çalıştırma Adımları

1. **Python ve watchdog kurulumu**  
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 python3-watchdog -y
Dizin ve dosya izinleri

bash
Kodu kopyala
sudo mkdir -p /home/yakup/bsm/test
sudo mkdir -p /home/yakup/bsm/logs
sudo chmod 777 /home/yakup/bsm/test
sudo touch /home/yakup/bsm/logs/changes.json
sudo chmod 666 /home/yakup/bsm/logs/changes.json
monitor.py dosyasını yükleyin

Bu dosyayı /home/yakup/bsm/ içine yerleştirin ve çalıştırılabilir yapın:
bash
Kodu kopyala
sudo chmod +x /home/yakup/bsm/monitor.py
bsm-monitor.service dosyasını yerleştirin

Dosyayı /etc/systemd/system/bsm-monitor.service olarak kaydedin.
İçeriğindeki User, WorkingDirectory ve ExecStart kısımlarında yolların doğru olduğundan emin olun (kullanıcı adınız yakup olmalı).
Servisi etkinleştirin ve başlatın

bash

sudo systemctl enable bsm-monitor.service
sudo systemctl start bsm-monitor.service
Durumu kontrol edin

bash

sudo systemctl status bsm-monitor.service
Çıktıda active (running) görüyorsanız script başarıyla çalışıyordur.

