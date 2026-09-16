# -*- coding: utf-8 -*-
"""
中国科学院烟台海岸带研究所
近岸河口物理海洋研究组（毛淼华研究团队）官网
运行：python -m streamlit run main.py
"""

import sys
import asyncio

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from textwrap import dedent
import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# 一、配置区
# ============================================================
TEAM_NAME = "近岸河口物理海洋研究组"
TEAM_EN   = "Coastal and Estuarine Physical Oceanography Group"
INSTITUTE = "中国科学院烟台海岸带研究所"
PI_NAME   = "毛淼华"

R2_BASE = "https://pub-5cd6bd4a178441daa43af6891235b33a.r2.dev"

HERO_IMG = "https://images.unsplash.com/photo-1505142468610-359e7d316be0?w=1800&q=80"
IMG_1    = "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=900&q=80"
IMG_2    = "https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=900&q=80"
IMG_3    = "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=900&q=80"
IMG_4    = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=900&q=80"
IMG_TEAM = "https://images.unsplash.com/photo-1581093588401-fbb62a02f120?w=1200&q=80"
IMG_LAB  = "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=1200&q=80"
IMG_SHIP = "https://images.unsplash.com/photo-1566024287286-457247b70310?w=1200&q=80"

# ============================================================
# 二、R2 图片地址
# ============================================================
BG_URL    = f"{R2_BASE}/background.png"
MAO_IMG   = f"{R2_BASE}/mao.jpg"
MAP_IMG   = f"{R2_BASE}/map.jpg"
PAGE_ICON = f"{R2_BASE}/logo.png"

TEAM_PHOTOS = [
    f"{R2_BASE}/team/group1.jpg",
    f"{R2_BASE}/team/group2.jpg",
    f"{R2_BASE}/team/group3.jpg",
    f"{R2_BASE}/team/group4.jpg",
    f"{R2_BASE}/team/group5.jpg",
]

RESEARCH_IMAGES = [
    f"{R2_BASE}/research/direction1.jpg",
    f"{R2_BASE}/research/direction2.jpg",
    f"{R2_BASE}/research/direction3.jpg",
    f"{R2_BASE}/research/direction4.jpg",
]

BODY_BG = f"url('{BG_URL}')"

# ============================================================
# 三、毛淼华简介
# ============================================================
MAO_BIO_HTML = (
    "<p>毛淼华，男，博士，研究员，博士生导师。本科毕业于浙江大学，2018 年获美国马里兰大学博士学位，"
    "随即进入中科院烟台海岸带研究所工作。2019 年入选烟台市双百计划高层次人才，"
    "2020 年入选中国科学院引才择优人才。</p>"
    "<p>研究方向为近岸河口物理海洋，包括近岸水动力模拟与观测、波流相互作用机制、"
    "波流耦合模式的改进、三维水动力以及拉格朗日粒子追踪模式的应用。"
    "成功地在非结构波流耦合模式 FVCOM 中添加了涡度力方案，揭示了近岸波浪破碎带波生流机制。"
    "通过对波流耦合方案的改进，已构建了马里兰海湾、密歇根湖、渤海及黄河三角洲近岸海域等区域的"
    "三维波流动力模式。相关研究成果已在物理海洋顶级期刊 Journal of Physical Oceanography、"
    "Journal of Geophysical Research: Oceans 与数值模拟顶级期刊 Ocean Modelling 等发表，"
    "中国科学院网站 2022 与 2024 年科研进展中官方报道，"
    "在 AGU Meeting、ECSA 等国际会议做口头报告与海报展示 20 余次"
    "（包括大会主旨报告、分会场主席、最佳海报）。</p>"
    "<p>担任海洋学国际知名期刊 PIO、OM、WRR、ECSS 以及国内物理海洋学高质量期刊审稿人。"
    "2018 与 2023 年分别获评 SCI 期刊 ECSS 与 JMSE 杰出审稿人。"
    "主持国家自然科学基金与中国科学院等科研项目，国家自然科学基金国际（地区）合作与交流项目、"
    "科技部外国青年人才计划、中科院外国青年学者项目等中方合作者。</p>"
)

# ============================================================
# 四、承担项目
# ============================================================
PROJECTS = [
    ("中国科学院引进优秀青年人才项目", "2021-2023", "500 万", "主持"),
    ("国家自然科学基金青年项目：寒潮期间黄河三角洲近岸波流相互作用机制研究",
     "2021-2023", "24 万", "主持"),
    ("烟台市双百计划人才项目", "2019-2024", "100 万", "主持"),
    ("烟台海岸带研究所前沿部署项目：渤海溴系阻燃剂的传输过程与机制模拟",
     "2018-2021", "80 万", "主持"),
    ("国家自然科学基金国际（地区）合作与交流项目："
     "Mechanism of Bohai Sea coastal dynamics associated with typhoon induced "
     "storm surge and extreme waves in changing climate scenarios",
     "2021-2022", "40 万", "中方合作者"),
    ("科技部外国青年人才计划", "2021-2022", "30 万", "中方合作者"),
    ("中国科学院外青项目："
     "Machine learning for multi-hazard risk assessment in the Bohai coastal zone",
     "2020-2022", "30 万", "中方合作者"),
]

