from pathlib import Path
import hashlib
import json
import shutil
import time
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
COMPANY_DATA = BASE_DIR / "company_data"
LOCAL_BACKUP = BASE_DIR / "local_backup"
OFFLINE_BACKUP = BASE_DIR / "offline_backup"
RESTORE_AREA = BASE_DIR / "restore_area"
LOG_DIR = BASE_DIR / "logs"

MANIFEST_NAME = "backup_manifest.json"

# Demo account. In a real system, never hard-code credentials.
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "123456"
DEMO_MFA_CODE = "888888"

def print_title(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def list_files(root: Path):
    if not root.exists():
        return []
    return sorted([p for p in root.rglob("*") if p.is_file()])

def relative_to_root(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()

def clear_directory(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    for item in path.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

def copy_tree(src: Path, dst: Path):
    dst.mkdir(parents=True, exist_ok=True)
    for file in list_files(src):
        rel = file.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, target)

def build_manifest(source_dir: Path):
    files = []
    for file in list_files(source_dir):
        files.append({
            "path": relative_to_root(file, source_dir),
            "sha256": sha256_file(file),
            "size_bytes": file.stat().st_size
        })
    return {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": source_dir.name,
        "file_count": len(files),
        "files": files
    }

def save_manifest(manifest: dict, backup_dir: Path):
    manifest_path = backup_dir / MANIFEST_NAME
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

def load_manifest(backup_dir: Path):
    manifest_path = backup_dir / MANIFEST_NAME
    if not manifest_path.exists():
        raise FileNotFoundError(f"找不到備份紀錄：{manifest_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))

def authenticate() -> bool:
    print("Zero Trust 驗證：重要操作前必須重新驗證")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    mfa = input("MFA Code: ").strip()

    if username == DEMO_USERNAME and password == DEMO_PASSWORD and mfa == DEMO_MFA_CODE:
        print("驗證成功：允許執行操作")
        return True

    print("驗證失敗：拒絕存取")
    return False

def now_seconds():
    return time.perf_counter()
