# Prompt Hub Skills

快捷命令，快速访问 70+ 个提示词模板。

---

## 可用 Skills

| Skill | 说明 | 示例 |
|-------|------|------|
| `/prompt-list` | 列出所有模板或指定分类 | `/prompt-list` `/prompt-list code_gen` |
| `/prompt-search` | 搜索模板（支持中文） | `/prompt-search SQL` `/prompt-search 邮件` |
| `/prompt-show` | 查看模板详情 | `/prompt-show sql` `/prompt-show k8s` |
| `/prompt-fill` | 填充模板生成提示词 | `/prompt-fill sql query="xxx"` |
| `/prompt-add` | 添加新的提示词模板 | `/prompt-add template_name="xxx"` |
| `/prompt-new` | 创建新模板（交互式） | `/prompt-new` |
| `/prompt-register` | 注册模板文件到系统 | `/prompt-register xxx.md` |
| `/prompt-template` | AI 模板生成器 | `/prompt-template 我需要...` |
| `/prompt-delete` | 删除模板 | `/prompt-delete template_name` |

---

## 支持的模板（70+ 个，18 个分类）

### code_gen（12 个）
sql, function, class, api, refactor, unit_test, code_review, commit_message, dockerfile, react_component, python_script, database_design

### data_analysis（8 个）
eda, cleaning, visualization, ml_pipeline, sql_analysis, excel_formula, regex, json_yaml

### docs（5 个）
readme, api_docs, meeting_notes, weekly_report, adr

### devops（5 个）
k8s, cicd, shell_script, nginx, deployment

### email（3 个）
business, notice, ppt_outline

### project（4 个）
plan, status_report, roadmap, prd

### architecture（5 个）
service_overview, architecture, domain_design, threat_model, prd

### task（4 个）
story_develop, refactoring, document_design, problem_analysis

### ai_command（4 个）
analyze_design, optimize_design, summarize_folder, review_folder

### testing（1 个）
test_strategy

### storage（1 个）
schema

### system（2 个）
base, role

### 其他分类
marketing, education, hr, legal, career, general, security

---

## 使用示例

### 1. 列出模板
```
/prompt-list
/prompt-list code_gen
/prompt-list devops
```

### 2. 搜索模板
```
/prompt-search SQL
/prompt-search 邮件
/prompt-search K8s
/prompt-search 会议
```

### 3. 查看模板详情
```
/prompt-show sql
/prompt-show k8s
/prompt-show meeting_notes
/prompt-show function
```

### 4. 填充模板
```
# SQL 查询
/prompt-fill sql query="查询最近 30 天的订单" db_type="MySQL" table_schema="orders(id,user_id,amount,created_at)"

# K8s 部署
/prompt-fill k8s app_name="nginx" image="nginx:1.24" port="80"

# 会议纪要
/prompt-fill meeting_notes title="周会" date="2026-03-15" attendees="张三，李四"

# 函数生成
/prompt-fill function language="Python" function_name="parse_data" description="解析 JSON 数据"
```

### 5. 添加/删除模板
```
# 添加新模板
/prompt-add template_name="my_template" category="code_gen" description="我的模板"

# 删除模板
/prompt-delete old_template
```

---

## 在 Claude Code 中使用

### 方式一：直接使用 Skills
```
/prompt-list
/prompt-search SQL
/prompt-show sql
/prompt-fill sql query="xxx" db_type="MySQL"
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
├── prompt-list.md       # 列出模板
├── prompt-search.md     # 搜索模板
├── prompt-show.md       # 查看模板详情
├── prompt-fill.md       # 填充模板
├── prompt-add.md        # 添加模板
├── prompt-new.md        # 创建新模板
├── prompt-register.md   # 注册模板
├── prompt-template.md   # AI 生成模板
├── prompt-delete.md     # 删除模板
└── skills.json          # Skills 配置
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
- 明确知道要哪个模板 → 用 **Skills** (`/prompt-fill sql ...`)
- 探索/不确定用哪个 → 用 **Agent** (`帮我找个...`)
