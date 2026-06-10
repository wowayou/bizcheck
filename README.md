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
git clone git@github.com:wowayou/bizcheck.git ~/Dev/devtools
cd ~/Dev/devtools
chmod +x bizcheck.py
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

# 自动补全 .com
bizcheck domain example test google

# 快速全面检查
bizcheck all
```

## 输出示例

### 域名检查
```bash
$ bizcheck domain tradebridge.com google.com test123xyz.com

✓ tradebridge.com 可注册
✗ google.com 已注册 (markmonitor inc.) 1997-09-15
✗ test123xyz.com 已注册 (namecheap, inc.) 2020-01-15

在线验证（可选）:
  • https://who.is/whois/<domain>
  • https://domainanalyzer.com/
```

### 商标查询
```bash
$ bizcheck  # 选择菜单 2

┌───────────────────────┐
│       商标查询        │
└───────────────────────┘

公司名称: 青岛贸桥国际贸易有限公司
查询国家: CN

请访问以下网站查询:
  • 中国商标网: http://wcjs.sbj.cnipa.gov.cn/txnT01.do
  • 企查查商标: https://www.qcc.com/web/search?key=青岛贸桥国际贸易有限公司
  • 天眼查: https://www.tianyancha.com/search?key=青岛贸桥国际贸易有限公司
```

### 相似度分析
```bash
$ bizcheck  # 选择菜单 4

┌───────────────────────┐
│      相似度分析       │
└───────────────────────┘

公司名称: 青岛贸桥国际贸易有限公司

发现 3 个提示:
  ⚠ 包含常见词汇: 国际, 贸易, 有限公司
  ⚠ 名称较长(15字符)，建议简化
```

## 占位符说明

在代码中使用占位符时，请按以下规范：

```bash
# 域名占位符
bizcheck domain <your-domain>.com <another-domain>.com

# 公司名称占位符
bizcheck  # 然后输入: <您的公司名称>

# 示例
bizcheck domain example.com test.com
```

## 技术说明

- **Python 版本**：3.7+
- **依赖**：仅标准库（subprocess, re, sys, shutil）
- **外部工具**：whois 命令
- **超时设置**：8秒/域名
- **编码**：UTF-8
- **支持平台**：Linux, macOS, WSL

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
# 测试域名检查
python3 bizcheck.py domain test.com

# 调试模式
python3 -u bizcheck.py  # unbuffered output

# 查看代码
cat bizcheck.py | grep -A 5 "def check_domain"
```

## 常见问题

**Q: 域名显示可注册，但无法购买？**  
A: 可能是域名预留或高级域名。请访问提供的在线验证链接二次确认。

**Q: 查询速度慢？**  
A: whois 查询依赖网络和注册商响应速度，超时设置为8秒。

**Q: 支持其他 TLD (.net, .cn) 吗？**  
A: 支持，直接输入完整域名即可：`bizcheck domain example.net test.cn`

## 贡献

欢迎提交 Issue 和 Pull Request！

## License

MIT

---

**GitHub**: https://github.com/wowayou/bizcheck  
**作者**: wowayou  
**版本**: 1.0.0
