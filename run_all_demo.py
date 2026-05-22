import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def run(script):
    print("\n\n>>> 執行", script)
    subprocess.run([sys.executable, str(BASE_DIR / script)], check=False)

def main():
    print("完整展示流程：")
    print("1. reset_demo.py")
    print("2. backup.py")
    print("3. simulate_ransomware.py")
    print("4. restore.py")
    print("5. verify.py")
    print("\n注意：backup.py 與 restore.py 需要輸入驗證資料")
    print("Username: admin")
    print("Password: 123456")
    print("MFA Code: 888888")

    run("reset_demo.py")
    run("backup.py")
    run("simulate_ransomware.py")
    run("restore.py")
    run("verify.py")

if __name__ == "__main__":
    main()
