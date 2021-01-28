from flask import Flask, render_template
import webbrowser


url = "http://localhost:80/"
webbrowser.open_new_tab(url)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')
    
 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
    



