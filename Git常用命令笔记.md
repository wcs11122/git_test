# Git 常用命令笔记

> 纯命令行版 · 无需图形界面
> 适用：Git Bash（UCRT64）/ PowerShell / CMD

---

## 📌 一、日常标准工作流（最高频，背下来）

```bash
git pull                    # 1. 先拉远程最新代码
#  ...修改你的文件...
git add .                   # 2. 改动加入暂存区
git commit -m "提交说明"     # 3. 提交到本地仓库
git push                    # 4. 推送到远程
```

**一次性绑定上游（绑定后 `git pull` / `git push` 不用再写 `origin main`）**

```bash
git branch --set-upstream-to=origin/main main
```

---

## ⚙️ 二、初次配置（装完 Git 只做一次）

| 命令 | 作用 |
|---|---|
| `git config --global user.name "你的名字"` | 设置用户名 |
| `git config --global user.email "你的邮箱"` | 设置邮箱 |
| `git config --list` | 查看所有配置 |
| `git config --global --unset user.name` | 删除某项配置 |

---

## 📦 三、仓库初始化 & 克隆

| 命令 | 作用 |
|---|---|
| `git init` | 在当前目录新建 Git 仓库 |
| `git clone 仓库地址` | 克隆远程仓库到本地 |
| `git clone 仓库地址 自定义目录名` | 克隆并重命名目录 |

---

## 👀 四、查看状态与日志（最常用）

| 命令 | 作用 |
|---|---|
| `git status` | 查看文件状态（改了/暂存了/干净） |
| `git diff` | 查看**未暂存**的具体修改内容 |
| `git diff --staged` | 查看**已暂存**的修改内容 |
| `git log` | 查看完整提交历史 |
| `git log --oneline` | 一行一条，看 commit 短 ID（✨推荐） |
| `git log --oneline --graph --all` | 树形图显示所有分支历史 |
| `git log -- 文件名` | 只看某个文件的提交记录 |

**状态字段含义：**
- `Changes not staged for commit` → 改了但没 `add`
- `Changes to be committed` → 已 `add`，等 `commit`
- `nothing to commit, working tree clean` → 干净，全部已提交

---

## ✅ 五、暂存与提交

| 命令 | 作用 |
|---|---|
| `git add 文件名` | 把指定文件加入暂存区 |
| `git add .` | 所有改动加入暂存区 |
| `git add *.txt` | 按通配符批量添加 |
| `git commit -m "说明"` | 提交暂存区内容 |
| `git commit -a -m "说明"` | 跳过 add，直接提交**已追踪**文件（新文件无效） |
| `git commit --amend -m "新说明"` | 修改**上一条**提交的说明（未 push 时安全） |
| `git commit --amend --no-edit` | 补充文件到上一条提交，不改说明 |

> 💡 **提交说明规范**：动词开头 + 说清改了什么，如 `修复登录接口空指针`、`新增说明文档`

---

## 🌿 六、分支操作

| 命令 | 作用 |
|---|---|
| `git branch` | 查看本地分支（`*` 为当前） |
| `git branch -a` | 查看本地 + 远程所有分支 |
| `git branch 分支名` | 创建分支（不切换） |
| `git switch 分支名` | 切换分支（新版推荐） |
| `git switch -c 分支名` | 创建并切换（✨最常用） |
| `git checkout 分支名` | 切换分支（老写法，功能相同） |
| `git checkout -b 分支名` | 创建并切换（老写法） |
| `git merge 分支名` | 把指定分支合并到**当前**分支 |
| `git branch -d 分支名` | 删除已合并的分支 |
| `git branch -D 分支名` | 强制删除未合并的分支 |
| `git branch -m 新名` | 重命名当前分支 |

---

## 🔗 七、远程仓库

| 命令 | 作用 |
|---|---|
| `git remote -v` | 查看远程地址 |
| `git remote add origin 仓库地址` | 添加远程仓库，别名 origin |
| `git remote set-url origin 仓库地址` | 修改远程地址 |
| `git remote remove origin` | 删除远程关联 |
| `git push` | 推送（需已绑定上游） |
| `git push origin main` | 推送指定分支 |
| `git push -u origin main` | 首次推送并**同时绑定上游**（推荐） |
| `git push --force` | 强制推送（⚠️覆盖远程，慎用） |
| `git pull` | 拉取并自动合并（= fetch + merge） |
| `git pull origin main` | 拉取指定分支 |
| `git fetch origin` | 只拉取更新，**不合并**（安全，可先看变化） |
| `git fetch --all` | 拉取所有远程更新 |

> ⚠️ `git remote -v` 只显示一行 `(push)` 时：不影响 pull/push 使用，执行 `git remote set-url origin 地址` 即可补成 fetch + push 两行。

---

## ↩️ 八、撤销与回退（踩坑急救）

### 场景 1：改了文件但没 add —— 丢弃修改
```bash
git restore 文件名          # 恢复成上次提交的版本
git restore .               # 丢弃全部工作区修改
```

### 场景 2：add 了但没 commit —— 撤出暂存区
```bash
git restore --staged 文件名     # 新版写法
git reset HEAD 文件名            # 老版写法
```

### 场景 3：commit 了想回退版本
```bash
git reset --soft HEAD~1     # 撤销 commit，改动保留在暂存区
git reset --mixed HEAD~1    # 撤销 commit + 撤销 add，改动还在工作区（默认）
git reset --hard HEAD~1     # 撤销 commit 并【丢弃全部改动】⚠️不可恢复

git reset --hard commit短ID # 回退到指定版本
```
> `HEAD~1` = 上一个版本，`HEAD~2` = 上两个版本

