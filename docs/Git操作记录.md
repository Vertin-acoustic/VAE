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
