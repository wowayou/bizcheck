# BizCheck - 业务检查工具

检查域名可用性、商标注册、公司名称查重的命令行工具。

## 功能

- **域名可用性检查** — 基于 whois 查询（依赖网络环境）
- **商标查询** — 提供官方查询链接
- **公司名称查重** — 提供查询入口
- **相似度分析** — 基础的本地分析
- **全面检查** — 组合上述功能

## 安装

### 1. 系统依赖

```bash
# Debian/Ubuntu/WSL
sudo apt install whois

# macOS
brew install whois
```

### 2. 下载工具

```bash
git clone <repository-url> ~/Dev/devtools
cd ~/Dev/devtools
chmod +x bizcheck.py
```

## 使用方式

### 交互式菜单

```bash
./bizcheck.py
```

### 快捷命令

```bash
# 快速检查域名
./bizcheck.py domain example.com test.com

# 自动补全 .com
./bizcheck.py domain example test
```

## 技术说明

- **Python 版本**：3.7+
- **依赖**：标准库 + whois 命令
- **查询超时**：5秒/域名（有重试机制）
- **编码**：UTF-8
- **支持平台**：Linux, macOS, WSL

## 限制

1. **域名查询**
   - 依赖网络和 whois 服务器响应
   - 部分域名可能查询超时或失败
   - 结果仅供参考，建议使用在线工具二次确认

2. **商标和公司名称**
   - 仅提供查询链接，需要手动访问网站
   - 不提供自动化查询功能

3. **相似度分析**
   - 仅做基础的模式匹配
   - 不能替代专业的商标检索

4. **中文输入**
   - 依赖终端的 UTF-8 支持
   - 建议在支持中文的终端环境下使用

## 常见问题

**Q: 域名查询总是超时？**  
A: 可能是网络环境限制。建议直接使用在线工具：https://who.is/whois/

**Q: 中文输入显示乱码？**  
A: 确保终端设置为 UTF-8 编码：`echo $LANG`（应显示包含 UTF-8）

**Q: 查询结果可靠吗？**  
A: 域名查询结果仅供参考，建议使用提供的在线工具二次确认。商标和公司名称需要访问官方网站核实。

## License

MIT
