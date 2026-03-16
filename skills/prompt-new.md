---
name: prompt-new
description: 创建新的提示词模板（交互式）
---

创建新的提示词模板 - 交互式向导

你好！我来帮你创建一个新的提示词模板。

## 第一步：基本信息

请提供以下信息：

1. **模板名称**（英文，用于命令引用）
   - 例如：`sql`, `function`, `meeting_notes`

2. **所属分类**
   - `code_gen` - 代码生成
   - `data_analysis` - 数据分析
   - `docs` - 文档
   - `devops` - DevOps
   - `email` - 邮件/文书
   - `project` - 项目管理
   - `system` - 系统
   - 或创建新分类

3. **模板描述**（一句话说明用途）
   - 例如："SQL 查询生成模板"

---

## 第二步：模板结构

选择一个模板结构：

### A. 简单结构
```markdown
# 角色
{role}

# 任务
{task}

# 输出
{output}
```

### B. 标准结构
```markdown
# 角色
{role_description}

# 任务
{task_description}

# 输入
{input_params}

# 要求
- {requirement_1}
- {requirement_2}

# 输出格式
{output_format}
```

### C. 复杂结构
```markdown
# 角色
{role_description}

# 背景
{context}

# 任务
{task_description}

# 输入参数
{input_params}

# 处理要求
- {requirement_1}
- {requirement_2}
- {requirement_3}

# 输出格式
{output_format}

# 示例
{examples}
```

---

## 第三步：变量定义

列出模板中使用的所有变量：

| 变量名 | 必需 | 默认值 | 说明 |
|--------|------|--------|------|
| var1 | ✅ | - | 说明 |
| var2 | ❌ | default | 说明 |

---

## 第四步：生成文件

我会生成以下内容：

1. **模板文件**: `{{ category }}/{{ template_name }}.md`
2. **更新 skills/** 下的配置文件
3. **更新 README.md** 模板列表

---

**请开始：告诉我模板名称、分类和描述**

例如：
```
名称：terraform
分类：devops
描述：Terraform 基础设施即代码模板
```
