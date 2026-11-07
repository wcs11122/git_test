# Git 常用命令笔记

> 纯命令行版 · Git Bash / PowerShell / CMD 通用 · 只用 `switch` / `restore` 等新命令

## 一、日常流程

```bash
git pull                 # 拉取远程最新
git add .                # 改动加入暂存区
git commit -m "说明"     # 提交到本地
git push                 # 推送到远程

git push -u origin main  # 首次推送：绑定上游，之后 pull / push 免写分支名
```

提交说明：动词开头、说清改了什么，如 `修复登录接口空指针`。

## 二、初次配置（只需一次）

| 命令 | 作用 |
|---|---|
| `git config --global user.name "名字"` | 设置用户名 |
| `git config --global user.email "邮箱"` | 设置邮箱 |
| `git config --global core.quotepath false` | 中文文件名正常显示 |
| `git config --global init.defaultBranch main` | 默认分支名设为 main |
| `git config --list` | 查看全部配置 |
| `git config --global --unset user.name` | 删除某项配置 |

## 三、建库与克隆

| 命令 | 作用 |
|---|---|
| `git init` | 当前目录建仓库 |
| `git clone 地址` | 克隆远程仓库 |
| `git clone 地址 目录名` | 克隆到指定目录 |

## 四、查看状态与历史

| 命令 | 作用 |
|---|---|
| `git status` | 文件状态（未暂存 / 已暂存 / 干净） |
| `git diff` | 未暂存的改动内容 |
| `git diff --staged` | 已暂存的改动内容 |
| `git log --oneline --graph --all` | 一行一条 + 树形图，看全部分支 |
| `git log -- 文件` | 某个文件的提交历史 |
| `git show 提交ID` | 某次提交的具体改动 |
| `git show 提交ID:文件名` | 某个历史版本的文件内容 |

## 五、暂存与提交

| 命令 | 作用 |
|---|---|
| `git add 文件` / `git add .` | 指定 / 全部改动加入暂存区 |
| `git commit -m "说明"` | 提交暂存区内容 |
| `git commit -a -m "说明"` | 跳过 add，提交已追踪文件的改动 |
| `git commit --amend -m "新说明"` | 修改上一条提交的说明（未推送时） |
| `git commit --amend --no-edit` | 补文件进上一条提交，说明不变 |

## 六、分支

| 命令 | 作用 |
|---|---|
| `git branch` | 本地分支（`*` 为当前） |
| `git branch -a` | 含远程分支 |
| `git switch 分支` | 切换分支 |
| `git switch -c 分支` | 创建并切换（最常用） |
| `git merge 分支` | 把该分支合并到当前分支 |
| `git branch -d 分支` / `-D` | 删除已合并 / 强制删除分支 |
| `git branch -m 新名` | 重命名当前分支 |

## 七、远程仓库

| 命令 | 作用 |
|---|---|
| `git remote -v` | 查看远程地址 |
| `git remote add origin 地址` | 关联远程仓库 |
| `git remote set-url origin 地址` | 修改远程地址 |
| `git remote remove origin` | 取消关联 |
| `git push` | 推送（已绑定上游） |
| `git fetch origin` | 只下载更新，不合并 |
| `git pull` | 拉取并合并（= fetch + merge） |
| `git push --force-with-lease` | 安全强推：远程有他人新提交时会被拒绝 ⚠️ |

`想确认远程有没有新改动`

远程更新 → 你不 fetch → origin/main 影子不变 → status 看不出差别
远程更新 → 执行 git fetch → origin/main 影子刷新 → status 才会告诉你落后了

>git fetch
>git status

## 八、撤销与回退

> 原则：按改动所处阶段选命令；已 push 的公共分支用 `revert`，不改写历史。

