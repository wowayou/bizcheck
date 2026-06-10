#!/usr/bin/env bash
# 快速配置Windows Terminal + Claude Code开发环境
# 适用于WSL2/Linux

set -e

COLOR_GREEN='\033[0;32m'
COLOR_BLUE='\033[0;34m'
COLOR_YELLOW='\033[1;33m'
COLOR_RESET='\033[0m'

echo_step() {
    echo -e "${COLOR_BLUE}==>${COLOR_RESET} $1"
}

echo_success() {
    echo -e "${COLOR_GREEN}✓${COLOR_RESET} $1"
}

echo_info() {
    echo -e "${COLOR_YELLOW}ℹ${COLOR_RESET} $1"
}

# 检查命令是否存在
command_exists() {
    command -v "$1" &>/dev/null
}

echo_step "Windows Terminal + Claude Code 开发环境配置"
echo ""

# ============================================================================
# 1. Starship Prompt
# ============================================================================
echo_step "1/3 安装Starship prompt（自动显示git状态）"

if command_exists starship; then
    echo_success "Starship已安装"
else
    echo_info "正在下载安装..."
    curl -sS https://starship.rs/install.sh | sh -s -- -y
    echo_success "Starship安装完成"
fi

# 配置bash启用starship
if grep -q "starship init bash" ~/.bashrc; then
    echo_info "~/.bashrc已配置starship"
else
    echo "" >> ~/.bashrc
    echo '# Starship prompt' >> ~/.bashrc
    echo 'eval "$(starship init bash)"' >> ~/.bashrc
    echo_success "已添加starship到~/.bashrc"
fi

# ============================================================================
# 2. Git别名
# ============================================================================
echo_step "2/3 配置Git别名"

git config --global alias.st 'status --short --branch' 2>/dev/null || true
git config --global alias.lg 'log --graph --oneline --decorate --all -15' 2>/dev/null || true
git config --global alias.br 'branch -vv' 2>/dev/null || true
git config --global alias.staged 'diff --cached' 2>/dev/null || true
git config --global alias.unstaged 'diff' 2>/dev/null || true
git config --global alias.changed 'diff HEAD' 2>/dev/null || true

echo_success "Git别名配置完成"
echo_info "可用命令: git st, git lg, git br"

# ============================================================================
# 3. 可选工具提示
# ============================================================================
echo_step "3/3 可选增强工具"
echo ""

if command_exists lazygit; then
    echo_success "lazygit已安装"
else
    echo_info "lazygit未安装（终端Git GUI，强烈推荐）"
    read -p "是否安装lazygit? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')
        curl -Lo /tmp/lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
        tar xf /tmp/lazygit.tar.gz -C /tmp lazygit
        sudo install /tmp/lazygit /usr/local/bin
        rm /tmp/lazygit.tar.gz /tmp/lazygit
        echo_success "lazygit安装完成，运行 lazygit 启动"
    fi
fi

if command_exists delta; then
    echo_success "delta已安装"
else
    echo_info "delta未安装（美化git diff输出）"
    echo_info "安装: wget https://github.com/dandavison/delta/releases/download/0.17.0/git-delta_0.17.0_amd64.deb && sudo dpkg -i git-delta_*.deb"
fi

# ============================================================================
# 完成
# ============================================================================
echo ""
echo_step "配置完成！"
echo ""
echo_info "请运行以下命令使配置生效:"
echo "    source ~/.bashrc"
echo ""
echo_info "或者关闭并重新打开终端"
echo ""
echo_step "快速测试:"
echo "  1. 运行 git st   - 查看简洁的git状态"
echo "  2. 运行 git lg   - 查看分支树状图"
echo "  3. 观察prompt   - 现在会自动显示分支和文件状态"
echo ""
echo_info "完整文档: WINDOWS_TERMINAL_SETUP.md"
