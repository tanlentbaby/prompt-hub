---
name: prompt-add
alias: pa
description: 添加新的提示词模板到 Prompt Hub
---

添加新的提示词模板到 Prompt Hub

## 步骤

### 1. 确定模板分类

首先选择模板所属分类：
- `code_gen` - 代码生成
- `data_analysis` - 数据分析
- `docs` - 文档
- `devops` - DevOps
- `email` - 邮件/文书
- `project` - 项目管理
- `system` - 系统

或创建新分类。

### 2. 模板信息

**模板名称**: {{ template_name }}
**所属分类**: {{ category }}
**模板描述**: {{ description }}

### 3. 模板内容

请提供模板内容，使用 `{variable}` 语法表示变量：

```markdown
# 角色
{role_description}

# 任务
{task_description}

# 要求
- {requirement_1}
- {requirement_2}

# 输出
{output_format}
```

### 4. 变量定义

| 变量名 | 必需 | 默认值 | 说明 |
|--------|------|--------|------|
| {var1} | ✅/❌ | - | 变量说明 |
| {var2} | ✅/❌ | - | 变量说明 |

---

## 输出

### 生成的模板文件

文件名：`{{ category }}/{{ template_name }}.md`

```markdown
{{ template_content }}
```

### 更新 Skills 配置

需要在以下文件中添加新模板支持：

1. **skills/prompt-show.md** - 添加模板详情
2. **skills/prompt-fill.md** - 添加填充逻辑
3. **skills/prompt-search.md** - 添加搜索关键词
4. **skills/skills.json** - 更新模板列表

---

## 快速添加命令

```bash
# 使用模板添加
/pa template_name="xxx" category="xxx" description="xxx"

# 或自然语言
帮我添加一个 xxx 模板，用于 xxx
```

---

**下一步：**
1. 提供模板名称、分类、描述
2. 提供模板内容（或使用默认结构）
3. 定义变量列表
4. 生成模板文件并更新配置
