# 中文输入处理方案

## 问题背景

在测试过程中发现，当用户使用退格键编辑中文输入时，会出现乱码现象：
- 输入："青岛识 源 国际贸易 有限公司"
- 显示："青岛识�源�国际贸易有�有限公司"

## 根本原因

这**不是** Python 的问题，而是**终端显示问题**。

当你看到输出中的乱码（如 `�`），这是因为：
1. 退格键在某些终端中可能产生了不完整的 UTF-8 字节序列
2. Python 的 `input()` 函数本身处理得很好，但**终端的回显**可能有问题
3. 实际的字符串数据可能是正确的，只是显示出了问题

## 调研结果

### 市面上常见的输入处理方案

1. **Python 标准 input() + readline**（推荐 ✓）
   - 最简单、最可靠
   - 自动利用 GNU Readline 的编辑功能
   - 终端负责所有编辑操作，Python 只接收最终结果
   - 适用场景：命令行工具、脚本

2. **prompt_toolkit**（功能强大但需额外依赖）
   - 提供高级输入功能（语法高亮、自动补全）
   - 适用于需要复杂交互的 TUI 应用
   - 依赖：需要 `pip install prompt_toolkit`

3. **click.prompt()**（简洁优雅）
   - Click 框架的一部分
   - 提供类型验证、默认值等
   - 依赖：需要 `pip install click`

4. **rich.Console.input()**（现代化）
   - Rich 库的输入功能
   - 更好的样式和格式化
   - 依赖：需要 `pip install rich`

### 选择的方案：标准 input() + readline

**原因**：
- ✅ 无需额外依赖
- ✅ 终端原生支持最可靠
- ✅ 适合简单的命令行工具
- ✅ 兼容性最好

## 实现细节

### 1. 启用 readline 支持

```python
# 在文件开头添加
try:
    import readline
except ImportError:
    pass  # Windows 上可能没有，但不影响基本功能
```

**作用**：
- 提供命令行编辑功能（←→移动光标、Ctrl+A/E 等）
- 历史记录（↑↓ 翻看历史输入）
- 自动处理退格、删除等编辑操作

### 2. 简化输入清理函数

```python
def clean_input(text: str) -> str:
    """清理用户输入，只做最基础的规范化"""
    # 只做基础的空格规范化
    # 终端已经处理了退格等编辑操作，input() 返回的是最终结果
    return ' '.join(text.split())
```

**原则**：
- **信任终端的输入处理能力**
- 不要尝试手动处理控制字符
- 只做必要的空格规范化

### 3. 标准化大小写

```python
country = get_input("输入国家代码", "CN").upper()
```

## 关于乱码的说明

如果在**输出时**仍然看到乱码（`�`），这通常是：

1. **终端编码问题**
   ```bash
   # 检查终端编码
   echo $LANG  # 应该包含 UTF-8
   
   # 如果不是，设置为 UTF-8
   export LANG=en_US.UTF-8
   ```

2. **SSH 连接的编码问题**
   - 确保 SSH 客户端使用 UTF-8 编码
   - PuTTY: Settings → Window → Translation → UTF-8
   - SecureCRT: Session Options → Appearance → Character Encoding → UTF-8

3. **Python 输出编码问题**（罕见）
   ```python
   import sys
   print(sys.stdout.encoding)  # 应该是 'utf-8'
   ```

## 测试

```bash
# 测试中文输入
./bizcheck.py

# 选择功能 2（商标查询）
# 输入：青岛识 源 国际贸易 有限公司
# 尝试使用退格键删除和重新输入
```

## 结论

**不要过度处理输入**。Python 的 `input()` 函数配合 `readline` 模块已经能够正确处理各种编辑操作。我们只需要：

1. 启用 readline 支持（如果可用）
2. 做最基础的空格规范化
3. 确保终端使用 UTF-8 编码

**复杂的控制字符过滤往往适得其反**，因为：
- `input()` 返回的是最终结果，控制字符已被终端处理
- 手动过滤可能破坏正常的 Unicode 字符
- 不同终端的行为不同，统一过滤很难做对
