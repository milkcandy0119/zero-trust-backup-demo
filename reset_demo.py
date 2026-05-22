from common import print_title, COMPANY_DATA, LOCAL_BACKUP, OFFLINE_BACKUP, RESTORE_AREA, clear_directory

SAMPLE_FILES = {
    "customer_list.txt": "Customer ID,Name,Plan\nC001,Alice,Enterprise\nC002,Bob,Standard\nC003,Charlie,Premium\n",
    "sales_report.txt": "2026 Q2 Sales Report\nRevenue: 1,250,000 NTD\nGrowth: 12.5%\n",
    "accounting.txt": "Accounting Summary\nPayroll: 300,000 NTD\nCloud Service: 28,000 NTD\nSecurity Budget: 80,000 NTD\n",
}

def main():
    print_title("Reset Demo Environment")

    for folder in [COMPANY_DATA, LOCAL_BACKUP, OFFLINE_BACKUP, RESTORE_AREA]:
        clear_directory(folder)

    for filename, content in SAMPLE_FILES.items():
        (COMPANY_DATA / filename).write_text(content, encoding="utf-8")

    print("Demo 已重置")
    print("接下來可執行：python backup.py")

if __name__ == "__main__":
    main()
