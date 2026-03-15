# Prompt Hub 模板扩展指南

本文档说明如何向 Prompt Hub 添加新的提示词模板。

---

## 目录

1. [快速添加](#快速添加)
2. [交互式创建](#交互式创建)
3. [手动添加](#手动添加)
4. [模板语法](#模板语法)
5. [Skills 配置](#skills-配置)
6. [示例](#示例)

---

## 快速添加

使用命令行工具快速添加模板：

```bash
# 进入模板目录
cd /Users/cq/Documents/doc/prompt_templates

# 运行添加脚本
./add-template.sh -n my_template -c code_gen -d "我的模板描述"
```

参数说明：
- `-n` 模板名称（英文）
- `-c` 所属分类
- `-d` 模板描述

### 可用分类

| 分类 | 说明 | 现有模板数 |
|------|------|-----------|
| `code_gen` | 代码生成 | 9 |
| `data_analysis` | 数据分析 | 8 |
| `docs` | 文档 | 4 |
| `devops` | DevOps | 4 |
| `email` | 邮件/文书 | 3 |
| `project` | 项目管理 | 3 |
| `system` | 系统 | 2 |
| `skills` | 扩展工具 | 4 |

---

## 交互式创建

使用 Skills 命令交互式创建：

```
/pn
```

系统会引导你完成：
1. 输入模板名称
2. 选择分类
3. 填写描述
4. 选择模板结构
5. 定义变量

---

## 手动添加

### 步骤 1：创建模板文件

在对应分类目录下创建 `.md` 文件：

```bash
# 例如添加一个 terraform 模板
touch devops/terraform.md
```

### 步骤 2：编写模板内容

```markdown
# 角色
你是一位 Terraform 专家

# 任务
为以下基础设施生成 Terraform 配置：
{infrastructure_description}

# 云提供商
{cloud_provider:-AWS}

# 资源类型
{resource_type}

# 配置要求
- 使用最新版本
- 遵循最佳实践
- 添加必要标签

# 输出
- main.tf
- variables.tf
- outputs.tf
```

### 步骤 3：更新 skills/prompt-show.md

添加模板详情分支：

```liquid
{%- elsif template_name == "terraform" %}

## 模板：devops/terraform

**描述**: Terraform 基础设施配置模板

**变量**:
| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| infrastructure_description | ✅ | - | 基础设施描述 |
| cloud_provider | ❌ | AWS | 云提供商 |
| resource_type | ✅ | - | 资源类型 |

**使用**: `/pf terraform infrastructure_description="EC2 实例" resource_type="aws_instance"`
```

### 步骤 4：更新 skills/prompt-fill.md

添加填充逻辑：

```liquid
{%- elsif template_name == "terraform" %}

## 生成的 Terraform 配置提示词

```markdown
# 角色
你是一位 Terraform 专家

# 任务
为以下基础设施生成 Terraform 配置：
{{ infrastructure_description }}

# 云提供商
{{ cloud_provider | default: "AWS" }}

# 资源类型
{{ resource_type }}

# 输出
- main.tf
- variables.tf
- outputs.tf
```

✅ **复制以上提示词发送给 AI 助手**
```

### 步骤 5：更新 skills/prompt-search.md

添加搜索关键词：

```liquid
{%- if keyword contains "terraform" or keyword contains "基础设施" %}

### 基础设施相关

1. **devops/terraform** - Terraform 配置生成
   - 变量：infrastructure_description, cloud_provider, resource_type
   - 使用：`/pf terraform infrastructure_description="EC2 实例"`

{%- endif %}
```

### 步骤 6：更新 skills/skills.json

在 templates 部分添加：

```json
{
  "templates": {
    "devops": [
      "k8s",
      "cicd",
      "shell_script",
      "nginx",
      "terraform"  // 新增
    ]
  }
}
```

---

## 模板语法

### 变量语法

| 语法 | 说明 | 示例 |
|------|------|------|
| `{variable}` | 必需参数 | `{query_description}` |
| `{variable:-default}` | 可选参数（有默认值） | `{db_type:-MySQL}` |

### 结构建议

```markdown
# 角色
你是一位{role}专家

# 任务
{task_description}

# 输入
{input_params}

# 要求
- {requirement_1}
- {requirement_2}

# 输出
{output_format}
```

### 最佳实践

1. **角色明确** - 指定专业领域
2. **任务清晰** - 一句话说明要做什么
3. **变量合理** - 必需/可选区分
4. **示例完整** - 提供使用示例
5. **格式规范** - 使用 Markdown

---

## Skills 配置

### 文件结构

```
skills/
├── prompt-list.md      # 列出模板
├── prompt-search.md    # 搜索模板
├── prompt-show.md      # 查看详情
├── prompt-fill.md      # 填充模板
├── prompt-add.md       # 添加模板
├── prompt-new.md       # 创建模板
├── prompt-register.md  # 注册模板
├── prompt-template.md  # 模板生成器
└── skills.json         # 注册表
```

### 注册表格式

```json
{
  "name": "Prompt Hub Skills",
  "version": "2.0",
  "skills": [...],
  "templates": {
    "code_gen": ["sql", "function", ...],
    "devops": ["k8s", "terraform", ...]
  }
}
```

---

## 示例

### 添加一个"Python 爬虫"模板

**1. 创建文件** `code_gen/python_crawler.md`:

```markdown
# 角色
你是一位 Python 爬虫专家

# 任务
编写一个 Python 爬虫：{crawler_description}

# 目标网站
{target_url}

# 抓取内容
{target_content}

# 存储方式
{storage:-CSV}

# 要求
- 使用 requests 和 BeautifulSoup
- 处理反爬机制
- 添加日志
- 错误重试

# 输出
- 完整代码
- 依赖列表
- 使用说明
```

**2. 更新配置** - 在三个 Skills 文件中添加对应分支

**3. 测试**:
```
/psh python_crawler
/pf python_crawler crawler_description="抓取新闻" target_url="https://example.com" target_content="标题，正文"
```

---

## 快速参考

### 命令速查

| 命令 | 别名 | 说明 |
|------|------|------|
| `/prompt-list` | `/pl` | 列出模板 |
| `/prompt-search` | `/ps` | 搜索模板 |
| `/prompt-show` | `/psh` | 查看详情 |
| `/prompt-fill` | `/pf` | 填充模板 |
| `/prompt-add` | `/pa` | 添加模板 |
| `/prompt-new` | `/pn` | 创建模板 |
| `/prompt-register` | `/pr` | 注册模板 |
| `/prompt-template` | `/pt` | 模板生成器 |

### 添加流程

```
1. /pn 或 ./add-template.sh 创建文件
2. 编辑模板内容
3. 更新 prompt-show.md
4. 更新 prompt-fill.md
5. 更新 prompt-search.md
6. 更新 skills.json
7. 测试：/psh <模板名>
```

---

## 常见问题

### Q: 添加模板后 Skills 不生效？
A: 确保更新了所有配置文件（show/fill/search/json）

### Q: 如何创建新分类？
A: 创建对应目录，并在 skills.json 中添加分类条目

### Q: 变量不识别？
A: 检查变量名是否一致，使用 `{variable}` 格式

---

**需要帮助？** 使用 `/pt 描述你的需求` 让系统帮你生成模板！
