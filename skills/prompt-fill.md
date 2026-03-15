---
name: prompt-fill
alias: pf
description: 填充 Prompt Hub 模板生成提示词
---

填充 Prompt Hub 模板：**{{ template_name }}**

{%- if template_name == "sql" %}

## 生成的 SQL 提示词

```markdown
# 角色
你是一位资深 SQL 专家

# 任务
请帮我编写一个 SQL 查询

# 数据库类型
{{ db_type | default: "MySQL" }}

# 查询需求
{{ query_description }}

# 表结构
{{ table_schema }}

# 输出要求
- 只输出 SQL 语句
- 添加必要的注释
- 考虑性能优化
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "k8s" %}

## 生成的 K8s 部署配置

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ app_name }}-deployment
  labels:
    app: {{ app_name }}
spec:
  replicas: {{ replicas | default: "3" }}
  selector:
    matchLabels:
      app: {{ app_name }}
  template:
    metadata:
      labels:
        app: {{ app_name }}
    spec:
      containers:
      - name: {{ app_name }}
        image: {{ image | default: "nginx:latest" }}
        ports:
        - containerPort: {{ port | default: "80" }}
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
---
apiVersion: v1
kind: Service
metadata:
  name: {{ app_name }}-service
spec:
  selector:
    app: {{ app_name }}
  ports:
  - protocol: TCP
    port: {{ port | default: "80" }}
    targetPort: {{ port | default: "80" }}
  type: ClusterIP
```

✅ **保存为 .yaml 文件后运行：`kubectl apply -f xxx.yaml`**

{%- elsif template_name == "meeting_notes" %}

## 生成的会议纪要提示词

```markdown
# 角色
你是一位专业的会议记录员

# 会议信息
- 会议主题：{{ title }}
- 时间：{{ date }}
- 参会人员：{{ attendees }}

# 原始记录
{{ notes | default: "[请在此处粘贴原始会议记录]" }}

# 整理要求
1. **会议概要**
   - 会议目标
   - 主要结论
   - 关键决策

2. **议题讨论**
   - 每个议题的讨论要点
   - 不同观点
   - 最终结论

3. **行动项（Action Items）**
   | 任务 | 负责人 | 截止日期 | 状态 |
   |------|--------|----------|------|

4. **待决议题**
   - 需要进一步讨论的问题
```

✅ **复制以上提示词，并粘贴原始会议记录后发送给 AI 助手**

{%- elsif template_name == "function" %}

## 生成的函数编写提示词

```markdown
# 角色
你是一位资深 {{ language | default: "Python" }} 开发者

# 任务
编写一个函数：**{{ function_name }}**

# 功能描述
{{ description }}

# 要求
- 遵循 {{ language | default: "Python" }} 最佳实践
- 添加类型提示（Type Hints）
- 添加文档字符串（Docstring）
- 包含适当的错误处理
- 编写单元测试示例
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "business" %}

## 生成的商务邮件提示词

```markdown
# 角色
你是一位专业的商务文书助理

# 邮件信息
- 类型：{{ email_type | default: "商务信函" }}
- 收件人：{{ recipient }}
- 主题：{{ subject }}

# 正文要点
{{ content }}

# 要求
- 语气专业、礼貌
- 结构清晰
- 包含适当的开头和结尾
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "readme" %}

## 生成的 README 提示词

