# Demo Econ

## 快速开始
- 安装依赖：`just setup`
- 常用流程：`just all` 或按需调用 `just data:clean`、`just model:fit`、`just report`
- 渲染报告：`just report`

## 项目结构
```
demo-econ/
├─ config/
│  └─ project.yaml
├─ data/
│  ├─ external/
│  ├─ raw/
│  ├─ interim/
│  └─ processed/
├─ src/
│  ├─ py/
│  └─ r/
├─ scripts/
├─ notebooks/
│  ├─ py/
│  ├─ r/
│  └─ qmd/
└─ reports/
   ├─ _quarto.yml
   ├─ index.qmd
   ├─ supplement.qmd
   ├─ references.bib
   ├─ csl/
   ├─ figures/
   ├─ tables/
   └─ _extensions/andrewheiss/hikmah-academic-quarto/
```

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
- Python 3.11（`uv` 管理）
- R（`renv` 管理，建议使用 rig 切换版本）
- Quarto（附带 hikmah-academic-quarto 扩展）
- 自动化使用 `just`

## 常用命令
- `just setup`：创建 Python 虚拟环境、安装依赖、初始化 renv、安装 Quarto 扩展、注册 pre-commit 钩子。
- `just report`：渲染 `reports/` 下的 Quarto 项目。
- `just check`：运行 ruff、pytest、R lintr/styler 等质量检查。
- `just clean`：清理可再生产物（`data/interim/`、`data/processed/`、`reports/_site/` 等）。
- `just snapshot`：记录 Python、R 环境锁定信息。

## 后续自定义
- 更新 `LICENSE` 与 `README` 中的作者、单位信息。
- 在 `config/project.yaml` 扩展更多全局配置。
- 根据需要向 `scripts/`、`src/` 与 `notebooks/` 添加具体分析逻辑。
- 若需其他语言或工具链，保持 `just` 中命令统一调用 `uv run` / `Rscript`。
