cd /etc
mkdir ikmp
cd /etc/ikmp
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp_web.py -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp.py -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/config.json -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/uptime.json -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/requirements.txt -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp_web.service -q --directory-prefix=/etc/systemd/system
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp.service -q --directory-prefix=/etc/systemd/system
systemctl reload-daemon
systemctl enable ikmp ikmp_web
apt install pip3 -y
pip3 install -r /etc/ikmp/requirements.txt
echo "installed requirements"
nano /etc/ikmp/config.json
systemctl start ikmp ikmp_web