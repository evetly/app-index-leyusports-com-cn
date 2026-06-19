import json
from datetime import datetime

SITE_DATA = {
    "name": "乐鱼体育",
    "url": "https://app-index-leyusports.com.cn",
    "tags": ["体育", "娱乐", "综合平台"],
    "description": "乐鱼体育是一个专注于体育赛事与娱乐互动的综合平台，提供多元化的体育内容和互动体验。",
    "keywords": ["乐鱼体育", "体育赛事", "在线娱乐", "体育资讯"],
    "creation_seed": "574514abea6df081"
}

def generate_summary(data: dict) -> str:
    """生成站点结构化摘要"""
    lines = []
    lines.append("=" * 50)
    lines.append("站点摘要报告")
    lines.append("=" * 50)
    lines.append(f"站点名称: {data['name']}")
    lines.append(f"站点URL: {data['url']}")
    lines.append(f"标签: {', '.join(data['tags'])}")
    lines.append(f"关键词: {', '.join(data['keywords'])}")
    lines.append(f"简要说明: {data['description']}")
    lines.append("-" * 50)
    return "\n".join(lines)

def format_json_output(data: dict) -> str:
    """返回结构化的JSON格式摘要"""
    output = {
        "site_name": data["name"],
        "site_url": data["url"],
        "tags": data["tags"],
        "keywords": data["keywords"],
        "description": data["description"],
        "generated_at": datetime.now().isoformat()
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def write_report_to_file(data: dict, filename: str = "site_summary_report.txt") -> None:
    """将文本摘要写入文件"""
    summary = generate_summary(data)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"报告已写入: {filename}")

def display_compact_info(data: dict) -> None:
    """以紧凑格式显示站点信息"""
    info = f"[{data['name']}]({data['url']}) — 关键词: {', '.join(data['keywords'][:3])}"
    print("紧凑信息:", info)

def main() -> None:
    print("正在处理站点资料...\n")
    data = SITE_DATA.copy()

    # 输出文本摘要
    summary = generate_summary(data)
    print(summary)

    # 输出JSON摘要
    print("\nJSON格式输出:")
    print(format_json_output(data))

    # 写入文件
    write_report_to_file(data)

    # 紧凑显示
    display_compact_info(data)

    print("\n处理完成。")

if __name__ == "__main__":
    main()