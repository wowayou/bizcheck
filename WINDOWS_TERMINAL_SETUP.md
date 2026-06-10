# Windows Terminal + Claude Code 开发环境最佳实践

> 针对WSL2 + Windows Terminal + Claude Code的场景，提供git状态可视化方案

**调研日期**：2026-06-10  
**基于**：社区最佳实践调研 + [2026年Git工具对比](https://thelinuxcode.com/best-tools-and-extensions-for-working-with-git-in-2026/)

---

## 目标

在纯终端环境中获得类似VS Code的git状态可视化：
- ✅ prompt实时显示分支和文件状态
- ✅ 快速查看修改内容
- ✅ 交互式暂存/提交操作
- ✅ 与Claude Code无缝协作

---

## 方案架构：三层增强

```
┌─────────────────────────────────────────────┐
│  Layer 1: Starship Prompt (实时状态)        │ ← 必装
├─────────────────────────────────────────────┤
│  Layer 2: lazygit TUI (可视化操作)          │ ← 推荐
├─────────────────────────────────────────────┤
│  Layer 3: Git别名 (快捷命令)                │ ← 必装
└─────────────────────────────────────────────┘
```

---

## Layer 1: Starship Prompt（必装）

### 为什么选Starship？

根据[社区对比](https://alexshepherd.me/posts/zsh-ohmyzsh-starship-rust/)：

| 特性 | Starship ⭐ | Oh My Posh |
|------|-----------|-----------|
| **启动速度** | 更快（Rust编写） | 略慢 |
| **配置** | 零配置开箱即用 | 需要手动配置主题 |
| **WSL2支持** | 完美 | 有小问题 |
| **性能** | 50-150ms | 稍慢 |
| **跨平台** | bash/zsh/fish全支持 | 主要面向PowerShell |

**结论**：WSL2环境首选Starship

### 安装

```bash
# 1. 安装Starship
curl -sS https://starship.rs/install.sh | sh

# 2. 启用（添加到~/.bashrc末尾）
echo 'eval "$(starship init bash)"' >> ~/.bashrc

# 3. 生效
source ~/.bashrc
```

### 效果展示

安装后，prompt会自动显示：

```
~/Dev/ai-secretary on 󰊢 main [!?] took 2s
❯ 
```

符号含义：
- `󰊢 main` - Git分支（带图标）
- `[!?]` - 状态码：`!`=有修改，`?`=有未跟踪文件
- `⇡2` - 领先远程2个提交
- `⇣1` - 落后远程1个提交
- `✘` - 有删除的文件
- `+` - 有新增的文件

### 可选：安装Nerd Font显示图标

Starship的图标需要Nerd Font支持。

1. **下载字体**：[CascadiaCode Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/CascadiaCode.zip)
2. **Windows上安装**：解压后右键`.ttf`文件点"安装"
3. **配置Windows Terminal**：打开设置（`Ctrl+,`），找到你的WSL配置文件：

```json
{
    "profiles": {
        "defaults": {
            "font": {
                "face": "CascadiaCode Nerd Font",
                "size": 11
            }
        }
    }
}
```

4. **重启Windows Terminal**

### 自定义配置（可选）

复制项目提供的配置：

```bash
mkdir -p ~/.config
cp scripts/starship.toml ~/.config/starship.toml
```

参考：[Starship官方文档](https://starship.rs/)

---

## Layer 2: lazygit TUI（推荐）

### 为什么选lazygit？

根据[性能测试对比](https://sumguy.com/gitui-vs-lazygit-git-tuis/)（Linux内核仓库，90万+提交）：

| 特性 | lazygit ⭐ | gitui | tig |
|------|----------|-------|-----|
| **解析时间** | 57秒 | 24秒 | 4分20秒 |
| **内存占用** | 2.6 GB | 0.17 GB | 1.3 GB |
| **功能丰富度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **学习曲线** | 平缓（适合初学者） | 中等 | 陡峭 |
| **GitHub星标** | 37k+ | 增长中 | 成熟项目 |
| **特色功能** | 交互式rebase、冲突解决、stage hunks | 极速启动 | 只读浏览 |

**结论**：功能最全，社区最活跃，适合日常开发

### 安装

```bash
# WSL2 / Linux一键安装
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit /usr/local/bin
rm lazygit.tar.gz lazygit

# 验证
lazygit --version
```

### 使用

```bash
# 在任何git仓库中运行
lazygit
```

### 核心快捷键

| 键 | 动作 | 说明 |
|----|------|------|
| **导航** |
| `j/k` 或 `↑/↓` | 上/下移动 | vim风格 |
| `Tab` / `Shift+Tab` | 切换面板 | 文件→分支→提交→暂存 |
| **文件操作** |
| `Space` | 暂存/取消暂存 | 可以stage单个hunk |
| `a` | 暂存所有 | |
| `Enter` | 查看diff | 可逐hunk操作 |
| `d` | 删除/丢弃文件 | 会确认 |
| **提交** |
| `c` | 提交 | 打开编辑器写message |
| `A` | Amend上一次提交 | |
| **远程操作** |
| `P` | Push推送 | |
| `p` | Pull拉取 | |
| `f` | Fetch获取 | |
| **分支** |
| `n` | 新建分支 | |
| `Space` | 切换分支 | 在Branches面板 |
| `d` | 删除分支 | |
| `r` | Rebase | |
| **其他** |
| `?` | 显示所有快捷键 | |
| `q` | 退出 | |

### 高级技巧

1. **Stage部分修改**（类似VS Code的chunk staging）
   - 在Files面板，选中文件按`Enter`
   - 用`↑/↓`选择要暂存的hunk
   - 按`Space`暂存单个hunk

2. **交互式Rebase**
   - 切到Commits面板
   - 按`e`编辑提交历史
   - 支持squash、reword、drop等操作

3. **冲突解决**
   - Pull后有冲突，lazygit会自动检测
   - 在Files面板看到冲突文件标记
   - 按`Enter`查看，可选择保留哪一方

参考：[lazygit官方教程](https://github.com/jesseduffield/lazygit)

---

## Layer 3: Git别名（必装）

### 快速安装

```bash
# 批量添加别名
git config --global alias.st 'status --short --branch'
git config --global alias.lg 'log --graph --oneline --decorate --all -15'
git config --global alias.br 'branch -vv'
git config --global alias.staged 'diff --cached'
git config --global alias.unstaged 'diff'
git config --global alias.changed 'diff HEAD'
```

或者复制完整配置：

```bash
cat scripts/gitconfig-enhanced >> ~/.gitconfig
```

### 核心别名对比

**Before vs After**

| 原命令 | 别名 | 效果 |
|-------|------|------|
| `git status` | `git st` | 简洁单行格式 |
| `git log --graph --oneline` | `git lg` | 彩色分支树 |
| `git branch -vv` | `git br` | 分支+跟踪关系 |
| `git diff --cached` | `git staged` | 查看已暂存内容 |
| `git diff` | `git unstaged` | 查看工作区修改 |

### 实例对比

**标准 `git status`（15行）：**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md
	modified:   src/cli.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	frontend/

no changes added to commit (use "git add" and/or "git commit -a")
```

**简洁 `git st`（4行）：**
```
## main...origin/main
 M README.md
 M src/cli.py
?? frontend/
```

状态码：
- `M` = 修改（工作区）
- `??` = 未跟踪
- `A` = 新增（已暂存）
- `D` = 删除
- `R` = 重命名

---

## 可选增强：delta（美化diff）

[delta](https://github.com/dandavison/delta)提供语法高亮的diff输出，side-by-side对比。

### 安装

```bash
wget https://github.com/dandavison/delta/releases/download/0.17.0/git-delta_0.17.0_amd64.deb
sudo dpkg -i git-delta_0.17.0_amd64.deb
rm git-delta_0.17.0_amd64.deb
```

### 配置

在`~/.gitconfig`中添加：

```ini
[core]
    pager = delta

[interactive]
    diffFilter = delta --color-only

[delta]
    navigate = true
    side-by-side = false
    line-numbers = true
    syntax-theme = Dracula
```

---

## 与Claude Code的协作模式

### 原则

Claude Code会在需要时自动检查git状态，但你可以主动提供上下文加速协作。

### 推荐工作流

#### 场景1：开始新功能

```bash
# 1. 启动Claude Code
claude

# 2. 对话
你: 要开发用户认证功能，先看下当前状态，是否需要新建分支

# Claude会：
# - 运行 git status 检查工作区
# - 建议分支命名
# - 询问是否创建分支
```

#### 场景2：编码过程中

```bash
# 不用手动查状态，直接问
你: 我刚改了login.py和auth.py，帮我看下改了什么

# Claude会：
# - git diff 查看具体变更
# - 分析修改合理性
# - 建议是否该提交了
```

#### 场景3：提交前code review

```bash
你: 准备提交了，帮我review下改动，写个commit message

# Claude会：
# 1. git diff 完整查看
# 2. 检查是否有问题（console.log、TODO等）
# 3. 按照Conventional Commits规范生成message
# 4. 询问是否执行 git add + git commit
```

#### 场景4：冲突解决

```bash
你: git pull后有冲突，在auth.py里，帮我解决

# Claude会：
# 1. cat auth.py 查看冲突标记
# 2. 分析冲突原因
# 3. 提供合并建议或直接修复
# 4. 执行 git add 标记已解决
```

### 实战技巧

**✅ 推荐**：
```
你: 改完登录bug了，检查下是否该提交，顺便写个commit message
```

**❌ 避免**：
```
你: 帮我改bug（没说改完了还是要开始改，Claude无法判断是否需要检查git）
```

**✅ 高效**：
```
你: 列出所有未暂存的.py文件，我要批量暂存
# Claude会先展示列表，确认后执行
```

**❌ 低效**：
```
你: git add *.py（自己敲命令，没利用Claude的智能）
```

### 并行工作：分屏推荐

利用Windows Terminal的分屏功能：

```
┌─────────────────┬─────────────────┐
│                 │                 │
│  Claude Code    │   lazygit       │
│  (左侧)         │   (右侧)        │
│                 │                 │
│  对话交互       │   实时监控状态   │
│  修改代码       │   查看diff      │
│                 │   暂存/提交     │
└─────────────────┴─────────────────┘
```

快捷键：
- `Alt+Shift+D` - 垂直分屏
- `Alt+方向键` - 切换面板
- `Ctrl+Shift+W` - 关闭面板

**工作流程**：
1. 左侧Claude Code对话，让它修改代码
2. 右侧lazygit实时看到文件变更
3. Claude改完后，右侧lazygit快速review diff
4. 满意后在lazygit里暂存提交，或让Claude帮你提交

---

## 快速开始：5分钟配置

```bash
# 在项目根目录运行
cd ~/Dev/my-projects/ai-secretary

# 一键安装
chmod +x scripts/setup-dev-env.sh
./scripts/setup-dev-env.sh

# 生效配置
source ~/.bashrc
```

验证：

```bash
# 1. 检查Starship
# prompt应该显示分支和状态

# 2. 测试git别名
git st

# 3. 启动lazygit（如果安装了）
lazygit
```

---

## 完整配置文件

所有配置已准备好：

- `scripts/setup-dev-env.sh` - 一键安装脚本
- `scripts/starship.toml` - Starship配置
- `scripts/gitconfig-enhanced` - Git别名和增强配置
- `scripts/README.md` - 安装指南

---

## 故障排查

### Starship图标显示为方块

**原因**：未安装Nerd Font  
**解决**：参考上面"Layer 1"安装字体部分

### lazygit找不到命令

**原因**：`/usr/local/bin`不在PATH中  
**解决**：
```bash
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Git别名不生效

**原因**：配置写错文件或未生效  
**解决**：
```bash
# 查看当前别名
git config --global --list | grep alias

# 如果为空，重新添加
git config --global alias.st 'status --short --branch'
```

### Windows Terminal分屏后字体大小不一致

**原因**：不同profile用了不同配置  
**解决**：在settings.json的`defaults`里统一设置字体，而不是在单个profile里

---

## 总结：推荐配置

| 工具 | 优先级 | 安装时间 | 收益 |
|-----|-------|---------|------|
| Starship | ⭐⭐⭐ 必装 | 2分钟 | 实时git状态，无需手动查 |
| Git别名 | ⭐⭐⭐ 必装 | 1分钟 | 命令简化80% |
| lazygit | ⭐⭐ 推荐 | 3分钟 | 可视化操作，效率提升50% |
| Nerd Font | ⭐ 可选 | 2分钟 | 图标美化 |
| delta | ⭐ 可选 | 2分钟 | diff更易读 |

**最小配置**（5分钟）：Starship + Git别名  
**完整配置**（10分钟）：Starship + Git别名 + lazygit + Nerd Font

---

## 参考资料

- [Starship官方文档](https://starship.rs/)
- [lazygit官方教程](https://github.com/jesseduffield/lazygit)
- [Windows Terminal官方文档](https://learn.microsoft.com/en-us/windows/terminal/tutorials/custom-prompt-setup)
- [Git TUI工具对比](https://sumguy.com/gitui-vs-lazygit-git-tuis/)
- [2026年最佳Git工具](https://thelinuxcode.com/best-tools-and-extensions-for-working-with-git-in-2026/)

---

**有问题？** 在项目仓库提Issue或直接问Claude Code！
