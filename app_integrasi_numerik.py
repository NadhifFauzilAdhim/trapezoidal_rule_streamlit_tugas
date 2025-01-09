import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(x, y):
    n = len(x)  
    integral = (x[-1] - x[0]) * (y[0] + 2 * np.sum(y[1:n - 1]) + y[-1]) / (2 * (n - 1))
    return integral

st.title("Kalkulator Integral Metode Trapezoidal Rule")
st.write("Aplikasi ini menghitung nilai integral menggunakan metode Trapezoidal Rule berdasarkan input titik-titik pembagi dan nilai fungsi.")

st.header("Input Data")

num_points = st.slider("Jumlah titik pembagi:", min_value=2, max_value=20, value=7)

x_start = st.number_input("Masukkan nilai awal (x start):", value=1.0)
x_end = st.number_input("Masukkan nilai akhir (x end):", value=2.8)
x = np.linspace(x_start, x_end, num_points)

y_input = st.text_area("Masukkan nilai fungsi pada titik-titik tersebut (y) dipisahkan dengan koma:", "1.449, 2.06, 2.645, 3.216, 3.779, 4.338, 4.898")

try:
    y = np.array([float(i) for i in y_input.split(",")])
    if len(x) != len(y):
        st.error("Jumlah nilai x dan y harus sama!")
    else:
        result = trapezoidal_rule(x, y)
        st.subheader("Hasil Perhitungan")
        st.write(f"Integral menggunakan metode Trapezoidal Rule adalah: {result:.4f}")

        st.subheader("Grafik")
        fig, ax = plt.subplots()
        ax.plot(x, y, 'o-', label="Data")
        for i in range(len(x) - 1):
            ax.fill_between([x[i], x[i + 1]], [y[i], y[i + 1]], alpha=0.3, color='orange')
        ax.set_title("Visualisasi Data dan Luas Trapezoid")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        st.pyplot(fig)

except ValueError:
    st.error("Pastikan Anda memasukkan angka yang valid dan dipisahkan dengan koma.")
