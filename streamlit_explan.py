# 项目介绍和使用说明
# 股票分析系统 - 项目说明文档

def get_project_introduction():
    """获取项目介绍"""
    return """
    ## 📈 股票分析系统
    
    ### 项目简介
    基于Streamlit开发的股票分析系统，集成了多种股票数据查询和分析功能。
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
    ## 🚀 使用指南
    
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
    ## 🔧 技术实现
    
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
    """

def show_explan():
    """显示项目介绍"""
    import streamlit as st
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📋 项目介绍")
    
    # 创建选项卡
    tab1, tab2, tab3 = st.sidebar.tabs([
        "📈 简介", "🚀 使用", "🔧 技术"
    ])
    
    with tab1:
        st.markdown(get_project_introduction())
    
    with tab2:
        st.markdown(get_usage_guide())
    
    with tab3:
        st.markdown(get_technical_details())

def show_quick_help():
    """显示快速帮助"""
    import streamlit as st
    
    with st.expander("❓ 快速帮助", expanded=True):
        st.markdown(get_quick_help())

def show_welcome_message():
    """显示欢迎信息"""
    import streamlit as st
    
    st.success("🎉 欢迎使用股票分析系统！")
    st.info("💡 使用建议：点击'❓ 快速帮助'查看使用指南，点击'🔧 系统状态'检查模块加载情况。")

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
