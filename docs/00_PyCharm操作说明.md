# 第 0 课：先找到运行代码的地方

## 1．打开课程目录

在 PyCharm 中用 **File → Open（文件 → 打开）**，选择：

`D:\AAA文献库\A仿生通信\生成式\VAE`

如果你已经打开了上一级“生成式”项目，也可以直接在左侧展开 VAE 目录。本课不要求重新创建项目或迁移文件。

## 2．检查项目解释器

在 **File → Settings → Project → Python Interpreter（Python 解释器）** 查看路径。不同语言界面的菜单名称可能略有差别。

应当使用：`D:\Anaconda3\envs\HEUhuqiao\python.exe`。

如果已经是这个路径，保持即可。否则添加已有本地解释器（Existing environment），选择上述 `python.exe`，不要创建新环境。

## 3．打开 Notebook

双击 `notebooks/00_运行第一段代码.ipynb`。你应看到说明文字和可运行的代码块。

- 点击代码块左侧的运行三角形，运行当前单元格。
- 通常 `Shift+Enter` 也能运行并前往下一格；若快捷键不同，先用运行按钮。
- 文字块用于说明，不是发给 Python 执行的命令。
- 第一次运行可能需要启动服务和内核，稍等片刻。

优先使用 PyCharm 管理的本地 Jupyter 服务，并选择 `HEUhuqiao` 对应的解释器或内核。**项目解释器与 Notebook 内核可能不同**，所以第一格会输出实际路径；这比界面上的名字更可靠。

先只执行课程中的路径检查。如果输出不是指定路径，停在这里调整内核，不继续运行后面的练习。

## 4．怎样保存与重新开始

- `Ctrl+S` 保存 Notebook 中的文字、代码及当前输出。
- 内核保存本次会话的变量；保存文件不等于保存内核状态。
- 用 Notebook 工具栏的 **Restart Kernel（重启内核）** 清除变量，然后从上往下运行。
- 正式检查顺序时用 **Restart Kernel and Run All（重启并运行全部）** 或重启后逐格执行。这一步放在练习结束后，第一次阅读不要直接跳到结果。

## 5．如果内置服务启动失败

这是备用步骤，正常能运行就跳过。

在 PyCharm 的 PowerShell 终端中，先进入课程目录，再执行：

```powershell
Set-Location -LiteralPath 'D:\AAA文献库\A仿生通信\生成式\VAE'
& '.\scripts\start_jupyter.ps1'
```

脚本使用指定 Python，在课程目录 `.runtime` 下准备专用内核配置并启动本地 Jupyter 服务，不修改全局内核配置。

如果 PowerShell 提示执行策略阻止脚本，仅对这一次启动使用：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File '.\scripts\start_jupyter.ps1'
```

把终端给出的本机 URL 填入 PyCharm 的 Jupyter **Existing/External Server（已有服务）** 配置，选择 **Python (HEUhuqiao - VAE)** 内核。该 URL 含本机会话令牌，无需贴到学习记录或 Git。

如果当前 PyCharm 的许可或插件状态仍然不提供 Notebook 界面，可以暂时在本机浏览器打开同一个 URL，使用同一份文件和环境；把具体提示告诉讲解者，继续排查 PyCharm。不要为了这一课先重装 Python。

服务运行时保持终端打开。结束后在该终端按 `Ctrl+C`，根据提示停止服务。

## 6．本课独立脚本的检查方式

这段由讲解者验证过，你不需要先理解内部实现。在课程目录的终端执行：

```powershell
& 'D:\Anaconda3\envs\HEUhuqiao\python.exe' '.\scripts\check_environment.py'
```

这里前一个路径指定“用谁执行”，后一个路径指定“执行哪个文件”。同样的原则也适用于 Notebook：文件和执行它的 Python 是两件不同的事。

界面操作参考：[JetBrains 2024 年 Notebook 使用说明](https://blog.jetbrains.com/pycharm/2024/09/how-to-use-jupyter-notebooks-in-pycharm/)。
