---
name: prompt-show
alias: psh
description: 查看 Prompt Hub 模板详情
---

查看 Prompt Hub 模板详情：**{{ template_name }}**

{%- if template_name == "sql" %}

## 模板：code_gen/sql

**描述**: SQL 查询生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| query_description | ✅ | - | 查询描述 |
| db_type | ❌ | MySQL | 数据库类型 |
| table_schema | ✅ | - | 表结构 |

**使用**: `/pf sql query="查询" db_type="MySQL" table_schema="表结构"`

{%- elsif template_name == "function" %}

## 模板：code_gen/function

**描述**: 函数/方法生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| language | ✅ | - | 编程语言 |
| function_name | ✅ | - | 函数名 |
| description | ✅ | - | 功能描述 |

**使用**: `/pf function language="Python" function_name="parse" description="解析数据"`

{%- elsif template_name == "k8s" %}

## 模板：devops/k8s

**描述**: Kubernetes 资源配置模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| app_name | ✅ | - | 应用名称 |
| image | ✅ | - | 容器镜像 |
| port | ❌ | 80 | 容器端口 |
| replicas | ❌ | 3 | 副本数 |

**使用**: `/pf k8s app_name="nginx" image="nginx:1.24"`

{%- elsif template_name == "meeting_notes" %}

## 模板：docs/meeting_notes

**描述**: 会议纪要整理模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| title | ✅ | - | 会议主题 |
| date | ✅ | - | 会议时间 |
| attendees | ✅ | - | 参会人员 |
| notes | ❌ | - | 原始记录 |

**使用**: `/pf meeting_notes title="周会" date="2026-03-15" attendees="张三，李四"`

{%- elsif template_name == "plan" %}

## 模板：project/plan

**描述**: 项目计划制定模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| project_name | ✅ | - | 项目名称 |
| start_date | ✅ | - | 开始日期 |
| end_date | ✅ | - | 结束日期 |
| project_manager | ❌ | - | 负责人 |
| background | ❌ | - | 背景 |

**使用**: `/pf plan project_name="ERP" start_date="2026-04-01" end_date="2026-09-30"`

{%- elsif template_name == "business" %}

## 模板：email/business

**描述**: 商务邮件生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| email_type | ❌ | 商务信函 | 邮件类型 |
| recipient | ✅ | - | 收件人 |
| subject | ✅ | - | 主题 |
| content | ✅ | - | 正文要点 |

**使用**: `/pf business email_type="合作" recipient="张总" subject="合作邀请"`

{%- elsif template_name == "readme" %}

## 模板：docs/readme

**描述**: README 文档生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| project_name | ✅ | - | 项目名称 |
| description | ✅ | - | 项目描述 |
| features | ✅ | - | 主要功能 |

**使用**: `/pf readme project_name="XXX" description="描述" features="功能列表"`

{%- elsif template_name == "nginx" %}

## 模板：devops/nginx

**描述**: Nginx 配置生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| domain | ✅ | - | 域名 |
| backend | ✅ | - | 后端服务 |
| port | ❌ | 80 | 端口 |

**使用**: `/pf nginx domain="example.com" backend="http://localhost:3000"`

{%- elsif template_name == "unit_test" %}

## 模板：code_gen/unit_test

**描述**: 单元测试生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| code | ✅ | - | 待测试代码 |
| language | ❌ | Python | 语言 |
| test_framework | ❌ | pytest | 测试框架 |

**使用**: `/pf unit_test code="..." language="Python"`

{%- elsif template_name == "dockerfile" %}

## 模板：code_gen/dockerfile

**描述**: Dockerfile 生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| language | ✅ | - | 语言 |
| framework | ❌ | - | 框架 |
| port | ❌ | 5000 | 端口 |

**使用**: `/pf dockerfile language="Python" framework="Flask" port="5000"`

{%- elsif template_name == "weekly_report" %}

## 模板：docs/weekly_report

**描述**: 周报/日报生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| report_type | ❌ | 周报 | 报告类型 |
| name | ✅ | - | 姓名 |
| department | ✅ | - | 部门 |
| completed_tasks | ✅ | - | 完成的工作 |

