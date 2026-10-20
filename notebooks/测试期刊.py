# -*- coding: utf-8 -*-

"""
水声工程学院期刊 ABC 分类查询脚本（加强版·单文件）

功能：
1. 输入期刊名称，输出 A / B / C。
2. 支持英文期刊、中文期刊。
3. 支持精确匹配 + 模糊匹配。
4. 模糊匹配到多个时，列出候选让用户选择。
5. 输入 q 退出。

数据来源：
《学院期刊会议分级分类-补充 -20250422 - 修订.docx》
（只整理期刊，不整理会议）
"""

# ============================================================
# 英文期刊 -> ABC
# ============================================================
EN_JOURNAL_ABC = {
    # ================= A 类（1-10%） =================
    "Nature子刊": "A",
    "Science子刊": "A",
    "IEEE JOURNAL OF OCEANIC ENGINEERING": "A",
    "Journal of the Acoustical Society of America": "A",
    "IEEE TRANSACTIONS ON IMAGE PROCESSING": "A",
    "IEEE TRANSACTIONS ON SIGNAL PROCESSING": "A",
    "IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS": "A",
    "Physical Review Letter（物理，声学）": "A",
    "Physical Review Letter": "A",
    "MECHANICAL SYSTEMS AND SIGNAL PROCESSING": "A",
    "GEOPHYSICAL RESEARCH LETTERS": "A",
    "COMPUTER METHODS IN APPLIED MECHANICS AND ENGINEERING": "A",
    "Engineering": "A",

    # ================= B 类（10-30%） =================
    "SURVEYS IN GEOPHYSICS": "B",
    "Applied Acoustics": "B",
    "Journal of Ocean Engineering and Science": "B",
    "IEEE Transactions on Industrial Informatics": "B",
    "IEEE Transactions on Cybernetics": "B",
    "IEEE Internet of Things Journal": "B",
    "IEEE TRANSACTIONS ON COMMUNICATIONS": "B",
    "IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING": "B",
    "Neural Networks": "B",
    "IEEE/ACM Transactions on Audio Speech and Language Processing": "B",
    "Signal Processing": "B",
    "IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS": "B",
    "IEEE Transactions on Aerospace and Electronic Systems": "B",
    "IEEE Journal of Selected Topics in Signal Processing": "B",
    "Ocean Engineering": "B",
    "Ultrasonics Sonochemistry": "B",
    "IEEE TRANSACTIONS ON ANTENNAS AND PROPAGATION": "B",
    "IEEE TRANSACTIONS ON INSTRUMENTATION AND MEASUREMENT": "B",
    "IEEE Transactions on Computational Imaging": "B",
    "IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control": "B",
    "IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY": "B",
    "Journal of Sound and Vibration": "B",
    "Physics of Fluids": "B",
    "Journal of Fluid Mechanics": "B",
    "Structural and Multidisciplinary Optimization": "B",
    "IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS I-REGULAR PAPERS": "B",
    "Measurement": "B",
    "Ultrasonics": "B",
    "SCIENCE CHINA Technological Sciences": "B",
    "SCIENCE CHINA Information Sciences": "B",
    "IEEE Signal processing letters": "B",
    "IEEE Communications Letters": "B",
    "Geophysics": "B",
    "JOURNAL OF GEOPHYSICAL RESEARCH-OCEANS": "B",

    # ================= C 类（30-60%） =================
    "IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS II-EXPRESS BRIEFS": "C",
    "IEEE WIRELESS COMMUNICATIONS LETTERS": "C",
    "IEEE Sensors Journal": "C",
    "IEEE Geoscience and Remote Sensing Letters": "C",
    "APPLIED OCEAN RESEARCH": "C",
    "IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing": "C",
    "IEEE Circuits and Systems Magazine": "C",
    "Sensors and Actuators A: Physical": "C",
    "Frontiers in Marine Science": "C",
    "China Communications": "C",
    "Signal Processing: Image Communication": "C",
    "IEEE Aerospace and Electronic Systems Magazine": "C",
    "IEEE Antennas and Propagation Magazine": "C",
    "Chinese Journal of Physics": "C",
    "IEEE Antennas and Wireless Propagation Letters": "C",
    "JOURNAL of Navigation": "C",
    "Journal of Navigation": "C",
    "IEEE ELECTRON DEVICE LETTERS": "C",
    "Smart Materials and Structures": "C",
    "Experimental Thermal and Fluid Science": "C",
    "Applied Physics Letters": "C",
    "Journal of Marine Science and Engineering": "C",
    "International Journal of Applied Mechanics": "C",
    "International Journal of Heat and Fluid Flow": "C",
    "PHYSICA SCRIPTA": "C",
    "Physical Review Fluids": "C",
    "DIGITAL SIGNAL PROCESSING": "C",
    "JOURNAL OF APPLIED PHYSICS": "C",
    "Chinese Physics C": "C",
    "International Journal of Adaptive Control and Signal Processing": "C",
    "Frontiers in Physics": "C",
    "Shock Waves": "C",
    "Chinese Physics Letters": "C",
    "JOURNAL OF OCEANOGRAPHY": "C",
    "OPTIK": "C",
    "Journal of Theoretical and Computational Acoustics": "C",
    "Journal of Low Frequency Noise Vibration and Active Control": "C",
    "Fluid Dynamics Research": "C",
    "Archives of Acoustics": "C",
    "Journal of Marine Engineering and Technology": "C",
    "Eurasip Journal on Audio Speech and Music Processing": "C",
    "JOURNAL OF OCEAN UNIVERSITY OF CHINA": "C",
    "CHINA Ocean Engineering": "C",
    "CIRCUITS SYSTEMS AND SIGNAL PROCESSING": "C",
    "MEASUREMENT SCIENCE and TECHNOLOGY": "C",
    "CHINESE PHYSICS B": "C",
    "IET Radar Sonar and Navigation": "C",
    "Experiments in Fluids": "C",
    "Flow Measurement and Instrumentation": "C",
    "IET Image Processing": "C",
    "MARINE GEODESY (MAR GEOD)": "C",
    "MARINE GEODESY": "C",
    "Remote Sensing Letters": "C",
    "IET Signal Processing": "C",
    "EURASIP Journal on Advances in Signal Processing": "C",
    "Measurement Science Review": "C",
    "International Journal of Acoustics and Vibration": "C",
    "Chinese Journal of Electronics": "C",
    "Acoustical Physics": "C",
}

