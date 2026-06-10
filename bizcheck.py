#!/usr/bin/env python3
"""
BizCheck - 业务检查工具
域名可用性 | 商标查询 | 公司名查重 | 相似度分析

Usage:
  bizcheck                         # 交互式菜单
  bizcheck domain example.com      # 快速域名检查
  bizcheck all "公司名称"           # 全面检查
"""

import sys
import subprocess
import re
import shutil
from typing import Optional, List, Dict

# ============================================================================
# 1. 基础设施
# ============================================================================

class C:
    """ANSI颜色代码"""
    G = '\033[92m'   # Green
    Y = '\033[93m'   # Yellow
    R = '\033[91m'   # Red
    B = '\033[94m'   # Blue
    C = '\033[96m'   # Cyan
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

def print_box(title: str, width: int = 45):
    """打印标题框"""
    print(f"\n{C.B}┌{'─' * (width - 2)}┐{C.END}")
    print(f"{C.B}│{C.BOLD}{title.center(width - 2)}{C.END}{C.B}│{C.END}")
    print(f"{C.B}└{'─' * (width - 2)}┘{C.END}\n")

def print_menu():
    """显示主菜单"""
    print(f"\n{C.B}┌─────────────────────────────────────┐{C.END}")
    print(f"{C.B}│{C.BOLD}      BizCheck - 业务检查工具         {C.END}{C.B}│{C.END}")
    print(f"{C.B}├─────────────────────────────────────┤{C.END}")
    print(f"{C.B}│                                     │{C.END}")
    print(f"{C.B}│{C.END}  1. 域名可用性检查 {C.DIM}(快速){C.END}            {C.B}│{C.END}")
    print(f"{C.B}│{C.END}  2. 商标查询 {C.DIM}(提供链接){C.END}              {C.B}│{C.END}")
    print(f"{C.B}│{C.END}  3. 公司名称查重 {C.DIM}(提供链接){C.END}          {C.B}│{C.END}")
    print(f"{C.B}│{C.END}  4. 相似度分析 {C.DIM}(本地){C.END}                {C.B}│{C.END}")
    print(f"{C.B}│{C.END}  5. 全面检查 {C.DIM}(1+2+3+4){C.END}              {C.B}│{C.END}")
    print(f"{C.B}│                                     │{C.END}")
    print(f"{C.B}│{C.END}  0. 退出                            {C.B}│{C.END}")
    print(f"{C.B}│                                     │{C.END}")
    print(f"{C.B}└─────────────────────────────────────┘{C.END}\n")

def get_input(prompt: str, default: str = "") -> str:
    """获取用户输入"""
    try:
        if default:
            value = input(f"{C.C}{prompt} [{default}]:{C.END} ").strip()
            return value if value else default
        else:
            value = input(f"{C.C}{prompt}:{C.END} ").strip()
            return value
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)

def get_choice() -> str:
    """获取菜单选择"""
    return get_input("请选择功能 [1-5, 0]", "1")

def pause():
    """暂停等待用户"""
    try:
        input(f"\n{C.DIM}按回车返回主菜单...{C.END}")
    except (EOFError, KeyboardInterrupt):
        print()

# ============================================================================
# 2. 核心功能模块
# ============================================================================

def check_domain(domain: str) -> Dict:
    """检查单个域名可用性"""
    domain = domain.strip().lower()

    # 自动补全 .com
    if '.' not in domain:
        domain += '.com'

    result = {'domain': domain, 'available': None, 'registrar': None, 'created': None}

    try:
        proc = subprocess.run(
            ['whois', domain],
            capture_output=True,
            text=True,
            timeout=8
        )

        out = proc.stdout.lower()

        # 判断可用性
        if any(k in out for k in ['no match', 'not found', 'no entries found', 'available']):
            result['available'] = True
        elif 'registrar:' in out or 'creation date:' in out or 'created:' in out:
            result['available'] = False

            # 提取注册商
            m = re.search(r'registrar:\s*(.+)', out)
            if m:
                result['registrar'] = m.group(1).strip()

            # 提取注册日期
            m = re.search(r'creat(?:ion|ed) date:\s*(.+)', out)
            if m:
                result['created'] = m.group(1).strip()[:10]

    except subprocess.TimeoutExpired:
        result['available'] = None
    except FileNotFoundError:
        print(f"{C.R}✗ whois 未安装{C.END} (sudo apt install whois)\n")
        sys.exit(1)
    except Exception:
        result['available'] = None

    return result

