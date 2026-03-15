# Prompt Hub 扩展能力说明

## 概述

Prompt Hub 现在支持**随时添加新的提示词模板**，提供了完整的模板扩展生态系统。

---

## 新增 Skills（4 个）

| 命令 | 别名 | 用途 |
|------|------|------|
| `/prompt-add` | `/pa` | 快速添加模板到系统 |
| `/prompt-new` | `/pn` | 交互式向导创建模板 |
| `/prompt-register` | `/pr` | 注册已有模板文件 |
| `/prompt-template` | `/pt` | 根据需求自动生成模板 |

---

## 添加模板的 4 种方式

### 方式 1：快速添加（适合明确需求）

```bash
# 命令行
./add-template.sh -n my_template -c code_gen -d "模板描述"

# Skills
/pa template_name="terraform" category="devops" description="Terraform 配置生成"
```

### 方式 2：交互式创建（适合探索性）

```
/pn
```

系统会引导你完成：
1. 模板名称
2. 所属分类
3. 模板描述
4. 选择结构
5. 定义变量

### 方式 3：注册已有模板

```
/pr template_file="path/to/template.md"
```

适用于你已经有一个 `.md` 模板文件，想注册到系统中。

### 方式 4：AI 生成模板

```
/pt 我需要一个代码审查模板，可以检查代码质量和安全问题
```

系统会分析需求，自动生成完整的模板结构和变量定义。

---

## 模板文件结构

```
prompt_templates/
├── code_gen/           # 代码生成模板
│   ├── sql.md
│   ├── function.md
│   └── ...
├── data_analysis/      # 数据分析模板
├── docs/               # 文档模板
├── devops/             # DevOps 模板
├── email/              # 邮件模板
├── project/            # 项目管理模板
├── system/             # 系统模板
├── skills/             # 扩展工具模板
│   ├── prompt-add.md
│   ├── prompt-new.md
│   ├── prompt-register.md
│   ├── prompt-template.md
│   └── ...
├── add-template.sh     # 命令行添加工具
├── EXTENSION_GUIDE.md  # 扩展指南
└── skills/skills.json  # 注册表
```

---

## 自动更新机制

当你添加新模板时，系统会自动：

1. ✅ 创建模板文件（`.md`）
2. ✅ 更新 `skills.json` 注册表
3. ✅ 提供 `prompt-show.md` 更新代码
4. ✅ 提供 `prompt-fill.md` 更新代码
5. ✅ 提供 `prompt-search.md` 更新代码

---

## 使用示例

### 示例 1：添加 Terraform 模板

```bash
# 方式 1：命令行
./add-template.sh -n terraform -c devops -d "Terraform 配置生成"

# 方式 2：Skills
/pa template_name="terraform" category="devops" description="Terraform 配置生成"

# 方式 3：AI 生成
/pt 我需要一个 Terraform 模板，可以生成 AWS 资源配置
```

### 示例 2：添加 Python 爬虫模板

```bash
# 命令行
./add-template.sh -n python_crawler -c code_gen -d "Python 爬虫生成"

# Skills
/pa template_name="python_crawler" category="code_gen" description="Python 爬虫"
```

### 示例 3：创建自定义分类

```bash
# 创建新分类
mkdir prompt_templates/ml_ops

# 添加模板
./add-template.sh -n training -c ml_ops -d "ML 模型训练"
```

---

## 扩展指南

详细文档：`EXTENSION_GUIDE.md`

内容包括：
- 模板语法说明
- Skills 配置步骤
- 完整示例
- 最佳实践
- 常见问题

---

## 统计

| 类别 | 数量 |
|------|------|
| 提示词模板 | 33 个 |
| Skills 工具 | 8 个 |
| 分类 | 8 个 |
| **总计** | **41 个** |

---

## 快速参考

### 添加模板流程

```
1. 选择方式
   ├── /pa (快速添加)
   ├── /pn (交互式)
   ├── /pr (注册)
   └── /pt (AI 生成)

2. 提供信息
   ├── 模板名称
   ├── 所属分类
   └── 模板描述

3. 系统自动
   ├── 创建模板文件
   ├── 更新注册表
   └── 提供配置代码

4. 手动完成
   ├── 编辑模板内容
   ├── 更新 Skills 配置
   └── 测试：/psh <模板名>
```

### 命令速查

```bash
# 列出
/pl
/pl code_gen

# 搜索
/ps SQL
/ps 邮件

# 查看
/psh sql
/psh k8s

# 填充
/pf sql query="xxx" db_type="MySQL"
/pf k8s app_name="nginx"

# 扩展
/pa template_name="xxx" category="xxx"
/pn
/pr template_file="xxx.md"
/pt <需求描述>
```

---

## 下一步

1. **尝试添加一个模板**：`/pa template_name="test" category="system"`
2. **查看扩展指南**：阅读 `EXTENSION_GUIDE.md`
3. **自定义你的模板**：根据需求修改模板内容

---

**Prompt Hub - 你的可扩展提示词模板管理系统**
