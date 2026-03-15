---
name: prompt-list
alias: pl
description: 列出所有 Prompt Hub 模板或指定分类
---

列出 Prompt Hub 模板：

{%- if category %}

## 分类：{{ category }}

{%- if category == "code_gen" %}
function, class, api, refactor, sql, unit_test, code_review, commit_message, dockerfile
{%- elsif category == "data_analysis" %}
eda, cleaning, visualization, ml_pipeline, sql_analysis, excel_formula, regex, json_yaml
{%- elsif category == "docs" %}
readme, api_docs, meeting_notes, weekly_report
{%- elsif category == "devops" %}
k8s, cicd, shell_script, nginx
{%- elsif category == "email" %}
business, notice, ppt_outline
{%- elsif category == "project" %}
plan, status_report, roadmap
{%- elsif category == "system" %}
base, role
{%- elsif category == "skills" %}
prompt-add, prompt-new, prompt-register, prompt-template
{%- else %}
未知分类

可用分类：code_gen, data_analysis, docs, devops, email, project, system, skills
{%- endif %}

使用 `/psh <模板名>` 查看模板详情

{%- else %}

## 所有模板 (37 个，8 个分类)

| 分类 | 模板列表 | 数量 |
|------|----------|------|
| **code_gen** (代码生成) | function, class, api, refactor, sql, unit_test, code_review, commit_message, dockerfile | 9 |
| **data_analysis** (数据分析) | eda, cleaning, visualization, ml_pipeline, sql_analysis, excel_formula, regex, json_yaml | 8 |
| **docs** (文档) | readme, api_docs, meeting_notes, weekly_report | 4 |
| **devops** (DevOps) | k8s, cicd, shell_script, nginx | 4 |
| **email** (邮件/文书) | business, notice, ppt_outline | 3 |
| **project** (项目管理) | plan, status_report, roadmap | 3 |
| **system** (系统) | base, role | 2 |
| **skills** (扩展工具) | prompt-add, prompt-new, prompt-register, prompt-template | 4 |

**总计：37 个模板**

---

**使用方式：**
- `/pl <分类>` - 查看指定分类
- `/psh <模板名>` - 查看模板详情
- `/pf <模板名> 变量="值"` - 填充模板
- `/ps 关键词` - 搜索模板

**添加新模板：**
- `/pa` - 添加模板
- `/pn` - 创建新模板（交互式）
- `/pt` - 模板生成器

{%- endif %}
