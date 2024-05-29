cd /etc
mkdir ikmp
cd /etc/ikmp
mkdir templates
cd /etc/ikmp/templates
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/templates/web.template.html -q
cd /etc/ikmp
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp_web.py -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp.py -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/config.json -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/uptime.json -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/requirements.txt -q
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp_web.service -q --directory-prefix=/etc/systemd/system
wget https://raw.githubusercontent.com/kioydiolabs/IKMP/main/ikmp.service -q --directory-prefix=/etc/systemd/system
systemctl daemon-reload
systemctl enable ikmp ikmp_web
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq python3-pip < /dev/null > /dev/null
pip install -r /etc/ikmp/requirements.txt
echo "installed requirements"
nano /etc/ikmp/config.json
systemctl start ikmp ikmp_web