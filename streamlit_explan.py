# 项目介绍和使用说明
# 股票分析系统 - 项目说明文档

def get_project_introduction():
    """获取项目介绍"""
    return """
    ## 📈 股票分析系统 v2.0
    
    ### 项目简介
    这是一个基于Streamlit开发的股票分析系统，集成了多种股票数据查询和分析功能。
    系统支持API和数据库双数据源，提供实时股票数据查询、K线图绘制、龙虎榜查询、
    同花顺热榜等功能。
    
    ### 主要功能
    - **股票查询与K线图**: 支持通过股票代码或名称查询，自动生成K线图
    - **龙虎榜查询**: 查询股票是否在龙虎榜及获取详细数据
    - **同花顺热榜**: 获取实时热门股票榜单，支持数据筛选
    - **数据库管理**: 测试数据库连接和更新股票数据
    
    ### 技术特点
    - 双数据源支持（API + 数据库）
    - 智能缓存机制，提升查询性能
    - 模块化设计，易于维护和扩展
    - 响应式界面，支持多种设备
    """

def get_usage_guide():
    """获取使用指南"""
    return """
    ## 🚀 快速使用指南
    
    ### 1. 股票查询与K线图
    **步骤：**
    1. 在输入框中输入股票代码（如：000001）或股票名称（如：平安银行）
    2. 选择数据源：API查询 或 数据库查询
    3. 点击查询按钮获取数据
    4. 查询成功后点击"显示K线图"查看图表
    
    **功能特点：**
    - 支持代码和名称双向查询
    - 自动获取股票名称和代码对应关系
    - 后台自动保存K线图
    - 显示实时价格、涨跌幅等信息
    
    ### 2. 龙虎榜查询
    **使用方法：**
    1. 输入股票代码或名称
    2. 点击"查询是否在龙虎榜"检查上榜情况
    3. 点击"获取龙虎榜详细数据"查看详细信息
    
    ### 3. 同花顺热榜
    **功能：**
    - 获取实时热门股票榜单
    - 支持按价格、涨跌幅、成交量筛选
    - 可绘制热榜股票的K线图
    
    ### 4. 数据库管理
    **功能：**
    - 测试数据库连接状态
    - 更新本地股票数据库
    """

def get_technical_details():
    """获取技术细节"""
    return """
    ## 🔧 技术实现细节
    
    ### 数据源
    - **API数据源**: 使用adata库获取实时股票数据
    - **数据库数据源**: 本地SQLite数据库存储股票信息
    
    ### 缓存机制
    - 股票代码数据缓存30分钟
    - 股票数据缓存3分钟
    - 使用Streamlit的@st.cache_data装饰器
    
    ### 模块化设计
    - api_search_draw.py: API查询模块
    - db_search_draw.py: 数据库查询模块
    - find_lhs.py: 龙虎榜查询模块
    - ths_hot.py: 同花顺热榜模块
    - k_line.py: K线图绘制模块
    - db_connect.py: 数据库连接模块
    - flush_db.py: 数据库更新模块
    
    ### 错误处理
    - 模块导入失败时显示警告
    - 数据查询失败时提供错误信息
    - 网络连接问题自动重试
    """

def get_troubleshooting():
    """获取故障排除指南"""
    return """
    ## 🔍 故障排除
    
    ### 常见问题
    
    **1. 股票名称显示"未知"**
    - 原因：API数据源可能无法获取股票名称
    - 解决：尝试使用数据库查询，或检查股票代码是否正确
    
    **2. 数据库查询失败**
    - 原因：数据库连接问题或数据不存在
    - 解决：先测试数据库连接，确保数据库已更新
    
    **3. K线图无法显示**
    - 原因：数据获取失败或绘图模块问题
    - 解决：检查网络连接，重新查询数据
    
    **4. 热榜数据为空**
    - 原因：API限制或网络问题
    - 解决：稍后重试，或检查网络连接
    
    ### 性能优化建议
    - 使用缓存减少重复查询
    - 避免频繁刷新页面
    - 合理使用数据筛选功能
    """

def get_developer_info():
    """获取开发者信息"""
    return """
    ## 👨‍💻 开发者信息
    
    **项目名称**: 股票分析系统  
    **版本**: v2.0 (优化版)  
    **开发者**: Lambda-zhou  
    **技术栈**: Python, Streamlit, Pandas, Matplotlib, SQLite  
    **更新时间**: 2024年
    
    ### 更新日志
    - v2.0: 优化代码结构，修复数据库查询问题，增加错误处理
    - v1.0: 基础功能实现
    
    ### 联系方式
    如有问题或建议，请联系开发者。
    """

