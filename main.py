from pddiktipy import api

# Initialize the API object
a = api()

def get_details_by_nim(nim):
    """Searches for the student by NIM and returns the full details."""
    result = a.search_all(nim)
    if 'mahasiswa' in result:
        for mahasiswa in result['mahasiswa']:
            if mahasiswa['nim'] == nim:
                return {
                    'id': mahasiswa['id'],
                    'nama': mahasiswa['nama'],
                    'nama_prodi': mahasiswa.get('nama_prodi', "Unknown Program"),
                    'nama_pt': mahasiswa.get('nama_pt', "Unknown University"),
                    'nim': mahasiswa['nim'],
                    'sinkatan_pt': mahasiswa.get('sinkatan_pt', "Unknown")
                }
    return None

def single_mode():
    """Handles single NIM input."""
    nim = input("Masukkan NIM: ")
    details = get_details_by_nim(nim)
    if details:
        print(f"Detail Mahasiswa untuk NIM {nim}:")
        print(details)
    else:
        print("NIM tidak ditemukan.")

def multiple_mode():
    """Handles multiple NIM inputs from a file."""
    with open('nims.txt', 'r') as file:
        nims = file.read().splitlines()

    with open('nama_mahasiswa.txt', 'w') as output_file:
        for nim in nims:
            details = get_details_by_nim(nim)
            if details:
                output_file.write(f"{details}\n")
                print(f"Detail Mahasiswa untuk NIM {nim}: {details}")
            else:
                print(f"NIM {nim} tidak ditemukan.")

# Main function to choose mode
def main():
    print("Pilih mode:")
    print("1. Single")
    print("2. Multiple")
    choice = input("Masukkan pilihan (1/2): ").strip()
    
    if choice == "1":
        single_mode()
    elif choice == "2":
        multiple_mode()
    else:
        print("Pilihan tidak valid. Masukkan 1 atau 2.")

# Run the script
if __name__ == "__main__":
    main()
