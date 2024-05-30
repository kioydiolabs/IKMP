from flask import Flask, request, Response, render_template
import json

with open('/etc/ikmp/config.json', 'r') as f:
        config = json.load(f)
color_up = config['colors']['up']
color_down = config['colors']['down']

app = Flask(__name__, template_folder="./templates/")


@app.route("/")
def index():
        data = ""
        with open('/etc/ikmp/config.json', 'r') as f:
                config = json.load(f)
        with open('/etc/ikmp/uptime.json', 'r') as f:
                uptimeFile = json.load(f)
        for i in config['hosts']:
                if uptimeFile['hosts'][i] == "UP":
                        color = color_up
                elif uptimeFile['hosts'][i] == "DOWN":
                        color = color_down
                data += (f"<div style='display: flex; flex-direction: row; align-items: center; justify-items: center;'><a style='color: white;' href='{config['hosts'][i]['webpage_link']}'>{config['hosts'][i]['webpage_name']}</a><p style='color: {color};'>  - {uptimeFile['hosts'][i]}</p></div>")
        return render_template('web.template.html',data = data)


app.run(host='0.0.0.0', port=80,
        debug=False)