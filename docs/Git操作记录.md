# Git 操作记录

## 第 0 课材料准备：2026-10-05

本次目标：将已有本地目录接到你的原仓库历史，并保存第 0 课材料。原仓库是 `https://github.com/Vertin-acoustic/VAE.git`，无需另建仓库。

### 已做的接入操作

1. `git init -b main`：让本地 VAE 目录具备 Git 版本管理能力。
2. `git remote add origin https://github.com/Vertin-acoustic/VAE.git`：把远程仓库地址命名为 origin。
3. `git config --local user.name Vertin-acoustic` 与 `git config --local user.email 1434571123@qq.com`：只设置本仓库提交身份，未修改全局身份。
4. `git fetch origin main`：下载远程历史，不上传本地文件。由于直连失败，成功命令额外使用本次命令级别的 `http.proxy=http://127.0.0.1:7897`；由于沙箱与桌面账户不同，还指定了仅对当前目录生效的 `safe.directory` 参数。两者均未写入全局配置。
5. `git ls-tree`、`git hash-object`：检查远程文件清单，并确认本地目标论文与远程文件完全一致。
6. `git branch main origin/main`、`git read-tree HEAD`、`git branch --set-upstream-to=origin/main main`：将尚无本地提交的分支接到远程已有提交，并建立初始索引，不覆盖工作目录中的文件。这组接入命令只适用于此次初始状态，不是以后每次保存都要执行。
7. 修复账户所有权：Windows 拒绝直接更改沙箱创建的 `.git` 所有者，因此由你的桌面账户在课程目录内复制并接替 Git 元数据，原元数据保存在忽略的 `.runtime/git-sandbox-backup`。已在你的账户下使用普通 `git status` 和 `git log` 验证，无需全局信任例外。提交历史和暂存内容均保留。这是本次工具环境修复，不是学习 Git 必须掌握的操作。

远程原始提交为 `fda2367`，说明是“复现这篇论文”。目标论文的 Git blob 哈希为 `7a29c50d5ba8933dd12fc427021472a0a3d8e8e6`。现有两篇 PDF 均保留，补充阅读 PDF 暂时忽略。

### 本次材料的本地保存

提交前会检查 `git status`、`git diff --cached` 和暂存文件清单，只将课程文档、Notebook、检查脚本以及 Git 规则纳入提交。

材料提交说明：`Add lesson 00: Python and notebook learning setup`。

提交完成后的真实编号以终端 `git log -1 --oneline` 和交付消息为准。提交内容是“第 0 课材料准备与验证”，不是“学习者已经完成第 0 课”。

### 以后保存改动的基本顺序

```text
git status
git diff
git add <这次要保存的具体文件>
git diff --cached
git commit -m "描述这次改动"
git log -3 --oneline
```

尖括号部分是说明占位符，不要原样执行。以后我们会用你实际修改的文件演示。

`git diff` 主要看已跟踪文件尚未暂存的改动；新文件在第一次 add 前通常只出现在 status 中，add 后再用 `git diff --cached` 查看。

### 当前同步约定

本次不执行 `git push`。本地 commit 和远程 push 是两件事；首次推送时再一起学习。

你补充授权“找不到原仓库时可新建并上传”。现在原仓库已找到并接入，因此不需要启动新建仓库的备用方案。

## 第一次亲手提交与上传：2026-10-08

**状态：操作说明已准备，以下提交与推送由你执行，尚未记录为已完成。**

已检查：本地 `main` 关联 `origin/main`，远程地址为你的原 VAE 仓库。本地已有材料提交 `f26cdf1`，相对上次获取的远程记录领先 1 个提交；这不代表已经重新查询了远程最新状态。你的学习记录、Notebook 有未提交修改，独立 `计划.md` 尚未跟踪。本次讲解者另外更新了 README、反馈、计划与本文档，保留你的原回答和 Notebook。

### 第一步：先保存想要上传的文件

Notebook 当前有旧输出：源代码赋值 3，输出却为 6，最终为 7。选择你要保留的赋值，重启内核并从上往下运行后保存；保留 3 时最终结果为 4。这样 Git 保存的代码和实验输出才能相互对应。

### 第二步：查看当前变化

在 PyCharm 下方的 **Terminal（终端）** 中执行，使用 PowerShell，不是在 Notebook 的代码格或 Python Console 中执行：

```powershell
Set-Location -LiteralPath 'D:\AAA文献库\A仿生通信\生成式\VAE'
git status
git diff -- docs/学习记录.md
```

`modified` 表示已跟踪文件被修改；`untracked` 表示新文件还未纳入版本记录。`git diff` 显示旧版本与新版本差异，行前的 `-`、`+` 分别表示删去和加入。若出现分页器，按 `q` 退出。

### 第三步：选择本次要保存的文件

```powershell
git add -- README.md 计划.md docs/学习记录.md docs/Git操作记录.md notebooks/00_运行第一段代码.ipynb
git diff --cached --stat
git status
```

`add` 把当前文件内容放进暂存区；`--cached` 查看准备进入本次提交的改动。这里明确选择 5 个本课文件，避免把其他课程或无关文件一起提交。此后如果又编辑了这些文件，先保存并再次 add，才能把最新内容包含进去。

### 第四步：保存一个本地版本

```powershell
git commit -m "Review lesson 00 and record learning progress"
git log -2 --oneline
```

`-m` 后面是这次提交的说明。提交成功后会出现一个新的提交编号；这时版本在你的电脑上，尚未因为 commit 自动上传。

### 第五步：上传到 GitHub

```powershell
git push origin main
```

`origin` 是之前保存的 GitHub 远程地址别名，`main` 是这次要推送的分支。推送会发送远程缺少的提交，包括之前准备课程的提交和你刚做的学习记录提交。

如果出现登录提示，按 Git 凭据工具的提示在你自己的界面完成认证。如果出现连接超时、认证失败或 `rejected/non-fast-forward`，保留提示来排查；不要重新 init、新建重复仓库或强制推送。之前直连曾失败，通过本机 Clash 7897 端口成功；若再次超时，需要先确认代理当前仍可用，再考虑一次性指定代理。

### 第六步：确认上传结果

```powershell
git status
```

在没有新改动的情况下，应看到工作区干净且与 `origin/main` 同步。再刷新 [GitHub 仓库页面](https://github.com/Vertin-acoustic/VAE)，查看新提交说明以及 Notebook、学习记录和计划是否出现。

记住这个顺序：**编辑后保存 → add 选择内容 → commit 保存本地版本 → push 同步远程**。