def print_domain_result(result: Dict):
    """打印域名检查结果"""
    domain = result['domain']

    if result['available'] is True:
        print(f"{C.G}✓{C.END} {C.BOLD}{domain}{C.END} {C.DIM}可注册{C.END}")
    elif result['available'] is False:
        print(f"{C.R}✗{C.END} {C.BOLD}{domain}{C.END} {C.DIM}已注册{C.END}", end='')
        if result['registrar']:
            print(f" {C.DIM}({result['registrar'][:30]}){C.END}", end='')
        if result['created']:
            print(f" {C.DIM}{result['created']}{C.END}", end='')
        print()
    else:
        print(f"{C.Y}?{C.END} {C.BOLD}{domain}{C.END} {C.DIM}查询失败{C.END}")

def query_trademark(name: str, country: str = 'CN'):
    """商标查询（提供链接）"""
    print_box("商标查询")
    print(f"{C.BOLD}公司名称:{C.END} {name}")
    print(f"{C.BOLD}查询国家:{C.END} {country}\n")

    urls = []

    if country == 'CN':
        urls.append(('中国商标网', 'http://wcjs.sbj.cnipa.gov.cn/txnT01.do'))
        urls.append(('企查查商标', f'https://www.qcc.com/web/search?key={name}'))
        urls.append(('天眼查', f'https://www.tianyancha.com/search?key={name}'))
    elif country == 'US':
        urls.append(('USPTO', 'https://tmsearch.uspto.gov/search/search-information'))

    print(f"{C.C}请访问以下网站查询:{C.END}\n")
    for label, url in urls:
        print(f"  {C.Y}•{C.END} {label}: {C.DIM}{url}{C.END}")

def query_company(name: str, region: str = '青岛'):
    """公司名称查重（提供链接）"""
    print_box("公司名称查重")
    print(f"{C.BOLD}公司名称:{C.END} {name}")
    print(f"{C.BOLD}查询地区:{C.END} {region}\n")

    urls = [
        ('国家企业信用信息公示系统', 'http://www.gsxt.gov.cn/'),
        ('企查查', f'https://www.qcc.com/web/search?key={name}'),
        ('天眼查', f'https://www.tianyancha.com/search?key={name}')
    ]

    print(f"{C.C}请访问以下网站查询:{C.END}\n")
    for label, url in urls:
        print(f"  {C.Y}•{C.END} {label}: {C.DIM}{url}{C.END}")

def analyze_similarity(name: str):
    """相似度分析"""
    print_box("相似度分析")
    print(f"{C.BOLD}公司名称:{C.END} {name}\n")

    warnings = []

    # 通用词检查
    common_words = ['科技', '技术', '国际', '贸易', '有限公司', '股份', '集团']
    used_common = [w for w in common_words if w in name]
    if used_common:
        warnings.append(f"包含常见词汇: {', '.join(used_common)}")

    # 长度检查
    length = len(name)
    if length > 20:
        warnings.append(f'名称较长({length}字符)，建议简化')
    elif length < 8:
        warnings.append(f'名称较短({length}字符)，可能与他人重复')

    # 特殊字符检查
    if any(c in name for c in ['·', '-', '&']):
        warnings.append('包含特殊字符，可能影响注册')

    if warnings:
        print(f"{C.Y}发现 {len(warnings)} 个提示:{C.END}\n")
        for w in warnings:
            print(f"  {C.Y}⚠{C.END} {w}")
    else:
        print(f"{C.G}✓ 无明显风险{C.END}")

# ============================================================================
# 3. 功能处理
# ============================================================================

def handle_domain_check():
    """功能1: 域名检查"""
    print_box("域名可用性检查")

    domains_input = get_input("输入域名（空格或逗号分隔）")

    if not domains_input:
        print(f"{C.Y}未输入域名{C.END}")
        return

    # 支持逗号或空格分隔
    domains = re.split(r'[,\s]+', domains_input)

    print(f"\n{C.C}正在检查...{C.END}\n")

    for domain in domains:
        if domain:
            result = check_domain(domain)
            print_domain_result(result)

