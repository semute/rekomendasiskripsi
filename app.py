from flask import Flask, render_template, request
import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, "templates"),
            static_folder=os.path.join(BASE_DIR, "static"))

# Load data rekomendasi
csv_path = os.path.join(BASE_DIR, "data", "hasil_rekomendasi_mahasiswa_cosine08.csv")

if os.path.exists(csv_path):
    data_rekomendasi = pd.read_csv(csv_path)
else:
    data_rekomendasi = None


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nim = request.form.get("nim")

        if data_rekomendasi is not None:
            rekomendasi = data_rekomendasi[data_rekomendasi["NIM"] == nim]

            if rekomendasi.empty:
                return render_template("result.html", nim=nim, rekomendasi=None)

            return render_template("result.html", nim=nim, rekomendasi=rekomendasi.to_dict(orient="records"))

        return "File CSV tidak ditemukan", 500

    return render_template("index.html")


def handler(event, context):
    return app(event, context)


if __name__ == "__main__":
    app.run(debug=True)
