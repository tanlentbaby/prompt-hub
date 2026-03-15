#!/usr/bin/env python3
"""
Prompt Hub - 提示词模板管理系统

使用示例:
    from prompt_manager import PromptTemplate

    # 加载模板
    template = PromptTemplate.load("code_gen/function")

    # 填充参数
    prompt = template.fill(
        language="Python",
        function_name="parse_data",
        description="解析 JSON 数据"
    )

    print(prompt)
"""

import json
import re
import argparse
from pathlib import Path
from typing import Optional


class PromptTemplate:
    """提示词模板类"""

    BASE_DIR = Path(__file__).parent

    def __init__(self, name: str, content: str, variables: list[str] = None):
        self.name = name
        self.content = content
        self.variables = variables or []

    @classmethod
    def load(cls, template_name: str) -> "PromptTemplate":
        """从注册表加载模板"""
        registry_path = cls.BASE_DIR / "registry.json"

        with open(registry_path, "r", encoding="utf-8") as f:
            registry = json.load(f)

        # 查找模板
        parts = template_name.split("/")
        template_info = None

        for category in registry["templates"].values():
            if template_name in category:
                template_info = category[template_name]
                break

        if not template_info:
            raise ValueError(f"模板 '{template_name}' 未找到")

        # 读取模板内容
        template_path = cls.BASE_DIR / template_info["path"]
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()

        return cls(
            name=template_name,
            content=content,
            variables=template_info.get("variables", [])
        )

    def fill(self, **kwargs) -> str:
        """填充模板变量"""
        result = self.content

        # 支持 {var} 和 {var:-default} 语法
        def replace_var(match):
            var_name = match.group(1)
            default = match.group(3) if match.group(3) else ""

            value = kwargs.get(var_name, default)
            if value is None:
                raise ValueError(f"缺少必需参数：{var_name}")
            return str(value)

        # 正则匹配 {var} 或 {var:-default}
        pattern = r"\{(\w+)(:-([^}]*))?\}"
        result = re.sub(pattern, replace_var, result)

        return result

    def list_variables(self) -> list[str]:
        """列出模板中的所有变量"""
        return self.variables

    def get_required_variables(self) -> list[str]:
        """获取必需的变量（无默认值）"""
        required = []
        for var in self.variables:
            if var not in self.content.split(f"{var}:-")[1] if f"{var}:-" in self.content else True:
                required.append(var)
        return required

    def __str__(self) -> str:
        return f"PromptTemplate({self.name})"

    def __repr__(self) -> str:
        return self.__str__()