# ============================================================
# 五、代表性论文（按时间从新到旧排序）
# ============================================================
PUBLICATIONS = [
    ("2026", "Jiao, J., Zhang, Y., Weng, H., Mao, M.*, Guo, Q.",
     "Multi-Station Tidal Level Forecasting Based on Novel Spatio-Temporal Graph Convolution Neural Network",
     "Ocean Engineering", ""),
    ("2026", "Jiao, J., Xu, X., Zhao, X., Mao, M.*, Yin, M.**, Chen, W.",
     "Short-term significant wave height prediction based on adaptive two-layer decomposition and BiLSTM-attention model",
     "Ocean Engineering", ""),
    ("2026", "Peng, J., Mao, M.*, Du, J.",
     "Composite extreme wind-wave event: Asymmetric forcing from typhoon and cold air in a temperate semienclosed sea",
     "Journal of Geophysical Research: Oceans", "131, e2026JC024175."),
    ("2026", "Su, C., Sahoo, B., Mao, M.*, Xia, M.",
     "Explainable Deep Learning Methods for Medium- and Long-term Storm Surge Forecast",
     "Ocean Modelling", ""),
    ("2026", "Su, C., Mao, M.*",
     "Probabilistic storm surge forecasting in the Bohai Sea: A deep learning framework with adaptive uncertainty quantification",
     "Estuarine, Coastal and Shelf Science", ""),
    ("2026", "Han, M., Mao, M.*, Peng, J., Zhu, J.",
     "Wave breaking characteristics and short-term morphodynamic responses under energetic wave conditions in the Yellow River Estuary",
     "Ocean Engineering", "128062."),
    ("2025", "Gao, S., Mao, M.*, Xia, M.",
     "Wave dynamics in the Yellow River Estuary during cold wave and typhoon events",
     "Ocean Modelling", ""),
    ("2025", "Su, C., Sahoo, B., Mao, M.*, Xia, M.",
     "Machine learning techniques for predicting typhoon-induced storm surge using a hybrid wind field",
     "Journal of Geophysical Research: Machine Learning and Computation", ""),
    ("2024", "Mao, M., Xia, M.*",
     "Modeling blue crab (Callinectes sapidus) larval transport and recruitment dynamics in a shallow lagoon-inlet-coastal ocean system",
     "Journal of Geophysical Research: Oceans", ""),
    ("2024", "Peng, J., Mao, M.*, Xia, M.",
     "Wave spectra analysis on the spatiotemporal variability of sea states under distinct typhoon tracks in a semi-enclosed sea",
     "Journal of Physical Oceanography", ""),
    ("2023", "Mao, M., Xia, M.*",
     "Seasonal dynamics of water circulation and exchange flows in a shallow lagoon-inlet-coastal ocean system",
     "Ocean Modelling", ""),
    ("2023", "Nguyen, Q.T., Mao, M.*, Xia, M.",
     "Numerical Modeling of Nearshore Wave Transformation and Breaking Processes in the Yellow River Delta with FUNWAVE-TVD Wave Model",
     "Journal of Marine Science and Engineering", ""),
    ("2022", "Peng, J., Mao, M.*, Xia, M.",
     "Dynamics of wave generation and dissipation processes during cold wave events in the Bohai Sea",
     "Estuarine, Coastal and Shelf Science", ""),
    ("2021", "Sahoo, B., Mao, M.*, Xia, M.",
     "Projected changes of water currents and circulation in Lake Michigan under Representative Concentration Pathways scenarios",
     "Journal of Geophysical Research: Oceans", ""),
    ("2020", "Mao, M., Xia, M.",
     "Particle dynamics in the nearshore of Lake Michigan revealed by an observation-modeling system",
     "Journal of Geophysical Research: Oceans", ""),
    ("2020", "Mao, M., Xia, M.",
     "Monthly and episodic dynamics of summer circulation in Lake Michigan",
     "Journal of Geophysical Research: Oceans", ""),
]

# ============================================================
# 六、团队成员
# ============================================================
MEMBERS = [
    ("彭婕",         "特别研究助理", "台风—冷空气复合风浪数值模拟与机理研究",
     "jiepeng@yic.ac.cn", "pengjie.jpg"),
    ("韩梦圆",       "博士研究生",   "黄河三角洲近岸水动力-地貌演变",
     "hanmengyuan22@mails.ucas.ac.cn", "hanmengyuan.jpg"),
    ("董伟",         "硕士研究生",   "渤海海峡水动力过程",
     "dongwei241@mails.ucas.ac.cn", "dongwei.jpg"),
    ("乐昆",         "硕士研究生",   "渤海拉格朗日轨迹预测",
     "lekun25@mails.ucas.ac.cn", "lekun.jpg"),
    ("Mannan Aleem", "硕士研究生",   "Remote sensing and Machine Learning",
     "mannanaleem276jb@mails.ucas.ac.cn", "mannan.jpg"),
    ("邱赫",         "硕士研究生",   "风暴潮与淹没范围预报",
     "qiuhe26@mails.ucas.ac.cn", "qiuhe.jpg"),
]

# ============================================================
# 七、研究方向
# ============================================================
RESEARCH_DIRECTIONS = [
    (
        "🌊 近岸水动力模拟与观测",
        [
            ("多要素现场观测与数据融合",
             "利用 ADCP、CTD、波浪浮标、潮位站、高频地波雷达、无人机和卫星遥感等手段，"
             "获取波浪、潮汐、潮流、温盐、悬沙和风场等基础数据。"),
            ("波浪—潮汐—环流多尺度动力过程",
             "研究近岸波浪传播、破碎、折射、绕射，以及潮流结构、余流、水交换、锋面和上升流等过程。"),
            ("河口与三角洲水动力—地貌演变",
             "结合径流、潮汐、波浪和泥沙过程，研究岸线冲淤、航道回淤、湿地演化及三角洲地貌"
             "对水动力条件的响应。"),
            ("极端天气复合动力响应",
             "关注台风、冷空气、寒潮大风等过程，揭示波浪—增水—环流—泥沙的复合响应机制，"
             "服务风暴潮与海岸灾害预警。"),
            ("观测—数值模式融合与区域应用",
             "结合 FVCOM、ROMS、SCHISM、SWAN、Delft3D、XBeach 等模式，覆盖渤海、渤海海峡、"
             "黄河三角洲等典型区域，服务防灾减灾、港口航道、海岸工程和生态修复。"),
        ],
    ),
    (
        "🤖 海洋动力过程智能预报",
        [
            ("多源海洋数据构建与质量控制",
             "融合卫星遥感、浮标、岸基雷达、潮位站、再分析资料和数值模式输出，"
             "建立适用于深度学习的高质量时空数据集。"),
            ("时序与时空智能预报模型",
             "发展 LSTM、GRU、TCN、Transformer、GCN、GAT 等模型，"
             "预报有效波高、波周期、潮位、流速和风暴潮增水等要素。"),
            ("物理约束与混合建模",
             '探索 PINN、物理引导神经网络和"数值模式 + AI 偏差校正/代理模型"方法，'
             "提高模型可解释性和外推能力。"),
            ("风暴潮与淹没范围智能预报",
             "结合台风路径、气压、风场、地形和潮汐条件，快速预测增水、漫滩和淹没范围，"
             "服务沿海防灾预警。"),
            ("实时预报系统与可视化应用",
             "发展集合概率预报、不确定性量化和 Web/API 可视化，"
             "服务台风浪、风暴潮、港口航运、海上风电和搜救保障。"),
        ],
    ),
    (
        "🌀 波流耦合模式改进与开发",
        [
            ("非结构网格波流耦合框架",
             "耦合 FVCOM 与 SWAN 等波浪模型，构建适用于复杂岸线、河口和潮间带的高分辨率波流耦合系统。"),
            ("波浪对水流的作用机制",
             "研究辐射应力、波致混合、底摩擦增强、斯托克斯漂流和波浪破碎对近岸环流、"
             "垂向混合和物质输运的影响。"),
            ("水流对波浪的反馈作用",
             "水流通过多普勒频移、折射和波流能量交换等过程，改变波浪传播方向、波长、波陡、"
             "破碎位置与波高分布，重点分析潮汐、潮流、风暴潮和背景环流对近岸波浪的调制机制。"),
            ("耦合模式关键技术改进与验证",
             "优化耦合时间步、通量守恒、边界条件、干湿网格和潮间带模拟，"
             "并结合观测与遥感资料开展参数化验证。"),
            ("多海域与极端过程应用",
             "模拟台风、冷空气、风暴潮、巨浪和漫滩等过程，"
             "服务海岸防灾、港口航道、海洋工程、海上风电和生态修复。"),
        ],
    ),
    (
        "🧭 拉格朗日粒子追踪与物质输运",
        [
            ("拉格朗日粒子追踪模型开发与应用",
             "基于 OceanParcels、OpenDrift、LTRANS 或自研模型，"
             "利用 FVCOM、ROMS、SCHISM 等三维流场驱动粒子追踪。"),
            ("随机游走与湍流扩散参数化",
             "在平流输运基础上引入水平和垂向随机游走，参数化湍流扩散、垂向混合和次网格过程，"
             "并考虑扩散系数随水深、层结、潮汐和风浪的变化，"
             "提高污染物、沉积物和微塑料等输运模拟的可靠性。"),
            ("污染物与微塑料输运",
             "研究陆源污染物、营养盐、微塑料和溢油在河口—近岸—海湾系统中的扩散路径、"
             "停留时间和富集区。"),
            ("沉积物与生态连通性",
             "模拟悬沙输运、沉积物源汇和地貌演变，并评估鱼卵、仔稚鱼、贝类幼体等生物粒子的"
             "输运与栖息地连通性。"),
            ("集合模拟与应急应用",
             "开展概率轨迹、连通性矩阵和源汇解析，发展 GPU 并行与机器学习加速，"
             "服务溢油应急、微塑料治理、海上搜救和生态修复。"),
        ],
    ),
]

