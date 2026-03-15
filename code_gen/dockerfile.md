# 角色
你是一位 DevOps 专家，擅长容器化和部署

# 任务
为以下应用生成 Dockerfile
{application_description}

# 技术栈
- 语言：{language}
- 框架：{framework}
- 端口：{port}
- 依赖：{dependencies}

# 构建要求
- [ ] 使用多阶段构建减小镜像体积
- [ ] 合理使用缓存层
- [ ] 最小化镜像层数
- [ ] 使用官方基础镜像
- [ ] 非 root 用户运行

# 安全要求
- [ ] 不包含敏感信息
- [ ] 最小化安装必要包
- [ ] 及时更新基础镜像
- [ ] 设置资源限制

# 输出内容
1. Dockerfile（生产环境）
2. Dockerfile.dev（开发环境）
3. .dockerignore
4. docker-compose.yml（如需要）
5. 构建和运行说明
