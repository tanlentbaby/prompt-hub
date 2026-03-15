---
name: prompt-register
alias: pr
description: 注册模板到 Prompt Hub 系统
---

注册模板到 Prompt Hub 系统

## 用途

当你已经有一个模板文件（.md），使用此命令将其注册到 Prompt Hub 系统中，使 Skills 可以访问。

---

## 输入

**模板文件路径**: {{ template_file }}
**模板名称**: {{ template_name }}
**所属分类**: {{ category }}
**描述**: {{ description }}

---

## 注册步骤

### 1. 读取模板文件

```bash
cat {{ template_file }}
```

### 2. 提取变量

从模板内容中提取所有 `{variable}` 模式的变量。

### 3. 更新 skills.json

在 `skills.json` 的 `templates` 部分添加：

```json
{
  "{{ category }}": [
    "...现有模板...",
    "{{ template_name }}"
  ]
}
```

### 4. 更新 prompt-show.md

在 `skills/prompt-show.md` 中添加模板详情分支：

```liquid
{%- elsif template_name == "{{ template_name }}" %}

## 模板：{{ category }}/{{ template_name }}

**描述**: {{ description }}

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| ... | ... | ... | ... |

**使用**: `/pf {{ template_name }} 变量="值"`
```

### 5. 更新 prompt-fill.md

在 `skills/prompt-fill.md` 中添加填充逻辑：

```liquid
{%- elsif template_name == "{{ template_name }}" %}

## 生成的{{ description }}

```markdown
{{ template_content_with_variables }}
```

✅ **复制以上提示词发送给 AI 助手**
```

### 6. 更新 prompt-search.md

在 `skills/prompt-search.md` 中添加搜索关键词映射。

---

## 输出

注册完成后：

1. ✅ 模板文件存在于 `{{ category }}/{{ template_name }}.md`
2. ✅ `/psh {{ template_name }}` 可以查看详情
3. ✅ `/pf {{ template_name }}` 可以填充
4. ✅ `/ps 关键词` 可以搜索到

---

## 快速注册

```bash
# 完整注册
/pr template_name="xxx" category="xxx" description="xxx" template_file="xxx.md"

# 简化（自动检测）
/pr xxx.md
```

---

**请提供模板文件路径和基本信息**
