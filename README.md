# Prompt Hub - 提示词模板管理系统

> **v3.0** - 现在支持随时扩展添加新模板！

## 目录结构

```
prompt_templates/
├── README.md           # 本文件
├── registry.json       # 模板注册表
├── prompt_manager.py   # Python 管理器
├── code_gen/           # 代码生成模板（9 个）
│   ├── function.md     # 函数生成
│   ├── class.md        # 类生成
│   ├── api.md          # API 生成
│   ├── refactor.md     # 重构优化
│   ├── sql.md          # SQL 查询生成
│   ├── unit_test.md    # 单元测试生成
│   ├── code_review.md  # 代码审查 Checklist
│   ├── commit_message.md # Git Commit 生成
│   └── dockerfile.md   # Dockerfile 生成
├── data_analysis/      # 数据分析模板（8 个）
│   ├── eda.md          # 探索性分析
│   ├── cleaning.md     # 数据清洗
│   ├── visualization.md # 可视化
│   ├── ml_pipeline.md  # 机器学习管道
│   ├── sql_analysis.md # SQL 数据分析
│   ├── excel_formula.md # Excel 公式生成
│   ├── regex.md        # 正则表达式生成
│   └── json_yaml.md    # JSON/YAML 处理
├── docs/               # 文档模板（4 个）
│   ├── readme.md       # README 生成
│   ├── api_docs.md     # API 文档生成
│   ├── meeting_notes.md # 会议纪要整理
│   └── weekly_report.md # 周报/日报生成
├── devops/             # DevOps 模板（4 个）
│   ├── k8s.md          # K8s 资源配置
│   ├── cicd.md         # CI/CD 流水线
│   ├── shell_script.md # Shell 脚本
│   └── nginx.md        # Nginx 配置
├── email/              # 邮件模板（3 个）
│   ├── business.md     # 商务邮件
│   ├── notice.md       # 通知邮件
│   └── ppt_outline.md  # PPT 大纲
├── project/            # 项目模板（3 个）
│   ├── plan.md         # 项目计划
│   ├── status_report.md # 状态报告
│   └── roadmap.md      # 产品路线图
└── system/             # 系统模板（2 个）
    ├── base.md         # 基础模板
    └── role.md         # 角色设定

**扩展工具**:
├── skills/             # Skills 工具（8 个）
│   ├── prompt-list.md      # 列出模板
│   ├── prompt-search.md    # 搜索模板
│   ├── prompt-show.md      # 查看详情
│   ├── prompt-fill.md      # 填充模板
│   ├── prompt-add.md       # 添加模板
│   ├── prompt-new.md       # 创建模板
│   ├── prompt-register.md  # 注册模板
│   └── prompt-template.md  # 模板生成器
├── add-template.sh     # 命令行添加工具
├── EXTENSION_GUIDE.md  # 扩展指南
└── EXTENSION_README.md # 扩展能力说明
```

**总计：41 个**（33 个提示词模板 + 8 个 Skills 工具）

## 使用方法

### 方式一：命令行工具（推荐）

```bash
cd /Users/cq/Documents/doc/prompt_templates

# 1. 查看所有分类
python prompt_manager.py categories

# 2. 列出所有模板
python prompt_manager.py list

# 3. 按分类查看模板
python prompt_manager.py list code_gen
python prompt_manager.py list data_analysis
python prompt_manager.py list devops

# 4. 搜索模板（支持中文关键词）
python prompt_manager.py search SQL
python prompt_manager.py search 邮件
python prompt_manager.py search K8s

# 5. 查看详细搜索结果（显示变量）
python prompt_manager.py search -v 测试

# 6. 按范围搜索
python prompt_manager.py search --in name function      # 只搜索名称
python prompt_manager.py search --in description 分析   # 只搜索描述
python prompt_manager.py search --in variable language  # 只搜索变量

# 7. 查看模板详情（显示完整内容和变量）
python prompt_manager.py show code_gen/sql
python prompt_manager.py show devops/k8s
python prompt_manager.py show project/plan

# 8. 查看帮助
python prompt_manager.py --help
```

### 方式二：Python 调用

```python
from prompt_manager import PromptTemplate, quick_prompt, TemplateRegistry

# --- 快速生成 ---
prompt = quick_prompt(
    "code_gen/function",
    language="Python",
    function_name="parse_data",
    description="解析 JSON 数据"
)

# --- 加载模板后填充 ---
template = PromptTemplate.load("code_gen/sql")
sql_prompt = template.fill(
    query_description="查询最近 30 天的订单",
    db_type="MySQL",
    table_schema="orders(id, user_id, amount, created_at)"
)

# --- 搜索模板 ---
results = TemplateRegistry.search("SQL")
for r in results:
    print(f"{r['path']}: {r['description']}")

# --- 查看模板变量 ---
template = PromptTemplate.load("devops/k8s")
print(template.list_variables())

# --- 获取模板详情 ---
info = TemplateRegistry.get_template_info("sql")
print(info)

# --- 列出分类 ---
categories = TemplateRegistry.list_categories()
print(categories)
```

### 方式三：直接读取文件

