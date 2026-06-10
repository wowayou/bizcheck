# BizCheck 示例演示手册

## 📚 使用场景完整演示

---

## 场景1: 创业公司域名选择

### 背景
你正在创建一家贸易公司，需要选择合适的域名。

### 步骤演示

```bash
# 1. 检查首选域名
$ bizcheck domain tradebridge.com

✗ tradebridge.com 已注册 (123-reg limited) 1997-06-21

在线验证（可选）:
  • https://who.is/whois/<domain>
  • https://domainanalyzer.com/

# 2. 批量检查备选方案
$ bizcheck domain tradebridgecn.com maoqiao.com yuanliu.com

✓ tradebridgecn.com 可注册
✓ maoqiao.com 可注册
✗ yuanliu.com 已注册 (spaceship, inc.) 2006-03-05

# 3. 选定 maoqiao.com，进行全面检查
$ bizcheck  # 选择菜单 5

输入公司名称: 青岛贸桥国际贸易有限公司
输入要检查的域名: maoqiao.com
查询国家 [CN]: 
查询地区 [青岛]: 

[执行完整检查流程]
```

**结果**: 确定使用 maoqiao.com，品牌名"贸桥"

---

## 场景2: 品牌名可用性验证

### 背景
你有了一个品牌创意"源流"，需要验证域名和商标可用性。

### 步骤演示

```bash
# 1. 快速检查域名（自动补全 .com）
$ bizcheck domain sourceflow yuanliu

✓ sourceflow.com 可注册
✗ yuanliu.com 已注册 (spaceship, inc.) 2006-03-05

# 2. 检查商标（交互式）
$ bizcheck
请选择功能 [1-5, 0]: 2

输入公司名称: 源流
输入国家代码 [CN]: CN

请访问以下网站查询:
  • 中国商标网: http://wcjs.sbj.cnipa.gov.cn/txnT01.do
  • 企查查商标: https://www.qcc.com/web/search?key=源流
  • 天眼查: https://www.tianyancha.com/search?key=源流

# 3. 检查相似度
$ bizcheck
请选择功能 [1-5, 0]: 4

输入公司名称: 青岛源流国际贸易有限公司

发现 3 个提示:
  ⚠ 包含常见词汇: 国际, 贸易, 有限公司
  ⚠ 名称较长(15字符)，建议简化
```

**结果**: sourceflow.com 可用，需要手动查询商标

---

## 场景3: 多 TLD 策略

### 背景
你想保护品牌，注册多个顶级域名。

### 步骤演示

```bash
# 检查 .com, .net, .cn
$ bizcheck domain example.com example.net example.cn

✗ example.com 已注册 (iana) 1992-01-01
✗ example.net 已注册 (iana) 1992-01-01
✗ example.cn 已注册 (某公司) 2003-03-17

# 检查自己的品牌
$ bizcheck domain mybrand.com mybrand.net mybrand.io

✓ mybrand.com 可注册
✓ mybrand.net 可注册
✓ mybrand.io 可注册
```

**结果**: 所有 TLD 可用，可全部注册

---

## 场景4: 竞品域名调研

### 背景
调研竞品的域名注册情况。

### 步骤演示

```bash
# 批量检查竞品域名
$ bizcheck domain competitor1.com competitor2.com competitor3.com

✗ competitor1.com 已注册 (godaddy) 2010-05-12
✗ competitor2.com 已注册 (namecheap) 2015-08-20
✓ competitor3.com 可注册

# 分析注册时间，了解竞品历史
# competitor1: 2010年注册，老牌企业
# competitor2: 2015年注册，中期企业
# competitor3: 域名可用，可能是新品牌或尚未启用
```

**结果**: 了解竞品成立时间和市场布局

---

## 场景5: 公司更名合规检查

### 背景
公司计划更名，需要确保新名称无冲突。

### 步骤演示

```bash
# 1. 全面检查新公司名
$ bizcheck
请选择功能 [1-5, 0]: 5

输入公司名称: 青岛新贸科技有限公司

[1/4] 域名可用性检查
输入要检查的域名: xinmao.com

✓ xinmao.com 可注册

[2/4] 商标查询
查询国家 [CN]: CN
[显示查询链接]

[3/4] 公司名称查重
查询地区 [青岛]: 青岛
[显示查询链接]

[4/4] 相似度分析
发现 2 个提示:
  ⚠ 包含常见词汇: 科技, 有限公司
  ⚠ 名称较短(10字符)，可能与他人重复

# 2. 访问提供的链接，手动确认无冲突
# 3. 提交工商注册申请
```

