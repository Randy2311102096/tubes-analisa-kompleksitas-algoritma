import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Implementasi algoritma Linear Search
def linear_search(arr, x):
    iterations = 0
    for i in range(len(arr)):
        iterations += 1
        if arr[i] == x:
            return i, iterations
    return -1, iterations

# Implementasi algoritma Binary Search
def binary_search(arr, x):
    iterations = 0
    l = 0
    r = len(arr) - 1
    while l <= r:
        iterations += 1
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid, iterations
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1, iterations

# Implementasi algoritma Bubble Sort
def bubble_sort(arr):
    iterations = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, iterations

# Grafik untuk menyimpan data
sizes = []
linear_iters = []
binary_iters = []
bubble_iters = []
linear_times = []
binary_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_iters, 'ro-', label='Linear Search')
    plt.plot(sizes, binary_iters, 'bo-', label='Binary Search')
    plt.plot(sizes, bubble_iters, 'go-', label='Bubble Sort')
    plt.title('Performance Comparison: Linear Search vs Binary Search vs Bubble Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Number of Iterations')
    plt.grid(True)
    plt.legend()
    plt.show()

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Nomor Penerbangan", "Waktu Eksekusi Linear (s)", "Waktu Eksekusi Binary (s)", "Waktu Eksekusi Bubble Sort (s)"]
    for i in range(len(sizes)):
        table.add_row([
            sizes[i],
            f"{linear_times[i]:.15e}",
            f"{binary_times[i]:.15e}",
            f"{bubble_iters[i]:.15e}"
        ])
    print(table)

# Program utama
flights = []

while True:
    try:
        flight_number = input('Masukkan nomor penerbangan (atau ketik "exit" untuk keluar): ')
        if flight_number.lower() == "exit":
            print('Program selesai. Terima kasih!')
            break

        fuel_amount = int(input('Masukkan jumlah bahan bakar (liter): '))
        takeoff_time = input('Masukkan waktu lepas landas (HH:MM): ')
        travel_time = input('Masukkan waktu perjalanan (HH:MM): ')
        emergency = input('Apakah ada keadaan darurat? (yes/no): ').lower() == 'yes'

        flights.append({
            'Nomor Penerbangan': flight_number,
            'Jumlah Bahan Bakar (liter)': fuel_amount,
            'Waktu Lepas Landas': takeoff_time,
            'Waktu Perjalanan': travel_time,
            'Darurat': 'Yes' if emergency else 'No'
        })

        # Menyimpan ukuran untuk grafik
        sizes.append(len(flights))

        # Mencari penerbangan menggunakan Linear Search
        start_time = time.perf_counter()
        _, linear_iter = linear_search([f['Nomor Penerbangan'] for f in flights], flight_number)
        end_time = time.perf_counter()
        linear_times.append(end_time - start_time)
        linear_iters.append(linear_iter)

        # Mencari penerbangan menggunakan Binary Search (harus diurutkan)
        sorted_flights = sorted(flights, key=lambda x: x['Nomor Penerbangan'])
        start_time = time.perf_counter()
        _, binary_iter = binary_search([f['Nomor Penerbangan'] for f in sorted_flights], flight_number)
        end_time = time.perf_counter()
        binary_times.append(end_time - start_time)
        binary_iters.append(binary_iter)

        # Mengurutkan penerbangan menggunakan Bubble Sort
        start_time = time.perf_counter()
        _, bubble_iter = bubble_sort([f['Nomor Penerbangan'] for f in flights.copy()])
        end_time = time.perf_counter()
        bubble_iters.append(bubble_iter)

        # Update grafik dan tabel setelah setiap input
        update_graph()
        print_execution_table()

    except ValueError:
        print("Error: Masukkan angka yang valid untuk jumlah bahan bakar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
