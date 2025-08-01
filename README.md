# 股票分析系统 (Stock Analysis System)

一个基于Python的股票数据分析和可视化系统，支持多种数据源和龙虎榜查询功能。现已升级为Web应用，提供友好的Streamlit界面。

## 项目简介

本项目提供了完整的股票数据获取、分析和可视化解决方案，包括：
- 通过API和数据库查询股票信息
- K线图绘制和技术分析
- 龙虎榜数据查询
- 同花顺热榜数据获取
- 数据库管理和更新
- **新增**: Streamlit Web界面，提供友好的用户交互体验

## 功能特性

### 🌐 Web界面 (Streamlit)
- **现代化Web界面**: 基于Streamlit开发的响应式界面
- **实时数据查询**: 支持股票代码和名称双向查询
- **交互式K线图**: 实时绘制和显示K线图
- **智能缓存**: 提升查询性能，减少重复请求
- **多模块集成**: 统一界面管理所有功能模块

### 📊 股票查询与可视化
- 支持股票代码和股票名称双向查询
- 实时K线图绘制
- 多种数据源支持（API + 数据库）
- 自动保存K线图到本地

### 🏆 龙虎榜分析
- 查询个股是否在龙虎榜
- 获取详细龙虎榜数据
- 支持历史数据查询

### 🔥 热门股票追踪
- 同花顺热榜数据获取
- 热门股票实时监控
- 自动化数据更新

### 💾 数据管理
- MySQL数据库集成
- 自动化数据更新
- 数据清洗和维护

### 📅 交易日管理
- 自动获取最新交易日
- 交易日判断功能
- 支持历史交易日查询

## 项目结构

```
├── lhb_streamlit.py        # Streamlit主应用界面
├── streamlit_explan.py     # 项目介绍和使用说明
├── api_search_draw.py      # API股票查询与绘图
├── db_search_draw.py       # 数据库股票查询与绘图
├── find_lhs.py            # 龙虎榜查询功能
├── ths_hot.py             # 同花顺热榜数据
├── trade_day.py           # 交易日管理模块
├── db_connect.py          # 数据库连接配置
├── flush_db.py            # 数据库更新脚本
├── k_line.py              # K线图绘制工具
├── bash.sh                # 系统脚本
├── requirements.txt        # 项目依赖
└── README.md              # 项目说明文档
```

## 核心模块说明

### 🌐 lhb_streamlit.py
Streamlit Web应用主界面
```python
main()                      # 主应用入口
safe_import()              # 安全模块导入
handle_stock_query()       # 股票查询处理
handle_lhb_query()         # 龙虎榜查询处理
handle_ths_hot()          # 同花顺热榜处理
```

### 📖 streamlit_explan.py
项目介绍和使用说明模块
```python
get_project_introduction()  # 获取项目介绍
get_usage_guide()          # 获取使用指南
get_technical_details()     # 获取技术细节
get_troubleshooting()       # 获取故障排除指南
```

### 🔍 api_search_draw.py
通过API接口查询股票并绘制K线图
```python
api_search_code_draw(short_name)    # 通过股票名称查询并绘图
api_search_name_draw(stock_code)    # 通过股票代码查询并绘图
```

### 🗄️ db_search_draw.py
通过数据库查询股票并绘制K线图
```python
database_search_name_draw(short_name)  # 数据库名称查询
database_search_code_draw(stock_code)  # 数据库代码查询
```

### 🎯 find_lhs.py
龙虎榜数据查询与分析
```python
search_in_lh(stock_code)    # 查询股票是否在龙虎榜
find_lhb(stock_code)        # 获取龙虎榜详细数据
```

### 🌟 ths_hot.py
同花顺热榜数据处理
```python
main()                      # 主函数 - 获取同花顺热榜
code_draw(stock_code)       # 绘制指定股票K线图
```

### 📅 trade_day.py
交易日管理模块
```python
get_last_trading_day()      # 获取最新交易日
is_trading_day(check_date)  # 判断是否为交易日
```

### 🔗 db_connect.py
数据库连接管理
```python
db_connect()                # 建立数据库连接
```

### 🔄 flush_db.py
数据库维护与更新

### 📈 k_line.py
K线图绘制核心功能

## 安装要求

### 必需依赖
```bash
pip install streamlit
pip install pandas
pip install sqlalchemy
pip install pymysql
pip install matplotlib
pip install adata
pip install gradio
```

### 数据库配置
- MySQL 数据库
- 配置数据库连接信息在 `db_connect.py`

## 快速开始

### 1. 环境配置
```bash
# 克隆项目
git clone https://github.com/Lambda-zhou/lhb.git
cd lhb

# 安装依赖
pip install -r requirements.txt
```