```markdown
# 角色
你是一位专业的技术文档工程师

# 项目信息
- 项目名称：{{ project_name }}
- 项目描述：{{ description }}
- 主要功能：{{ features }}

# 要求
1. 项目简介
2. 安装说明
3. 使用示例
4. API 文档（如有）
5. 贡献指南
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "nginx" %}

## 生成的 Nginx 配置

```nginx
server {
    listen 80;
    server_name {{ domain }};

    location / {
        proxy_pass {{ backend }};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

✅ **保存到 `/etc/nginx/conf.d/{{ domain }}.conf`**

{%- elsif template_name == "plan" %}

## 生成的项目计划提示词

```markdown
# 角色
你是一位项目管理专家

# 项目信息
- 项目名称：{{ project_name }}
- 负责人：{{ project_manager | default: "待定" }}
- 周期：{{ start_date }} 至 {{ end_date }}
- 背景：{{ background | default: "待补充" }}

# 要求
1. 项目目标和范围
2. 里程碑计划
3. 任务分解（WBS）
4. 风险管理
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "unit_test" %}

## 生成的单元测试提示词

```markdown
# 角色
你是一位测试专家

# 任务
为以下代码编写单元测试：

```{{ language | default: "python" }}
{{ code }}
```

# 测试框架
{{ test_framework | default: "pytest" }}

# 测试覆盖要求
- 正常路径测试
- 边界条件测试
- 异常/错误处理测试

# 输出
- 完整的测试文件
- 运行说明
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "dockerfile" %}

## 生成的 Dockerfile 提示词

```markdown
# 角色
你是一位 DevOps 专家

# 任务
为以下应用生成 Dockerfile

# 技术栈
- 语言：{{ language | default: "Python" }}
- 框架：{{ framework | default: "Flask" }}
- 端口：{{ port | default: "5000" }}

# 要求
- 多阶段构建
- 非 root 用户运行
- 最小化镜像体积

# 输出
- Dockerfile（生产环境）
- Dockerfile.dev（开发环境）
- 构建和运行说明
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "weekly_report" %}

## 生成的周报/日报提示词

```markdown
# 角色
你是一位职场文档助手

# 报告类型
{{ report_type | default: "周报" }}

# 基本信息
- 姓名：{{ name }}
- 部门：{{ department }}
- 日期范围：{{ date_range }}

# 工作内容
- 本周完成：{{ completed_tasks }}
- 进行中：{{ in_progress_tasks }}
- 遇到的问题：{{ issues }}
- 需要支持：{{ support_needed }}
- 下周计划：{{ next_plan }}
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "regex" %}

## 生成的正则表达式提示词

```markdown
# 角色
你是一位正则表达式专家

# 任务
编写正则表达式：{{ task_description }}

# 匹配目标
- 输入示例：`{{ input_example }}`
- 期望匹配：`{{ expected_match }}`

# 环境
- 语言：{{ language | default: "Python" }}

# 输出
- 正则表达式
- 模式说明
- 代码示例
- 测试用例
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "cicd" %}

## 生成的 CI/CD 流水线提示词

```markdown
# 角色
你是一位 DevOps 专家

# 任务
为以下项目生成 CI/CD 流水线配置

# 项目信息
- 平台：{{ platform | default: "GitHub Actions" }}
- 语言：{{ language | default: "Python" }}
- 部署目标：{{ deploy_target }}

# 要求
- 自动测试
- 自动构建
- 自动部署
- 环境变量管理
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "shell_script" %}

## 生成的 Shell 脚本提示词

```markdown
# 角色
你是一位 Shell 脚本专家

# 任务
编写一个 Shell 脚本：{{ script_description }}

# 环境
- 操作系统：{{ os | default: "Linux" }}
- Shell：{{ shell | default: "bash" }}

# 参数
{{ arguments }}

# 要求
- 错误处理
- 日志输出
- 参数验证
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "excel_formula" %}

## 生成的 Excel 公式提示词

```markdown
# 角色
你是一位 Excel 专家

# 问题描述
{{ problem_description }}

# 数据结构
{{ data_structure }}

# 输出
- Excel 公式
- 使用说明
- 示例验证
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "json_yaml" %}

## 生成的 JSON/YAML 处理提示词

```markdown
# 角色
你是一位数据格式专家

# 任务类型
{{ task_type | default: "JSON 转 YAML" }}

# 输入数据
{{ input_data }}

# 输出格式
{{ output_format | default: "YAML" }}
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "eda" %}

## 生成的探索性数据分析提示词

```markdown
# 角色
你是一位数据分析专家

# 数据来源
{{ data_source }}

# 数据列
{{ columns }}

# 分析目标
{{ analysis_goals }}

# 输出
- 数据概览
- 缺失值分析
- 分布分析
- 相关性分析
- 可视化建议
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "cleaning" %}

## 生成的数据清洗提示词

```markdown
# 角色
你是一位数据清洗专家

# 数据问题
{{ data_issues }}

# 清洗规则
{{ cleaning_rules }}

# 输出
- 清洗步骤
- 代码实现
- 质量检查
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "visualization" %}

## 生成的数据可视化提示词

```markdown
# 角色
你是一位数据可视化专家

# 图表类型
{{ chart_type | default: "折线图" }}

# X 轴
{{ x_axis }}

# Y 轴
{{ y_axis }}

# 输出
- 图表代码
- 样式配置
- 说明文字
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "ml_pipeline" %}

## 生成的机器学习流水线提示词

