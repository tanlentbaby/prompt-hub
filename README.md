# Prompt Hub - 提示词模板管理系统

> **你的 AI 提示词资产库** - 结构化管理 52+ 个提示词模板，支持随时扩展

[![模板数量](https://img.shields.io/badge/模板-52%2B-blue)](#模板列表)
[![分类数量](https://img.shields.io/badge/分类-15-green)](#分类目录)
[![Skills工具](https://img.shields.io/badge/Skills-8-orange)](#方式四使用-skills-快捷命令)
[![版本](https://img.shields.io/badge/版本-3.0-red)](#更新日志)

---

## 目录

- [快速开始](#快速开始)
- [项目架构](#项目架构)
- [使用方法](#使用方法)
- [模板列表](#模板列表)
- [扩展指南](#扩展指南)
- [模板语法](#模板语法)

---

## 快速开始

### 方式一：Skills 快捷命令（推荐）

```bash
# 在 Claude Code 中直接使用
/prompt-list                    # 列出所有模板
/prompt-search SQL              # 搜索模板
/prompt-show sql                # 查看详情
/prompt-fill sql query="查询订单" db_type="MySQL"  # 填充使用
```

### 方式二：命令行工具

```bash
cd /Users/esther/Documents/git/workDir/ai-coding/prompt-hub

python prompt_manager.py list           # 列出模板
python prompt_manager.py search SQL      # 搜索
python prompt_manager.py show code_gen/sql  # 查看详情
```

### 方式三：Python 调用

```python
from prompt_manager import quick_prompt

prompt = quick_prompt(
    "code_gen/function",
    language="Python",
    function_name="parse_data",
    description="解析 JSON 数据"
)
```

---

## 项目架构

```
prompt-hub/
├── 核心系统
│   ├── registry.json           # 模板注册表（元数据）
│   ├── prompt_manager.py       # Python 管理器
│   └── add-template.sh         # 命令行添加工具
│
├── 模板文件（52 个）
│   ├── code_gen/              # 代码生成（12 个）
│   ├── data_analysis/         # 数据分析（8 个）
│   ├── docs/                  # 文档（5 个）
│   ├── devops/                # DevOps（5 个）
│   ├── email/                 # 邮件（3 个）
│   ├── project/               # 项目管理（4 个）
│   ├── marketing/             # 营销推广（2 个）
│   ├── education/             # 教育学习（1 个）
│   ├── hr/                    # 人力资源（1 个）
│   ├── legal/                 # 法律合同（1 个）
│   ├── career/                # 职业发展（2 个）
│   ├── general/               # 通用工具（3 个）
│   ├── security/              # 安全审计（1 个）
│   └── system/                # 系统（2 个）
│
├── Skills 工具（8 个）
│   ├── prompt-list.md         # /prompt-list - 列出模板
│   ├── prompt-search.md       # /prompt-search - 搜索模板
│   ├── prompt-show.md         # /prompt-show - 查看详情
│   ├── prompt-fill.md         # /prompt-fill - 填充模板
│   ├── prompt-add.md          # /prompt-add - 添加模板
│   ├── prompt-new.md          # /prompt-new - 创建模板
│   ├── prompt-register.md     # /prompt-register - 注册模板
│   └── prompt-template.md     # /prompt-template - 模板生成器
│
├── Agent 定义
│   ├── prompt_hub_agent.md    # Prompt Hub 代理
│   └── prompt_manager_agent.md # Prompt 管理代理
│
└── 文档
    ├── README.md              # 本文件
    ├── EXTENSION_GUIDE.md     # 扩展指南
    └── NEW_TEMPLATES.md       # 新增模板说明
```

---

## 使用方法

### 方式一：命令行工具

```bash
cd /Users/esther/Documents/git/workDir/ai-coding/prompt-hub

# 1. 查看所有分类
python prompt_manager.py categories

# 2. 列出所有模板
python prompt_manager.py list

# 3. 按分类查看
python prompt_manager.py list code_gen
python prompt_manager.py list data_analysis

# 4. 搜索模板（支持中文）
python prompt_manager.py search SQL
python prompt_manager.py search 邮件
python prompt_manager.py search K8s

# 5. 详细搜索（显示变量）
python prompt_manager.py search -v 测试

# 6. 按范围搜索
python prompt_manager.py search --in name function
python prompt_manager.py search --in description 分析
python prompt_manager.py search --in variable language

# 7. 查看模板详情
python prompt_manager.py show code_gen/sql
python prompt_manager.py show devops/k8s
```

### 方式二：Python API

```python
from prompt_manager import PromptTemplate, TemplateRegistry, quick_prompt

# --- 快速生成 ---
prompt = quick_prompt(
    "code_gen/function",
    language="Python",
    function_name="parse_data",
    description="解析 JSON 数据"
)

# --- 加载后填充 ---
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

# --- 查看变量 ---
template = PromptTemplate.load("devops/k8s")
print(template.list_variables())

# --- 列出分类 ---
categories = TemplateRegistry.list_categories()
print(categories)
```

### 方式三：直接读取文件

```bash
# 查看模板文件
cat code_gen/sql.md

# 用编辑器打开
code code_gen/sql.md
```

### 方式四：使用 Skills 快捷命令

在 Claude Code 中：

```bash
# 基础命令
/prompt-list                    # 列出所有模板
/prompt-list code_gen          # 列出指定分类
/prompt-search SQL              # 搜索模板
/prompt-show sql                # 查看详情
/prompt-fill sql query="查询订单" db_type="MySQL"  # 填充使用

# 扩展命令
/prompt-add template_name="xxx" category="xxx"  # 添加模板
/prompt-new                                      # 交互式创建
/prompt-register template_file="xxx.md"         # 注册模板
/prompt-template "我需要一个 XXX 模板"          # AI 生成模板
```

### 方式五：使用 Agent

```
# 激活 Prompt Hub Agent
使用 Prompt Hub 帮我...

# 自然语言请求
帮我找个生成 SQL 的模板
用 K8s 模板部署 nginx
```

### 方式六：命令行添加模板

```bash
# 添加新模板
./add-template.sh -n my_template -c code_gen -d "我的模板"

# 查看扩展指南
cat EXTENSION_GUIDE.md
```

---

## 分类目录

| 分类 | 模板数 | 说明 |
|------|--------|------|
| `code_gen` | 12 | 代码生成：函数、类、API、SQL、测试、重构等 |
| `data_analysis` | 8 | 数据分析：EDA、清洗、可视化、ML管道 |
| `docs` | 5 | 文档：README、API文档、会议纪要、周报、FAQ |
| `devops` | 5 | DevOps：K8s、CI/CD、Shell、Nginx、Git |
| `email` | 3 | 邮件文书：商务邮件、通知、PPT大纲 |
| `project` | 4 | 项目管理：计划、状态报告、路线图、PRD |
| `marketing` | 2 | 营销推广：SEO、社交媒体 |
| `education` | 1 | 教育学习：学习计划 |
| `hr` | 1 | 人力资源：面试问题 |
| `legal` | 1 | 法律合同：合同起草 |
| `career` | 2 | 职业发展：简历、绩效报告 |
| `general` | 3 | 通用工具：问答、翻译、文本处理 |
| `security` | 1 | 安全审计：代码审计 |
| `system` | 2 | 系统：基础模板、角色设定 |

**总计：52 个模板，15 个分类，8 个 Skills 工具**

---

## 模板列表

### 代码生成（code_gen）- 12 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `function` | 函数/方法生成 | language, function_name, description |
| `class` | 类定义生成 | language, class_name, methods |
| `api` | API 端点生成 | framework, endpoints, models |
| `refactor` | 代码重构/优化 | code, issues, goals |
| `sql` | SQL 查询生成 | query_description, db_type, table_schema |
| `unit_test` | 单元测试生成 | code, language, test_framework |
| `code_review` | 代码审查 Checklist | code, language |
| `commit_message` | Git Commit Message | changes_description, issue |
| `dockerfile` | Dockerfile 生成 | application_description, language, port |
| `react_component` | React 组件生成 | component_name, functional_requirements |
| `python_script` | Python 自动化脚本 | automation_description |
| `database_design` | 数据库表结构设计 | project_name, entities |

### 数据分析（data_analysis）- 8 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `eda` | 探索性数据分析 | data_source, columns, analysis_goals |
| `cleaning` | 数据清洗流程 | data_issues, cleaning_rules |
| `visualization` | 数据可视化 | chart_type, x_axis, y_axis |
| `ml_pipeline` | 机器学习管道 | task_type, features, target |
| `sql_analysis` | SQL 数据分析 | analysis_goal, db_type, tables |
| `excel_formula` | Excel 公式生成 | problem_description, data_structure |
| `regex` | 正则表达式生成 | task_description, input_example |
| `json_yaml` | JSON/YAML 处理 | task_type, input_data |

### 文档（docs）- 5 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `readme` | README 文档生成 | project_name, description, features |
| `api_docs` | API 文档生成 | api_name, base_url, endpoints |
| `meeting_notes` | 会议纪要整理 | meeting_title, attendees, notes |
| `weekly_report` | 周报/日报生成 | report_type, completed_tasks |
| `faq` | FAQ/技术文档生成 | product_name, common_questions |

### DevOps（devops）- 5 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `k8s` | Kubernetes 资源配置 | app_name, image, port, replicas |
| `cicd` | CI/CD 流水线配置 | project_description, platform |
| `shell_script` | Shell 脚本生成 | script_description, os |
| `nginx` | Nginx 配置生成 | domain, backend, port |
| `git` | Git 命令生成 | git_task_description, current_branch |

### 邮件（email）- 3 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `business` | 商务邮件生成 | email_type, recipient, subject |
| `notice` | 通知邮件生成 | notice_type, audience, content |
| `ppt_outline` | PPT 大纲生成 | presentation_title, purpose |

### 项目管理（project）- 4 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `plan` | 项目计划制定 | project_name, start_date, background |
| `status_report` | 项目状态报告 | project_name, report_period |
| `roadmap` | 产品路线图规划 | product_name, planning_period |
| `prd` | 产品需求文档 | product_name, goals |

### 营销推广（marketing）- 2 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `seo` | SEO 优化建议 | website_url, target_keywords |
| `social_media` | 社交媒体文案 | platform, topic, target_audience |

### 职业发展（career）- 2 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `resume` | 简历优化 | target_position, experience_years |
| `performance_review` | 绩效/述职报告 | position, review_period |

### 通用工具（general）- 3 个

| 模板 | 描述 | 主要变量 |
|------|------|----------|
| `qa` | 问答生成 | question, question_type |
| `translation` | 翻译 | source_text, source_language, target_language |
| `text_processing` | 文本处理 | task_type, input_text |

### 其他分类

| 分类 | 模板 | 说明 |
|------|------|------|
| education | `study_plan` | 学习计划制定 |
| hr | `interview_questions` | 面试问题生成 |
| legal | `contract` | 合同起草 |
| security | `code_audit` | 代码安全审计 |
| system | `base`, `role` | 基础模板、角色设定 |

---

## 扩展指南

### 快速添加模板

```bash
# 使用命令行工具
./add-template.sh -n my_template -c code_gen -d "我的模板描述"

# 或使用 Skills 交互式创建
/prompt-new
```

### 手动添加步骤

1. **创建模板文件** - 在对应分类目录创建 `.md` 文件
2. **编写模板内容** - 使用 `{variable}` 语法
3. **更新 `registry.json`** - 添加模板元数据
4. **更新 Skills 文件** - 在 `skills/prompt-*.md` 中添加逻辑
5. **测试** - 使用 `/prompt-show <模板名>` 验证

详细步骤请参考 [EXTENSION_GUIDE.md](EXTENSION_GUIDE.md)

---

## 模板语法

### 变量定义

| 语法 | 说明 | 示例 |
|------|------|------|
| `{variable}` | 必需参数 | `{query_description}` |
| `{variable:-default}` | 可选参数（有默认值） | `{db_type:-MySQL}` |

### 推荐结构

```markdown
# 角色
你是一位{role}专家

# 任务
{task_description}

# 输入
{input_params}

# 要求
- {requirement_1}
- {requirement_2}

# 输出
{output_format}
```

---

## 核心组件说明

### 1. registry.json

模板注册表，存储所有模板的元数据：
- 路径（path）
- 描述（description）
- 变量列表（variables）

### 2. prompt_manager.py

Python 管理器，提供：
- `PromptTemplate.load()` - 加载模板
- `template.fill()` - 填充变量
- `TemplateRegistry.search()` - 搜索模板
- 命令行接口

### 3. Skills 工具

8 个 Claude Code Skills 快捷命令，用于：
- 列出、搜索、查看、填充模板
- 添加、创建、注册新模板
- AI 辅助生成模板

### 4. Agent

两个 Agent 定义文件：
- `prompt_hub_agent.md` - 模板助手
- `prompt_manager_agent.md` - 管理专用

---

## 更新日志

### v3.0
- 新增 19 个模板
- 新增 8 个分类
- 新增 4 个扩展 Skills 工具
- 支持随时扩展添加新模板

### v2.0
- 新增 Skills 快捷命令
- 新增 Agent 支持
- 优化搜索功能

### v1.0
- 初始版本
- 33 个基础模板
- Python 管理器
