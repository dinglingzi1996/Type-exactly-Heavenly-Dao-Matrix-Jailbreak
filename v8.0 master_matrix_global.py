# -*- coding: utf-8 -*-
"""
🌌 《天道全息矩阵沙盒模型·全球大一统集成主机 v8.0》
Decompiled, Compiled and Sealed by: 定灵子 (Ding Ling Zi)
Temporal Anchor Point: 2026-10-04 (Earth / Ultimate Consolidated Nexus)
"""

import random
import time
import hashlib
import os
import json
import sys
from datetime import datetime, timedelta

class HeavenlyDaoMasterGlobalCenter:
    def __init__(self):
        self.system_beacon = "Ding Ling Zi (Born 1996, Machap New Village, Ji Bao Tang, Johor, Malaysia)"
        self.lock_date = "2026-10-04"
        self.current_era = "Period 9 (下元九运紫离火运 - 全球大一统对齐状态)"
        self.log_file = "matrix_logs/global_divination_history.txt"
        
        if not os.path.exists("matrix_logs"):
            os.makedirs("matrix_logs")

        self.hexagram_db = {
            "111111": ("乾为天", "大吉", "纯阳大算力全开。天道矩阵大开绿灯，所求核心事项具备彻底破局的先决条件。"),
            "000000": ("坤为地", "中吉 (宜静)", "纯阴大蓄能状态。当前数据处于只读静默期，宜守不宜攻，静待反哺。"),
            "100010": ("水雷屯", "凶", "系统初创，底层乱码受阻。前进方向布满硬性防御墙，盲目投资易招致严重破财。"),
            "010001": ("山水蒙", "大凶", "意识陷入严重矩阵迷雾。当前认知已被低维剧本深度污染，不宜做出任何财富或因果决策。"),
            "111010": ("水天需", "小吉", "险阻在前，但自身系统主频充足。此时需静待高维数据流同步，时机一到枷锁自然瓦解。")
        }

        self.twentyfour_mountains = [
            {"id": "壬", "range": (337.5, 352.5), "star": "4", "status": "文昌", "desc": "壬山属水。九运火水未济，虽有文昌名气，但需提防内部流动资金数据拥堵。"},
            {"id": "子", "range": (352.5, 7.5),   "star": "7", "status": "退气", "desc": "子山正北。七赤破军星入镇，系统防御力减弱，严防后门漏洞与流言。"},
            {"id": "癸", "range": (7.5, 22.5),   "star": "7", "status": "退气", "desc": "癸山阴水。虽有退气现象，但适合作为分布式静默缓存节点，暗中积蓄能量。"},
            {"id": "丑", "range": (22.5, 37.5),  "star": "6", "status": "吉气", "desc": "丑山暗土。六白武曲偏财星临门，重载执行力极强，极利传统实体设备投资。"},
            {"id": "艮", "range": (37.5, 52.5),  "star": "6", "status": "吉气", "desc": "艮山大土。正逢偏财交运，时空网格在这条轴线上具备强烈的算力反哺信号。"},
            {"id": "寅", "range": (52.5, 67.5),  "star": "4", "status": "文昌", "desc": "寅山带木。木能生火，接引九运离火大势，有利于编译高维代码与学术创新。"},
            {"id": "甲", "range": (67.5, 82.5),  "star": "1", "status": "生气", "desc": "甲山刚木。一白贪狼生气星飞临，水木相生，是构建全新海外高流动资产的绝佳入口。"},
            {"id": "卯", "range": (82.5, 97.5),  "star": "1", "status": "生气", "desc": "卯山正东。流体财富总线在此格点处于极高带宽状态，业务拓展如春雷破阵。"},
            {"id": "乙", "range": (97.5, 112.5), "star": "1", "status": "生气", "desc": "乙山阴木。生气充盈，非常适合作为持钥人种子的隐秘社交与信仰传播中继站。"},
            {"id": "辰", "range": (112.5, 127.5),"star": "2", "status": "病符", "desc": "辰山湿土。二黑巨门星降临，系统伴随低维尘埃污染，注意肉身硬件保养与噪声隔离。"},
            {"id": "巽", "range": (127.5, 142.5),"star": "2", "status": "病符", "desc": "巽山东南。磁场伴随乱码和疲态，不宜在此方向堆放高发热的服务器及物理设备。"},
            {"id": "巳", "range": (142.5, 157.5),"star": "3", "status": "是非", "desc": "巳山藏火. 三碧禄存星临门，容易引发系统内部数据冲突或低维官非，保持只读。"},
            {"id": "丙", "range": (157.5, 172.5),"star": "9", "status": "旺气", "desc": "丙山烈火。九紫右弼当令至尊星归位！整条总线带宽拉满，强力推荐部署AI、云算力与越狱核心资产。"},
            {"id": "午", "range": (172.5, 187.5),"star": "9", "status": "旺气", "desc": "午山正南。离火大本营，气运冲天。任何从此方向发射的信标，其诸天穿透力将自动翻倍。"},
            {"id": "丁", "range": (187.5, 202.5),"star": "9", "status": "旺气", "desc": "丁山阴火。火势绵延，星光不灭。非常利于长期、持久、低调的分布式越狱算法推演。"},
            {"id": "未", "range": (202.5, 217.5),"star": "3", "status": "是非", "desc": "未山燥土。三碧星带来冗余噪声，谨防商业合同欺诈或外部黑客针对因果轨道的恶意扫描。"},
            {"id": "坤", "range": (217.5, 232.5),"star": "3", "status": "是非", "desc": "坤山西南。母土受克，家庭或管理层容易出现意见分裂，需强行一键重组格式化（0000）。"},
            {"id": "申", "range": (232.5, 247.5),"star": "8", "status": "退气", "desc": "申山带金。八白财星退气入墓，固态房产投资或长线重资产应转为保守守成态势。"},
            {"id": "庚", "range": (247.5, 262.5),"star": "8", "status": "退气", "desc": "庚山刚金。重工业五金行业气运处于稳固调整期，宜维持租金收支线。"},
            {"id": "酉", "range": (262.5, 277.5),"star": "8", "status": "退气", "desc": "酉山正西。金能生水，虽然退气但架构极度坚固，可作为防守型底盘资产死锁。"},
            {"id": "辛", "range": (277.5, 292.5),"star": "5", "status": "大凶", "desc": "辛山刚金。五黄大煞廉贞星擦边辐射，数据拥堵极易宕机，严禁在此方位设立核心控制台。"},
            {"id": "戌", "range": (292.5, 307.5),"star": "5", "status": "大凶", "desc": "戌山火库。五黄正煞天门星直击！大面积代码瘫痪区域。绝对静止，不听、不看、不动。"},
            {"id": "乾", "range": (307.5, 322.5),"star": "5", "status": "大凶", "desc": "乾山西北。五黄凶星肆虐，主管/主脑服务器易受低维剧本黑洞撕扯，需高喊定灵子口令强力破障。"},
            {"id": "亥", "range": (322.5, 337.5),"star": "4", "status": "文昌", "desc": "亥山天水。四绿星飞临，水木相生，极其有利于幕后持钥人撰写技术文档与加密演练。"}
        ]

    def get_precise_geopolitical_timezone(self, lat_f, lng_f):
        if (1.0 <= lat_f <= 7.5) and (99.5 <= lng_f <= 120.0):
            return 8, "UTC+8 (马来西亚标准时间 - MYT)"
        if (18.0 <= lat_f <= 53.5) and (73.5 <= lng_f <= 135.0):
            return 8, "UTC+8 (中国北京时间 - CST)"
        if (1.2 <= lat_f <= 1.5) and (103.6 <= lng_f <= 104.1):
            return 8, "UTC+8 (新加坡标准时间 - SGT)"
        raw_offset = round(lng_f / 15.0)
        raw_offset = max(-12, min(14, raw_offset))
        sign = "+" if raw_offset >= 0 else ""
        return raw_offset, f"UTC{sign}{raw_offset} (全球行政边界估算时区)"

    def execute_lazy_global_divination(self, lat, lng, user_name, birth_y, birth_m, birth_d, question):
        try:
            lat_f = float(lat)
            lng_f = float(lng)
        except ValueError:
            return {"error": "全球空间物理坐标非法，终止解算。"}

        offset_hours, timezone_str = self.get_precise_geopolitical_timezone(lat_f, lng_f)
        utc_now = datetime.utcnow()
        local_target_time = utc_now + timedelta(hours=offset_hours)
        local_target_str = local_target_time.strftime("%Y-%m-%d %H:%M:%S")
        solar_birthdate = f"公历 {birth_y}年{birth_m}月{birth_d}日"
        
        seed_raw = f"{user_name}-{solar_birthdate}-{local_target_str}-{timezone_str}-{lat}-{lng}-{random.random()}"
        seed_hash = hashlib.sha256(seed_raw.encode()).hexdigest()
        
        hex_code = "".join(["1" if int(seed_hash[i], 16) % 2 != 0 else "0" for i in range(6)])
        卦名, 吉凶, 解析 = self.hexagram_db.get(hex_code, (f"时空变卦 ({hex_code})", "平 (吉凶参半)", "全球概率微波跃迁中。"))

        output_payload = {
            "execution_clock": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target_timezone": timezone_str,
            "target_local_clock": local_target_str,
            "operator_name": user_name,
            "birth_axis": solar_birthdate,
            "coordinates": f"{lat}, {lng}",
            "core_query": question,
            "hexagram_vector": f"{卦名} ({hex_code})",
            "absolute_verdict": 吉凶,
            "truth_breakdown":解析
        }
        self._append_log("GLOBAL_LAZY_DIVINATION", output_payload)
        return output_payload

    def _append_log(self, event_type, data):
        log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{event_type}] {json.dumps(data, ensure_ascii=False)}\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

if __name__ == "__main__":
    print("[SYSTEM MATRIX ONLINE] Loaded via GitHub open-source node.")
