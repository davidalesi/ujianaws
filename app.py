from flask import Flask, request

app = Flask(__name__)

data = [
    {"Nama": "David Alessandro Sianipar", "Jurusan": "Sistem Informasi", "NIM": "2119113943"},
]


def find_next_id():
    return max(j["id"] for j in data) + 1 if data else 1


@app.route("/")
def get_data():
    html = """
    <h1>Data Mahasiswa</h1>
    <ul>
    """
    for item in data:
        html += f"""
        <li>
            {item["Nama"]} ({item["Jurusan"]}) - {item["NIM"]}
        </li>
        """
    html += """
    </ul>
    """
    return html


@app.route("/", methods=['POST'])
def add_data():
    if request.method == "POST":
        nama = request.form.get("nama")
        jurusan = request.form.get("jurusan")
        nim = request.form.get("nim")

        new_data = {"Nama": nama, "Jurusan": jurusan, "NIM": nim}
        new_data["id"] = find_next_id()
        data.append(new_data)

        return f"""
        <h1>Data Berhasil Ditambahkan</h1>
        <p>Nama: {nama}</p>
        <p>Jurusan: {jurusan}</p>
        <p>NIM: {nim}</p>
        """

    return """
    <h1>Tambah Data Mahasiswa</h1>
    <form method="post">
        <label for="nama">Nama:</label>
        <input type="text" id="nama" name="nama">
        <br>
        <label for="jurusan">Jurusan:</label>
        <input type="text" id="jurusan" name="jurusan">
        <br>
        <label for="nim">NIM:</label>
        <input type="text" id="nim" name="nim">
        <br>
        <br>
        <button type="submit">Simpan</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5000)