### 场景 4：已经 push 了，要撤回远程提交
```bash
git reset --hard commit短ID   # 本地先回退
git push --force              # 强制覆盖远程（⚠️团队协作慎用）
```

### 场景 5：想看历史版本文件内容
```bash
git show commit短ID:文件名
```

---

## 💾 九、储藏 stash（临时存改动，不提交就切分支）

| 命令 | 作用 |
|---|---|
| `git stash` | 暂存当前所有改动 |
| `git stash -u` | 连未追踪的新文件一起存 |
| `git stash list` | 查看储藏列表 `stash@{0}` |
| `git stash pop` | 取出最近一次并**删除**记录 |
| `git stash apply` | 取出但**保留**记录 |
| `git stash drop` | 删除最近一次储藏 |
| `git stash clear` | 清空所有储藏 |

**典型用法：代码写到一半要紧急切分支**
```bash
git stash          # 先存起来
git switch main    # 切过去处理紧急问题
git switch dev     # 回来
git stash pop      # 恢复改动
```

---

## 🧹 十、忽略文件 .gitignore

在项目根目录新建 `.gitignore`，逐行写规则：

```gitignore
# 注释用 #
*.log               # 所有日志文件
node_modules/       # 整个文件夹
build/              # 编译输出
.env                # 环境变量文件
*.exe
.DS_Store
```

**已提交过的文件想让它失效**（重要）：
```bash
git rm --cached 文件名        # 从版本控制移除，本地文件保留
git rm -r --cached 文件夹/
git commit -m "移除已跟踪文件"
```

**查看忽略规则生效情况：**
```bash
git check-ignore -v 文件名
```

---

## 🏷️ 十一、标签 Tag（版本发布）

| 命令 | 作用 |
|---|---|
| `git tag` | 查看所有标签 |
| `git tag v1.0` | 打轻量标签 |
| `git tag -a v1.0 -m "版本说明"` | 打附注标签（推荐） |
| `git push origin v1.0` | 推送单个标签 |
| `git push --tags` | 推送所有标签 |
| `git tag -d v1.0` | 删除本地标签 |

---

## ⚔️ 十二、冲突处理

**冲突出现时机**：`git pull` 或 `git merge` 时同一行代码被两边改了。

**文件里会出现冲突标记：**
```text
<<<<<<< HEAD
你本地的代码
=======
远程/别人的代码
>>>>>>> origin/main
```

**处理步骤（纯命令）：**
```bash
# 1. 打开冲突文件，手动删掉 <<<、===、>>> 标记，保留正确的代码
# 2. 标记为已解决
git add 冲突文件
# 3. 完成合并提交
git commit -m "解决合并冲突"
# 4. 推送
git push
```

**放弃这次合并，回到合并前状态：**
```bash
git merge --abort
git pull --abort
```

**查看哪些文件冲突了：**
```bash
git status
git diff --name-only --diff-filter=U
```

---

## 📊 十三、其他实用命令

| 命令 | 作用 |
|---|---|
| `git rm 文件名` | 删除文件并加入暂存 |
| `git mv 老名 新名` | 重命名文件并加入暂存 |
| `git clean -n` | 预览哪些未追踪文件会被删除 |
| `git clean -fd` | 删除所有未追踪文件和文件夹（⚠️不可恢复） |
| `git shortlog -sn` | 统计各人提交次数 |
| `git show commitID` | 查看某次提交的具体改动 |
| `git blame 文件名` | 查看每行代码最后由谁修改 |
| `git reflog` | 查看所有 HEAD 移动记录（✨找回误删提交的救星） |

### 🔥 救命命令：reflog 找回 `reset --hard` 丢的提交
```bash
git reflog                  # 找到被删提交的 commit ID
git reset --hard 那个commitID
```

---

## 🗂️ 十四、命令速查卡（打印版）

```bash
# ===== 日常三件套 =====
git pull && git add . && git commit -m "说明" && git push

# ===== 看状态 =====
git status
git log --oneline
git diff

# ===== 分支 =====
git switch -c dev
git switch main
git merge dev

# ===== 撤销 =====
git restore 文件          # 丢工作区改动
git restore --staged 文件  # 撤暂存
git reset --soft HEAD~1   # 撤 commit 留改动
git reset --hard HEAD~1   # 撤 commit 丢改动

# ===== 远程 =====
git remote -v
git push -u origin main
git fetch origin
```

---

## ⚠️ 十五、危险命令黑名单

| 命令 | 风险 |
|---|---|
| `git reset --hard` | 永久丢弃工作区改动，无法恢复（可用 reflog 找回 commit） |
| `git clean -fd` | 永久删除未追踪文件，**无法恢复** |
| `git push --force` | 覆盖远程历史，可能毁掉同事的提交 |
| `git branch -D` | 强制删除未合并分支，提交可能丢失 |

> 原则：执行前先 `git status` + `git log --oneline` 确认清楚；不放心就先 `git stash` 或 `git branch 备份名`。

---

## 📎 附：中文文件名显示乱码问题

Git Bash 中出现 `"\350\257\264\346\230\216.txt"` 是**八进制转义**，指的就是 `说明.txt`，不是乱码也不是报错。

**配置成正常显示中文：**
```bash
git config --global core.quotepath false
```

---
