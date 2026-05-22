from common import (
    print_title, COMPANY_DATA, LOCAL_BACKUP, OFFLINE_BACKUP,
    clear_directory, copy_tree, build_manifest, save_manifest, authenticate
)

def main():
    print_title("Zero-Trust Backup Recovery Demo - Backup")

    if not authenticate():
        return

    if not COMPANY_DATA.exists():
        print("錯誤：找不到 company_data 資料夾")
        return

    print("\n[1] 清空舊的 local_backup 與 offline_backup")
    clear_directory(LOCAL_BACKUP)
    clear_directory(OFFLINE_BACKUP)

    print("[2] 建立本機備份 local_backup")
    copy_tree(COMPANY_DATA, LOCAL_BACKUP)

    print("[3] 建立離線 / 不可變備份 offline_backup")
    copy_tree(COMPANY_DATA, OFFLINE_BACKUP)

    print("[4] 產生 SHA-256 備份完整性紀錄")
    local_manifest = build_manifest(LOCAL_BACKUP)
    offline_manifest = build_manifest(OFFLINE_BACKUP)
    save_manifest(local_manifest, LOCAL_BACKUP)
    save_manifest(offline_manifest, OFFLINE_BACKUP)

    print("\n備份完成")
    print("對應概念：3-2-1-1-0")
    print("- 原始資料：company_data")
    print("- 本機備份：local_backup")
    print("- 離線 / 不可變備份：offline_backup")
    print("- 0 錯誤目標：使用 verify.py 驗證 Hash")

if __name__ == "__main__":
    main()
