import pandas as pd

def get_data():
    data = {
        'Tanggal': ['2025-04-01', '2025-04-02', '2025-04-03'],
        'Nama Produk': ['Kaos Polos', 'Kemeja Flanel', 'Hoodie'],
        'Jumlah Terjual': [20, 15, 10],
        'Harga Satuan': [50000, 120000, 150000]
    }

    df = pd.DataFrame(data)
    df['Total Penjualan'] = df['Jumlah Terjual'] * df['Harga Satuan']
    return df
