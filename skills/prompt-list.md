---
name: prompt-list
alias: pl
description: 列出所有 Prompt Hub 模板或指定分类
---

列出 Prompt Hub 模板：

{%- if category %}

## 分类：{{ category }}

{%- if category == "code_gen" %}
sql, function, class, api, refactor, unit_test, code_review, commit_message, dockerfile, react_component, python_script, database_design
{%- elsif category == "data_analysis" %}
eda, cleaning, visualization, ml_pipeline, sql_analysis, excel_formula, regex, json_yaml
{%- elsif category == "docs" %}
readme, api_docs, meeting_notes, weekly_report, faq
{%- elsif category == "devops" %}
k8s, cicd, shell_script, nginx, git
{%- elsif category == "email" %}
business, notice, ppt_outline
{%- elsif category == "project" %}
plan, status_report, roadmap, prd
{%- elsif category == "marketing" %}
seo, social_media
{%- elsif category == "education" %}
study_plan
{%- elsif category == "hr" %}
interview_questions
{%- elsif category == "legal" %}
contract
{%- elsif category == "career" %}
resume, performance_review
{%- elsif category == "general" %}
qa, translation, text_processing
{%- elsif category == "security" %}
code_audit
{%- elsif category == "system" %}
base, role
{%- elsif category == "skills" %}
prompt-add, prompt-new, prompt-register, prompt-template
{%- else %}
未知分类

可用分类：code_gen, data_analysis, docs, devops, email, project, marketing, education, hr, legal, career, general, security, system, skills
{%- endif %}

使用 `/psh <模板名>` 查看模板详情

{%- else %}

## Prompt Hub - 所有模板 (52 个，15 个分类)

| 分类 | 模板 | 数量 |
|------|------|------|
| **code_gen** (代码生成) | sql, function, class, api, refactor, unit_test, code_review, commit_message, dockerfile, react_component, python_script, database_design | 12 |
| **data_analysis** (数据分析) | eda, cleaning, visualization, ml_pipeline, sql_analysis, excel_formula, regex, json_yaml | 8 |
| **docs** (文档) | readme, api_docs, meeting_notes, weekly_report, faq | 5 |
| **devops** (DevOps) | k8s, cicd, shell_script, nginx, git | 5 |
| **email** (邮件/文书) | business, notice, ppt_outline | 3 |
| **project** (项目管理) | plan, status_report, roadmap, prd | 4 |
| **marketing** (营销) | seo, social_media | 2 |
| **education** (教育) | study_plan | 1 |
| **hr** (人力资源) | interview_questions | 1 |
| **legal** (法律) | contract | 1 |
| **career** (职业发展) | resume, performance_review | 2 |
| **general** (通用) | qa, translation, text_processing | 3 |
| **security** (安全) | code_audit | 1 |
| **system** (系统) | base, role | 2 |
| **skills** (扩展工具) | prompt-add, prompt-new, prompt-register, prompt-template | 4 |

**总计：52 个模板**

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
