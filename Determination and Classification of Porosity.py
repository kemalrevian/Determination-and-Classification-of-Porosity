# Kemal Reviansyah Hermawanto_101320118
# Achmad Iyan Alfadany_101320032
# TUGAS PTIA 2021

import pandas as pd
def porosity(Vb,Vg):
    porosity = (Vb - Vg)/Vb * 100
    return porosity
def kelporosity():
    data = {
    "Kualitas":["Diabaikan (Negligible)", "Buruk (Poor)", "Cukup (Fair)" , "Baik (Good)", "Sangat Baik (Very Good)", "Istimewa (Excellent)"],
    "Porositas" :["0 - 5 %","5 - 10 %","10 - 15 %","15 - 20 %","20 - 25 %","> 25 %"]
    }
    df = pd.DataFrame(data)
    print(df)
while True:
    print(">>>>>MENU<<<<<")
    print(" [0] Exit\n [1] Klasifikasi Porositas\n [2] Perhitungan Porositas ")
    print(">>>>>>><<<<<<<")
    option = input("Masukkan Pilihan Anda: ")
    if option == "1":
        print("=====TABEL KUALITAS POROSITAS SUATU BATUAN=====")
        print(kelporosity())
    elif option == "2":
        print("=====PERHITUNGAN POROSITAS=====")
        x= float(input("Masukkan Nilai Volume Bulk : "))
        y= float(input("Masukkan Nilai Volume Grain : "))
        print("nilai Porositas :", porosity(x,y), "%")
        data = float(porosity(x,y))
        while True:
            if data >= 0 and data <= 5.0:
                print("Kualitas Porositas : Diabaikan")
                break 
            elif data > 5.0 and data <= 10.0:
                print ("Kualitas Porositas : Buruk")
                break
            elif data > 10.0 and data <= 15.0:
                print ("Kualitas Porositas : Cukup")
                break
            elif data > 15.0 and data <= 20.0:
                print ("Kualitas Porositas : Baik")
                break
            elif data > 20.0 and data <= 25.0:
                print ("Kualitas Porositas : Sangat Baik")
                break
            elif data > 25.0:
                print ("Kualitas Porositas : Istimewa")
                break
            else:
                print("ERROR")
                print("POROSITAS TIDAK DAPAT DI KLASIFIKASIKAN")
                break
    elif option == "0":
        print("AKHIR DARI PROGRAM")
        break    
    else:
        print("Invalid Option")
