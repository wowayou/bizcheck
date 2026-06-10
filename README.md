# BizCheck - 业务检查工具

快速检查域名可用性、商标注册、公司名称查重的命令行工具。

## 功能

- ✅ **域名可用性检查** — 基于 whois 实时查询
- ✅ **商标查询** — 提供官方查询链接（中国商标网、企查查、天眼查）
- ✅ **公司名称查重** — 提供国家企业信用查询链接
- ✅ **相似度分析** — 本地分析常见词汇、长度、特殊字符
- ✅ **全面检查** — 一键执行所有检查

## 安装

### 1. 系统依赖

```bash
# Debian/Ubuntu
sudo apt install whois

# macOS
brew install whois
```

### 2. 下载工具

```bash
git clone <your-repo-url> ~/Dev/devtools
chmod +x ~/Dev/devtools/bizcheck.py
```

### 3. 添加到 PATH（可选）

```bash
# 创建软链接
mkdir -p ~/bin  # 如果目录不存在，先创建
ln -s ~/Dev/devtools/bizcheck.py ~/bin/bizcheck

# 确保 ~/bin 在 PATH 中
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 使用方式

### 交互式菜单

```bash
bizcheck
```

会显示菜单：
```
┌─────────────────────────────────────┐
│      BizCheck - 业务检查工具         │
├─────────────────────────────────────┤
│  1. 域名可用性检查 (快速)            │
│  2. 商标查询 (提供链接)              │
│  3. 公司名称查重 (提供链接)          │
│  4. 相似度分析 (本地)                │
│  5. 全面检查 (1+2+3+4)              │
│  0. 退出                            │
└─────────────────────────────────────┘
```

### 快捷命令

```bash
# 快速检查域名
bizcheck domain tradebridge.com sourcebridge.com

# 快速全面检查
bizcheck all
```

## 输出示例

### 域名检查
```
✓ tradebridge.com 可注册
✗ sourcebridge.com 已注册 (GoDaddy.com, LLC) 2015-03-12
? example123456.com 查询失败
```

### 商标查询
```
【商标查询】
公司名称: 青岛贸桥国际贸易有限公司
查询国家: CN

请访问以下网站查询:
  • 中国商标网: http://wcjs.sbj.cnipa.gov.cn/txnT01.do
  • 企查查商标: https://www.qcc.com/web/search?key=...
  • 天眼查: https://www.tianyancha.com/search?key=...
```

### 相似度分析
```
【相似度分析】
公司名称: 青岛贸桥国际贸易有限公司

发现 2 个提示:
  ⚠ 包含常见词汇: 国际, 贸易, 有限公司
  ⚠ 名称较长(15字符)，建议简化
```

## 技术说明

- **Python 版本**：3.7+
- **依赖**：仅标准库（subprocess, re, sys, shutil）
- **外部工具**：whois 命令
- **超时设置**：8秒/域名
- **编码**：UTF-8

## 错误处理

```bash
# whois 未安装
✗ whois 未安装
请安装: sudo apt install whois

# 域名查询超时
? example.com 查询失败

# 用户中断（Ctrl+C）
已取消
```

## 开发

```bash
# 测试
python3 bizcheck.py domain test.com

# 调试
python3 -u bizcheck.py  # unbuffered output
```

## License

MIT
