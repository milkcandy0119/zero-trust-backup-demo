from common import (
    print_title, OFFLINE_BACKUP, RESTORE_AREA, MANIFEST_NAME,
    clear_directory, copy_tree, authenticate, now_seconds
)
from pathlib import Path

def main():
    print_title("Zero-Trust Backup Recovery Demo - Restore")

    if not authenticate():
        return

    if not OFFLINE_BACKUP.exists():
        print("錯誤：找不到 offline_backup")
        return

    start = now_seconds()

    print("\n[1] 清空 restore_area")
    clear_directory(RESTORE_AREA)

    print("[2] 從 offline_backup 還原資料")
    copy_tree(OFFLINE_BACKUP, RESTORE_AREA)

    # 還原區不需要再保留 manifest 當作企業資料，刪除以便驗證時更直觀。
    manifest_copy = RESTORE_AREA / MANIFEST_NAME
    if manifest_copy.exists():
        manifest_copy.unlink()

    end = now_seconds()
    rto = end - start

    print("\n還原完成")
    print(f"RTO：{rto:.4f} 秒")
    print("接下來可執行：python verify.py")

if __name__ == "__main__":
    main()
