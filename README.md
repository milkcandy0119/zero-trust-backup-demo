# Zero-Trust Backup Recovery Demo

這是一份可用於「物聯網安全 / 企業數位韌性」專題的簡易 Demo。

## Demo 主題

**零信任備份與災難復原展示系統**

目標是模擬企業資料在遭遇勒索軟體攻擊後，如何透過：

- 3-2-1-1-0 備份原則
- 離線 / 不可變備份
- Hash 完整性驗證
- RTO 復原時間計算
- MFA / 零信任驗證

來恢復重要資料。

---

## 資料夾說明

```text
zero_trust_backup_demo/
├── company_data/              # 模擬企業原始資料
├── local_backup/              # 本機備份
├── offline_backup/            # 模擬離線 / 不可變備份
├── restore_area/              # 還原測試區
├── backup.py                  # 執行備份
├── simulate_ransomware.py      # 模擬勒索軟體破壞資料
├── restore.py                 # 從離線備份還原
├── verify.py                  # 驗證還原資料 Hash
├── reset_demo.py              # 重置 Demo
├── run_all_demo.py            # 一次跑完整流程
└── common.py                  # 共用函式
```

---

## 驗證帳號

這是 Demo 用的簡化帳號：

```text
Username: admin
Password: 123456
MFA Code: 888888
```

報告時可以說明：實務上不應該把帳號密碼寫死在程式裡，這裡只是為了展示「重要操作前必須重新驗證」的零信任精神。

---

## 建議展示流程

### 1. 重置環境

```bash
python reset_demo.py
```

### 2. 執行備份

```bash
python backup.py
```

這會把 `company_data` 備份到：

- `local_backup`
- `offline_backup`

並產生 `backup_manifest.json`，記錄每個檔案的 SHA-256 Hash。

### 3. 模擬勒索軟體攻擊

```bash
python simulate_ransomware.py
```

這會把 `company_data` 裡的檔案改成 `.locked`，模擬原始資料被加密。

### 4. 執行還原

```bash
python restore.py
```

這會從 `offline_backup` 還原資料到 `restore_area`，並計算 RTO。

### 5. 驗證還原結果

```bash
python verify.py
```

若成功會看到：

```text
結果：0 recovery errors，符合 3-2-1-1-0 的 0 目標
```

---

## 對應專題預期結果

| 專題概念 | Demo 對應 |
|---|---|
| 3 份資料 | company_data、local_backup、offline_backup |
| 2 種儲存位置 | 原始資料夾與備份資料夾 |
| 1 份異地 | 用 offline_backup 模擬異地 / 離線備份 |
| 1 份離線或不可變 | offline_backup 模擬 Air-gap 備份 |
| 0 recovery errors | verify.py 使用 SHA-256 驗證 |
| RTO | restore.py 計算還原花費時間 |
| RPO | 可說明最後一次備份後新增但未備份的資料會遺失 |
| 零信任 | backup.py / restore.py 執行前要求帳號、密碼與 MFA |
| MFA | 使用 MFA Code 模擬多因素驗證 |
| 數位韌性 | 攻擊後仍可由備份恢復核心資料 |

---

## 報告時可用說法

本 Demo 模擬一間企業的重要資料夾，在遭受勒索軟體攻擊後，原始資料被加密破壞。系統透過 3-2-1-1-0 備份概念，保留本機備份與離線備份，並在執行備份與還原前加入帳號密碼與 MFA 驗證，模擬零信任架構中「永不信任，始終驗證」的精神。最後使用 SHA-256 Hash 驗證還原資料，確認達成 0 recovery errors，展示企業數位韌性的基本流程。