**使用**: `/pf weekly_report report_type="周报" name="张三" completed_tasks="..."`

{%- elsif template_name == "regex" %}

## 模板：data_analysis/regex

**描述**: 正则表达式生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| task_description | ✅ | - | 任务描述 |
| input_example | ✅ | - | 输入示例 |
| language | ❌ | Python | 语言 |

**使用**: `/pf regex task_description="匹配邮箱" input_example="test@example.com"`

{%- elsif template_name == "cicd" %}

## 模板：devops/cicd

**描述**: CI/CD 流水线配置模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| platform | ❌ | GitHub Actions | 平台 |
| language | ❌ | Python | 语言 |
| deploy_target | ✅ | - | 部署目标 |

**使用**: `/pf cicd platform="GitHub Actions" deploy_target="AWS"`

{%- elsif template_name == "shell_script" %}

## 模板：devops/shell_script

**描述**: Shell 脚本生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| script_description | ✅ | - | 脚本描述 |
| os | ❌ | Linux | 操作系统 |

**使用**: `/pf shell_script script_description="备份脚本" os="Linux"`

{%- elsif template_name == "excel_formula" %}

## 模板：data_analysis/excel_formula

**描述**: Excel 公式生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| problem_description | ✅ | - | 问题描述 |
| data_structure | ✅ | - | 数据结构 |

**使用**: `/pf excel_formula problem_description="求和" data_structure="A1:A10"`

{%- elsif template_name == "json_yaml" %}

## 模板：data_analysis/json_yaml

**描述**: JSON/YAML 处理模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| task_type | ❌ | JSON 转 YAML | 任务类型 |
| input_data | ✅ | - | 输入数据 |

**使用**: `/pf json_yaml task_type="JSON 转 YAML" input_data="..."`

{%- elsif template_name == "eda" %}

## 模板：data_analysis/eda

**描述**: 探索性数据分析模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| data_source | ✅ | - | 数据来源 |
| columns | ✅ | - | 数据列 |
| analysis_goals | ✅ | - | 分析目标 |

**使用**: `/pf eda data_source="CSV" columns="age,income" analysis_goals="分布分析"`

{%- elsif template_name == "cleaning" %}

## 模板：data_analysis/cleaning

**描述**: 数据清洗模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| data_issues | ✅ | - | 数据问题 |
| cleaning_rules | ✅ | - | 清洗规则 |

**使用**: `/pf cleaning data_issues="缺失值" cleaning_rules="填充均值"`

{%- elsif template_name == "visualization" %}

## 模板：data_analysis/visualization

**描述**: 数据可视化模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| chart_type | ❌ | 折线图 | 图表类型 |
| x_axis | ✅ | - | X 轴 |
| y_axis | ✅ | - | Y 轴 |

**使用**: `/pf visualization chart_type="折线图" x_axis="日期" y_axis="销售额"`

{%- elsif template_name == "ml_pipeline" %}

## 模板：data_analysis/ml_pipeline

**描述**: 机器学习流水线模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| task_type | ❌ | 分类 | 任务类型 |
| features | ✅ | - | 特征 |
| target | ✅ | - | 目标变量 |

**使用**: `/pf ml_pipeline task_type="分类" features="age,income" target="label"`

{%- elsif template_name == "sql_analysis" %}

## 模板：data_analysis/sql_analysis

**描述**: SQL 数据分析模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| analysis_goal | ✅ | - | 分析目标 |
| db_type | ❌ | MySQL | 数据库类型 |
| tables | ✅ | - | 数据表 |

**使用**: `/pf sql_analysis analysis_goal="销售分析" tables="orders,users"`

{%- elsif template_name == "api_docs" %}

## 模板：docs/api_docs

**描述**: API 文档生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| api_name | ✅ | - | API 名称 |
| base_url | ✅ | - | 基础 URL |
| endpoints | ✅ | - | 端点列表 |

**使用**: `/pf api_docs api_name="User API" base_url="/api/v1" endpoints="GET /users"`

{%- elsif template_name == "ppt_outline" %}

## 模板：email/ppt_outline

**描述**: PPT 大纲生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| presentation_title | ✅ | - | 演示主题 |
| purpose | ✅ | - | 演示目的 |
| audience | ✅ | - | 受众 |

