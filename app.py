from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data rekomendasi
data_rekomendasi = pd.read_csv("data/hasil_rekomendasi_mahasiswa.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nim = request.form.get("nim")

        # Filter rekomendasi berdasarkan NIM
        rekomendasi = data_rekomendasi[data_rekomendasi["NIM"] == nim]

        if rekomendasi.empty:
            return render_template("result.html", nim=nim, rekomendasi=None)

        return render_template("result.html", nim=nim, rekomendasi=rekomendasi.to_dict(orient="records"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