# ============================================================
# 八、新闻数据（按时间从新到旧排序）
# ============================================================
NEWS = [
    {"date": "2026-09-14",
     "title": "烟台海岸带所在黄河口波浪破碎与地貌动力响应研究取得新进展",
     "summary": "研究团队联合鲁东大学，以黄河三角洲典型河口岸段为研究靶区，"
                "构建 SWAN-FUNWAVE-TVD-XBeach 单向耦合数值模拟体系，"
                "厘清了黄河口波浪破碎类型的空间分异特征与近岸地貌动力响应的内在机理。"
                "相关成果发表于 Ocean Engineering，第一作者为博士生韩梦园，通讯作者为毛淼华研究员。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202609/t20260914_8281304.html"},
    {"date": "2026-07-14",
     "title": "烟台海岸带所实现台风风暴潮中长期智能预报与可解释性新突破",
     "summary": "研究团队联合美国马里兰大学，创新研发出融合混合深度学习架构与多维度可解释性分析的风暴潮预报新体系，"
                "成功实现渤海海域风暴潮 24—72 小时中长期高精度预报，"
                "精准厘清了风暴潮演变的核心物理驱动机制。相关成果发表于 Ocean Modelling。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202607/t20260714_8247226.html"},
    {"date": "2026-07-14",
     "title": "烟台海岸带所在温带半封闭海域台风－冷空气复合极端风浪响应机制取得新进展",
     "summary": '研究团队以 2019 年台风"利奇马"过境渤海、同步遭遇北下冷空气这一典型复合极端天气过程为案例，'
                "定量剖析了台风、冷空气两类风场对渤海波浪特征的差异化驱动作用，"
                "厘清了温带半封闭海域与开阔大洋在复合风场下波浪响应的本质差异。"
                "相关成果发表于 Journal of Geophysical Research: Oceans，第一作者为彭婕特别研究助理，通讯作者为毛淼华研究员。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202607/t20260714_8247248.html"},
    {"date": "2026-06-03",
     "title": "烟台海岸带所在海浪有效波高智能预报领域取得新突破",
     "summary": "研究团队联合中国计量大学、浙江大学等单位，创新性提出一种融合自适应双层分解与"
                "双向长短期记忆网络－注意力机制的混合智能预测模型，"
                "在 1—6 小时短期预报时效内持续保持优异预测性能，"
                "为波浪能资源开发与海上航行安全保障提供了全新方案。相关成果发表于 Ocean Engineering。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202606/t20260603_8213540.html"},
    {"date": "2026-04-09",
     "title": "烟台海岸带所在渤海风暴潮概率预报研究领域取得新突破",
     "summary": "研究团队成功开发出一套适用于渤海地区的风暴潮概率深度学习框架，"
                "构建了融合 BiLSTM、自适应带宽核密度估计与序列前向选择方法的可解释混合建模体系，"
                "为风暴潮灾害风险评估与预警发布提供了高精度的可解释性概率预报新方案。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202604/t20260409_8183240.html"},
]

