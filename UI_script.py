from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder="UI", static_folder="graphs")

@app.route("/")
def home():
    df = pd.read_csv("cdr_voice.csv")
    df_sms = pd.read_csv("cdr_sms.csv")

    total_calls = len(df)
    total_sms = len(df_sms)
    total_duration = df['Duration_sec'].sum()

    return render_template(
        "web_page.html",
        total_calls=total_calls,
        total_sms=total_sms,
        total_duration=total_duration
    )

if __name__ == "__main__":
    app.run(debug=True)