from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# File to store IP addresses
LOG_FILE = "ip_log.txt"

# Simple HTML template
HTML = '''
<!DOCTYPE html>
<html>
<body>
    <h2>IP Address Logger</h2>
    <p>By clicking the button below, you agree to share your IP address for [state your legitimate reason].</p>
    <form method="post">
        <input type="submit" value="I agree to share my IP">
    </form>
    {% if ip %}
    <p>Your IP address ({{ ip }}) has been logged. Thank you for participating.</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.remote_addr
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, 'a') as f:
            f.write(f"{timestamp}: {ip}\n")
        return render_template_string(HTML, ip=ip)
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)