直接打开 `.md` 文件，手动替换 `{变量}` 后使用。

```bash
# 查看模板文件
cat code_gen/sql.md

# 或用编辑器打开
code code_gen/sql.md
```

### 方式四：使用 Skills（快捷命令）

在 Claude Code 中，可以使用 Skills 快捷命令：

```bash
/pl              # 列出所有模板
/pl code_gen     # 列出指定分类
/ps SQL          # 搜索模板
/psh sql         # 查看模板详情
/pf sql query="查询订单" db_type="MySQL"  # 填充模板

# 扩展命令（v3.0 新增）
/pa template_name="xxx" category="xxx"  # 添加模板
/pn                                     # 交互式创建模板
/pr template_file="xxx.md"              # 注册模板
/pt "我需要一个 XXX 模板"                # AI 生成模板
```

### 方式五：在 Claude Code 中使用 Agent

```
# 激活 Prompt Hub Agent
使用 Prompt Hub 帮我...

# 自然语言请求
帮我找个生成 SQL 的模板
用 K8s 模板部署 nginx
```

### 方式六：命令行添加模板

```bash
cd /Users/cq/Documents/doc/prompt_templates

# 添加新模板
./add-template.sh -n my_template -c code_gen -d "我的模板"

# 查看扩展指南
cat EXTENSION_GUIDE.md
```

## 模板语法

- `{variable}` — 必需参数
- `{variable:-默认值}` — 有默认值，可不填

示例：
```markdown
# 数据库类型：{db_type:-PostgreSQL}  ← 不填就用 PostgreSQL
# 必填参数：{query_description}       ← 必须提供
```

## 模板列表

### 代码生成（code_gen）- 9 个

| # | 模板名 | 描述 | 主要变量 |
|---|--------|------|----------|
| 1 | function | 函数/方法生成 | language, function_name, description |
| 2 | class | 类定义生成 | language, class_name, methods |
| 3 | api | API 端点生成 | framework, endpoints, models |
| 4 | refactor | 代码重构/优化 | code, issues, goals |
| 5 | sql | SQL 查询生成 | query_description, db_type, table_schema |
| 6 | unit_test | 单元测试生成 | code, language, test_framework |
| 7 | code_review | 代码审查 Checklist | code, language |
| 8 | commit_message | Git Commit Message | changes_description, issue |
| 9 | dockerfile | Dockerfile 生成 | application_description, language, port |

### 数据分析（data_analysis）- 8 个

| # | 模板名 | 描述 | 主要变量 |
|---|--------|------|----------|
| 1 | eda | 探索性数据分析 | data_source, columns, analysis_goals |
| 2 | cleaning | 数据清洗流程 | data_issues, cleaning_rules |
| 3 | visualization | 数据可视化 | chart_type, x_axis, y_axis |
| 4 | ml_pipeline | 机器学习管道 | task_type, features, target, models |
| 5 | sql_analysis | SQL 数据分析 | analysis_goal, db_type, tables |
| 6 | excel_formula | Excel 公式生成 | problem_description, data_structure |
| 7 | regex | 正则表达式生成 | task_description, input_example |
| 8 | json_yaml | JSON/YAML 处理 | task_type, input_data, output_format |

### 文档（docs）- 4 个

| # | 模板名 | 描述 | 主要变量 |
|---|--------|------|----------|
| 1 | readme | README 文档生成 | project_name, description, features |
| 2 | api_docs | API 文档生成 | api_name, base_url, endpoints |
| 3 | meeting_notes | 会议纪要整理 | meeting_title, attendees, notes |
| 4 | weekly_report | 周报/日报生成 | report_type, completed_tasks |

### DevOps（devops）- 4 个

| # | 模板名 | 描述 | 主要变量 |
|---|--------|------|----------|
| 1 | k8s | Kubernetes 资源配置 | app_name, image, port, replicas |
| 2 | cicd | CI/CD 流水线配置 | project_description, platform, language |
| 3 | shell_script | Shell 脚本生成 | script_description, os, arguments |
| 4 | nginx | Nginx 配置生成 | domain, backend, port, app_type |

### 邮件（email）- 3 个

| # | 模板名 | 描述 | 主要变量 |
|---|--------|------|----------|
| 1 | business | 商务邮件生成 | email_type, recipient, subject |
| 2 | notice | 通知邮件生成 | notice_type, audience, content |
| 3 | ppt_outline | PPT 大纲生成 | presentation_title, purpose, audience |

### 项目管理（project）- 3 个

| # | 模板名 | 描述 | 主要变量 |
|---|--------|------|----------|
| 1 | plan | 项目计划制定 | project_name, start_date, background |
| 2 | status_report | 项目状态报告 | project_name, report_period |
| 3 | roadmap | 产品路线图规划 | product_name, planning_period, vision |

### 系统（system）- 2 个

| # | 模板名 | 描述 | 主要变量 |
|---|--------|------|----------|
| 1 | base | 基础通用模板 | role, task, context, constraints |
| 2 | role | 角色设定模板 | role, expertise, style, tone |

---

**总计：33 个模板，7 个分类**
