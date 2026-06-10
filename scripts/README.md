# 快速开始

## 一键安装（推荐）

```bash
# 在项目根目录运行
./scripts/setup-dev-env.sh
```

安装完成后：
```bash
source ~/.bashrc
```

## 手动安装

### 1. Starship Prompt

```bash
# 安装
curl -sS https://starship.rs/install.sh | sh

# 启用
echo 'eval "$(starship init bash)"' >> ~/.bashrc

# 复制配置（可选）
mkdir -p ~/.config
cp scripts/starship.toml ~/.config/starship.toml
```

### 2. Git别名

```bash
# 方式1：批量导入
cat scripts/gitconfig-enhanced >> ~/.gitconfig

# 方式2：逐个添加
git config --global alias.st 'status --short --branch'
git config --global alias.lg 'log --graph --oneline --decorate --all -15'
git config --global alias.br 'branch -vv'
```

### 3. 可选工具

**lazygit（终端Git GUI）**
```bash
# 获取最新版本
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')

# 下载安装
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit /usr/local/bin
rm lazygit.tar.gz lazygit
```

**delta（美化diff）**
```bash
wget https://github.com/dandavison/delta/releases/download/0.17.0/git-delta_0.17.0_amd64.deb
sudo dpkg -i git-delta_0.17.0_amd64.deb
```

## 验证安装

```bash
# 测试Starship
starship --version

# 测试Git别名
git st
git lg

# 测试lazygit（如果安装了）
lazygit --version
```

## 下一步

阅读完整文档：`WINDOWS_TERMINAL_SETUP.md`
