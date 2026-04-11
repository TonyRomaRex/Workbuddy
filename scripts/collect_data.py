#!/usr/bin/env python3
"""
HK Deposit Rates - 數據收集腳本
抓取各銀行最新利率數據，輸出 JSON 供生成 HTML 使用
"""
import json
import re
from datetime import datetime

# ==================== 數據源配置 ====================
HKET_MAIN = "https://wealth.hket.com/article/3947091/"
BANK_ARTICLES = {
    "南洋商業銀行": "https://wealth.hket.com/article/3909866/?lcc=aw",
    "創興銀行": "https://wealth.hket.com/article/3909893/?lcc=aw",
    "Mox Bank": "https://wealth.hket.com/article/3909934/?lcc=aw",
    "富邦銀行": "https://wealth.hket.com/article/3909896/?lcc=aw",
    "WeLab 匯立": "https://wealth.hket.com/article/3909925/?lcc=aw",
    "建行亞洲": "https://wealth.hket.com/article/3909879/?lcc=aw",
    "東亞銀行": "https://wealth.hket.com/article/3909860/?lcc=aw",
    "集友銀行": "https://wealth.hket.com/article/3909922/?lcc=aw",
    "恒生銀行": "https://wealth.hket.com/article/3909885/?lcc=aw",
    "HSBC 滙豐": "https://wealth.hket.com/article/3909928/?lcc=aw",
}

# ==================== 核實規則 ====================
MAX_AGE_DAYS = 30  #數據不超過30天
VALID_TENORS = ["1星期", "2星期", "1個月", "2個月", "3個月", "4個月", 
                "5個月", "6個月", "8個月", "9個月", "100天", "12個月",
                "18個月", "24個月", "36個月", "48個月", "2年", "3年"]

def is_valid_data(article_date_str):
    """檢查數據是否在有效期內"""
    if not article_date_str:
        return False
    # 解析類似 "2026年4月10日" 或 "April 10, 2026" 或相對時間 "11 小時前"
    if "小時前" in article_date_str or "分鐘前" in article_date_str:
        return True  #當天發布，肯定有效
    # 簡化：如果包含當前年月，視為有效
    now = datetime.now()
    if f"{now.year}年" in article_date_str and f"{now.month}月" in article_date_str:
        return True
    return False

def extract_table_data(html_content, bank_name):
    """
    從 HTML 內容中提取利率表數據
    返回格式：{tenor: {rate: "X.XX%", min_amount: "XXX", condition: "XXX"}, ...}
    """
    # 提取存款期、年利率、起存額、條件
    pass
    
def is_special_condition(rate_str, condition_text):
    """
    判斷是否為特殊條件：
    - 兌換資金
    - 新開戶 + 推薦碼
    - 限量快閃
    - 交易薈
    - 貴賓新客
    """
    special_keywords = ["兌換", "推薦碼", "限量", "快閃", "交易薈", "貴賓新客", 
                       "手機新客", "全新客戶", "新客", "指定項目"]
    for kw in special_keywords:
        if kw in condition_text:
            return True
    return False

def categorize_rate(tenor, rate_data):
    """分類利率到 新資金/現有資金/特殊條件"""
    tenor_norm = tenor.replace("年", "Y").replace("個月", "M").replace("星期", "W").replace("天", "D")
    # 邏輯：
    # - 如果條件包含"兌換" → 特殊條件
    # - 如果條件包含"新開戶"或"推薦碼" → 特殊條件
    # - 如果條件包含"新資金" → 新資金
    # - 否則 → 現有資金（不分新舊）
    pass

if __name__ == "__main__":
    print("HK Deposit Rates - 數據收集腳本")
    print(f"運行時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