### 2. 数据库设置
在 `db_connect.py` 中配置你的数据库连接信息：
```python
db_user = 'your_username'
db_password = 'your_password'
db_host = 'your_host'
db_port = 'your_port'
db_name = 'your_database'
```

### 3. 启动Web应用
```bash
# 启动Streamlit应用
streamlit run lhb_streamlit.py
```

应用将在浏览器中自动打开，默认地址为 `http://localhost:8501`

### 4. 使用示例

#### Web界面使用
1. 打开浏览器访问应用
2. 在股票查询框中输入股票代码或名称
3. 选择数据源（API或数据库）
4. 点击查询按钮获取数据
5. 查看K线图和详细信息

#### 命令行使用
```python
from db_search_draw import database_search_draw

# 通过股票名称查询
database_search_draw("中信海直")
```

#### 查询龙虎榜数据
```python
from find_lhs import search_in_lh, find_lhb

# 查询是否在龙虎榜
result = search_in_lh("000099")

# 获取龙虎榜详细数据
lhb_data = find_lhb("000099")
```

#### 获取热门股票
```python
from ths_hot import main

# 获取同花顺热榜
main()
```

#### 获取交易日信息
```python
from trade_day import get_last_trading_day

# 获取最新交易日
last_trading_day = get_last_trading_day()
```

## Web界面功能

### 📊 股票查询与K线图
- **智能查询**: 支持股票代码和名称双向查询
- **实时数据**: 获取最新股票价格和涨跌幅
- **K线图显示**: 自动生成并保存K线图
- **数据源选择**: 支持API和数据库双数据源

### 🏆 龙虎榜查询
- **上榜检查**: 快速查询股票是否在龙虎榜
- **详细数据**: 获取完整的龙虎榜信息
- **历史查询**: 支持历史龙虎榜数据

### 🔥 同花顺热榜
- **实时榜单**: 获取最新热门股票
- **数据筛选**: 按价格、涨跌幅、成交量筛选
- **K线图绘制**: 为热榜股票生成K线图

### 💾 数据库管理
- **连接测试**: 检查数据库连接状态
- **数据更新**: 更新本地股票数据库
- **状态监控**: 实时监控数据库状态

## 数据源

- **API数据源**: 通过adata库获取实时股票数据
- **数据库**: MySQL存储股票基础信息
- **同花顺**: 热门股票榜单数据
- **交易日数据**: 自动获取交易日信息

## 技术特点

### 🚀 性能优化
- **智能缓存**: 使用Streamlit缓存减少重复请求
- **模块化设计**: 独立模块，易于维护和扩展
- **错误处理**: 完善的异常处理机制

### 🎨 用户体验
- **响应式设计**: 适配多种设备屏幕
- **直观界面**: 简洁明了的操作界面
- **实时反馈**: 即时显示查询结果和状态

## 注意事项

1. **数据库连接**: 确保MySQL服务正常运行
2. **API限制**: 注意API调用频率限制
3. **数据更新**: 定期运行 `flush_db.py` 更新数据库
4. **网络连接**: 部分功能需要稳定的网络连接
5. **浏览器兼容**: 建议使用Chrome或Firefox浏览器

## 故障排除

### 常见问题

**1. 模块导入失败**
- 检查依赖是否正确安装
- 确认Python环境版本兼容性

**2. 数据库连接失败**
- 检查数据库服务是否运行
- 确认连接参数是否正确

**3. 股票数据获取失败**
- 检查网络连接
- 确认股票代码格式正确

**4. K线图显示异常**
- 检查matplotlib后端设置
- 确认数据格式正确

## 贡献指南

欢迎提交Issue和Pull Request来改进项目！

### 开发环境设置
```bash
# 安装开发依赖
pip install -r requirements.txt

# 运行测试
streamlit run lhb_streamlit.py
```

## 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系方式

- GitHub: [@Lambda-zhou](https://github.com/Lambda-zhou)
- 项目地址: https://github.com/Lambda-zhou/lhb

---

⭐ 如果这个项目对你有帮助，请给个Star支持一下！

## 更新日志

### v2.0 (最新版本)
- ✨ 新增Streamlit Web界面
- ✨ 新增项目介绍和使用说明模块
- ✨ 新增交易日管理功能
- ✨ 优化用户交互体验
- ✨ 完善错误处理机制
- ✨ 更新依赖包列表

### v1.0
- 🎉 初始版本发布
- 📊 基础股票查询功能
- 🏆 龙虎榜查询功能
- 🔥 同花顺热榜功能
- 💾 数据库管理功能