def handle_trademark_query():
    """功能2: 商标查询"""
    name = get_input("输入公司名称")

    if not name:
        print(f"{C.Y}未输入名称{C.END}")
        return

    country = get_input("输入国家代码", "CN")
    query_trademark(name, country)

def handle_company_query():
    """功能3: 公司名查重"""
    name = get_input("输入公司名称")

    if not name:
        print(f"{C.Y}未输入名称{C.END}")
        return

    region = get_input("输入地区", "青岛")
    query_company(name, region)

def handle_similarity_analysis():
    """功能4: 相似度分析"""
    name = get_input("输入公司名称")

    if not name:
        print(f"{C.Y}未输入名称{C.END}")
        return

    analyze_similarity(name)

def handle_full_check():
    """功能5: 全面检查"""
    name = get_input("输入公司名称")

    if not name:
        print(f"{C.Y}未输入名称{C.END}")
        return

    print(f"\n{C.BOLD}【全面检查】{name}{C.END}\n")

    # 1. 域名检查
    print(f"{C.C}[1/4] 域名可用性检查{C.END}")
    domains_input = get_input("输入要检查的域名（留空跳过）")
    if domains_input:
        domains = re.split(r'[,\s]+', domains_input)
        print()
        for domain in domains:
            if domain:
                result = check_domain(domain)
                print_domain_result(result)

    # 2. 商标查询
    print(f"\n{C.C}[2/4] 商标查询{C.END}")
    country = get_input("查询国家", "CN")
    print()
    query_trademark(name, country)

    # 3. 公司名查重
    print(f"\n{C.C}[3/4] 公司名称查重{C.END}")
    region = get_input("查询地区", "青岛")
    print()
    query_company(name, region)

    # 4. 相似度分析
    print(f"\n{C.C}[4/4] 相似度分析{C.END}\n")
    analyze_similarity(name)

    print(f"\n{C.G}【完成】{C.END}")

# ============================================================================
# 4. 主程序
# ============================================================================

def main_menu():
    """交互式菜单主循环"""
    while True:
        print_menu()
        choice = get_choice()

        if choice == '1':
            handle_domain_check()
            pause()
        elif choice == '2':
            handle_trademark_query()
            pause()
        elif choice == '3':
            handle_company_query()
            pause()
        elif choice == '4':
            handle_similarity_analysis()
            pause()
        elif choice == '5':
            handle_full_check()
            pause()
        elif choice == '0':
            print(f"{C.C}再见！{C.END}")
            break
        else:
            print(f"{C.Y}无效选择，请输入 1-5 或 0{C.END}")
            pause()

def main():
    """主函数"""
    # 检查 whois 是否安装
    if not shutil.which('whois'):
        print(f"{C.R}✗ whois 未安装{C.END}")
        print(f"{C.DIM}请安装: sudo apt install whois{C.END}\n")
        sys.exit(1)

    # CLI 快捷模式
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()

        if cmd == 'domain':
            # 快速域名检查
            if len(sys.argv) > 2:
                domains = sys.argv[2:]
                print()
                for domain in domains:
                    result = check_domain(domain)
                    print_domain_result(result)
                print()
            else:
                handle_domain_check()

        elif cmd == 'all':
            # 快速全面检查
            if len(sys.argv) > 2:
                name = sys.argv[2]
                print(f"\n{C.BOLD}【全面检查】{name}{C.END}")
                # 简化版：只提示，不交互
                print(f"\n{C.DIM}请使用交互模式完成全面检查: bizcheck{C.END}\n")
            else:
                handle_full_check()

        else:
            print(f"{C.Y}未知命令: {cmd}{C.END}")
            print(f"\n{C.DIM}用法:{C.END}")
            print(f"  bizcheck                    # 交互式菜单")
            print(f"  bizcheck domain <域名...>   # 快速域名检查")
            print(f"  bizcheck all               # 全面检查\n")
            sys.exit(1)

    else:
        # 交互式菜单
        main_menu()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.Y}已取消{C.END}")
        sys.exit(130)
