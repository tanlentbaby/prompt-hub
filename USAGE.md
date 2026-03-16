# Prompt Hub 使用文档

> 完整的操作指南与实战示例

---

## 目录

- [快速入门](#快速入门)
- [命令行工具详解](#命令行工具详解)
- [Python API 详解](#python-api-详解)
- [Skills 快捷命令详解](#skills-快捷命令详解)
- [Agent 使用指南](#agent-使用指南)
- [实战场景](#实战场景)
- [高级技巧](#高级技巧)
- [常见问题](#常见问题)

---

## 快速入门

### 安装准备

```bash
# 1. 克隆或进入项目目录
cd /Users/esther/Documents/git/workDir/ai-coding/prompt-hub

# 2. 确认 Python 版本（需要 Python 3.7+）
python --version

# 3. 验证安装
python prompt_manager.py categories
```

### 第一个模板

```bash
# 搜索 SQL 相关模板
python prompt_manager.py search SQL

# 查看模板详情
python prompt_manager.py show code_gen/sql

# 使用 Python 快速生成
python -c "
from prompt_manager import quick_prompt
print(quick_prompt('code_gen/sql', query_description='查询所有用户', db_type='MySQL', table_schema='users(id, name, email)'))
"
```

---

## 命令行工具详解

### 1. categories - 查看所有分类

```bash
python prompt_manager.py categories
```

**输出示例：**
```
============================================================
可用分类:
============================================================

  code_gen (12 个模板)

  data_analysis (8 个模板)

  docs (5 个模板)

  devops (5 个模板)

  email (3 个模板)

  project (4 个模板)

  marketing (2 个模板)

  education (1 个模板)

  hr (1 个模板)

  legal (1 个模板)

  career (2 个模板)

  general (3 个模板)

  security (1 个模板)

  system (2 个模板)
```

### 2. list - 列出模板

#### 列出所有模板

```bash
python prompt_manager.py list
```

**输出示例：**
```
============================================================
所有模板:
============================================================

[code_gen]
  - function: 生成函数/方法代码
  - class: 生成类定义
  - api: 生成 API 端点
  - refactor: 代码重构/优化
  - sql: 生成 SQL 查询
  - unit_test: 生成单元测试
  - code_review: 代码审查 Checklist
  - commit_message: 生成 Git Commit Message
  - dockerfile: 生成 Dockerfile
  - react_component: React 组件生成
  - python_script: Python 自动化脚本
  - database_design: 数据库表结构设计

[data_analysis]
  - eda: 探索性数据分析
  - cleaning: 数据清洗流程
  ...
```

#### 列出指定分类

```bash
python prompt_manager.py list code_gen
```

**输出示例：**
```
============================================================
分类：code_gen
============================================================
  - function
  - class
  - api
  - refactor
  - sql
  - unit_test
  - code_review
  - commit_message
  - dockerfile
  - react_component
  - python_script
  - database_design
```

### 3. search - 搜索模板

#### 基础搜索

```bash
# 搜索 SQL 相关
python prompt_manager.py search SQL

# 搜索中文关键词
python prompt_manager.py search 邮件
python prompt_manager.py search 测试
python prompt_manager.py search K8s
```

**输出示例：**
```
找到 2 个相关模板:

----------------------------------------------------------------------
1. code_gen/sql
   描述：生成 SQL 查询
   匹配：[名称] (相关度：3)

----------------------------------------------------------------------
2. data_analysis/sql_analysis
   描述：SQL 数据分析
   匹配：[名称] (相关度：3)
```

#### 详细搜索（显示变量）

```bash
python prompt_manager.py search -v SQL
```

**输出示例：**
```
找到 2 个相关模板:

----------------------------------------------------------------------
1. code_gen/sql
   描述：生成 SQL 查询
   变量：query_description, db_type, table_schema
   匹配：[名称] (相关度：3)

----------------------------------------------------------------------
2. data_analysis/sql_analysis
   描述：SQL 数据分析
   变量：analysis_goal, db_type, tables, time_range, metrics
   匹配：[名称] (相关度：3)
```

#### 按范围搜索

```bash
# 只搜索名称
python prompt_manager.py search --in name function

# 只搜索描述
python prompt_manager.py search --in description 分析

# 只搜索变量
python prompt_manager.py search --in variable language
```

### 4. show - 查看模板详情

```bash
# 使用完整路径
python prompt_manager.py show code_gen/sql

# 使用简短名称
python prompt_manager.py show sql
```

**输出示例：**
```
============================================================
模板：code_gen/sql
描述：生成 SQL 查询
============================================================

变量列表 (3 个):
  - query_description
  - db_type
  - table_schema

模板预览:
------------------------------------------------------------
# 角色
你是一位 SQL 专家

# 任务
请帮我编写一个 SQL 查询

# 数据库类型
{db_type:-MySQL}

# 查询需求
{query_description}

# 表结构
{table_schema}

# 输出要求
- 只输出 SQL 语句
- 添加必要的注释
------------------------------------------------------------
```

---

## Python API 详解

### PromptTemplate 类

#### 加载模板

```python
from prompt_manager import PromptTemplate

# 加载模板
template = PromptTemplate.load("code_gen/sql")

print(f"模板名称: {template.name}")
print(f"变量列表: {template.list_variables()}")
```

#### 填充模板

```python
# 基础填充
prompt = template.fill(
    query_description="查询最近 30 天的订单",
    db_type="MySQL",
    table_schema="orders(id, user_id, amount, created_at)"
)
print(prompt)

# 使用默认值（不填 db_type）
prompt = template.fill(
    query_description="查询所有用户",
    table_schema="users(id, name, email)"
)
# db_type 会使用默认值 MySQL
```

#### 查看变量信息

```python
template = PromptTemplate.load("devops/k8s")

# 列出所有变量
print(template.list_variables())
# 输出: ['application_description', 'app_name', 'image', 'port', 'replicas', 'namespace']

# 检查必需变量（需要在实现中完善）
```

### TemplateRegistry 类

#### 列出所有模板

```python
from prompt_manager import TemplateRegistry

# 列出所有模板信息
registry = TemplateRegistry.list_all()
print(registry)

# 获取版本
print(registry['version'])  # 1.2.0
```

#### 按分类列出

```python
# 列出指定分类的模板
templates = TemplateRegistry.list_templates("code_gen")
print(templates)
# 输出: ['function', 'class', 'api', 'refactor', ...]

# 列出所有模板（带分类前缀）
all_templates = TemplateRegistry.list_templates()
print(all_templates)
# 输出: ['code_gen/function', 'code_gen/class', ...]
```

#### 搜索模板

```python
# 基础搜索
results = TemplateRegistry.search("SQL")
for r in results:
    print(f"{r['path']}: {r['description']}")

# 查看搜索详情
results = TemplateRegistry.search("测试")
for r in results:
    print(f"""
路径: {r['path']}
描述: {r['description']}
匹配: {r['match_reasons']}
相关度: {r['score']}
    """)
```

#### 按范围搜索

```python
# 只在名称中搜索
results = TemplateRegistry.search("function", search_in="name")

# 只在描述中搜索
results = TemplateRegistry.search("分析", search_in="description")

# 只在变量中搜索
results = TemplateRegistry.search("language", search_in="variable")
```

#### 获取模板信息

```python
# 获取模板详细信息
info = TemplateRegistry.get_template_info("sql")
print(f"""
完整路径: {info['full_path']}
分类: {info['category']}
描述: {info['description']}
变量: {info['variables']}
文件路径: {info['path']}
""")

# 获取分类下所有模板
category_info = TemplateRegistry.get_category_info("code_gen")
print(category_info)
```

#### 列出分类

```python
categories = TemplateRegistry.list_categories()
print(categories)
# 输出: ['code_gen', 'data_analysis', 'docs', ...]
```

### 快捷函数

#### quick_prompt - 快速生成

```python
from prompt_manager import quick_prompt

# 一次性加载并填充
prompt = quick_prompt(
    "code_gen/function",
    language="Python",
    function_name="calculate_sum",
    description="计算列表中所有数字的总和"
)
print(prompt)
```

---

## Skills 快捷命令详解

### /pl 或 /prompt-list - 列出模板

#### 列出所有模板

```
/pl
```

#### 列出指定分类

```
/pl code_gen
/pl devops
/pl docs
```

### /ps 或 /prompt-search - 搜索模板

#### 基础搜索

```
/ps SQL
/ps 邮件
/ps 测试
/ps K8s
/ps 简历
```

#### 常用搜索关键词

```
# 代码相关
/ps 函数
/ps 类
/ps API
/ps 重构
/ps Docker

# 数据相关
/ps SQL
/ps 可视化
/ps 清洗
/ps 机器学习

# 文档相关
/ps README
/ps 会议
/ps 周报
/ps FAQ

# 运维相关
/ps K8s
/ps Nginx
/ps CI/CD
/ps Git

# 其他
/ps 简历
/ps 面试
/ps 合同
/ps SEO
```

### /psh 或 /prompt-show - 查看详情

```
# 使用简短名称
/psh sql
/psh k8s
/psh function

# 使用完整路径
/psh code_gen/sql
/psh devops/k8s
```

### /pf 或 /prompt-fill - 填充模板

#### SQL 查询生成

```
/pf sql query="查询最近 30 天的订单" db_type="MySQL" table_schema="orders(id, user_id, amount, created_at)"
```

#### 函数生成

```
/pf function language="Python" function_name="parse_json" description="解析 JSON 字符串并返回字典"
```

#### K8s 部署配置

```
/pf k8s app_name="nginx" image="nginx:1.24" port="80" replicas="3"
```

#### 会议纪要

```
/pf meeting_notes title="周会" date="2026-03-16" attendees="张三，李四，王五" notes="讨论项目进度..."
```

#### React 组件

```
/pf react_component component_name="UserProfile" functional_requirements="显示用户头像、姓名、个人简介"
```

#### 简历优化

```
/pf resume target_position="前端工程师" experience_years="3 年"
```

### /pa 或 /prompt-add - 添加模板

```
/pa template_name="my_template" category="code_gen" description="我的自定义模板"
```

### /pn 或 /prompt-new - 交互式创建

```
/pn
```

系统会引导你完成：
1. 输入模板名称
2. 选择分类
3. 填写描述
4. 定义变量
5. 生成模板

### /pr 或 /prompt-register - 注册模板

```
/pr template_file="my_template.md"
```

### /pt 或 /prompt-template - AI 生成模板

```
/pt 我需要一个生成 Python 爬虫的模板
/pt 帮我创建一个 Terraform 配置模板
```

---

## Agent 使用指南

### 激活方式

在 Claude Code 中直接说出需求：

```
使用 Prompt Hub 帮我找一个 SQL 模板
```

### 常用指令

#### 列出模板

```
列出所有模板
列出 code_gen 分类
```

#### 搜索模板

```
搜索 SQL 相关的模板
找一下 K8s 的配置模板
有没有生成函数的模板？
```

#### 查看详情

```
查看 SQL 模板的详情
show k8s
```

#### 填充使用

```
用 SQL 模板生成一个查询订单的语句
fill k8s app_name="myapp" image="myapp:1.0"
```

---

## 实战场景

### 场景一：Web 开发

```bash
# 1. 生成数据库设计
/pf database_design project_name="博客系统" entities="用户，文章，评论，分类"

# 2. 生成 API 端点
/pf api framework="FastAPI" endpoints="用户登录，文章列表，评论提交" models="User, Post, Comment"

# 3. 生成 Dockerfile
/pf dockerfile application_description="FastAPI 博客 API" language="Python" port="8000"

# 4. 生成 K8s 配置
/pf k8s app_name="blog-api" image="blog-api:1.0" port="8000" replicas="3"
```

### 场景二：数据分析

```bash
# 1. 探索性数据分析
/pf eda data_source="sales.csv" columns="日期，产品，销售额，地区" analysis_goals="了解销售趋势，找出热销产品"

# 2. 数据清洗
/pf cleaning data_issues="缺失值，重复行，异常值" cleaning_rules="删除重复，填充缺失"

# 3. 可视化
/pf visualization chart_type="折线图" x_axis="日期" y_axis="销售额"

# 4. SQL 分析
/pf sql_analysis analysis_goal="月度销售统计" db_type="MySQL" tables="orders,order_items"
```

### 场景三：项目管理

```bash
# 1. 项目计划
/pf plan project_name="移动端 App 开发" start_date="2026-04-01" end_date="2026-06-30" project_background="开发一款电商 App"

# 2. PRD 文档
/pf prd product_name="电商 App" goals="提供便捷的购物体验，支持多种支付方式"

# 3. 状态报告
/pf status_report project_name="移动端 App" report_period="第 2 周"
```

### 场景四：求职准备

```bash
# 1. 简历优化
/pf resume target_position="Python 后端工程师" experience_years="5 年"

# 2. 面试问题准备
/pf interview_questions job_title="Python 后端开发" tech_stack="Python,Django,Redis,MySQL"

# 3. 绩效报告
/pf performance_review position="后端工程师" review_period="2025 年度"
```

### 场景五：DevOps

```bash
# 1. CI/CD 配置
/pf cicd project_description="Web 应用自动部署" platform="GitHub Actions" language="Node.js"

# 2. Nginx 配置
/pf nginx domain="api.example.com" backend="localhost:3000" port="80" app_type="API"

# 3. Git 命令
/pf git git_task_description="合并功能分支到主分支" current_branch="feature/user-auth" target_branch="main"

# 4. Shell 脚本
/pf shell_script script_description="自动备份数据库" os="Linux" arguments="数据库名，备份路径"
```

---

## 高级技巧

### 技巧 1：组合使用模板

```bash
# 先设计数据库
/pf database_design project_name="任务管理系统" entities="用户，项目，任务"

# 再生成 API
/pf api framework="Django REST Framework" endpoints="CRUD 用户，项目，任务" models="User, Project, Task"

# 最后生成测试
/pf unit_test code="视图代码" language="Python" test_framework="pytest"
```

### 技巧 2：使用默认值

```bash
# 只填必需参数，其他使用默认值
/pf sql query="查询所有用户" table_schema="users(id, name)"
# db_type 会使用默认值 MySQL
```

### 技巧 3：批量操作

```python
from prompt_manager import PromptTemplate

# 批量生成多个函数
templates = [
    ("calculate_sum", "计算列表总和"),
    ("calculate_avg", "计算列表平均值"),
    ("find_max", "找出列表最大值"),
]

for func_name, desc in templates:
    prompt = PromptTemplate.load("code_gen/function").fill(
        language="Python",
        function_name=func_name,
        description=desc
    )
    print(f"\n{'='*50}\n{prompt}\n")
```

### 技巧 4：自定义默认值

```python
# 修改模板文件中的默认值
# 原来：{db_type:-MySQL}
# 修改为：{db_type:-PostgreSQL}
```

### 技巧 5：创建模板链

```bash
# 1. 创建项目计划
/pf plan project_name="CRM 系统" ...

# 2. 创建 PRD
/pf prd product_name="CRM 系统" ...

# 3. 生成数据库设计
/pf database_design project_name="CRM 系统" ...

# 4. 生成 API
/pf api framework="FastAPI" ...

# 5. 生成部署配置
/pf k8s app_name="crm-api" ...
```

---

## 常见问题

### Q1: 模板找不到？

```bash
# 使用完整路径
python prompt_manager.py show code_gen/sql

# 或搜索后确认名称
python prompt_manager.py search SQL
```

### Q2: 变量不生效？

检查变量格式是否正确：
```markdown
# 正确格式
{variable}
{variable:-default}

# 错误格式
{ variable }
{variable}
```

### Q3: 如何添加新分类？

1. 创建目录
```bash
mkdir my_category
```

2. 更新 registry.json
3. 更新 skills.json

### Q4: Skills 命令不生效？

检查 Skills 文件是否正确配置：
- 确认文件在 `skills/` 目录下
- 确认 skills.json 已更新
- 重启 Claude Code

### Q5: 如何备份模板？

```bash
# 备份整个目录
cp -r /path/to/prompt-hub /path/to/backup/prompt-hub-$(date +%Y%m%d)

# 或使用 git
git add .
git commit -m "backup templates"
```

### Q6: 模板可以嵌套使用吗？

可以，手动复制输出再使用：

```bash
# 先生成数据库设计
/pf database_design ... (复制输出)

# 再将输出作为 API 模板的输入
/pf api models="User, Project, Task (来自上一步)"
```

---

## 命令速查表

| 操作 | 命令行 | Python | Skills |
|------|--------|--------|--------|
| 列出分类 | `categories` | `list_categories()` | `/pl` |
| 列出模板 | `list [cat]` | `list_templates(cat)` | `/pl [cat]` |
| 搜索 | `search <kw>` | `search(kw)` | `/ps <kw>` |
| 查看详情 | `show <tmpl>` | `load(name)` | `/psh <tmpl>` |
| 填充 | - | `fill(**kwargs)` | `/pf <tmpl> ...` |
| 添加 | `./add-template.sh` | - | `/pa` |
| 创建 | - | - | `/pn` |

---

## 更多帮助

- [README.md](README.md) - 项目概述
- [EXTENSION_GUIDE.md](EXTENSION_GUIDE.md) - 扩展指南
- [NEW_TEMPLATES.md](NEW_TEMPLATES.md) - 新增模板说明

---

**版本**: v3.0 | **更新日期**: 2026-03-16
