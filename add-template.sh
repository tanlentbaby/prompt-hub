#!/bin/bash
# Prompt Hub 模板添加工具
# 用途：快速添加新的提示词模板到 Prompt Hub 系统

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 模板目录
TEMPLATE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$TEMPLATE_DIR/skills"

# 打印函数
print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}  Prompt Hub - 模板添加工具${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# 显示可用分类
show_categories() {
    echo -e "${YELLOW}可用分类:${NC}"
    echo "  code_gen      - 代码生成"
    echo "  data_analysis - 数据分析"
    echo "  docs          - 文档"
    echo "  devops        - DevOps"
    echo "  email         - 邮件/文书"
    echo "  project       - 项目管理"
    echo "  system        - 系统"
    echo ""
}

# 创建模板文件
create_template_file() {
    local name=$1
    local category=$2
    local description=$3

    local file_path="$TEMPLATE_DIR/$category/$name.md"

    # 检查分类目录是否存在
    if [ ! -d "$TEMPLATE_DIR/$category" ]; then
        mkdir -p "$TEMPLATE_DIR/$category"
        print_success "创建分类目录：$category"
    fi

    # 创建模板文件
    cat > "$file_path" << EOF
# 角色
你是一位${description}专家

# 任务
{task_description}

# 输入参数
{input_params}

# 处理要求
- {requirement_1}
- {requirement_2}

# 输出格式
{output_format}

# 示例
{examples}
EOF

    print_success "创建模板文件：$file_path"
    echo "$file_path"
}

# 更新 skills.json
update_skills_json() {
    local name=$1
    local category=$2

    if [ -f "$SKILLS_DIR/skills.json" ]; then
        # 使用 sed 添加模板到对应分类
        if grep -q "\"$category\"" "$SKILLS_DIR/skills.json"; then
            # 分类已存在，添加模板名
            sed -i.bak "/\"$category\"/a\\    \"$name\"," "$SKILLS_DIR/skills.json" 2>/dev/null || \
            sed -i '' "/\"$category\"/a\\    \"$name\"," "$SKILLS_DIR/skills.json" 2>/dev/null || true
            print_success "更新 skills.json：添加 $name 到 $category"
        else
            # 分类不存在，添加新分类
            print_warning "分类 $category 不存在，需要手动添加"
        fi
    fi
}

# 更新 prompt-list.md
update_prompt_list() {
    local name=$1
    local category=$2
    local description=$3

    print_warning "请手动更新 skills/prompt-list.md 添加 $name"
}

# 显示使用说明
show_usage() {
    echo "用法：$0 [选项]"
    echo ""
    echo "选项:"
    echo "  -n, --name <name>       模板名称（必填）"
    echo "  -c, --category <cat>    所属分类（必填）"
    echo "  -d, --description <desc> 模板描述（必填）"
    echo "  -h, --help              显示帮助"
    echo ""
    echo "示例:"
    echo "  $0 -n my_template -c code_gen -d \"我的模板\""
    echo "  $0 --name sql_plus --category devops --description \"SQL 增强\""
    echo ""
}

# 主函数
main() {
    local name=""
    local category=""
    local description=""

    # 解析参数
    while [[ $# -gt 0 ]]; do
        case $1 in
            -n|--name)
                name="$2"
                shift 2
                ;;
            -c|--category)
                category="$2"
                shift 2
                ;;
            -d|--description)
                description="$3"
                shift 2
                ;;
            -h|--help)
                show_usage
                exit 0
                ;;
            *)
                print_error "未知选项：$1"
                show_usage
                exit 1
                ;;
        esac
    done

    # 验证必填参数
    if [ -z "$name" ] || [ -z "$category" ] || [ -z "$description" ]; then
        print_error "缺少必填参数"
        show_categories
        show_usage
        exit 1
    fi

    # 开始创建
    print_header
    echo "正在添加模板..."
    echo "  名称：$name"
    echo "  分类：$category"
    echo "  描述：$description"
    echo ""

    # 创建模板文件
    local file_path
    file_path=$(create_template_file "$name" "$category" "$description")

    # 更新 skills.json
    update_skills_json "$name" "$category"

    echo ""
    print_success "模板添加完成！"
    echo ""
    echo "下一步:"
    echo "  1. 编辑模板文件：$file_path"
    echo "  2. 更新 skills/prompt-show.md 添加详情"
    echo "  3. 更新 skills/prompt-fill.md 添加填充逻辑"
    echo "  4. 测试：/psh $name"
    echo ""
}

# 执行
main "$@"