**使用**: `/pf ppt_outline presentation_title="产品介绍" purpose="销售" audience="客户"`

{%- elsif template_name == "status_report" %}

## 模板：project/status_report

**描述**: 项目状态报告模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| project_name | ✅ | - | 项目名称 |
| report_period | ✅ | - | 报告周期 |

**使用**: `/pf status_report project_name="ERP" report_period="2026-W10"`

{%- elsif template_name == "roadmap" %}

## 模板：project/roadmap

**描述**: 产品路线图模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| product_name | ✅ | - | 产品名称 |
| planning_period | ✅ | - | 规划周期 |
| vision | ✅ | - | 愿景 |

**使用**: `/pf roadmap product_name="SaaS" planning_period="2026" vision="成为领先平台"`

{%- elsif template_name == "notice" %}

## 模板：email/notice

**描述**: 通知邮件模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| notice_type | ✅ | - | 通知类型 |
| audience | ✅ | - | 受众 |
| content | ✅ | - | 内容 |

**使用**: `/pf notice notice_type="放假通知" audience="全体员工" content="春节放假..."`

{%- elsif template_name == "class" %}

## 模板：code_gen/class

**描述**: 类定义生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| language | ✅ | - | 语言 |
| class_name | ✅ | - | 类名 |
| description | ✅ | - | 功能描述 |

**使用**: `/pf class language="Python" class_name="UserService" description="用户服务"`

{%- elsif template_name == "api" %}

## 模板：code_gen/api

**描述**: API 端点生成模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| framework | ❌ | FastAPI | 框架 |
| endpoints | ✅ | - | 端点列表 |
| models | ✅ | - | 数据模型 |

**使用**: `/pf api framework="FastAPI" endpoints="GET /users" models="User"`

{%- elsif template_name == "refactor" %}

## 模板：code_gen/refactor

**描述**: 代码重构模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| code | ✅ | - | 待重构代码 |
| issues | ✅ | - | 发现的问题 |
| goals | ✅ | - | 重构目标 |

**使用**: `/pf refactor code="..." issues="重复代码" goals="提高可维护性"`

{%- elsif template_name == "code_review" %}

## 模板：code_gen/code_review

**描述**: 代码审查模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| code | ✅ | - | 审查代码 |
| language | ❌ | Python | 语言 |

**使用**: `/pf code_review code="..." language="Python"`

{%- elsif template_name == "commit_message" %}

## 模板：code_gen/commit_message

**描述**: Git Commit Message 模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| changes_description | ✅ | - | 变更描述 |
| issue | ❌ | - | 关联 Issue |

**使用**: `/pf commit_message changes_description="修复登录 bug"`

{%- elsif template_name == "base" %}

## 模板：system/base

**描述**: 基础通用模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| role | ✅ | - | 角色 |
| task | ✅ | - | 任务 |
| context | ❌ | - | 上下文 |
| constraints | ❌ | - | 约束 |

**使用**: `/pf base role="专家" task="任务描述"`

{%- elsif template_name == "role" %}

## 模板：system/role

**描述**: 角色设定模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| role | ✅ | - | 角色 |
| expertise | ✅ | - | 专长 |
| style | ❌ | - | 风格 |
| tone | ❌ | - | 语气 |

**使用**: `/pf role role="医生" expertise="内科" style="专业" tone="温和"`

{%- else %}

## 未找到模板：{{ template_name }}

**可用模板：**

| 分类 | 模板 |
|------|------|
| code_gen | sql, function, class, api, refactor, unit_test, code_review, commit_message, dockerfile |
| data_analysis | eda, cleaning, visualization, ml_pipeline, sql_analysis, excel_formula, regex, json_yaml |
| docs | readme, api_docs, meeting_notes, weekly_report |
| devops | k8s, cicd, shell_script, nginx |
| email | business, notice, ppt_outline |
| project | plan, status_report, roadmap |
| system | base, role |

**使用 `/pl` 浏览所有模板**
{%- endif %}

---

**下一步操作：**
- `/pf <模板名> 变量="值"` - 填充此模板
- `/ps 关键词` - 搜索其他模板
- `/pl` - 浏览所有模板