| 阶段 | 命令 | 结果 |
|---|---|---|
| 改了，没 add | `git restore 文件` | 丢弃工作区改动（`git restore .` 全部） |
| add 了，没 commit | `git restore --staged 文件` | 撤出暂存区，改动回到工作区 |
| commit 了，没 push | `git reset --soft HEAD~1` | 撤 commit，改动保留在暂存区 |
| 同上 | `git reset --mixed HEAD~1` | 撤 commit + 撤 add，改动保留在工作区（默认） |
| 同上 | `git reset --hard HEAD~1` | ⚠️ 撤 commit 并丢弃改动，找不回 |
| 回退到指定版本 | `git reset --hard 提交ID` | ⚠️ 该版本之后的提交全部丢弃 |
| 已 push | `git revert 提交ID` | 生成反向提交抵消，不改写历史 |

`HEAD` 指向当前最新提交；`HEAD~1` = 上一个提交，`HEAD~2` = 上两个提交；`提交ID` 是哈希值。

- `restore` 是新命令，取代旧的 `checkout -- 文件`
- `reset` 会移动 HEAD 指针、改写本地历史，`--hard` 丢掉的改动很难找回
- `revert` 保留完整历史，团队协作首选

## 九、stash（不提交就切分支）

| 命令 | 作用 |
|---|---|
| `git stash` / `git stash -u` | 暂存改动 / 连未追踪新文件一起存 |
| `git stash list` | 查看储藏列表 `stash@{0}` |
| `git stash pop` / `git stash apply` | 取出并删除记录 / 取出但保留记录 |
| `git stash drop` / `git stash clear` | 删最近一条 / 清空所有 |

```bash
git stash          # 代码写到一半，先存起来
git switch main    # 去处理紧急问题
git switch -       # 回到原分支
git stash pop      # 恢复改动
```

## 十、忽略文件 .gitignore

在项目根目录新建 `.gitignore`，逐行写规则：

```gitignore
*.log
node_modules/
build/
.env
```

已提交过的文件要停止跟踪：

```bash
git rm -r --cached 文件或目录    # 移出版本控制，本地文件保留
git commit -m "移除已跟踪文件"
git check-ignore -v 文件         # 查看忽略规则是否命中
```

## 十一、标签 Tag（发布版本）

| 命令 | 作用 |
|---|---|
| `git tag` | 查看所有标签 |
| `git tag -a v1.0 -m "说明"` | 打附注标签（推荐） |
| `git push origin v1.0` / `git push --tags` | 推送单个 / 全部标签 |
| `git tag -d v1.0` | 删除本地标签 |

## 十二、冲突处理

`git pull` 或 `git merge` 时同一行被两边改动，文件里会出现：

```text
<<<<<<< HEAD
本地代码
=======
远程代码
>>>>>>> origin/main
```

```bash
# 1. 手动删掉 <<<、===、>>> 标记，留下正确内容
git add 冲突文件
git commit -m "解决冲突"
git push
```

- 放弃这次合并：`git merge --abort`
- 只列出冲突文件：`git diff --name-only --diff-filter=U`

## 十三、其他实用命令

| 命令 | 作用 |
|---|---|
| `git rm 文件` / `git mv 旧 新` | 删除 / 重命名并加入暂存 |
| `git clean -n` / `git clean -fd` | 预览 / 删除未追踪文件 ⚠️ 不可恢复 |
| `git shortlog -sn` | 统计各人提交次数 |
| `git blame 文件` | 每行最后由谁修改 |
| `git reflog` | HEAD 移动记录，找回误删提交的救星 |

误用 `reset --hard` 后找回提交：

```bash
git reflog
git reset --hard 那个提交ID
```

## 十四、危险命令

| 命令 | 风险 |
|---|---|
| `git reset --hard` | 丢弃工作区改动（commit 可用 reflog 找回） |
| `git clean -fd` | 永久删除未追踪文件，无法恢复 |
| `git push --force` | 覆盖远程历史，可能毁掉他人提交；优先用 `--force-with-lease` |
| `git branch -D` | 删未合并分支，提交可能丢失 |

> 执行前先 `git status` + `git log --oneline` 确认；不放心就先 `git stash` 或 `git branch 备份名`。