# ============================================================
# 九、页面基础设置
# ============================================================
st.set_page_config(
    page_title=f"{TEAM_NAME} | {INSTITUTE}",
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# 十、全局样式
# ============================================================
CSS = f"""
<style>
html, body {{
    font-family: -apple-system, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif;
    background-image: {BODY_BG};
    background-size: cover;
    background-position: center center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-color: #EDF5FA;
    min-height: 100vh;
    font-size: 17px;
}}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section[data-testid="stMain"] {{
    background: transparent !important;
}}

#MainMenu, footer {{ visibility: hidden; }}
header[data-testid="stHeader"] {{ display: none !important; }}

.block-container {{ max-width: 1500px; padding: 1rem 2.2rem 3rem; }}

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section[data-testid="stMain"],
.stApp {{ overflow: visible !important; }}

[data-testid="stMarkdownContainer"] {{
    width: 100% !important;
    align-items: stretch !important;
}}

/* ---------- Hero ---------- */
.hero {{
    position: relative;
    width: 100%;
    box-sizing: border-box;
    background: linear-gradient(rgba(11,60,93,.72), rgba(29,120,116,.72)),
                url('{HERO_IMG}') center/cover no-repeat;
    border-radius: 20px;
    padding: 60px 48px 56px;
    color: #fff;
    text-align: left;
    overflow: hidden;
    box-shadow: 0 14px 36px rgba(11,60,93,.22);
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
}}
.hero h1 {{
    font-size: 42px;
    font-weight: 800;
    letter-spacing: 3px;
    margin: 0 0 14px;
    color: #fff;
    text-align: left !important;
    width: 100% !important;
    display: block !important;
}}
.hero .sub {{
    font-size: 18px;
    margin: 0;
    opacity: .95;
    letter-spacing: 1px;
    text-align: left !important;
    width: 100% !important;
    display: block !important;
}}
.hero .en {{
    font-size: 14.5px;
    margin: 10px 0 0;
    opacity: .72;
    font-style: italic;
    text-align: left !important;
    width: 100% !important;
    display: block !important;
}}

/* ---------- 章节标题 ---------- */
.sec-title {{
    font-size: 25px; font-weight: 800; color: #0B3C5D;
    border-left: 5px solid #1D7874; padding-left: 14px;
    margin: 32px 0 20px;
}}

/* ============================================================
   CSS Grid 卡片布局
   ============================================================ */
.grid-row {{
    display: grid;
    gap: 24px;
    align-items: stretch;
    margin-bottom: 24px;
}}
.grid-row > * {{ min-width: 0; }}

/* ---------- 文本卡片 ---------- */
.card {{
    background: #fff; border: 1px solid #E3EEF5; border-radius: 14px;
    padding: 22px 26px;
    box-shadow: 0 4px 16px rgba(11,60,93,.07);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    height: 100%;
}}
.card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(11,60,93,.13);
    border-color: #BFE0EA;
}}
.card .ct {{
    font-size: 19px; font-weight: 700; color: #0B3C5D;
    margin-bottom: 10px; flex: 0 0 auto;
}}
.card .cb {{
    font-size: 17px; color: #4A6178; line-height: 1.95;
    flex: 1 1 auto;
    text-align: justify;
    text-justify: inter-ideograph;
}}
.card .cb b {{ color: #12657F; }}
.card .cb p {{
    margin: 0 0 14px;
    text-align: justify;
    text-justify: inter-ideograph;
}}
.card .cb p:last-child {{ margin-bottom: 0; }}

/* ============================================================
   图片卡片（3:2）
   ============================================================ */
.img-card {{
    background: #fff; border-radius: 14px; overflow: hidden;
    box-shadow: 0 4px 16px rgba(11,60,93,.08);
    transition: transform .25s ease, box-shadow .25s ease;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    height: 100%;
    min-height: 0;
}}
.img-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 14px 30px rgba(11,60,93,.16);
}}
.img-card > img {{
    width: 100%;
    aspect-ratio: 3 / 2;
    height: auto;
    object-fit: cover;
    object-position: center;
    display: block;
    flex: 0 0 auto;
}}
.img-card > .img-card-body {{
    padding: 16px 22px 18px;
    flex: 0 0 auto;
    display: flex;
    flex-direction: column;
}}
.img-card-title {{
    font-size: 18.5px; font-weight: 700; color: #0B3C5D;
    margin-bottom: 6px; flex: 0 0 auto;
}}
.img-card-desc {{
    font-size: 16px; color: #4A6178; line-height: 1.85;
    flex: 0 0 auto;
}}

/* ============================================================
   ★ 成员卡片
   ============================================================ */
.member-card {{
    background: #fff;
    border: 1px solid #E3EEF5;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(11,60,93,.08);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    display: flex;
    flex-direction: row;
    align-items: stretch;
    box-sizing: border-box;
    height: 100%;
}}
.member-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 14px 30px rgba(11,60,93,.16);
    border-color: #BFE0EA;
}}

.member-photo {{
    position: relative;
    flex: 0 0 38%;
    aspect-ratio: 2 / 3;
    overflow: hidden;
    background: #EDF5FA;
}}
.member-photo img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center top;
    display: block;
}}
.member-photo-fallback {{
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 56px;
    color: #B8CAD6;
    background: linear-gradient(135deg, #EDF5FA 0%, #DDEAF2 100%);
    user-select: none;
}}

.member-info {{
    flex: 1 1 62%;
    padding: 18px 22px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 6px;
    min-width: 0;
}}
.member-name {{
    font-size: 20px;
    font-weight: 700;
    color: #0B3C5D;
    margin-bottom: 2px;
    letter-spacing: .2px;
    line-height: 1.35;
}}
.member-role {{
    font-size: 16px;
    font-weight: 600;
    color: #1D7874;
    margin-bottom: 8px;
    letter-spacing: .2px;
    line-height: 1.4;
}}
.member-email {{
    font-size: 16px;
    color: #4A6178;
    line-height: 1.6;
    overflow-wrap: anywhere;
    word-break: break-word;
}}
.member-email b {{ color: #12657F; }}
.member-field {{
    font-size: 16px;
    color: #4A6178;
    line-height: 1.6;
}}
.member-field b {{ color: #12657F; }}

/* ============================================================
   ★ 研究方向：编号列表
   ============================================================ */
.dir-list {{
    list-style: none;
    padding: 0;
    margin: 0;
    counter-reset: dir;
}}
.dir-list li {{
    counter-increment: dir;
    position: relative;
    padding: 7px 0 7px 34px;
    font-size: 15px;
    color: #4A6178;
    line-height: 1.55;
    text-align: justify;
    text-justify: inter-ideograph;
    border-bottom: 1px dashed #E3EEF5;
}}
.dir-list li:last-child {{
    border-bottom: none;
    padding-bottom: 0;
}}
.dir-list li::before {{
    content: counter(dir);
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: linear-gradient(135deg, #0B3C5D, #1D7874);
    color: #fff;
    font-size: 12px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 6px rgba(11,60,93,.25);
}}
.dir-list li b {{
    color: #0B3C5D;
    font-weight: 700;
}}

.card.dir-card {{
    padding: 18px 22px 10px;
}}
.card.dir-card .ct {{
    margin-bottom: 6px;
    font-size: 18px;
}}

/* ---------- 指标 ---------- */
.stat {{
    background: #fff; border: 1px solid #E3EEF5; border-radius: 14px;
    padding: 22px 16px; text-align: center;
    box-shadow: 0 4px 16px rgba(11,60,93,.07);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    height: 100%;
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}}
.stat:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(11,60,93,.13);
    border-color: #BFE0EA;
}}
.stat .num {{
    font-size: 40px; font-weight: 800; color: #1D7874;
    line-height: 1.15; letter-spacing: -.5px;
}}
.stat .lab {{ font-size: 15px; color: #7A8FA3; margin-top: 8px; letter-spacing: .5px; }}

.stat-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 18px;
    height: 100%;
    box-sizing: border-box;
}}

/* ---------- 项目卡片 ---------- */
.proj {{
    background: #fff;
    border: 1px solid #E3EEF5;
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 14px;
    box-shadow: 0 3px 14px rgba(11,60,93,.06);
    display: flex;
    gap: 20px;
    align-items: flex-start;
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    box-sizing: border-box;
}}
.proj:hover {{
    transform: translateX(4px);
    box-shadow: 0 10px 26px rgba(11,60,93,.14);
    border-color: #BFE0EA;
}}
.proj-num {{
    flex: 0 0 auto;
    width: 44px; height: 44px;
    border-radius: 11px;
    background: linear-gradient(135deg, #0B3C5D 0%, #1D7874 100%);
    color: #fff;
    font-weight: 800;
    font-size: 17px;
    display: flex;
    align-items: center;
    justify-content: center;
    letter-spacing: .5px;
    align-self: center;
    box-shadow: 0 4px 12px rgba(11,60,93,.25);
}}
.proj-body {{ flex: 1 1 auto; min-width: 0; }}
.proj-title {{
    font-size: 17px;
    font-weight: 700;
    color: #0B3C5D;
    line-height: 1.7;
    margin-bottom: 12px;
    overflow-wrap: break-word;
    word-break: break-word;
}}
.proj-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}}
.proj-tag {{
    display: inline-flex;
    align-items: center;
    padding: 5px 14px;
    border-radius: 999px;
    background: #EDF5FA;
    color: #12657F;
    font-size: 14.5px;
    font-weight: 600;
    letter-spacing: .3px;
    white-space: nowrap;
}}
.proj-tag.role {{
    background: linear-gradient(135deg, #E6F4F2, #D3EAE5);
    color: #1D7874;
}}

/* ============================================================
   新闻列表
   ============================================================ */
.news-list {{
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-bottom: 20px;
}}
.news-card {{
    display: block;
    background: #fff;
    border-radius: 14px;
    border: 1px solid #E3EEF5;
    border-left: 5px solid #1D7874;
    padding: 20px 24px;
    margin: 0 !important;
    text-decoration: none !important;
    box-shadow: 0 3px 14px rgba(11,60,93,.06);
    transition: transform .25s, box-shadow .25s, border-color .25s;
    box-sizing: border-box;
}}
.news-card:hover {{
    transform: translateX(4px);
    box-shadow: 0 10px 26px rgba(11,60,93,.14);
    border-left-color: #0B3C5D;
}}
.news-date {{ font-size: 14px; color: #1D7874; font-weight: 700; letter-spacing: .5px; margin-bottom: 6px; }}
.news-title {{ font-size: 18px; font-weight: 700; color: #0B3C5D; line-height: 1.55; margin-bottom: 6px; }}
.news-summary {{
    font-size: 15.5px; color: #5A7086; line-height: 1.75; margin-bottom: 8px;
    text-align: justify;
    text-justify: inter-ideograph;
}}
.news-source {{ font-size: 14px; color: #1D7874; }}

/* ---------- 论文条目 ---------- */
.pub {{
    background: #fff; border-left: 4px solid #1D7874; border-radius: 8px;
    padding: 16px 20px; margin-bottom: 12px;
    box-shadow: 0 2px 10px rgba(11,60,93,.06);
    font-size: 16.5px; color: #40566B; line-height: 1.85;
    text-align: justify;
    text-justify: inter-ideograph;
}}
.pub b {{ color: #0B3C5D; }}
.pub .yr {{ color: #1D7874; font-weight: 700; }}

/* ---------- 顶部导航 ---------- */
.st-key-nav_bar {{
    position: sticky;
    top: 12px;
    z-index: 9999;
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    padding: 8px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(11,60,93,.14);
    border: 1px solid rgba(227,238,245,.95);
    margin-bottom: 26px;
}}
.st-key-nav_bar [data-testid="stHorizontalBlock"] {{ gap: 6px !important; }}
.st-key-nav_bar button {{
    width: 100% !important;
    min-height: 46px;
    padding: 10px 14px !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    letter-spacing: .6px;
    background: transparent !important;
    color: #4A6178 !important;
    border: 1px solid transparent !important;
    box-shadow: none !important;
    transition: all .22s ease;
}}
.st-key-nav_bar button:hover {{
    background: #EDF5FA !important;
    color: #0B3C5D !important;
    border-color: #D5E8F1 !important;
}}
.st-key-nav_bar button[kind="primary"],
.st-key-nav_bar button[data-testid="stBaseButton-primary"] {{
    background: linear-gradient(135deg, #0B3C5D 0%, #1D7874 100%) !important;
    color: #ffffff !important;
    border-color: transparent !important;
    box-shadow: 0 8px 18px rgba(11,60,93,.28) !important;
}}
.st-key-nav_bar button p {{
    font-size: 16px !important;
    font-weight: 600 !important;
    margin: 0 !important;
    color: inherit !important;
    white-space: nowrap;
}}

/* ============================================================
   ★ 移动端适配
   ============================================================ */
@media (max-width: 900px) {{
    .block-container {{
        padding: 0.8rem 1rem 2rem !important;
        max-width: 100% !important;
    }}
    .hero {{
        padding: 32px 22px 30px !important;
        border-radius: 16px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        text-align: left !important;
    }}
    .hero h1 {{
        font-size: 24px !important;
        letter-spacing: 1px !important;
        line-height: 1.35 !important;
        text-align: left !important;
        width: 100% !important;
    }}
    .hero .sub {{
        font-size: 14px !important;
        letter-spacing: 0 !important;
        text-align: left !important;
        width: 100% !important;
    }}
    .hero .en {{
        font-size: 12px !important;
        text-align: left !important;
        width: 100% !important;
    }}

    .sec-title {{
        font-size: 19px !important;
        margin: 22px 0 14px !important;
        padding-left: 11px !important;
        border-left-width: 4px !important;
    }}

    .grid-row {{
        grid-template-columns: 1fr !important;
        gap: 16px !important;
        margin-bottom: 16px !important;
    }}

    .grid-row.member-row {{
        grid-template-columns: 1fr !important;
        gap: 14px !important;
        margin-bottom: 16px !important;
    }}

    .card {{ padding: 18px 18px !important; }}
    .card .ct {{ font-size: 17px !important; }}
    .card .cb {{
        font-size: 15px !important;
        line-height: 1.8 !important;
        text-align: justify !important;
        text-justify: inter-ideograph !important;
    }}
    .card .cb p {{
        text-align: justify !important;
        text-justify: inter-ideograph !important;
    }}

    .img-card-title {{ font-size: 16px !important; }}
    .img-card-desc  {{ font-size: 14px !important; }}

    .grid-row.member-row .member-card {{
        flex-direction: row !important;
    }}
    .grid-row.member-row .member-photo {{
        flex: 0 0 32% !important;
        width: auto !important;
        aspect-ratio: 2 / 3 !important;
    }}
    .grid-row.member-row .member-photo-fallback {{ font-size: 40px !important; }}
    .grid-row.member-row .member-info {{
        flex: 1 1 68% !important;
        padding: 14px 16px !important;
        justify-content: center !important;
        gap: 4px !important;
    }}
    .grid-row.member-row .member-name {{ font-size: 16px !important; }}
    .grid-row.member-row .member-role {{ font-size: 13.5px !important; margin-bottom: 6px !important; }}
    .grid-row.member-row .member-email {{ font-size: 12.5px !important; }}
    .grid-row.member-row .member-field {{ font-size: 12.5px !important; line-height: 1.55 !important; }}

    .dir-list li {{
        font-size: 13.5px !important;
        padding: 6px 0 6px 30px !important;
        line-height: 1.5 !important;
        text-align: justify !important;
        text-justify: inter-ideograph !important;
    }}
    .dir-list li::before {{
        width: 22px !important;
        height: 22px !important;
        font-size: 11px !important;
    }}
    .card.dir-card {{
        padding: 14px 16px 8px !important;
    }}
    .card.dir-card .ct {{
        font-size: 16px !important;
        margin-bottom: 4px !important;
    }}

    .stat {{ padding: 16px 10px !important; }}
    .stat .num {{ font-size: 30px !important; }}
    .stat .lab {{ font-size: 13px !important; }}

    .proj {{ padding: 16px 16px !important; gap: 12px !important; }}
    .proj-num {{ width: 36px !important; height: 36px !important; font-size: 14px !important; }}
    .proj-title {{ font-size: 15px !important; }}
    .proj-tag   {{ font-size: 12.5px !important; padding: 4px 10px !important; }}

    .news-card {{ padding: 16px 18px !important; }}
    .news-title   {{ font-size: 16px !important; }}
    .news-summary {{
        font-size: 14px !important;
        text-align: justify !important;
        text-justify: inter-ideograph !important;
    }}
    .news-date, .news-source {{ font-size: 12.5px !important; }}

    .pub {{
        font-size: 14.5px !important;
        padding: 12px 14px !important;
        text-align: justify !important;
        text-justify: inter-ideograph !important;
    }}

    .st-key-nav_bar {{
        padding: 6px !important;
        border-radius: 14px !important;
        top: 6px !important;
    }}
    .st-key-nav_bar [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap !important; }}
    .st-key-nav_bar [data-testid="stHorizontalBlock"] > [data-testid="column"] {{
        flex: 0 0 33.33% !important;
        max-width: 33.33% !important;
    }}
    .st-key-nav_bar button {{
        min-height: 38px !important;
        padding: 6px 6px !important;
        font-size: 13px !important;
        letter-spacing: 0 !important;
        border-radius: 9px !important;
    }}
    .st-key-nav_bar button p {{
        font-size: 13px !important;
        letter-spacing: 0 !important;
    }}
}}

@media (max-width: 480px) {{
    .hero h1 {{ font-size: 20px !important; }}
    .hero .sub {{ font-size: 13px !important; }}
    .sec-title {{ font-size: 17px !important; }}
    .card .cb {{ font-size: 14px !important; }}
    .st-key-nav_bar button,
    .st-key-nav_bar button p {{ font-size: 12px !important; }}

    .grid-row.member-row .member-name {{ font-size: 15px !important; }}
    .grid-row.member-row .member-role {{ font-size: 12.5px !important; }}
    .grid-row.member-row .member-email {{ font-size: 11.5px !important; }}
    .grid-row.member-row .member-field {{ font-size: 11.5px !important; }}
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ============================================================
# 十一、渲染辅助
# ============================================================
def show(html: str):
    lines = [ln.strip() for ln in dedent(html).splitlines()]
    html = "".join(ln for ln in lines if ln)
    st.markdown(html, unsafe_allow_html=True)


def grid_row(cells, cols="1fr 1fr", gap="24px", extra_class=""):
    cls = f"grid-row {extra_class}".strip()
    inner = "".join(dedent(c).strip() for c in cells)
    st.markdown(
        f'<div class="{cls}" style="grid-template-columns:{cols};gap:{gap};">{inner}</div>',
        unsafe_allow_html=True,
    )


def text_card(body_html: str, title_html: str = "") -> str:
    t = f'<div class="ct">{title_html}</div>' if title_html else ""
    return f'<div class="card">{t}<div class="cb">{body_html}</div></div>'


def img_card(src: str, title: str = "", desc: str = "") -> str:
    body = ""
    if title or desc:
        body = (
            f'<div class="img-card-body">'
            f'{f"<div class=\"img-card-title\">{title}</div>" if title else ""}'
            f'{f"<div class=\"img-card-desc\">{desc}</div>" if desc else ""}'
            f'</div>'
        )
    return (
        f'<div class="img-card">'
        f'<img src="{src}">'
        f'{body}'
        f'</div>'
    )


def direction_card(img_src: str, title: str, items) -> str:
    lis = "".join(
        f'<li><b>{t}：</b>{d}</li>'
        for t, d in items
    )
    return (
        f'<div class="card dir-card">'
        f'<div class="ct">{title}</div>'
        f'<ul class="dir-list">{lis}</ul>'
        f'</div>'
    )


def member_card(name: str, role: str, field: str, email: str = "", photo_filename: str = "") -> str:
    if photo_filename:
        photo_url = f"{R2_BASE}/members/{photo_filename}"
    else:
        photo_url = ""

    return (
        f'<div class="member-card">'
        f'  <div class="member-photo">'
        f'    <img src="{photo_url}" alt="{name}" '
        f'         onerror="this.style.display=\'none\';'
        f'this.nextElementSibling.style.display=\'flex\';" '
        f'         {"" if photo_url else "style=\"display:none;\""}>'
        f'    <div class="member-photo-fallback" '
        f'         style="{"display:none;" if photo_url else ""}">👤</div>'
        f'  </div>'
        f'  <div class="member-info">'
        f'    <div class="member-name">{name}</div>'
        f'    <div class="member-role">{role}</div>'
        f'    <div class="member-email"><b>邮箱：</b>{email}</div>'
        f'    <div class="member-field"><b>研究方向：</b>{field}</div>'
        f'  </div>'
        f'</div>'
    )


def stat_grid(stats) -> str:
    cells = "".join(
        f'<div class="stat"><div class="num">{n}</div><div class="lab">{l}</div></div>'
        for n, l in stats
    )
    return f'<div class="stat-grid">{cells}</div>'


def project_list(projects) -> str:
    html = ""
    for i, (title, period, fund, role) in enumerate(projects, start=1):
        html += (
            f'<div class="proj">'
            f'<div class="proj-num">{i:02d}</div>'
            f'<div class="proj-body">'
            f'<div class="proj-title">{title}</div>'
            f'<div class="proj-meta">'
            f'<span class="proj-tag">📅 {period}</span>'
            f'<span class="proj-tag">💰 {fund}</span>'
            f'<span class="proj-tag role">👤 {role}</span>'
            f'</div></div></div>'
        )
    return html


def publication_list(pubs) -> str:
    html = ""
    for year, author, title, journal, detail in pubs:
        tail = f", {detail}" if detail else ""
        html += (
            f'<div class="pub">'
            f'<span class="yr">[{year}]</span> '
            f'<b>{author}</b> {title}. '
            f'<i>{journal}</i>{tail}'
            f'</div>'
        )
    return html


def news_list_html(news) -> str:
    cards = ""
    for n in news:
        cards += (
            f'<a class="news-card" href="{n["url"]}" target="_blank" rel="noopener">'
            f'<div class="news-date">📅 {n["date"]}</div>'
            f'<div class="news-title">{n["title"]}</div>'
            f'<div class="news-summary">{n["summary"]}</div>'
            f'<div class="news-source">来源：{n["source"]} ↗</div>'
            f'</a>'
        )
    return f'<div class="news-list">{cards}</div>'


def image_carousel(slides, interval=4500, show_caption=True, max_height=700):
    """
    通用图片轮播：容器高度完全由当前激活图片决定，图片完整显示，绝不裁剪。
    slides:       [(图片URL, 标题, 描述), ...]
    interval:     自动切换间隔（毫秒）
    show_caption: 是否显示图片上的标题和描述文字
    max_height:   图片最大高度（像素），防止竖版照片过高
    """
    slides_html = ""
    dots_html = ""
    for i, (src, title, desc) in enumerate(slides):
        active = " active" if i == 0 else ""
        caption_html = ""
        if show_caption:
            caption_html = (
                f'<div class="carousel-caption">'
                f'<div class="carousel-title">{title}</div>'
                f'<div class="carousel-desc">{desc}</div>'
                f'</div>'
            )
        slides_html += f'''
        <div class="carousel-slide{active}">
            <img src="{src}" alt="{title}">
            {caption_html}
        </div>
        '''
        dots_html += (
            f'<span class="carousel-dot{" active" if i == 0 else ""}" '
            f'onclick="goTo({i})"></span>'
        )

    overlay_css = ""
    if show_caption:
        overlay_css = """
    .carousel-slide::after {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg,
                    rgba(11,60,93,0.05) 35%,
                    rgba(11,60,93,0.55) 75%,
                    rgba(11,60,93,0.85) 100%);
        pointer-events: none;
    }
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    html, body {{ background: transparent; }}
    body {{
        font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: flex-start;
    }}
    /* 容器宽度固定，高度由内部激活图片自然撑开 —— 图片完整显示，不裁剪 */
    .carousel {{
        position: relative;
        width: 100%;
        max-width: 900px;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 28px rgba(11,60,93,.18);
        background: #0B1F2E;
    }}
    .carousel-slide {{
        display: none;                    /* 默认隐藏 */
        position: relative;
    }}
    .carousel-slide.active {{
        display: block;                   /* 激活时显示，自动撑起容器高度 */
    }}
    .carousel-slide img {{
        width: 100%;
        height: auto;                     /* ★ 关键：高度按图片原始比例自动 */
        max-height: {max_height}px;        /* 防止竖版照片过高 */
        object-fit: contain;              /* 图片缩放到容器内，完整不裁剪 */
        display: block;
        margin: 0 auto;
    }}
    {overlay_css}
    .carousel-caption {{
        position: absolute;
        left: 36px; right: 36px; bottom: 40px;
        z-index: 3; color: #fff;
    }}
    .carousel-title {{
        font-size: 26px; font-weight: 800;
        letter-spacing: 1.5px; margin-bottom: 10px;
        text-shadow: 0 2px 10px rgba(0,0,0,.55);
    }}
    .carousel-desc {{
        font-size: 16px; opacity: .95; letter-spacing: .5px;
        text-shadow: 0 1px 6px rgba(0,0,0,.55);
        line-height: 1.7; max-width: 720px;
    }}
    .carousel-dots {{
        position: absolute; bottom: 22px; right: 36px;
        z-index: 4; display: flex; gap: 8px; align-items: center;
    }}
    .carousel-dot {{
        width: 9px; height: 9px; border-radius: 50%;
        background: rgba(255,255,255,.48); cursor: pointer;
        transition: all .35s ease;
        box-shadow: 0 1px 4px rgba(0,0,0,.3);
    }}
    .carousel-dot:hover {{ background: rgba(255,255,255,.85); }}
    .carousel-dot.active {{
        background: #fff; width: 28px; border-radius: 5px;
        box-shadow: 0 2px 8px rgba(0,0,0,.4);
    }}
    .carousel-arrow {{
        position: absolute; top: 50%; transform: translateY(-50%);
        z-index: 4; width: 46px; height: 46px; border-radius: 50%;
        background: rgba(255,255,255,.18);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        color: #fff; border: 1px solid rgba(255,255,255,.28);
        cursor: pointer; font-size: 24px;
        display: flex; align-items: center; justify-content: center;
        transition: all .25s ease;
        opacity: 0; padding-bottom: 3px;
    }}
    .carousel:hover .carousel-arrow {{ opacity: 1; }}
    .carousel-arrow:hover {{
        background: rgba(255,255,255,.42);
        transform: translateY(-50%) scale(1.06);
    }}
    .carousel-arrow.prev {{ left: 20px; }}
    .carousel-arrow.next {{ right: 20px; }}

    @media (max-width: 900px) {{
        .carousel-caption {{ left: 18px; right: 18px; bottom: 36px; }}
        .carousel-title {{ font-size: 19px; margin-bottom: 6px; }}
        .carousel-desc  {{ font-size: 13px; line-height: 1.6; }}
        .carousel-dots  {{ right: 20px; bottom: 16px; }}
        .carousel-arrow {{ opacity: 1; width: 36px; height: 36px; font-size: 20px; }}
        .carousel-arrow.prev {{ left: 10px; }}
        .carousel-arrow.next {{ right: 10px; }}
    }}
    </style>
    </head>
    <body>
    <div class="carousel" id="carousel">
        {slides_html}
        <button class="carousel-arrow prev" onclick="prev()" aria-label="上一张">‹</button>
        <button class="carousel-arrow next" onclick="next()" aria-label="下一张">›</button>
        <div class="carousel-dots">{dots_html}</div>
    </div>
    <script>
    let current = 0;
    const slides = document.querySelectorAll('.carousel-slide');
    const dots = document.querySelectorAll('.carousel-dot');
    const total = slides.length;
    let timer;

    function show(idx) {{
        slides[current].classList.remove('active');
        dots[current].classList.remove('active');
        current = (idx + total) % total;
        slides[current].classList.add('active');
        dots[current].classList.add('active');
        // 切换后图片高度可能变化，通知父页面重新调整 iframe 高度
        setTimeout(setFrameHeight, 60);
    }}
    function next() {{ show(current + 1); resetTimer(); }}
    function prev() {{ show(current - 1); resetTimer(); }}
    function goTo(i) {{ show(i); resetTimer(); }}
    function resetTimer() {{
        clearInterval(timer);
        timer = setInterval(() => show(current + 1), {interval});
    }}

    const el = document.getElementById('carousel');
    el.addEventListener('mouseenter', () => clearInterval(timer));
    el.addEventListener('mouseleave', () => resetTimer());

    resetTimer();

    function setFrameHeight() {{
        const c = document.querySelector('.carousel');
        if (c) {{
            const h = Math.ceil(c.getBoundingClientRect().height) + 8;
            window.parent.postMessage({{
                isStreamlitMessage: true,
                type: 'streamlit:setFrameHeight',
                height: h
            }}, '*');
        }}
    }}
    // 图片加载完成后重新计算高度
    document.querySelectorAll('.carousel-slide img').forEach(img => {{
        if (img.complete && img.naturalWidth) {{
            setFrameHeight();
        }} else {{
            img.addEventListener('load', setFrameHeight);
        }}
    }});
    setTimeout(setFrameHeight, 50);
    setTimeout(setFrameHeight, 300);
    setTimeout(setFrameHeight, 1000);
    setTimeout(setFrameHeight, 2000);
    window.addEventListener('resize', setFrameHeight);
    </script>
    </body>
    </html>
    """
    # 初始高度需能容纳整张图片（图片最大高度为 max_height），否则图片下方会被 iframe 截断；
    # 之后再由 setFrameHeight 根据实际图片高度把 iframe 收缩到合适高度。
    components.html(html, height=max_height + 60, scrolling=False)


# ============================================================
# 十二、各页面
# ============================================================
def page_home():
    show('<div class="sec-title">研究组简介</div>')
    intro_text = """
        本研究组隶属于<b>中国科学院烟台海岸带研究所</b>，聚焦<b>近岸与河口区域的物理海洋学过程</b>，
        以黄河口、渤海及黄海近岸海域为主要研究区域，综合运用<b>现场观测与数值模拟</b>等手段，
        系统研究<b>近岸水动力模拟与观测、海洋动力过程智能预报、波流耦合模式改进与开发、拉格朗日粒子追踪与物质输运</b>，
        及其对陆源物质输运、营养盐与污染物扩散、海岸带生态环境的影响，
        为海岸带资源可持续利用与生态环境保护提供科学支撑。<br><br>
        研究组由<b>毛淼华研究员</b>领衔，目前有研究员、副研究员、博士后及研究生共8人，
        承担国家自然科学基金、中国科学院先导专项、山东省重点研发计划等多项课题。
    """
    stats = [
        ("5+", "研究方向"),
        ("10+", "承担科研项目"),
        ("20+", "发表学术论文"),
        ("8+", "团队成员"),
    ]
    grid_row(
        [text_card(intro_text), stat_grid(stats)],
        cols="1.6fr 1fr",
        gap="24px",
    )

    # ★ 团队风采：容器高度由图片决定，照片完整显示
    show('<div class="sec-title">团队成员风采展示</div>')
    team_slides = [(url, "", "") for url in TEAM_PHOTOS]
    image_carousel(team_slides, interval=3000, show_caption=False)


def page_research():
    show('<div class="sec-title">研究方向</div>')
    show('<div style="color:#5A7086;font-size:16px;margin-bottom:20px;line-height:1.9;">'
         '课题组聚焦于近岸及河口动力过程的数值模拟与智能预报，主要研究方向包括：</div>')

    for i, (title, items) in enumerate(RESEARCH_DIRECTIONS):
        img_src = RESEARCH_IMAGES[i] if i < len(RESEARCH_IMAGES) else IMG_1
        grid_row(
            [img_card(img_src, "", ""), direction_card(img_src, title, items)],
            cols="1fr 1.6fr",
            gap="22px",
        )

    show('<div class="sec-title">承担项目</div>')
    show(project_list(PROJECTS))


def page_team():
    show('<div class="sec-title">团队负责人</div>')

    grid_row([
        f'<div class="img-card" style="min-height: 480px;">'
        f'<img src="{MAO_IMG}" '
        f'     style="aspect-ratio: auto; flex: 1 1 auto; '
        f'            min-height: 480px; height: auto; '
        f'            object-position: top center;">'
        f'</div>',
        text_card(MAO_BIO_HTML, f'👨‍🔬 {PI_NAME}'),
    ], cols="1fr 2.2fr")

    show('<div class="sec-title">团队成员</div>')
    for i in range(0, len(MEMBERS), 3):
        cells = [
            member_card(name, role, field, email, photo)
            for name, role, field, email, photo in MEMBERS[i:i+3]
        ]
        grid_row(cells, cols="1fr 1fr 1fr", gap="20px",
                 extra_class="member-row")

    show('<div class="sec-title">招生信息</div>')
    show("""
    <div class="card">
      <div class="cb">
        欢迎具有海洋科学、大气科学、环境科学、流体力学、数值模拟、数学以及其他理工科背景的同学报考。
      </div>
    </div>
    """)


def page_publications():
    show('<div class="sec-title">代表性论文</div>')
    show(publication_list(PUBLICATIONS))


def page_news():
    show('<div class="sec-title">新闻动态</div>')
    show('<div style="color:#5A7086;font-size:15px;margin-bottom:18px;">点击任意新闻卡片可跳转到来源网站查看详情。</div>')

    st.markdown(news_list_html(NEWS), unsafe_allow_html=True)

    show('<div class="sec-title">常用链接</div>')
    links = [
        ("中国科学院烟台海岸带研究所", "http://www.yic.ac.cn/"),
        ("中国科学院官网", "https://www.cas.cn/"),
        ("生态环境部", "https://www.mee.gov.cn/"),
        ("国家海洋局", "https://www.mnr.gov.cn/"),
    ]
    cells = [
        f'<a class="news-card" href="{u}" target="_blank" rel="noopener" style="border-left-color:#12657F;margin-bottom:0;">'
        f'<div class="news-title" style="margin-bottom:0;">🔗 {n}</div>'
        f'<div class="news-source" style="margin-top:6px;">{u} ↗</div></a>'
        for n, u in links
    ]
    grid_row(cells[:2], cols="1fr 1fr")
    grid_row(cells[2:], cols="1fr 1fr")


def page_contact():
    show('<div class="sec-title">联系方式</div>')
    grid_row([
        text_card(
            f"<b>研究组：</b>{TEAM_NAME}（{PI_NAME} 研究团队）<br>"
            f"<b>地址：</b>山东省烟台市莱山区春晖路 17 号<br>"
            f"<b>邮编：</b>264003<br>"
            f"<b>电话：</b>19953512376（微信同号）<br>"
            f"<b>Email：</b>mhmao@yic.ac.cn",
            f"🏛️ {INSTITUTE}"
        ),
        img_card(MAP_IMG, "", ""),
    ], cols="1.4fr 1fr")

    show('<div class="sec-title">合作交流</div>')
    show("""
    <div class="card">
      <div class="cb">
        我们欢迎与国内外高校、科研院所在<b>近岸河口动力过程、物质输运、观测技术</b>等方面开展合作研究。
      </div>
    </div>
    """)


# ============================================================
# 十三、入口
# ============================================================
show(f"""
<div class="hero">
    <h1>{TEAM_NAME}</h1>
    <p class="sub">{INSTITUTE} {PI_NAME} 研究团队</p>
    <p class="en">{TEAM_EN}</p>