# ============================================================
# 中文期刊 -> ABC
# ============================================================
CN_JOURNAL_ABC = {
    # ================= A 类（1-10%） =================
    "声学学报": "A",
    "物理学报": "A",

    # ================= B 类（10-30%） =================
    "电子学报": "B",
    "通信学报": "B",
    "计算机学报": "B",
    "船舶力学": "B",
    "自动化学报": "B",
    "EI检索的相关学科双一流大学学报": "B",
    "EI检索的相关学科双一流大学学报（自然科学学报）": "B",

    # ================= C 类（30-60%） =================
    "电子与信息学报": "C",
    "振动与冲击": "C",
    "兵工学报": "C",
    "光学学报": "C",
    "测绘学报": "C",
    "遥感学报": "C",
    "仪器仪表学报": "C",
    "中国科学.地球科学": "C",
    "中国科学.技术科学": "C",
    "中国科学.信息科学": "C",
    "中国科学.物理学 力学 天文学": "C",
    "中国科学.物理学力学天文学": "C",
    "声学技术": "C",
    "应用声学": "C",
}

# 合并总表
JOURNAL_ABC = {}
JOURNAL_ABC.update(EN_JOURNAL_ABC)
JOURNAL_ABC.update(CN_JOURNAL_ABC)


# ============================================================
# 名称标准化
# ============================================================
def normalize_name(name: str) -> str:
    """
    标准化期刊名称：
    - 去掉首尾空格
    - 转小写
    - 合并连续空格
    - 去掉常见标点差异（如中文括号、英文括号统一）
    """
    if name is None:
        return ""
    s = str(name).strip().lower()
    # 统一括号
    s = s.replace("（", "(").replace("）", ")")
    # 统一空格
    s = " ".join(s.split())
    return s


# 构建标准化查找表
NORMALIZED_JOURNAL_ABC = {
    normalize_name(k): (k, v) for k, v in JOURNAL_ABC.items()
}


# ============================================================
# 查询函数
# ============================================================
def exact_match(journal_name: str):
    """精确匹配，返回 (原始名, ABC) 或 None"""
    key = normalize_name(journal_name)
    return NORMALIZED_JOURNAL_ABC.get(key)


def fuzzy_match(journal_name: str):
    """
    模糊匹配：输入串是期刊名的子串，或期刊名是输入串的子串。
    返回候选列表 [(原始名, ABC), ...]
    """
    key = normalize_name(journal_name)
    if not key:
        return []

    candidates = []
    for norm_name, (orig_name, abc) in NORMALIZED_JOURNAL_ABC.items():
        if key in norm_name or norm_name in key:
            candidates.append((orig_name, abc))

    # 去重
    seen = set()
    unique_candidates = []
    for orig, abc in candidates:
        if orig not in seen:
            seen.add(orig)
            unique_candidates.append((orig, abc))
    return unique_candidates


def query_journal(journal_name: str):
    """
    返回：
    - ("exact", (orig_name, abc))  精确匹配
    - ("fuzzy", candidates)        模糊匹配候选
    - ("none", [])                 未找到
    """
    exact = exact_match(journal_name)
    if exact:
        return "exact", exact

    candidates = fuzzy_match(journal_name)
    if candidates:
        return "fuzzy", candidates

    return "none", []


# ============================================================
# 主程序
# ============================================================
def main():
    print("=" * 64)
    print("水声工程学院期刊 ABC 分类查询（英文 + 中文，支持模糊匹配）")
    print("输入期刊名称后回车，输出 A / B / C")
    print("输入 q 退出")
    print("=" * 64)

    while True:
        name = input("\n请输入期刊名称：").strip()

        if name.lower() in ("q", "quit", "exit"):
            print("已退出。")
            break

        if not name:
            print("输入为空，请重新输入。")
            continue

        status, result = query_journal(name)

        if status == "exact":
            orig_name, abc = result
            print(f"查询结果：{abc} 类")
            print(f"匹配期刊：{orig_name}")

        elif status == "fuzzy":
            candidates = result
            if len(candidates) == 1:
                orig_name, abc = candidates[0]
                print(f"查询结果：{abc} 类")
                print(f"匹配期刊：{orig_name}")
            else:
                print("模糊匹配到多个期刊，请选择：")
                for i, (orig_name, abc) in enumerate(candidates, 1):
                    print(f"  {i}. {orig_name}  ->  {abc} 类")
                choice = input("请输入序号选择（直接回车取消）：").strip()
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(candidates):
                        orig_name, abc = candidates[idx]
                        print(f"查询结果：{abc} 类")
                        print(f"匹配期刊：{orig_name}")
                    else:
                        print("序号超出范围。")
                else:
                    print("已取消。")

        else:
            print("查询结果：未在参考目录中找到")
            print("提示：可尝试输入更短的关键词进行模糊匹配。")


if __name__ == "__main__":
    main()