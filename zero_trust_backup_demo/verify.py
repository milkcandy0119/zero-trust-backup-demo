from common import print_title, OFFLINE_BACKUP, RESTORE_AREA, load_manifest, sha256_file
from pathlib import Path

def main():
    print_title("Backup / Restore Verification")

    try:
        manifest = load_manifest(OFFLINE_BACKUP)
    except FileNotFoundError as e:
        print(e)
        return

    errors = 0
    checked = 0

    for item in manifest["files"]:
        rel_path = item["path"]
        expected_hash = item["sha256"]
        restored_file = RESTORE_AREA / rel_path

        checked += 1

        if not restored_file.exists():
            print(f"[ERROR] 缺少檔案：{rel_path}")
            errors += 1
            continue

        actual_hash = sha256_file(restored_file)
        if actual_hash != expected_hash:
            print(f"[ERROR] Hash 不一致：{rel_path}")
            errors += 1
        else:
            print(f"[OK] {rel_path}")

    print("\n驗證完成")
    print(f"檢查檔案數：{checked}")
    print(f"錯誤數：{errors}")

    if errors == 0:
        print("結果：0 recovery errors，符合 3-2-1-1-0 的 0 目標")
    else:
        print("結果：還原資料存在錯誤，需要重新檢查備份與還原流程")

if __name__ == "__main__":
    main()
