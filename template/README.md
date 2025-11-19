# {{ project_name }}

[![License: {{ license }}](https://img.shields.io/badge/License-{{ license }}-yellow.svg)](<https://opensource.org/licenses/{{> license }})

## 快速开始

- **初始化**：`just setup` (安装 Python/R 依赖, 配置 pre-commit)
- **日常开发**：
  - `just data-fetch` -> `just data-clean` -> ...
  - 或者直接 `just all` 跑通全流程
- **提交代码**：`just check` (运行测试与代码风格检查)
- **生成报告**：`just report`

## 项目结构

```
{{ project_slug }}/
├─ config/              # 全局配置 (project.yaml)
├─ data/                # 数据流水线
│  ├─ external/         # 外部数据 (Git LFS)
│  ├─ raw/              # 原始数据 (只读, gitignore)
│  ├─ interim/          # 中间数据 (parquet, gitignore)
│  └─ processed/        # 最终清洗数据 (parquet, gitignore)
├─ src/                 # 可复用代码库
│  ├─ py/               # Python 模块
│  └─ r/                # R 函数
├─ scripts/             # 数据处理脚本 (00-40)
├─ notebooks/           # 探索性分析 (Jupyter/RMarkdown)
├─ reports/             # Quarto 论文/幻灯片
├─ tests/               # 测试用例
└─ justfile             # 任务自动化入口
```

## 混合语言工作流

本项目采用 **"Heavily Python, Light R"** 模式：

1. **数据清洗与处理 (Python)**：使用 `polars`/`pandas` 进行繁重的数据清洗、特征工程，结果保存为 Parquet。
2. **统计分析与绘图 (R)**：利用 R 强大的统计生态 (`fixest`, `ggplot2`) 读取 Parquet 进行回归分析和绘图。
3. **流程编排 (Just)**：通过 `justfile` 统一管理跨语言调用。

## 数据目录约定

- `data/raw/`：原始数据，默认不提交（`.gitignore` 已忽略），保持只读。
- `data/external/`：可再获取的外部数据，默认走 Git LFS。
- `data/interim/` 与 `data/processed/`：可重复生成，已忽略提交。

## 关键约定

- 全局随机种子：`42`
- 表格：采用 Parquet；图片：PNG，默认 300 DPI
- 成果命名：编号制（示例 `T01_`、`F01_`、`D10_`），不使用时间戳
- `.env`：仅保留注释占位，如需变量请自行添加
- 凭证文件仅存放示例（`credentials.*`）

## 工具版本

- **Python {{ python_version }}**：由 `uv` 管理依赖与虚拟环境。
- **R**：由 `renv` 管理包版本。
- **Quarto**：用于撰写学术报告。
- **Just**：命令运行器。

## 常用命令

- `just setup`：初始化环境。
- `just check`：**提交前必跑**，运行 ruff, pytest, lintr。
- `just report`：渲染报告。
- `just clean`：清理临时文件。
- `just snapshot`：更新依赖锁文件 (`uv.lock`, `renv.lock`)。

## 贡献指南

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。遵守 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

## 后续自定义

- 更新 `LICENSE` 与 `README` 中的作者、单位信息。
- 在 `config/project.yaml` 扩展更多全局配置。
- 根据需要向 `scripts/`、`src/` 与 `notebooks/` 添加具体分析逻辑。