class TemplateRegistry:
    """模板注册表管理类"""

    BASE_DIR = Path(__file__).parent

    @classmethod
    def list_all(cls) -> dict:
        """列出所有模板"""
        registry_path = cls.BASE_DIR / "registry.json"

        with open(registry_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def list_templates(cls, category: str = None) -> list[str]:
        """列出模板名称"""
        registry = cls.list_all()

        if category:
            templates = []
            for cat_name, cat_templates in registry["templates"].items():
                if cat_name == category:
                    templates.extend(cat_templates.keys())
            return templates

        all_templates = []
        for cat_name, cat_templates in registry["templates"].items():
            for tmpl_name in cat_templates.keys():
                all_templates.append(f"{cat_name}/{tmpl_name}")
        return all_templates

    @classmethod
    def search(cls, keyword: str, search_in: str = "all") -> list[dict]:
        """
        搜索模板

        Args:
            keyword: 搜索关键词
            search_in: 搜索范围 - 'all' / 'name' / 'description' / 'variable'

        Returns:
            包含模板信息的字典列表
        """
        results = []
        registry = cls.list_all()
        keyword_lower = keyword.lower()

        for cat_name, cat_templates in registry["templates"].items():
            for tmpl_name, tmpl_info in cat_templates.items():
                score = 0
                match_reasons = []

                # 在名称中搜索
                if search_in in ("all", "name"):
                    if keyword_lower in tmpl_name.lower():
                        score += 3
                        match_reasons.append("名称")

                # 在描述中搜索
                if search_in in ("all", "description"):
                    description = tmpl_info.get("description", "")
                    if keyword_lower in description.lower():
                        score += 2
                        match_reasons.append("描述")

                # 在变量中搜索
                if search_in in ("all", "variable"):
                    variables = tmpl_info.get("variables", [])
                    for var in variables:
                        if keyword_lower in var.lower():
                            score += 1
                            match_reasons.append("变量")
                            break

                if score > 0:
                    results.append({
                        "path": f"{cat_name}/{tmpl_name}",
                        "description": tmpl_info.get("description", ""),
                        "variables": tmpl_info.get("variables", []),
                        "score": score,
                        "match_reasons": match_reasons
                    })

        # 按相关度排序
        results.sort(key=lambda x: x["score"], reverse=True)
        return results

    @classmethod
    def get_template_info(cls, template_name: str) -> dict:
        """获取模板详细信息"""
        registry = cls.list_all()

        for cat_name, cat_templates in registry["templates"].items():
            if template_name in cat_templates:
                info = cat_templates[template_name].copy()
                info["category"] = cat_name
                info["full_path"] = f"{cat_name}/{template_name}"
                return info

        raise ValueError(f"模板 '{template_name}' 未找到")

    @classmethod
    def list_categories(cls) -> list[str]:
        """列出所有分类"""
        registry = cls.list_all()
        return list(registry["templates"].keys())

    @classmethod
    def get_category_info(cls, category: str) -> dict:
        """获取分类下所有模板信息"""
        registry = cls.list_all()

        if category not in registry["templates"]:
            raise ValueError(f"分类 '{category}' 不存在")

        return registry["templates"][category]


def quick_prompt(template_name: str, **kwargs) -> str:
    """快速生成 prompt 的便捷函数"""
    template = PromptTemplate.load(template_name)
    return template.fill(**kwargs)


def print_search_results(results: list[dict], verbose: bool = False):
    """打印搜索结果"""
    if not results:
        print("未找到相关模板")
        return

    print(f"\n找到 {len(results)} 个相关模板:\n")
    print("-" * 70)

    for i, r in enumerate(results, 1):
        print(f"\n{i}. {r['path']}")
        print(f"   描述：{r['description']}")
        if verbose:
            print(f"   变量：{', '.join(r['variables'])}")
        print(f"   匹配：[{', '.join(r['match_reasons'])}] (相关度：{r['score']})")

    print("\n" + "-" * 70)


def print_template_detail(template_name: str):
    """打印模板详情"""
    try:
        template = PromptTemplate.load(template_name)
        info = TemplateRegistry.get_template_info(template_name.split("/")[-1])

        print(f"\n{'='*60}")
        print(f"模板：{template.name}")
        print(f"描述：{info.get('description', '')}")
        print(f"{'='*60}")
        print(f"\n变量列表 ({len(template.variables)} 个):")

        for var in template.variables:
            print(f"  - {var}")

        print(f"\n模板预览:")
        print(f"{'-'*60}")
        # 显示前 500 字符
        preview = template.content[:500]
        if len(template.content) > 500:
            preview += "\n... (省略)"
        print(preview)
        print(f"{'-'*60}")

    except ValueError as e:
        print(f"错误：{e}")


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description="Prompt Hub - 提示词模板管理系统",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python prompt_manager.py list                    # 列出所有模板
  python prompt_manager.py list code_gen           # 列出指定分类
  python prompt_manager.py search SQL              # 搜索模板
  python prompt_manager.py search -v 单元测试       # 详细搜索结果
  python prompt_manager.py show code_gen/sql       # 查看模板详情
  python prompt_manager.py categories              # 列出所有分类
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # list 命令
    list_parser = subparsers.add_parser("list", help="列出模板")
    list_parser.add_argument("category", nargs="?", help="分类名称")

    # search 命令
    search_parser = subparsers.add_parser("search", help="搜索模板")
    search_parser.add_argument("keyword", help="搜索关键词")
    search_parser.add_argument("-v", "--verbose", action="store_true", help="显示详细信息")
    search_parser.add_argument("--in", dest="search_in", choices=["all", "name", "description", "variable"],
                               default="all", help="搜索范围")

    # show 命令
    show_parser = subparsers.add_parser("show", help="查看模板详情")
    show_parser.add_argument("template", help="模板名称 (如：code_gen/sql)")

    # categories 命令
    subparsers.add_parser("categories", help="列出所有分类")

    args = parser.parse_args()

    if args.command == "list":
        print(f"\n{'='*60}")
        if args.category:
            print(f"分类：{args.category}")
            print(f"{'='*60}")
            templates = TemplateRegistry.list_templates(args.category)
            for tmpl in templates:
                print(f"  - {tmpl}")
        else:
            print("所有模板:")
            print(f"{'='*60}")
            for cat in TemplateRegistry.list_categories():
                print(f"\n[{cat}]")
                templates = TemplateRegistry.list_templates(cat)
                for tmpl in templates:
                    info = TemplateRegistry.get_template_info(tmpl)
                    print(f"  - {tmpl}: {info.get('description', '')}")

    elif args.command == "search":
        results = TemplateRegistry.search(args.keyword, args.search_in)
        print_search_results(results, args.verbose)

    elif args.command == "show":
        print_template_detail(args.template)

    elif args.command == "categories":
        print(f"\n{'='*60}")
        print("可用分类:")
        print(f"{'='*60}")
        for cat in TemplateRegistry.list_categories():
            templates = TemplateRegistry.list_templates(cat)
            print(f"\n  {cat} ({len(templates)} 个模板)")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
