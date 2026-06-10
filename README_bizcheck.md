# DevTools - 开发环境工具集

开发环境配置工具和脚本集合，适用于WSL2 + Windows Terminal环境。

## 项目列表

### 1. Windows Terminal + Git环境配置

**文件**: `WINDOWS_TERMINAL_SETUP.md`

为Windows Terminal + WSL2环境提供Git状态可视化方案，解决纯终端环境下缺少Git GUI的痛点。

**核心方案**:
- ✅ **Starship Prompt** - 实时显示git分支和文件状态
- ✅ **lazygit TUI** - 终端版Git GUI（37k+ stars）
- ✅ **Git别名** - 命令简化（`git st`替代`git status`）

**快速开始**:
```bash
cd ~/Dev/devtools
./scripts/setup-dev-env.sh
source ~/.bashrc
```

**特性**:
- 与Claude Code完美兼容
- 基于2026年社区最佳实践
- 包含完整的性能对比和选型理由
- 提供工作流实战案例

**详细文档**: 查看 [WINDOWS_TERMINAL_SETUP.md](./WINDOWS_TERMINAL_SETUP.md)

---

### 2. BizCheck - 业务检查工具

**文件**: `bizcheck.py`

检查域名可用性、商标注册、公司名称查重的命令行工具。

**功能**:
- 域名可用性检查（基于whois）
- 商标查询链接
- 公司名称查重入口
- 相似度分析

**使用**:
```bash
./bizcheck.py
# 或快捷命令
./bizcheck.py domain example.com
```

---

## 兼容性测试

### Claude Code兼容性 ✅

所有工具均经过与Claude Code的兼容性测试：

**Git命令兼容性** ✅
- `git status --porcelain` - Claude Code核心命令
- `git diff --name-only` - 文件变更检测
- `git log --oneline` - 提交历史
- 所有别名不影响Claude Code的git操作

**Starship兼容性** ✅
- 不影响shell命令执行
- 不干扰Claude Code的bash工具调用
- prompt变更仅影响视觉显示

**lazygit兼容性** ✅
- 独立TUI工具，不修改git配置
- 可与Claude Code并行使用
- 推荐分屏工作流：左侧Claude Code，右侧lazygit

### 测试环境

- ✅ WSL2 (Ubuntu)
- ✅ Windows Terminal
- ✅ Claude Code CLI
- ✅ Git 2.43+
- ✅ Python 3.12+
- ✅ Bash shell

---

## 安装

### 克隆仓库

```bash
git clone https://github.com/yourusername/devtools.git ~/Dev/devtools
cd ~/Dev/devtools
```

### 安装Git环境增强

```bash
./scripts/setup-dev-env.sh
source ~/.bashrc
```

### 安装BizCheck

```bash
chmod +x bizcheck.py
sudo apt install whois  # 如果需要
```

---

## 文件结构

```
devtools/
├── README.md                      # 本文件
├── WINDOWS_TERMINAL_SETUP.md      # Git环境配置完整文档
├── bizcheck.py                    # 业务检查工具
├── scripts/
│   ├── README.md                  # 安装指南
│   ├── setup-dev-env.sh          # 一键安装脚本
│   ├── starship.toml             # Starship配置
│   └── gitconfig-enhanced        # Git增强配置
└── LICENSE
```

---

## License

MIT
