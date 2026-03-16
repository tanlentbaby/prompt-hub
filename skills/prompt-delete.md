---
name: prompt-delete
description: 删除 Prompt Hub 中的提示词模板
---

删除 Prompt Hub 中的提示词模板

## 步骤

### 1. 确认要删除的模板

**模板名称**: {{ template_name }}

支持以下格式：
- `code_gen/sql` - 指定分类和模板名
- `sql` - 仅模板名（自动查找）

### 2. 确认删除信息

显示将被删除的模板信息：
- 模板名称
- 所属分类
- 模板描述
- 关联文件路径

### 3. 执行删除

删除操作包括：
1. 从 `registry.json` 移除注册信息
2. 删除对应的 `.md` 模板文件

---

## 用法

### 删除单个模板

```bash
# 删除指定模板（需确认）
/prompt-delete code_gen/unused

# 强制删除（跳过确认）
/prompt-delete code_gen/unused --force

# 使用模板名自动查找
/prompt-delete sql
```

### 删除整个分类

```bash
# 删除分类及其所有模板（需确认）
/prompt-delete my_category --category

# 强制删除分类
/prompt-delete my_category --category --force
```

---

## 注意事项

1. **删除不可恢复** - 请谨慎操作
2. **删除前会显示信息** - 默认需要确认
3. **强制删除** - 使用 `--force` 跳过确认

---

## CLI 命令

```bash
# 删除模板（交互式确认）
python prompt_manager.py delete <template_name>

# 强制删除
python prompt_manager.py delete <template_name> -f

# 删除整个分类
python prompt_manager.py delete <category_name> --category
```

---

**示例：**

```
/prompt-delete code_gen/old_template
→ 显示模板信息
→ 确认删除
→ 完成删除
```
