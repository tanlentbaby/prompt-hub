# Prompt Hub Skills

快捷命令，快速访问 33 个提示词模板。

---

## 可用 Skills

| Skill | 别名 | 说明 | 示例 |
|-------|------|------|------|
| `/prompt-list` | `/pl` | 列出所有模板或指定分类 | `/pl` `/pl code_gen` |
| `/prompt-search` | `/ps` | 搜索模板（支持中文） | `/ps SQL` `/ps 邮件` |
| `/prompt-show` | `/psh` | 查看模板详情 | `/psh sql` `/psh k8s` |
| `/prompt-fill` | `/pf` | 填充模板生成提示词 | `/pf sql query="xxx"` |

---

## 支持的模板（33 个）

### code_gen（9 个）
sql, function, class, api, refactor, unit_test, code_review, commit_message, dockerfile

### data_analysis（8 个）
eda, cleaning, visualization, ml_pipeline, sql_analysis, excel_formula, regex, json_yaml

### docs（4 个）
readme, api_docs, meeting_notes, weekly_report

### devops（4 个）
k8s, cicd, shell_script, nginx

### email（3 个）
business, notice, ppt_outline

### project（3 个）
plan, status_report, roadmap

### system（2 个）
base, role

---

## 使用示例

### 1. 列出模板
```
/pl
/pl code_gen
/pl devops
```

### 2. 搜索模板
```
/ps SQL
/ps 邮件
/ps K8s
/ps 会议
```

### 3. 查看模板详情
```
/psh sql
/psh k8s
/psh meeting_notes
/psh function
```

### 4. 填充模板
```
# SQL 查询
/pf sql query="查询最近 30 天的订单" db_type="MySQL" table_schema="orders(id,user_id,amount,created_at)"

# K8s 部署
/pf k8s app_name="nginx" image="nginx:1.24" port="80"

# 会议纪要
/pf meeting_notes title="周会" date="2026-03-15" attendees="张三，李四"

# 函数生成
/pf function language="Python" function_name="parse_data" description="解析 JSON 数据"
```

---

## 在 Claude Code 中使用

### 方式一：直接使用 Skills
```
/pl
/ps SQL
/psh sql
/pf sql query="xxx" db_type="MySQL"
```

### 方式二：使用 Agent 模式
```
使用 Prompt Hub 帮我找个 SQL 模板
```

### 方式三：自然语言
```
帮我生成一个 SQL 查询
我需要一个 K8s 部署配置
```

---

## Skills 文件结构

```
skills/
├── prompt-list.md    # 列出模板
├── prompt-search.md  # 搜索模板
├── prompt-show.md    # 查看模板详情
└── prompt-fill.md    # 填充模板
```

---

## 与 Agent 的区别

| 特性 | Skills | Agent |
|------|--------|-------|
| 触发方式 | `/命令` 直接触发 | 自然语言激活 |
| 执行模式 | 一次性执行 | 多轮对话 |
| 适用场景 | 明确、单一的操作 | 探索、多步骤任务 |
| 响应速度 | 更快 | 更灵活 |

**推荐**:
- 明确知道要哪个模板 → 用 **Skills** (`/pf sql ...`)
- 探索/不确定用哪个 → 用 **Agent** (`帮我找个...`)