def get_quick_help():
    """获取快速帮助信息"""
    return """
    ## 🚀 快速使用指南
    
    **1. 股票查询**
    - 输入股票代码（如：000001）或股票名称（如：平安银行）
    - 选择数据源（API查询 或 数据库查询）
    - 点击查询按钮获取数据
    - 查询成功后点击"显示K线图"
    
    **2. 龙虎榜查询**
    - 输入股票信息后点击相应按钮查询
    
    **3. 同花顺热榜**
    - 点击"获取同花顺热榜"获取热门股票
    - 使用筛选功能过滤数据
    
    **4. 数据库管理**
    - 先测试数据库连接
    - 需要时更新数据库
    
    **💡 提示：**
    - 使用数据库查询可以获得更准确的股票名称
    - 系统会自动缓存数据，提升查询速度
    - 如遇问题，请查看"系统状态"
    """

def get_welcome_message():
    """获取欢迎信息"""
    return """
    🎉 **欢迎使用股票分析系统！**
    
    💡 **首次使用建议：**
    - 点击'❓ 快速帮助'查看使用指南
    - 点击'🔧 系统状态'检查模块加载情况
    - 点击'📋 切换侧边栏'获得更大工作空间
    """

def get_all_documentation():
    """获取所有文档内容"""
    return {
        "introduction": get_project_introduction(),
        "usage_guide": get_usage_guide(),
        "technical_details": get_technical_details(),
        "troubleshooting": get_troubleshooting(),
        "developer_info": get_developer_info(),
        "quick_help": get_quick_help(),
        "welcome_message": get_welcome_message()
    }

def show_explan():
    """显示项目介绍"""
    import streamlit as st
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📋 项目介绍")
    
    # 创建选项卡
    tab1, tab2, tab3, tab4, tab5 = st.sidebar.tabs([
        "📈 简介", "🚀 使用", "🔧 技术", "🔍 故障", "👨‍💻 开发者"
    ])
    
    with tab1:
        st.markdown(get_project_introduction())
    
    with tab2:
        st.markdown(get_usage_guide())
    
    with tab3:
        st.markdown(get_technical_details())
    
    with tab4:
        st.markdown(get_troubleshooting())
    
    with tab5:
        st.markdown(get_developer_info())

def show_quick_help():
    """显示快速帮助"""
    import streamlit as st
    
    with st.expander("❓ 快速帮助", expanded=True):
        st.markdown(get_quick_help())

def show_welcome_message():
    """显示欢迎信息"""
    import streamlit as st
    
    st.success("🎉 欢迎使用股票分析系统！")
    st.info("💡 首次使用建议：点击'❓ 快速帮助'查看使用指南，点击'🔧 系统状态'检查模块加载情况。")

def show_system_status(import_status):
    """显示系统状态"""
    import streamlit as st
    
    with st.expander("🔧 系统状态", expanded=True):
        col_status1, col_status2 = st.columns(2)
        with col_status1:
            st.subheader("✅ 已加载模块")
            for module, status in import_status.items():
                if status:
                    st.success(f"✅ {module}")
        with col_status2:
            st.subheader("❌ 未加载模块")
            failed_modules = [module for module, status in import_status.items() if not status]
            if failed_modules:
                for module in failed_modules:
                    st.error(f"❌ {module}")
            else:
                st.success("所有模块加载成功！")

def show_ui_components(import_status=None, show_help=False, show_status=False, show_welcome=False):
    """统一显示UI组件"""
    import streamlit as st
    
    # 显示欢迎信息
    if show_welcome:
        show_welcome_message()
    
    # 显示快速帮助
    if show_help:
        show_quick_help()
    
    # 显示系统状态
    if show_status and import_status is not None:
        show_system_status(import_status)

def show_fallback_ui(import_status, show_help=False, show_status=False):
    """显示备用UI组件（当streamlit_explan不可用时）"""
    import streamlit as st
    
    # 备用快速帮助
    if show_help:
        with st.expander("❓ 快速帮助", expanded=True):
            st.markdown(get_quick_help())
    
    # 备用系统状态
    if show_status:
        with st.expander("🔧 系统状态", expanded=True):
            col_status1, col_status2 = st.columns(2)
            with col_status1:
                st.subheader("✅ 已加载模块")
                for module, status in import_status.items():
                    if status:
                        st.success(f"✅ {module}")
            with col_status2:
                st.subheader("❌ 未加载模块")
                failed_modules = [module for module, status in import_status.items() if not status]
                if failed_modules:
                    for module in failed_modules:
                        st.error(f"❌ {module}")
                else:
                    st.success("所有模块加载成功！")

def show_fallback_welcome():
    """显示备用欢迎信息"""
    import streamlit as st
    
    st.success("🎉 欢迎使用股票分析系统！")
    st.info("💡 首次使用建议：点击'❓ 快速帮助'查看使用指南，点击'�� 系统状态'检查模块加载情况。") 