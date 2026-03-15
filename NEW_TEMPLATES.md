# Prompt Hub - 新增模板说明

## 新增分类（6 个）

| 分类 | 说明 | 模板 |
|------|------|------|
| **marketing** | 营销推广 | seo, social_media |
| **education** | 教育学习 | study_plan |
| **hr** | 人力资源 | interview_questions |
| **legal** | 法律合同 | contract |
| **career** | 职业发展 | resume, performance_review |
| **general** | 通用工具 | qa, translation, text_processing |
| **security** | 安全审计 | code_audit |

---

## 新增模板详情（19 个）

### code_gen（新增 3 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `react_component` | React 组件生成 | `/pf react_component component_name="UserProfile" functional_requirements="显示用户信息"` |
| `python_script` | Python 自动化脚本 | `/pf python_script automation_description="批量处理 Excel 文件"` |
| `database_design` | 数据库表结构设计 | `/pf database_design project_name="电商系统" entities="用户，订单，商品"` |

### docs（新增 1 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `faq` | FAQ/技术文档生成 | `/pf faq product_name="API 服务" common_questions="如何认证"` |

### devops（新增 1 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `git` | Git 命令生成 | `/pf git git_task_description="合并分支" current_branch="feature" target_branch="main"` |

### project（新增 1 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `prd` | 产品需求文档 | `/pf prd product_name="用户中心" goals="统一管理用户信息"` |

### marketing（新增 2 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `seo` | SEO 优化建议 | `/pf seo website_url_or_description="电商网站" target_keywords="在线购物"` |
| `social_media` | 社交媒体文案 | `/pf social_media platform="小红书" topic="产品推广" target_audience="年轻女性"` |

### education（新增 1 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `study_plan` | 学习计划制定 | `/pf study_plan learning_goal="学习 Python" duration="3 个月" available_time="每天 2 小时"` |

### hr（新增 1 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `interview_questions` | 面试问题生成 | `/pf interview_questions job_title="Python 开发" tech_stack="Python,Django,MySQL"` |

### legal（新增 1 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `contract` | 合同起草 | `/pf contract contract_type="服务合同" party_a="甲方公司" party_b="乙方公司"` |

### career（新增 2 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `resume` | 简历优化 | `/pf resume target_position="产品经理" experience_years="5 年"` |
| `performance_review` | 绩效/述职报报 | `/pf performance_review position="开发工程师" review_period="2025 年"` |

### general（新增 3 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `qa` | 问答生成 | `/pf qa question="什么是机器学习" question_type="解释性"` |
| `translation` | 翻译 | `/pf translation source_text="Hello World" source_language="英语" target_language="中文"` |
| `text_processing` | 文本处理 | `/pf text_processing task_type="摘要" input_text="长文章..."` |

### security（新增 1 个）

| 模板 | 说明 | 使用示例 |
|------|------|----------|
| `code_audit` | 代码安全审计 | `/pf code_audit audit_scope="Web 应用安全" language_framework="Python/Django"` |

---

## 使用统计

| 指标 | 数量 |
|------|------|
| 总模板数 | 52 个 |
| 总分类 | 15 个 |
| Skills 工具 | 8 个 |

---

## 快速开始

### 搜索模板
```
/ps 简历
/ps SEO
/ps 面试
/ps 合同
```

### 使用模板
```
# 生成 React 组件
/psh react_component
/pf react_component component_name="Header" functional_requirements="导航栏"

# 优化简历
/psh resume
/pf resume target_position="前端开发" experience_years="3 年"

# 制定学习计划
/psh study_plan
/pf study_plan learning_goal="学习 React" duration="2 个月"
```

---

## 完整模板列表

### 按场景分类

**开发相关**
- sql, function, class, api, refactor, unit_test, code_review
- react_component, python_script, database_design
- commit_message, dockerfile

**运维/DevOps**
- k8s, cicd, shell_script, nginx, git

**数据分析**
- eda, cleaning, visualization, ml_pipeline
- sql_analysis, excel_formula, regex, json_yaml

**文档写作**
- readme, api_docs, meeting_notes, weekly_report, faq

**项目管理**
- plan, status_report, roadmap, prd

**营销推广**
- seo, social_media

**人力资源**
- interview_questions

**法律合同**
- contract

**职业发展**
- resume, performance_review

**通用工具**
- qa, translation, text_processing

**安全**
- code_audit

**教育学习**
- study_plan

**系统**
- base, role

**扩展工具**
- prompt-add, prompt-new, prompt-register, prompt-template

---

**需要添加更多模板？** 使用 `/pa` 或 `/pn` 命令！
