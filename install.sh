cd /etc
mkdir ikmp
cd /etc/ikmp
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp_web.py
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp.py
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/config.json
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/uptime.json
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/requirements.txt
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp_web.service --directory-prefix=/etc/systemd/system
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp.service --directory-prefix=/etc/systemd/system
systemctl reload-daemon
systemctl enable ikmp ikmp_web
apt install pip3 -y
pip3 install -r /etc/ikmp/requirements.txt
nano /etc/ikmp/config.json
systemctl start ikmp ikmp_web