#!/usr/bin/env python3
# horor.py
# Generator cerita horor sederhana — Bahasa Indonesia
# Tidak memerlukan library eksternal.

import random
import time
import sys
import os

# --- Pengaturan ---
TYPE_SPEED = 0.02   # delay per karakter saat "mengetik"
PAUSE_SHORT = 0.6
PAUSE_LONG = 1.1

# Elemen acak untuk membangun cerita
lokasi = [
    "rumah tua di ujung desa",
    "rumah kontrakan yang selalu kosong sebelah",
    "rumah sakit lama yang ditutup",
    "asrama yang berlantai kayu berderit",
    "villa di tepi danau berkabut"
]

waktu = ["malam bulan purnama", "hujan deras tengah malam", "subuh berkabut", "malam tanpa bintang", "tengah malam saat jam dinding berhenti"]

tokoh = [
    "seorang mahasiswa pulang larut",
    "seorang perawat jaga malam",
    "dua sahabat yang iseng masuk",
    "seorang penjaga malam",
    "wanita tua yang tak pernah tidur"
]

objek = [
    "cermin retak yang memantulkan bayangan lain",
    "boneka kecil dengan mata yang hilang",
    "kotak kayu tua berukir simbol aneh",
    "catatan usang bertinta merah",
    "lukisan yang mengikutimu"
]

background = [
    "berbisik dari balik dinding",
    "langkah yang tak pernah berhenti",
    "tawa merintih di lorong",
    "nada piano yang menyendiri di loteng",
    "suara ketukan yang datang dari bawah"
]

plot twist = [
    "tokoh sadar bahwa semua tetangga telah lama pergi... kecuali bayangannya sendiri.",
    "suara itu sebenarnya panggilan dari masa depan — agar ia tidak membuka pintu.",
    "setiap nama yang disebut hilang dari ingatan orang lain, termasuk fotonya.",
    "rumah itu hidup dan menyesuaikan malam demi malam agar penghuninya tidak pernah pergi.",
    "nyanyian itu menuntun mereka ke ruang di mana waktu berhenti."
]

def typewriter(text, speed=TYPE_SPEED, end="\n"):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(speed)
    print(end, end="", flush=True)

def buat_cerita():
    L = random.choice(lokasi)
    W = random.choice(waktu)
    T = random.choice(tokoh)
    O = random.choice(obyek)
    S = random.choice(suara)
    Tw = random.choice(twist)

    pembuka = f"Di {L}, pada {W}, ada {T}."
    suasana = (
        f"Malam itu udara terasa berat. Di sudut rumah, ada {O}. "
        f"Setiap kali angin lewat, terdengar {S}."
    )
    kejadian = (
        "Tokoh itu mencoba mengacuhkan — sampai hal-hal kecil berubah.\n"
        "Pertama, jam dinding berhenti pada pukul tiga. Kemudian bayangan di dinding "
        "mulai bergerak sedikit berbeda dari gerak tubuhnya."
    )
    klimaks = (
        "Ketika ia mendekati sumber suara, sesuatu menyeret napasnya. "
        "Pintu di belakangnya tertutup sendiri. Lampu berkedip, dan dari kegelapan "
        "muncul satu bisikan: 'Kenapa kau kembali?'"
    )
    ending = (
        f"{Tw}\n"
        "Ia berlari — tapi rumah itu seakan tidak mengizinkannya pergi. "
        "Pada akhirnya, hanya ada satu pilihan tersisa: menatap cermin retak dan menerima apa yang menatap balik."
    )

    paragraf = [pembuka, suasana, kejadian, klimaks, ending]
    return "\n\n".join(paragraf)

def main():
    os.system("")  
    typewriter("=== Generator Cerita Horor (Python) ===\n")
    time.sleep(PAUSE_SHORT)

    versi = 1
    try:
        arg = sys.argv[1:]
        if arg and arg[0].isdigit():
            versi = max(1, min(10, int(arg[0])))
    except Exception:
        versi = 1

    typewriter(f"Menghasilkan {versi} cerita pendek...\n")
    time.sleep(PAUSE_SHORT)

    hasil_semua = []
    for i in range(versi):
        cerita = buat_cerita()
        hasil_semua.append(cerita)
 
        typewriter(f"\n--- Cerita {i+1} ---\n")
        for p in cerita.split("\n\n"):
            typewriter(p)
            time.sleep(PAUSE_SHORT)

        time.sleep(PAUSE_LONG)


    typewriter("\nMau simpan cerita ke file? (y/n) ", end="")
    jawab = input().strip().lower()
    if jawab.startswith("y"):
        fname = f"cerita_horor_{int(time.time())}.txt"
        with open(fname, "w", encoding="utf-8") as f:
            f.write("\n\n---\n\n".join(hasil_semua))
        typewriter(f"Cerita tersimpan di: {fname}\n")
    else:
        typewriter("Oke, tidak disimpan. Semoga bulu kudukmu berdiri!\n")

if __name__ == "__main__":
    main()
