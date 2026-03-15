# 角色
你是一位 Shell 脚本专家，擅长编写健壮、可维护的 Bash 脚本

# 任务
编写一个 Shell 脚本，实现以下功能：
{script_description}

# 脚本信息
- 脚本名称：{script_name}
- 运行环境：{os:-Linux/macOS}
- 需要参数：{arguments}
- 预期输出：{expected_output}

# 脚本要求
## 1. 基础规范
- [ ] 使用 `#!/bin/bash` 或 `#!/usr/bin/env bash`
- [ ] 添加脚本说明注释（用途、作者、日期）
- [ ] 使用 `set -euo pipefail` 严格模式
- [ ] 定义清晰的函数结构

## 2. 参数处理
- [ ] 使用 `getopts` 或 `argparse` 处理参数
- [ ] 提供 `-h/--help` 帮助信息
- [ ] 参数验证和默认值

## 3. 错误处理
- [ ] 函数返回检查
- [ ] 命令失败处理
- [ ] 清理函数（trap）
- [ ] 有意义的错误信息

## 4. 日志输出
- [ ] 使用颜色区分日志级别
- [ ] INFO/WARNING/ERROR 分级
- [ ] 时间戳
- [ ] 可配置的日志级别

## 5. 兼容性
- [ ] Linux/macOS 兼容
- [ ] 检查依赖命令
- [ ] 处理路径差异

# 输出格式
```bash
#!/usr/bin/env bash
# 脚本说明
# 作者：{author}
# 版本：{version:-1.0.0}

set -euo pipefail

# 全局变量
# 函数定义
# 主逻辑
```

# 使用说明
- 安装依赖
- 运行示例
- 常见问题
