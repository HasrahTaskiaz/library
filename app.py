from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'Tanggal': ['2025-04-01', '2025-04-01', '2025-04-02', '2025-04-02', '2025-04-03', '2025-04-03'],
        'Nama Produk': ['Kaos Polos', 'Kemeja Flanel', 'Hoodie', 'Kaos Polos', 'Jaket Jeans', 'Kemeja Flanel'],
        'Ukuran': ['M', 'L', 'XL', 'S', 'L', 'M'],
        'Jumlah Terjual': [12, 8, 5, 10, 7, 6],
        'Harga Satuan': [50000, 120000, 150000, 50000, 180000, 120000]
    }

    df = pd.DataFrame(data)
    df['Total Penjualan'] = df['Jumlah Terjual'] * df['Harga Satuan']
    table = df.to_html(classes='table table-striped', index=False)

    # Siapkan data untuk grafik
    chart_data = df.groupby('Nama Produk')['Total Penjualan'].sum().reset_index()
    labels = chart_data['Nama Produk'].tolist()
    values = chart_data['Total Penjualan'].tolist()

    return render_template('index.html', table=table, labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug=True)