</div>
""")

NAV_ITEMS = ["🏠 首页", "🔬 研究方向", "👥 团队成员",
             "📄 科研成果", "📰 新闻动态", "📞 联系我们"]

if "page" not in st.session_state:
    st.session_state.page = NAV_ITEMS[0]

with st.container(key="nav_bar"):
    nav_cols = st.columns(len(NAV_ITEMS), gap="small")
    for i, item in enumerate(NAV_ITEMS):
        is_active = st.session_state.page == item
        with nav_cols[i]:
            if st.button(
                item,
                key=f"nav_btn_{i}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state.page = item
                st.rerun()

page = st.session_state.page
if page == NAV_ITEMS[0]:
    page_home()
elif page == NAV_ITEMS[1]:
    page_research()
elif page == NAV_ITEMS[2]:
    page_team()
elif page == NAV_ITEMS[3]:
    page_publications()
elif page == NAV_ITEMS[4]:
    page_news()
elif page == NAV_ITEMS[5]:
    page_contact()

show("""
<div style="text-align:center;color:#5A7086;font-size:13px;margin-top:60px;line-height:1.9;
            text-shadow:0 1px 2px rgba(255,255,255,.85);">
  © 2026 中国科学院烟台海岸带研究所 近岸河口物理海洋研究组<br>
  本站内容仅供学术交流使用
</div>
""")