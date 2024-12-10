# Cek Detail Mahasiswa Berdasarkan NIM

## Requirements
*  python3
*  pddiktipy

## Installation

```sh
sudo apt install python3 python3-pip git -y #untuk debian/ubuntu
pip install pddiktipy
https://github.com/QueenXuner/cek-nama-mahasiswa-berdasarkan-nim
cd cek-nama-mahasiswa-berdasarkan-nim
```

jika mengalami masalah saat install pddiktipy coba menggunakan ini
```sh
python3 -m venv myvenv
source myvenv/bin/activate
pip install pddiktipy
```

atau ini

```sh
pip install pddiktipy --break-system-packages
```

# Mode
terbagi menjadi 2 mode

Pilih mode:
1. Single
2. Multiple

Masukkan pilihan (1/2): 

## Mode Single
Mode ini hanya menginputkan 1 nim dan 1 output

## Mode Multiple
Mode ini menginputkan file nims.txt yang berisi beberapa nim dan akan mengeluarkan nama_mahasiswa.txt yang berisi nama-nama dari nim yang ada di file nims.txt
