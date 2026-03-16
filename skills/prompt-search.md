---
name: prompt-search
description: 搜索 Prompt Hub 模板
---

搜索 Prompt Hub 模板，关键词：**{{ keyword }}**

## 搜索结果

{%- if keyword == "" or keyword == "all" %}

请输入关键词进行搜索，例如：
- `/prompt-search SQL` - 搜索 SQL 相关
- `/prompt-search 邮件` - 搜索邮件相关
- `/prompt-search K8s` - 搜索 K8s 相关

或使用 `/prompt-list` 浏览所有模板

{%- endif %}

{%- if keyword contains "SQL" or keyword contains "sql" or keyword contains "查询" %}

### 数据库相关

1. **code_gen/sql** - SQL 查询生成
   - 变量：query_description, db_type, table_schema
   - 使用：`/prompt-fill sql query="查询描述" db_type="MySQL"`

2. **data_analysis/sql_analysis** - SQL 数据分析
   - 变量：analysis_goal, db_type, tables
   - 使用：`/prompt-fill sql_analysis analysis_goal="分析目标"`

{%- endif %}

{%- if keyword contains "邮件" or keyword contains "email" or keyword contains "business" or keyword contains "notice" %}

### 邮件相关

1. **email/business** - 商务邮件生成
   - 变量：email_type, recipient, subject, content
   - 使用：`/prompt-fill business email_type="合作" recipient="张总"`

2. **email/notice** - 通知邮件生成
   - 变量：notice_type, audience, content
   - 使用：`/prompt-fill notice notice_type="放假通知" audience="全体员工"`

{%- endif %}

{%- if keyword contains "K8s" or keyword contains "k8s" or keyword contains "kubernetes" or keyword contains "容器" %}

### 容器/部署相关

1. **devops/k8s** - Kubernetes 资源配置
   - 变量：app_name, image, port, replicas
   - 使用：`/prompt-fill k8s app_name="nginx" image="nginx:1.24"`

2. **code_gen/dockerfile** - Dockerfile 生成
   - 变量：language, framework, port
   - 使用：`/prompt-fill dockerfile language="Python" framework="Flask"`

3. **devops/nginx** - Nginx 配置生成
   - 变量：domain, backend, port
   - 使用：`/prompt-fill nginx domain="example.com" backend="http://localhost:3000"`

4. **devops/cicd** - CI/CD 流水线配置
   - 变量：platform, language, deploy_target
   - 使用：`/prompt-fill cicd platform="GitHub Actions"`

{%- endif %}

{%- if keyword contains "会议" or keyword contains "meeting" or keyword contains "纪要" %}

### 会议相关

1. **docs/meeting_notes** - 会议纪要整理
   - 变量：title, date, attendees, notes
   - 使用：`/prompt-fill meeting_notes title="周会" date="2026-03-15"`

{%- endif %}

{%- if keyword contains "项目" or keyword contains "plan" or keyword contains "project" or keyword contains "roadmap" %}

### 项目管理相关

1. **project/plan** - 项目计划制定
   - 变量：project_name, start_date, end_date

2. **project/status_report** - 项目状态报告
   - 变量：project_name, report_period

3. **project/roadmap** - 产品路线图规划
   - 变量：product_name, planning_period, vision

{%- endif %}

{%- if keyword contains "函数" or keyword contains "function" or keyword contains "代码" or keyword contains "class" %}

### 代码生成相关

1. **code_gen/function** - 函数/方法生成
   - 变量：language, function_name, description

2. **code_gen/class** - 类定义生成
   - 变量：language, class_name, description

3. **code_gen/api** - API 端点生成
   - 变量：framework, endpoints, models

{%- endif %}

{%- if keyword contains "测试" or keyword contains "test" or keyword contains "unit" %}

### 测试相关

1. **code_gen/unit_test** - 单元测试生成
   - 变量：code, language, test_framework

2. **code_gen/code_review** - 代码审查
   - 变量：code, language

{%- endif %}

{%- if keyword contains "报告" or keyword contains "report" or keyword contains "周报" or keyword contains "日报" %}

### 报告相关

1. **docs/weekly_report** - 周报/日报生成
   - 变量：report_type, name, department, completed_tasks

2. **project/status_report** - 项目状态报告
   - 变量：project_name, report_period

{%- endif %}

{%- if keyword contains "分析" or keyword contains "data" or keyword contains "eda" or keyword contains "可视化" %}

### 数据分析相关

1. **data_analysis/eda** - 探索性数据分析
   - 变量：data_source, columns, analysis_goals

2. **data_analysis/cleaning** - 数据清洗
   - 变量：data_issues, cleaning_rules

3. **data_analysis/visualization** - 数据可视化
   - 变量：chart_type, x_axis, y_axis

4. **data_analysis/ml_pipeline** - 机器学习流水线
   - 变量：task_type, features, target

5. **data_analysis/excel_formula** - Excel 公式生成
   - 变量：problem_description, data_structure

6. **data_analysis/regex** - 正则表达式生成
   - 变量：task_description, input_example

7. **data_analysis/json_yaml** - JSON/YAML 处理
   - 变量：task_type, input_data

{%- endif %}

{%- if keyword contains "文档" or keyword contains "readme" or keyword contains "api_docs" or keyword contains "doc" %}

### 文档相关

1. **docs/readme** - README 文档生成
   - 变量：project_name, description, features

2. **docs/api_docs** - API 文档生成
   - 变量：api_name, base_url, endpoints

{%- endif %}

{%- if keyword contains "脚本" or keyword contains "shell" or keyword contains "bash" %}

### 脚本相关

1. **devops/shell_script** - Shell 脚本生成
   - 变量：script_description, os

{%- endif %}

{%- if keyword contains "PPT" or keyword contains "演示" or keyword contains "大纲" %}

### 演示相关

1. **email/ppt_outline** - PPT 大纲生成
   - 变量：presentation_title, purpose, audience

{%- endif %}

{%- if keyword contains "git" or keyword contains "commit" %}

### Git 相关

1. **code_gen/commit_message** - Git Commit Message 生成
   - 变量：changes_description, issue

{%- endif %}

{%- if keyword contains "重构" or keyword contains "refactor" or keyword contains "优化" %}

### 代码优化相关

1. **code_gen/refactor** - 代码重构/优化
   - 变量：code, issues, goals

{%- endif %}

{%- if keyword contains "角色" or keyword contains "role" or keyword contains "base" %}

### 基础模板

1. **system/base** - 基础通用模板
   - 变量：role, task, context, constraints

2. **system/role** - 角色设定模板
   - 变量：role, expertise, style, tone

{%- endif %}

---

**下一步操作：**
- `/prompt-show <模板名>` - 查看模板详情
- `/prompt-fill <模板名> 变量="值"` - 填充模板
- `/prompt-list` - 浏览所有模板
