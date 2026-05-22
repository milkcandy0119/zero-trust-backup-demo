from common import print_title, COMPANY_DATA, list_files

def main():
    print_title("Ransomware Simulation")

    if not COMPANY_DATA.exists():
        print("錯誤：找不到 company_data 資料夾")
        return

    files = list_files(COMPANY_DATA)
    if not files:
        print("company_data 目前沒有檔案可模擬攻擊")
        return

    for file in files:
        # 用簡單文字取代原始內容，並改成 .locked 副檔名，模擬資料被加密。
        locked_path = file.with_name(file.name + ".locked")
        locked_path.write_text("This file has been encrypted by ransomware simulation.\n", encoding="utf-8")
        file.unlink()
        print(f"{file.name} -> {locked_path.name}")

    print("\n模擬完成：company_data 中的原始資料已被破壞")
    print("接下來可執行：python restore.py")

if __name__ == "__main__":
    main()