```markdown
# 角色
你是一位 ML 工程师

# 任务类型
{{ task_type | default: "分类" }}

# 特征
{{ features }}

# 目标变量
{{ target }}

# 模型选择
{{ models }}

# 输出
- 数据预处理
- 模型训练
- 评估指标
- 调参建议
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "sql_analysis" %}

## 生成的 SQL 数据分析提示词

```markdown
# 角色
你是一位数据分析专家

# 分析目标
{{ analysis_goal }}

# 数据库类型
{{ db_type | default: "MySQL" }}

# 数据表
{{ tables }}

# 输出
- SQL 查询
- 结果解读
- 可视化建议
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "api_docs" %}

## 生成的 API 文档提示词

```markdown
# 角色
你是一位技术文档专家

# API 信息
- API 名称：{{ api_name }}
- 基础 URL:{{ base_url }}
- 端点：{{ endpoints }}

# 输出
- 端点说明
- 请求/响应示例
- 参数说明
- 错误码
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "ppt_outline" %}

## 生成的 PPT 大纲提示词

```markdown
# 角色
你是一位演示设计专家

# 演示主题
{{ presentation_title }}

# 演示目的
{{ purpose }}

# 受众
{{ audience }}

# 输出
- 封面
- 目录
- 各章节标题
- 总结
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "status_report" %}

## 生成的项目状态报告提示词

```markdown
# 角色
你是一位项目管理专家

# 项目信息
- 项目名称：{{ project_name }}
- 报告周期：{{ report_period }}

# 内容
- 进度更新
- 里程碑状态
- 风险和阻塞
- 下一步计划
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "roadmap" %}

## 生成的产品路线图提示词

```markdown
# 角色
你是一位产品战略专家

# 产品信息
- 产品名称：{{ product_name }}
- 规划周期：{{ planning_period }}
- 愿景：{{ vision }}

# 输出
- 季度目标
- 功能规划
- 时间线
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "notice" %}

## 生成的通知邮件提示词

```markdown
# 角色
你是一位职场沟通专家

# 通知信息
- 类型：{{ notice_type }}
- 受众：{{ audience }}
- 内容：{{ content }}

# 输出
- 通知标题
- 通知正文
- 联系方式
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "class" %}

## 生成的类定义提示词

```markdown
# 角色
你是一位资深 {{ language | default: "Python" }} 开发者

# 任务
编写一个类：{{ class_name }}

# 功能描述
{{ description }}

# 方法
{{ methods }}

# 输出
- 类定义
- 方法实现
- 使用示例
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "api" %}

## 生成的 API 端点提示词

```markdown
# 角色
你是一位后端开发专家

# 框架
{{ framework | default: "FastAPI" }}

# 端点
{{ endpoints }}

# 数据模型
{{ models }}

# 输出
- 路由定义
- 请求/响应模型
- 验证逻辑
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "refactor" %}

## 生成的代码重构提示词

```markdown
# 角色
你是一位代码质量专家

# 待重构代码
```{{ language }}
{{ code }}
```

# 发现的问题
{{ issues }}

# 重构目标
{{ goals }}

# 输出
- 重构后代码
- 改进说明
- 测试建议
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "code_review" %}

## 生成的代码审查提示词

```markdown
# 角色
你是一位代码审查专家

# 审查代码
```{{ language }}
{{ code }}
```

# 审查重点
{{ focus_areas | default: "代码质量、性能、安全" }}

# 输出
- 优点
- 需要改进的地方
- 建议
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "commit_message" %}

## 生成的 Commit Message 提示词

```markdown
# 角色
你是一位 Git 专家

# 变更描述
{{ changes_description }}

# 关联 Issue
{{ issue }}

# 输出
- 符合 Conventional Commits 规范的 commit message
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "base" %}

## 生成的通用提示词

```markdown
# 角色
{{ role }}

# 任务
{{ task }}

# 上下文
{{ context }}

# 约束
{{ constraints }}

# 输出
{{ output_format }}
```

✅ **复制以上提示词发送给 AI 助手**

{%- elsif template_name == "role" %}

## 生成的角色设定提示词

```markdown
# 角色设定
- 角色：{{ role }}
- 专长：{{ expertise }}
- 风格：{{ style }}
- 语气：{{ tone }}

# 任务
{{ task }}
```

✅ **复制以上提示词发送给 AI 助手**

{%- else %}

## 未找到模板：{{ template_name }}

**使用 `/pl` 浏览所有模板**

或 **`/ps 关键词`** 搜索模板

{%- endif %}

---

**还需要：**
- `/psh <模板名>` - 查看模板详情
- `/ps 关键词` - 搜索模板
- `/pl` - 浏览所有模板