**结果**: 全面评估，降低注册风险

---

## 场景6: 错误处理演示

### 背景
演示工具的错误处理能力。

### 步骤演示

```bash
# 1. whois 未安装
$ bizcheck domain test.com
✗ whois 未安装
请安装: sudo apt install whois

# 2. 用户中断
$ bizcheck
请选择功能 [1-5, 0]: 1
输入域名: test.com
^C
已取消

# 3. 域名查询超时（少见）
$ bizcheck domain some-slow-domain.com
? some-slow-domain.com 查询失败

# 4. 无效输入
$ bizcheck
请选择功能 [1-5, 0]: 9
无效选择，请输入 1-5 或 0
```

**结果**: 所有错误都有清晰提示

---

## 占位符使用指南

### 基础占位符

```bash
# <domain> - 替换为您的域名
bizcheck domain <domain>
# 实际使用：
bizcheck domain example.com

# <domain1> <domain2> <domain3> - 多个域名
bizcheck domain <domain1> <domain2> <domain3>
# 实际使用：
bizcheck domain test1.com test2.com test3.com

# <company-name> - 公司名称
输入公司名称: <company-name>
# 实际使用：
输入公司名称: 青岛贸桥国际贸易有限公司
```

### 高级占位符

```bash
# <country-code> - 国家代码
输入国家代码 [CN]: <country-code>
# 实际使用：
输入国家代码 [CN]: US

# <region> - 地区名称
输入地区 [青岛]: <region>
# 实际使用：
输入地区 [青岛]: 北京
```

---

## 快速参考命令

```bash
# === 安装 ===
git clone git@github.com:wowayou/bizcheck.git ~/Dev/devtools
cd ~/Dev/devtools && chmod +x bizcheck.py
ln -s ~/Dev/devtools/bizcheck.py ~/bin/bizcheck

# === 单域名检查 ===
bizcheck domain example.com

# === 多域名检查 ===
bizcheck domain d1.com d2.com d3.com

# === 自动补全 ===
bizcheck domain example     # 自动变为 example.com

# === 交互式菜单 ===
bizcheck

# === 测试 ===
bizcheck domain google.com  # 已注册示例
bizcheck domain nonexist12345.com  # 可用示例
```

---

## 输出格式说明

### 符号含义

- `✓` 绿色 - 域名可注册
- `✗` 红色 - 域名已注册
- `?` 黄色 - 查询失败/状态未知
- `⚠` 黄色 - 警告提示

### 信息格式

```
✗ domain.com 已注册 (registrar-name) yyyy-mm-dd
│    │          │           │              │
│    │          │           │              └─ 注册日期
│    │          │           └─ 注册商名称
│    │          └─ 状态描述
│    └─ 域名
└─ 状态符号
```

---

## 常见问题场景

### Q1: 域名显示可注册，但访问注册商无法购买？

```bash
# 原因可能：
# 1. 域名被预留（premium domain）
# 2. 域名正在赎回期
# 3. whois 数据延迟

# 解决方案：
$ bizcheck domain example.com
✓ example.com 可注册

在线验证（可选）:
  • https://who.is/whois/example.com
  • https://domainanalyzer.com/

# 访问在线工具二次确认
```

### Q2: 查询速度慢？

```bash
# 原因：whois 查询依赖网络和注册商响应

# 优化方案：
# 1. 批量查询时耐心等待（超时8秒）
# 2. 网络不佳时减少并发数量
# 3. 使用在线工具作为备选
```

### Q3: 支持中文域名吗？

```bash
# 不推荐使用中文域名，但技术上支持

$ bizcheck domain 中文.com
# 工具会查询，但不推荐注册中文域名
```

---

## 进阶技巧

### 技巧1: 快速测试工具

```bash
# 测试工具是否正常
bizcheck domain google.com
# 应返回"已注册"
```

### 技巧2: 批量检查备选方案

```bash
# 准备候选列表
$ cat domains.txt
option1.com
option2.com
option3.com

# 批量检查（需手动输入）
$ bizcheck domain option1.com option2.com option3.com
```

### 技巧3: 组合使用占位符

```bash
# 检查品牌的多种变体
$ bizcheck domain <brand>.com <brand>cn.com <brand>hq.com

# 实际使用：
$ bizcheck domain mybrand.com mybrandcn.com mybrandhq.com
```

---

**演示文档版本**: 1.0.0  
**最后更新**: 2026-06-10  
**适用版本**: BizCheck 1.0.0
