# main.py

def paginate(data, page_size):
    """Bölünen verileri sayfalara ayırır"""
    for i in range(0, len(data), page_size):
        yield data[i:i + page_size]

def main():
    # Örnek veri: 1'den 50'ye kadar sayılar
    data = list(range(1, 51))
    page_size = 10
    pages = list(paginate(data, page_size))
    total_pages = len(pages)
    
    current_page = 0
    while True:
        print(f"\nPage {current_page + 1}/{total_pages}")
        print(pages[current_page])

        command = input("Enter 'n' for next, 'p' for previous, 'q' to quit: ").strip().lower()
        if command == 'n':
            if current_page < total_pages - 1:
                current_page += 1
            else:
                print("Already at the last page.")
        elif command == 'p':
            if current_page > 0:
                current_page -= 1
            else:
                print("Already at the first page.")
        elif command == 'q':
            print("Exiting pagination.")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
