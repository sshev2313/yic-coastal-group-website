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
INSTITUTE_EN = "Yantai Institute of Coastal Zone Research, CAS"
PI_NAME   = "毛淼华"
PI_NAME_EN = "Miaohua Mao"

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

TEAM_PHOTO_VERSION = "20260917"

TEAM_PHOTOS = [
    f"{R2_BASE}/team/group1.jpg?v={TEAM_PHOTO_VERSION}",
    f"{R2_BASE}/team/group2.jpg?v={TEAM_PHOTO_VERSION}",
    f"{R2_BASE}/team/group3.jpg?v={TEAM_PHOTO_VERSION}",
    f"{R2_BASE}/team/group4.jpg?v={TEAM_PHOTO_VERSION}",
    f"{R2_BASE}/team/group5.jpg?v={TEAM_PHOTO_VERSION}",
    f"{R2_BASE}/team/group6.jpg?v={TEAM_PHOTO_VERSION}",
    f"{R2_BASE}/team/group7.jpg?v={TEAM_PHOTO_VERSION}",
    f"{R2_BASE}/team/group8.jpg?v={TEAM_PHOTO_VERSION}",
    f"{R2_BASE}/team/group9.jpg?v={TEAM_PHOTO_VERSION}",
]

RESEARCH_IMAGES = [
    f"{R2_BASE}/research/direction1.jpg",
    f"{R2_BASE}/research/direction2.jpg",
    f"{R2_BASE}/research/direction3.jpg",
    f"{R2_BASE}/research/direction4.jpg",
]

BODY_BG = f"url('{BG_URL}')"

# ============================================================
# 三、毛淼华简介（双语）
# ============================================================
MAO_BIO_HTML_ZH = (
    "<p>毛淼华，男，博士，研究员，博士生导师。本科毕业于浙江大学，2018 年获美国马里兰大学博士学位，"
    "随即进入中科院烟台海岸带研究所工作。2019 年入选烟台市双百计划高层次人才，"
    "2020 年入选中国科学院引才择优人才。</p>"
    "<p>研究方向为近岸河口物理海洋，包括近岸水动力模拟与观测、波流相互作用机制、"
    "波流耦合模式的改进、三维水动力以及拉格朗日粒子追踪模式的应用。"
    "成功地在非结构波流耦合模式 FVCOM 中添加了涡度力方案，揭示了近岸波浪破碎带波生流机制。"
    "通过对波流耦合方案的改进，已构建了马里兰海湾、密歇根湖、渤海及黄河三角洲近岸海域等区域的"
    "三维波流动力模式。相关研究成果已在物理海洋顶级期刊 Journal of Physical Oceanography、"
    "Journal of Geophysical Research: Oceans 与数值模拟顶级期刊 Ocean Modelling 等发表，"
    "并获中国科学院网站科研进展栏目官方报道，2022年、2024年、2025年各报道1次，2026年连续报道3次，"
    "在 AGU Meeting、ECSA 等国际会议做口头报告与海报展示 20 余次"
    "（包括大会主旨报告、分会场主席、最佳海报）。</p>"
    "<p>担任 Nature 子刊以及 PIO、OM、WRR、ECSS 等海洋学国际知名期刊和国内物理海洋学高质量期刊审稿人。"
    "2018 与 2023 年分别获评 SCI 期刊 ECSS 与 JMSE 杰出审稿人。"
    "主持国家自然科学基金与中国科学院等科研项目，国家自然科学基金国际（地区）合作与交流项目、"
    "科技部外国青年人才计划、中科院外国青年学者项目等中方合作者。</p>"
)

MAO_BIO_HTML_EN = (
    "<p>Dr. Miaohua Mao is a Professor and Ph.D. supervisor at the Yantai Institute of Coastal Zone Research, "
    "Chinese Academy of Sciences (YIC, CAS). He received his B.S. from Zhejiang University and his Ph.D. from "
    "the University of Maryland in 2018, then joined YIC-CAS. He was selected for the Yantai Dual-Hundred Talent "
    "Program in 2019 and the CAS Talent Program in 2020.</p>"
    "<p>His research focuses on coastal and estuarine physical oceanography, including nearshore hydrodynamic "
    "modeling and observation, wave–current interaction, coupled wave–current model development, three-dimensional "
    "hydrodynamics, and Lagrangian particle tracking. He implemented a vortex-force formulation in the unstructured-grid "
    "coupled model FVCOM, revealing wave-induced current mechanisms in the nearshore surf zone. He has constructed "
    "three-dimensional coupled wave–current models for the Maryland coastal bays, Lake Michigan, the Bohai Sea and the "
    "Yellow River Delta. His work has been published in leading journals such as the Journal of Physical Oceanography, "
    "Journal of Geophysical Research: Oceans and Ocean Modelling, and has been featured by the official research "
    "highlights of the Chinese Academy of Sciences (2022, 2024, 2025, and three times in 2026). He has delivered more "
    "than 20 oral and poster presentations at international conferences including AGU and ECSA.</p>"
    "<p>He serves as a reviewer for Nature sister journals and internationally renowned oceanography journals "
    "(PIO, OM, WRR, ECSS, etc.), and was recognized as an Outstanding Reviewer for the SCI journals ECSS (2018) "
    "and JMSE (2023). He has led projects funded by the National Natural Science Foundation of China and the Chinese "
    "Academy of Sciences, and has served as the Chinese-side collaborator on NSFC international cooperation projects, "
    "the MOST Foreign Young Talent Program, and CAS foreign young scholar programs.</p>"
)

# ============================================================
# 四、承担项目（中英双语）
# ============================================================
PROJECTS_ZH = [
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
    ("山东省自然科学基金：台风天气下渤海海峡锋面动态变化及其对水交换影响研究", "2025-2028", "13 万", "主持"),
    ("中国博士后科学基金面上项目：寒潮期间波浪破碎混合对近岸锋面动态变化的影响机制研究", "2025-2027", "8 万", "主持"),
    ("中国科学院东方之星青年创新基金", "2025-2026", "10 万", "主持"),
    ("营口市海洋与渔业局", "2025-2029", "*** 万", "主持"),
    ("烟台北斗网络科技有限公司", "2025-2026", "*** 万", "主持"),
]

PROJECTS_EN = [
    ("CAS Program for Outstanding Young Talents",
     "2021-2023", "5.0 M CNY", "主持"),
    ("NSFC Young Scientists Fund: Wave–current interaction mechanisms in the nearshore Yellow River Delta during cold wave events",
     "2021-2023", "240 K CNY", "主持"),
    ("Yantai Dual-Hundred Talent Program",
     "2019-2024", "1.0 M CNY", "主持"),
    ("YIC Frontier Deployment Project: Transport processes and mechanism simulation of brominated flame retardants in the Bohai Sea",
     "2018-2021", "800 K CNY", "主持"),
    ("NSFC International (Regional) Cooperation and Exchange Program: Mechanism of Bohai Sea coastal dynamics associated with typhoon-induced storm surge and extreme waves in changing climate scenarios",
     "2021-2022", "400 K CNY", "中方合作者"),
    ("MOST Foreign Young Talent Program",
     "2021-2022", "300 K CNY", "中方合作者"),
    ("CAS Foreign Young Scholar Program: Machine learning for multi-hazard risk assessment in the Bohai coastal zone",
     "2020-2022", "300 K CNY", "中方合作者"),
    ("Natural Science Foundation of Shandong Province: Dynamic changes of fronts in the Bohai Strait during typhoon events and their impacts on water exchange",
     "2025-2028", "130 K CNY", "主持"),
    ("China Postdoctoral Science Foundation General Program: Mechanisms of wave-breaking-induced mixing on nearshore frontal dynamics during cold wave events",
     "2025-2027", "80 K CNY", "主持"),
    ("CAS Oriental Star Youth Innovation Fund",
     "2025-2026", "100 K CNY", "主持"),
    ("Yingkou Municipal Bureau of Ocean and Fisheries",
     "2025-2029", "*** K CNY", "主持"),
    ("Yantai Beidou Network Technology Co., Ltd.",
     "2025-2026", "*** K CNY", "主持"),
]

# ============================================================
# 五、国际合作机构
# ============================================================
PARTNERS = [
    ("WHOI", "Woods Hole Oceanographic Institution",
     "Research Institute", "https://www.whoi.edu"),
    ("NOAA", "National Oceanic and Atmospheric Administration",
     "Government Agency", "https://www.noaa.gov"),
    ("WGCM", "WCRP ESMO Working Group on Coupled Modelling",
     "International Programme", "https://www.wcrp-esmo.org/working-groups/wgcm"),
    ("CCRS", "Centre for Climate Research Singapore",
     "Research Centre", "https://ccrs.weather.gov.sg"),
    ("MSS",  "Meteorological Service Singapore",
     "Government Agency", "https://www.weather.gov.sg"),
    ("W&M",  "William & Mary",
     "University", "https://www.wm.edu"),
    ("UoN",  "University of Nottingham",
     "University", "https://www.nottingham.ac.uk"),
    ("UT",   "Faculty of Civil Engineering, University of Tabriz",
     "University", "https://civil.tabrizu.ac.ir"),
    ("IUST", "School of Civil Engineering, Iran University of Science & Technology",
     "University", "https://civil.iust.ac.ir"),
]

# ============================================================
# 六、代表性论文
# ============================================================
PUBLICATIONS = [
    ("2026", "Peng, J., Mao, M.*, Du, J.",
     "Composite extreme wind-wave event: Asymmetric forcing from typhoon and cold air in a temperate semienclosed sea",
     "Journal of Geophysical Research: Oceans", "131, e2026JC024175."),
    ("2026", "Su, C., Sahoo, B., Mao, M.*, Xia, M.",
     "Explainable deep learning methods for medium- and long-term storm surge forecast",
     "Ocean Modelling", "204, 102789."),
    ("2026", "Han, M., Mao, M.*, Peng, J., Zhu, J.",
     "Wave breaking characteristics and short-term morphodynamic responses under energetic wave conditions in the Yellow River Estuary",
     "Ocean Engineering", "367, 128062."),
    ("2026", "Jiao, J., Zhang, Y., Weng, H., Mao, M.*, Guo, Q.",
     "Multi-station tidal level forecasting based on novel spatio-temporal graph convolution neural network",
     "Ocean Engineering", "365, 127357."),
    ("2026", "Jiao, J., Xu, X., Zhao, X., Mao, M.*, Yin, M.**, Chen, W.",
     "Short-term significant wave height prediction based on adaptive two-layer decomposition and BiLSTM-attention model",
     "Ocean Engineering", "361, 126187."),
    ("2026", "Su, C., Mao, M.*",
     "Probabilistic storm surge forecasting in the Bohai Sea: A deep learning framework with adaptive uncertainty quantification",
     "Estuarine, Coastal and Shelf Science", "336, 109877."),
    ("2025", "Gao, S., Mao, M.*, Xia, M.",
     "Wave dynamics in the Yellow River Estuary during cold wave and typhoon events",
     "Ocean Modelling", "197, 102568."),
    ("2025", "Su, C., Sahoo, B., Mao, M.*, Xia, M.",
     "Machine learning techniques for predicting typhoon-induced storm surge using a hybrid wind field",
     "Journal of Geophysical Research: Machine Learning and Computation", "2, e2024JH000507."),
    ("2024", "Mao, M., Xia, M.*",
     "Modeling blue crab (Callinectes sapidus) larval transport and recruitment dynamics in a shallow lagoon-inlet-coastal ocean system",
     "Journal of Geophysical Research: Oceans", "129, e2023JC020785."),
    ("2024", "Peng, J., Mao, M.*, Xia, M.",
     "Wave spectra analysis on the spatiotemporal variability of sea states under distinct typhoon tracks in a semi-enclosed sea",
     "Journal of Physical Oceanography", "54(3), 783-807."),
    ("2023", "Mao, M., Xia, M.*",
     "Seasonal dynamics of water circulation and exchange flows in a shallow lagoon-inlet-coastal ocean system",
     "Ocean Modelling", "186, 102276."),
    ("2023", "Nguyen, Q.T., Mao, M.*, Xia, M.",
     "Numerical modeling of nearshore wave transformation and breaking processes in the Yellow River Delta with FUNWAVE-TVD wave model",
     "Journal of Marine Science and Engineering", "11(7), 1380."),
    ("2023", "Peng, J., Mao, M.*, Xia, M.",
     "Dynamics of wave generation and dissipation processes during cold wave events in the Bohai Sea",
     "Estuarine, Coastal and Shelf Science", "280, 108161."),
    ("2022", "Fitzenreiter, K., Mao, M.*, Xia, M.",
     "Characteristics of surface currents in a shallow lagoon–inlet–coastal ocean system revealed by surface drifter observations",
     "Estuaries and Coasts", "45, 2327-2344."),
    ("2021", "Sahoo, B., Mao, M.*, Xia, M.",
     "Projected changes of water currents and circulation in Lake Michigan under Representative Concentration Pathways scenarios",
     "Journal of Geophysical Research: Oceans", "126, e2020JC016651."),
    ("2020", "Mao, M., Xia, M.*",
     "Particle dynamics in the nearshore of Lake Michigan revealed by an observation-modeling system",
     "Journal of Geophysical Research: Oceans", "125, e2019JC015765."),
    ("2020", "Mao, M., Xia, M.*",
     "Monthly and episodic dynamics of summer circulation in Lake Michigan",
     "Journal of Geophysical Research: Oceans", "124, e2019JC015932."),
    ("2020", "Xia, M.*, Mao, M., Niu, Q.",
     "Implementation and comparison of the recent three-dimensional radiation stress theory and vortex-force formalism in an unstructured-grid coastal circulation model",
     "Estuarine, Coastal and Shelf Science", "240, 106771."),
    ("2018", "Mao, M., Xia, M.*",
     "Wave-current dynamics and interactions near the two inlets of a shallow lagoon-inlet-coastal ocean system under hurricane conditions",
     "Ocean Modelling", "129, 124-144."),
]

# ============================================================
# 七、团队成员（中英双语）
# ============================================================
MEMBERS_ZH = [
    ("彭婕",         "特别研究助理", "台风—冷空气复合风浪数值模拟与机理研究",
     "jiepeng@yic.ac.cn", "pengjie.jpg"),
    ("韩梦园",       "博士研究生",   "河口三角洲近岸水动力-地貌演变",
     "hanmengyuan22@mails.ucas.ac.cn", "hanmengyuan.jpg"),
    ("董伟",         "硕士研究生",   "海峡水动力过程",
     "dongwei241@mails.ucas.ac.cn", "dongwei.jpg"),
    ("乐昆",         "硕士研究生",   "拉格朗日轨迹预测",
     "lekun25@mails.ucas.ac.cn", "lekun.jpg"),
    ("Mannan Aleem", "CAS-ANSO Scholarship<br>硕士研究生", "Remote sensing and machine learning",
     "mannanaleem276jb@mails.ucas.ac.cn", "mannan.jpg"),
    ("邱赫",         "硕士研究生",   "风暴潮与淹没范围预报",
     "qiuhe26@mails.ucas.ac.cn", "qiuhe.jpg"),
    ("Uswa Batool",  "CAS-ANSO Scholarship<br>硕士研究生", "Remote sensing and data analysis",
     "uswabatool@mails.ucas.ac.cn", "uswa.jpg"),
]

MEMBERS_EN = [
    ("Jie Peng",     "特别研究助理", "台风—冷空气复合风浪数值模拟与机理研究",
     "jiepeng@yic.ac.cn", "pengjie.jpg"),
    ("Mengyuan Han", "博士研究生",   "河口三角洲近岸水动力-地貌演变",
     "hanmengyuan22@mails.ucas.ac.cn", "hanmengyuan.jpg"),
    ("Wei Dong",     "硕士研究生",   "海峡水动力过程",
     "dongwei241@mails.ucas.ac.cn", "dongwei.jpg"),
    ("Kun Le",       "硕士研究生",   "拉格朗日轨迹预测",
     "lekun25@mails.ucas.ac.cn", "lekun.jpg"),
    ("Mannan Aleem", "CAS-ANSO Scholarship<br>硕士研究生", "Remote sensing and machine learning",
     "mannanaleem276jb@mails.ucas.ac.cn", "mannan.jpg"),
    ("He Qiu",       "硕士研究生",   "风暴潮与淹没范围预报",
     "qiuhe26@mails.ucas.ac.cn", "qiuhe.jpg"),
    ("Uswa Batool",  "CAS-ANSO Scholarship<br>硕士研究生", "Remote sensing and data analysis",
     "uswabatool@mails.ucas.ac.cn", "uswa.jpg"),
]

ROLE_EN = {
    "特别研究助理": "Postdoctoral Research Associate",
    "博士研究生": "Ph.D. Student",
    "硕士研究生": "Master's Student",
    "CAS-ANSO Scholarship<br>硕士研究生": "CAS-ANSO Scholarship<br>Master's Student",
}

FIELD_EN = {
    "台风—冷空气复合风浪数值模拟与机理研究": "Numerical simulation of compound typhoon–cold-air wind-wave events",
    "河口三角洲近岸水动力-地貌演变": "Nearshore hydrodynamics and morphodynamics of estuarine deltas",
    "海峡水动力过程": "Hydrodynamic processes in straits",
    "拉格朗日轨迹预测": "Lagrangian trajectory prediction",
    "Remote sensing and machine learning": "Remote sensing and machine learning",
    "Remote sensing and data analysis": "Remote sensing and data analysis",
    "风暴潮与淹没范围预报": "Storm surge and inundation forecasting",
}

# ============================================================
# 八、已毕业研究生去向
# ============================================================
ALUMNI_MASTER = [
    ("QUAN NGUYEN",   '<span class="tag">全奖</span>赴英国 University of Nottingham 攻读 Ph.D.'),
    ("高盛涵", '<span class="tag">全奖</span>赴美国 College of William &amp; Mary 攻读 Ph.D.'),
    ("牟丽颖", "济南浪潮集团"),
]
ALUMNI_MASTER_EN = [
    ("QUAN NGUYEN",       '<span class="tag">Full Scholarship</span>Ph.D. at University of Nottingham, UK'),
    ("Shenghan Gao", '<span class="tag">Full Scholarship</span>Ph.D. at College of William &amp; Mary, USA'),
    ("Liying Mu",  "Inspur Group, Jinan"),
]

ALUMNI_PHD = [
    ("彭婕",   "中国科学院烟台海岸带研究所"),
    ("孙若涵", "国家海洋技术中心"),
    ("苏长宇", "大连工业大学"),
]
ALUMNI_PHD_EN = [
    ("Jie Peng",     "Yantai Institute of Coastal Zone Research, CAS"),
    ("Ruohan Sun",   "National Ocean Technology Center"),
    ("Changyu Su",   "Dalian Polytechnic University"),
]

# ============================================================
# 九、研究方向（中英双语）
# ============================================================
RESEARCH_DIRECTIONS_ZH = [
    ("🌊 近岸水动力模拟与观测", [
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
    ]),
    ("🤖 海洋动力过程智能预报", [
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
    ]),
    ("🌀 波流耦合模式改进与开发", [
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
    ]),
    ("🧭 拉格朗日粒子追踪与物质输运", [
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
    ]),
]

RESEARCH_DIRECTIONS_EN = [
    ("🌊 Nearshore Hydrodynamics: Modeling and Observation", [
        ("Multi-source Field Observation and Data Fusion",
         "ADCP, CTD, wave buoys, tide gauges, HF radar, UAVs and satellite remote sensing for waves, tides, currents, temperature, salinity, suspended sediment and wind."),
        ("Wave–Tide–Circulation Multi-scale Dynamics",
         "Nearshore wave propagation, breaking, refraction and diffraction; tidal currents, residual flow, water exchange, fronts and upwelling."),
        ("Estuarine and Deltaic Morphodynamics",
         "Coupled river discharge, tide, wave and sediment processes; shoreline change, channel siltation, wetland evolution and morphodynamic response."),
        ("Compound Extreme-Weather Response",
         "Typhoons, cold-air outbreaks and storm surges; coupled wave–surge–circulation–sediment response for coastal hazard warning."),
        ("Observation–Model Fusion and Regional Applications",
         "FVCOM, ROMS, SCHISM, SWAN, Delft3D and XBeach applied to the Bohai Sea, Bohai Strait and Yellow River Delta for disaster mitigation, ports, coastal engineering and ecological restoration."),
    ]),
    ("🤖 AI-based Forecasting of Ocean Dynamics", [
        ("Multi-source Data Assembly and Quality Control",
         "Fusing satellite, buoy, radar, tide-gauge, reanalysis and model outputs into high-quality spatiotemporal datasets."),
        ("Time-series and Spatiotemporal Forecasting Models",
         "LSTM, GRU, TCN, Transformer, GCN and GAT for significant wave height, wave period, tide, currents and storm surge."),
        ("Physics-informed and Hybrid Modeling",
         "PINN, physics-guided neural networks, and numerical-model + AI bias correction / surrogate approaches."),
        ("Intelligent Storm Surge and Inundation Forecasting",
         "Rapid prediction of surge, overtopping and inundation using typhoon track, pressure, wind, bathymetry and tide."),
        ("Real-time Forecasting Systems and Visualization",
         "Ensemble probabilistic forecasting, uncertainty quantification and web/API visualization for typhoon waves, storm surges, shipping, offshore wind and search-and-rescue."),
    ]),
    ("🌀 Wave–Current Coupled Model Development", [
        ("Unstructured-grid Wave–Current Coupling Framework",
         "Coupling FVCOM and SWAN for high-resolution simulation over complex coastlines, estuaries and intertidal zones."),
        ("Wave Effects on Currents",
         "Radiation stress, wave-induced mixing, bottom-friction enhancement, Stokes drift and wave breaking effects on nearshore circulation and transport."),
        ("Current Effects on Waves",
         "Doppler shift, refraction and wave–current energy exchange modulating wave direction, wavelength, steepness and breaking."),
        ("Key Technical Improvements and Validation",
         "Coupling time-step, flux conservation, boundary conditions, wetting–drying and intertidal simulation validated against observations and remote sensing."),
        ("Multi-region and Extreme-event Applications",
         "Simulating typhoons, cold air outbreaks, storm surges, extreme waves and inundation for coastal hazard mitigation and marine engineering."),
    ]),
    ("🧭 Lagrangian Particle Tracking and Material Transport", [
        ("Lagrangian Particle Tracking Model Development",
         "OceanParcels, OpenDrift, LTRANS or in-house models driven by FVCOM, ROMS or SCHISM 3-D currents."),
        ("Random Walk and Turbulent Diffusion Parameterization",
         "Horizontal and vertical random walk accounting for stratification, tide and wind–wave effects to improve pollutant, sediment and microplastic transport."),
        ("Pollutant and Microplastic Transport",
         "Dispersion pathways, residence time and accumulation zones of terrestrial pollutants, nutrients, microplastics and oil spills."),
        ("Sediment and Ecological Connectivity",
         "Suspended-sediment transport, source–sink dynamics and habitat connectivity for fish eggs, larvae and shellfish."),
        ("Ensemble Simulations and Emergency Applications",
         "Probabilistic trajectories, connectivity matrices, GPU parallelization and ML acceleration for oil-spill response, microplastic management, search-and-rescue and ecological restoration."),
    ]),
]

# ============================================================
# 十、新闻数据（中英双语）
# ============================================================
NEWS_ZH = [
    {"date": "2026-09-17",
     "title": "烟台海岸带所在黄河口波浪破碎与地貌动力响应研究取得新进展",
     "summary": "研究团队以黄河三角洲典型河口岸段为研究靶区，构建了 SWAN-FUNWAVE-TVD-XBeach "
                "单向耦合数值模拟体系，完整复现了从波浪破碎发生到地貌动力响应的因果演化链条。"
                "研究表明，水深诱导破碎是黄河口近岸主要波能耗散方式，在沿岸形成千米尺度高波能耗散带，"
                "成为驱动后续地貌过程的核心水动力强迫边界。河口南北岸段波浪破碎机制存在显著分异，"
                "北部以激破波为主导，南部以崩破波占绝对优势，该分异特征由岸坡坡度与入射波陡度共同决定。"
                "不同破碎类型进而塑造了差异化地貌响应格局。相关成果发表于 Ocean Engineering。",
     "source": "中国科学院",
     "url": "https://www.cas.cn/syky/202609/t20260915_5120329.shtml"},
    {"date": "2026-09-14",
     "title": "烟台海岸带所在黄河口波浪破碎与地貌动力响应研究取得新进展",
     "summary": "研究团队联合鲁东大学，以黄河三角洲典型河口岸段为研究靶区，"
                "构建 SWAN-FUNWAVE-TVD-XBeach 单向耦合数值模拟体系，"
                "厘清了黄河口波浪破碎类型的空间分异特征与近岸地貌动力响应的内在机理。"
                "相关成果发表于 Ocean Engineering。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202609/t20260914_8281304.html"},
    {"date": "2026-07-17",
     "title": "研究揭示温带半封闭海域台风与冷空气协同作用下的波浪演化机理",
     "summary": '研究团队以 2019 年台风"利奇马"过境渤海并同步遭遇北下冷空气为案例，'
                "耦合风场解耦技术与精细化波浪数值模拟，定量剖析台风与冷空气对渤海波浪特征的差异化驱动作用，"
                "厘清了温带半封闭海域与开阔大洋在复合风场下波浪响应的本质差异。"
                "相关成果发表于 Journal of Geophysical Research: Oceans。",
     "source": "中国科学院",
     "url": "https://www.cas.cn/syky/202607/t20260715_5115592.shtml"},
    {"date": "2026-07-16",
     "title": "研究提出渤海海域风暴潮中长期高精度预报方法",
     "summary": "研究团队研发出融合混合深度学习架构与多维度可解释性分析的风暴潮预报新体系，"
                "构建 CNN-BiLSTM-Attention 混合模型与独立 BiLSTM 模型，"
                "成功实现渤海海域风暴潮 24—72 小时中长期高精度预报，"
                "为沿海地区风暴潮风险评估与应急预警提供了技术支撑。"
                "相关成果发表于 Ocean Modelling。",
     "source": "中国科学院",
     "url": "https://www.cas.cn/syky/202607/t20260715_5115593.shtml"},
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
                "相关成果发表于 Journal of Geophysical Research: Oceans。",
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

NEWS_EN = [
    {"date": "2026-09-17",
     "title": "New Progress on Wave Breaking and Morphodynamic Response in the Yellow River Estuary",
     "summary": "Using a typical estuarine segment of the Yellow River Delta as the study area, the team constructed "
                "a one-way coupled SWAN-FUNWAVE-TVD-XBeach numerical modeling system, fully reproducing the causal "
                "chain from wave breaking to morphodynamic response. The study shows that depth-induced breaking is "
                "the dominant wave energy dissipation mechanism in the nearshore Yellow River Estuary, forming a "
                "kilometer-scale high-energy dissipation band along the coast that serves as the core hydrodynamic "
                "forcing boundary for subsequent morphological processes. Significant alongshore differences in wave "
                "breaking mechanisms were found: the northern section is dominated by plunging breakers while the "
                "southern section is dominated by spilling breakers, determined jointly by beach slope and incident "
                "wave steepness. Different breaking types shape differentiated morphodynamic response patterns. "
                "Published in Ocean Engineering.",
     "source": "Chinese Academy of Sciences",
     "url": "https://www.cas.cn/syky/202609/t20260915_5120329.shtml"},
    {"date": "2026-09-14",
     "title": "New Progress on Wave Breaking and Morphodynamic Response in the Yellow River Estuary",
     "summary": "In collaboration with Ludong University, the team constructed a one-way coupled "
                "SWAN-FUNWAVE-TVD-XBeach numerical modeling system for a typical estuarine segment of the "
                "Yellow River Delta, clarifying the spatial differentiation of wave breaking types and the "
                "intrinsic mechanisms of nearshore morphodynamic response. The results were published in "
                "Ocean Engineering.",
     "source": "Yantai Institute of Coastal Zone Research, CAS",
     "url": "https://yic.cas.cn/xwzx/kydt/202609/t20260914_8281304.html"},
    {"date": "2026-07-17",
     "title": "Study Reveals Wave Evolution Mechanisms under Typhoon–Cold Air Synergy in Temperate Semi-enclosed Seas",
     "summary": "Using Typhoon Lekima (2019) crossing the Bohai Sea concurrently with a southward cold-air "
                "outbreak as a case study, the team combined wind-field decomposition with high-resolution wave "
                "modeling to quantify the differentiated forcing of typhoon and cold air on Bohai Sea wave "
                "characteristics, and clarified the fundamental differences in wave response between temperate "
                "semi-enclosed seas and open oceans under compound wind fields. Published in Journal of "
                "Geophysical Research: Oceans.",
     "source": "Chinese Academy of Sciences",
     "url": "https://www.cas.cn/syky/202607/t20260715_5115592.shtml"},
    {"date": "2026-07-16",
     "title": "New Method Proposed for Medium- and Long-term High-precision Storm Surge Forecasting in the Bohai Sea",
     "summary": "The team developed a new storm surge forecasting framework integrating hybrid deep learning "
                "architectures with multi-dimensional explainability analysis. They built a CNN-BiLSTM-Attention "
                "hybrid model and an independent BiLSTM model, achieving 24–72 hour medium- to long-term "
                "high-precision storm surge forecasting in the Bohai Sea, providing technical support for coastal "
                "storm surge risk assessment and emergency warning. Published in Ocean Modelling.",
     "source": "Chinese Academy of Sciences",
     "url": "https://www.cas.cn/syky/202607/t20260715_5115593.shtml"},
    {"date": "2026-07-14",
     "title": "Breakthrough in Medium- to Long-term Intelligent Typhoon Storm Surge Forecasting with Explainability",
     "summary": "In collaboration with the University of Maryland, the team innovatively developed a storm surge "
                "forecasting system integrating hybrid deep learning architectures with multi-dimensional "
                "explainability analysis, achieving 24–72 hour medium- to long-term high-precision storm surge "
                "forecasting in the Bohai Sea, and precisely clarifying the core physical driving mechanisms of "
                "storm surge evolution. Published in Ocean Modelling.",
     "source": "Yantai Institute of Coastal Zone Research, CAS",
     "url": "https://yic.cas.cn/xwzx/kydt/202607/t20260714_8247226.html"},
    {"date": "2026-07-14",
     "title": "New Progress on Typhoon–Cold Air Compound Extreme Wind-Wave Response Mechanisms in Temperate Semi-enclosed Seas",
     "summary": "Using Typhoon Lekima (2019) crossing the Bohai Sea concurrently with a southward cold-air "
                "outbreak as a case study, the team quantitatively analyzed the differentiated forcing of typhoon "
                "and cold-air wind fields on Bohai Sea wave characteristics, clarifying the fundamental differences "
                "in wave response between temperate semi-enclosed seas and open oceans under compound wind fields. "
                "Published in Journal of Geophysical Research: Oceans.",
     "source": "Yantai Institute of Coastal Zone Research, CAS",
     "url": "https://yic.cas.cn/xwzx/kydt/202607/t20260714_8247248.html"},
    {"date": "2026-06-03",
     "title": "Breakthrough in Intelligent Significant Wave Height Forecasting",
     "summary": "In collaboration with China Jiliang University and Zhejiang University, the team proposed an "
                "innovative hybrid intelligent prediction model integrating adaptive two-layer decomposition with "
                "a bidirectional long short-term memory network–attention mechanism. The model maintained excellent "
                "predictive performance within 1–6 hour short-term forecasting windows, providing a new solution for "
                "wave energy resource development and maritime navigation safety. Published in Ocean Engineering.",
     "source": "Yantai Institute of Coastal Zone Research, CAS",
     "url": "https://yic.cas.cn/xwzx/kydt/202606/t20260603_8213540.html"},
    {"date": "2026-04-09",
     "title": "Breakthrough in Probabilistic Storm Surge Forecasting in the Bohai Sea",
     "summary": "The team successfully developed a probabilistic deep learning framework for storm surges in the "
                "Bohai Sea, building an explainable hybrid modeling system integrating BiLSTM, adaptive bandwidth "
                "kernel density estimation, and sequential forward selection, providing a high-precision explainable "
                "probabilistic forecasting solution for storm surge disaster risk assessment and warning issuance.",
     "source": "Yantai Institute of Coastal Zone Research, CAS",
     "url": "https://yic.cas.cn/xwzx/kydt/202604/t20260409_8183240.html"},
]

EXCHANGES_ZH = [
    {"date": "2026-06-11",
     "title": "意大利博洛尼亚大学 CO-GROWTH 项目 Module 1 交流",
     "summary": "毛淼华研究员参加由意大利博洛尼亚大学 CO-GROWTH 项目组织的 Module 1 活动，"
                "主题为“海岸韧性及其商业影响（Overview of Coastal Resilience and its Business Implications）”。"
                "活动期间与来自不同国家的学者围绕海岸带韧性建设、跨学科合作与成果转化展开深入交流。",
     "source": "University of Bologna (CENTRI)",
     "url": "https://centri.unibo.it/dcc-cr/en/events/co-growth-module-1-overview-of-coastal-resilience-and-its-business-implications"},
    {"date": "2026-05-20",
     "title": "浙江水利水电学院“尚水思辨”学术沙龙第十讲",
     "summary": "毛淼华研究员应邀主讲，主题为“近海物理海洋在海岸带研究中的应用、人才培养和国家基金申报”。"
                "报告涵盖数值模拟技术实践经验、人工智能方法在物理海洋研究中的新机遇，"
                "并针对青年学者基金申报常见问题给出具体建议。互动环节中，"
                "师生围绕海岸带数值模拟、AI 技术应用、国家基金申报难点等踊跃提问。",
     "source": "浙江水利水电学院水利工程学院",
     "url": "https://slx.zuwe.edu.cn/3a/87/c6585a146055/page.htm"},
    {"date": "2025-09-12",
     "title": "鲁东大学学术交流：渤海及黄河河口动力过程研究",
     "summary": "应鲁东大学水利土木学院邀请，毛淼华研究员与大连理工大学马玉祥教授一同来访，"
                "作题为“渤海及黄河河口动力过程研究”的学术报告。"
                "报告系统介绍了多种海岸带区域的水动力最新研究成果，"
                "揭示了水交换、沉积物输运及极端天气事件对海岸侵蚀与工程安全的影响规律，"
                "体现了多过程耦合的系统研究方法。",
     "source": "鲁东大学水利土木学院、科学技术处",
     "url": "https://sltm.ldu.edu.cn/c1/xyyw/28.htm"},
    {"date": "2024-05-11",
     "title": "中国科学院南海海洋研究所 LTO 学术报告",
     "summary": "毛淼华研究员作题为“寒潮与台风事件中渤海波浪动力机制研究”的学术报告，"
                "利用第三代波浪模型 SWAN 对渤海在典型寒潮与台风期间的波浪特征及动力过程进行研究，"
                "揭示了风浪与涌浪在不同天气过程中的主导机制差异。"
                "报告地点为中国科学院南海海洋研究所 2 号楼 801 会议室。",
     "source": "热带海洋环境国家重点实验室（LTO）",
     "url": "http://lto.scsio.ac.cn/xwtz/xsbg/202405/t20240509_460152.html"},
    {"date": "2024-03-23",
     "title": "浙江海洋大学第三届“研学知海”研究生学术论坛",
     "summary": "毛淼华研究员作为特邀专家出席论坛开幕式并作学术报告，论坛设物理海洋学等三个分论坛。",
     "source": "浙江海洋大学",
     "url": "https://msc.zjou.edu.cn/info/1151/5593.htm"},
]

EXCHANGES_EN = [
    {"date": "2026-06-11",
     "title": "CO-GROWTH Project Module 1 Exchange at the University of Bologna, Italy",
     "summary": "Prof. Mao participated in Module 1 of the CO-GROWTH Project organized by the University of "
                "Bologna, Italy, themed 'Overview of Coastal Resilience and its Business Implications'. "
                "During the event, he engaged in in-depth exchanges with scholars from various countries on "
                "coastal resilience, interdisciplinary collaboration and research translation.",
     "source": "University of Bologna (CENTRI)",
     "url": "https://centri.unibo.it/dcc-cr/en/events/co-growth-module-1-overview-of-coastal-resilience-and-its-business-implications"},
    {"date": "2026-05-20",
     "title": "10th Session of the 'Shangshui Sibian' Academic Salon, Zhejiang University of Water Resources and Electric Power",
     "summary": "Prof. Mao was invited to give a talk on 'Applications of coastal physical oceanography in "
                "coastal zone research, talent development, and NSFC grant applications'. The talk covered "
                "practical experience in numerical modeling, new opportunities for AI methods in physical "
                "oceanography, and specific advice for young scholars on common issues in grant applications. "
                "During the Q&A, students and faculty actively raised questions on coastal numerical modeling, "
                "AI applications, and NSFC application challenges.",
     "source": "School of Hydraulic Engineering, Zhejiang University of Water Resources and Electric Power",
     "url": "https://slx.zuwe.edu.cn/3a/87/c6585a146055/page.htm"},
    {"date": "2025-09-12",
     "title": "Academic Exchange at Ludong University: Dynamics of the Bohai Sea and Yellow River Estuary",
     "summary": "Invited by the School of Water Conservancy and Civil Engineering at Ludong University, Prof. Mao "
                "and Prof. Yuxiang Ma from Dalian University of Technology visited and delivered a talk titled "
                "'Dynamics of the Bohai Sea and Yellow River Estuary'. The talk systematically introduced the latest "
                "hydrodynamic research results from various coastal regions, revealing the influence of water "
                "exchange, sediment transport and extreme weather events on coastal erosion and engineering safety, "
                "reflecting an integrated multi-process research approach.",
     "source": "School of Water Conservancy and Civil Engineering, Ludong University; Office of Science and Technology",
     "url": "https://sltm.ldu.edu.cn/c1/xyyw/28.htm"},
    {"date": "2024-05-11",
     "title": "LTO Academic Seminar, South China Sea Institute of Oceanology, CAS",
     "summary": "Prof. Mao delivered a talk titled 'Wave dynamics mechanisms in the Bohai Sea during cold wave "
                "and typhoon events'. Using the third-generation wave model SWAN, he studied wave characteristics "
                "and dynamic processes in the Bohai Sea during typical cold waves and typhoons, revealing "
                "differences in the dominant mechanisms of wind waves and swell under different weather processes. "
                "The talk was held in Room 801, Building 2, South China Sea Institute of Oceanology, CAS.",
     "source": "State Key Laboratory of Tropical Oceanography (LTO)",
     "url": "http://lto.scsio.ac.cn/xwtz/xsbg/202405/t20240509_460152.html"},
    {"date": "2024-03-23",
     "title": "3rd 'Yanxue Zhihai' Graduate Academic Forum, Zhejiang Ocean University",
     "summary": "Prof. Mao attended the forum opening ceremony as an invited expert and delivered an academic "
                "presentation. The forum featured three sub-forums including physical oceanography.",
     "source": "Zhejiang Ocean University",
     "url": "https://msc.zjou.edu.cn/info/1151/5593.htm"},
]

# ============================================================
# 十一、页面基础设置
# ============================================================
st.set_page_config(
    page_title=f"{TEAM_NAME} | {INSTITUTE}",
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# 十二、全局样式
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

.sub-title {{
    font-size: 20px;
    font-weight: 800;
    color: #0B3C5D;
    letter-spacing: .6px;
    border-left: 5px solid #1D7874;
    padding-left: 14px;
    margin: 30px 0 8px;
}}
.sub-desc {{
    color: #5A7086;
    font-size: 15px;
    margin: 0 0 16px 19px;
    line-height: 1.85;
}}

.grid-row {{
    display: grid;
    gap: 24px;
    align-items: stretch;
    margin-bottom: 24px;
}}
.grid-row > * {{ min-width: 0; }}

.card {{
    background: #fff; border: 1px solid #E3EEF5; border-radius: 14px;
    padding: 22px 26px;
    box-shadow: 0 4px 16px rgba(11,60,93,.07);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    display: flex; flex-direction: column; box-sizing: border-box; height: 100%;
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
    flex: 1 1 auto; text-align: justify; text-justify: inter-ideograph;
}}
.card .cb b {{ color: #12657F; }}
.card .cb p {{ margin: 0 0 14px; text-align: justify; text-justify: inter-ideograph; }}
.card .cb p:last-child {{ margin-bottom: 0; }}

.img-card {{
    background: #fff; border-radius: 14px; overflow: hidden;
    box-shadow: 0 4px 16px rgba(11,60,93,.08);
    transition: transform .25s ease, box-shadow .25s ease;
    display: flex; flex-direction: column; justify-content: center;
    box-sizing: border-box; height: 100%; min-height: 0;
}}
.img-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 14px 30px rgba(11,60,93,.16);
}}
.img-card > img {{
    width: 100%; aspect-ratio: 3 / 2; height: auto;
    object-fit: cover; object-position: center;
    display: block; flex: 0 0 auto;
}}
.img-card > .img-card-body {{ padding: 16px 22px 18px; flex: 0 0 auto; display: flex; flex-direction: column; }}
.img-card-title {{ font-size: 18.5px; font-weight: 700; color: #0B3C5D; margin-bottom: 6px; flex: 0 0 auto; }}
.img-card-desc  {{ font-size: 16px; color: #4A6178; line-height: 1.85; flex: 0 0 auto; }}

.member-card {{
    background: #fff;
    border: 1px solid #E3EEF5;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(11,60,93,.08);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    display: flex; flex-direction: row; align-items: stretch;
    box-sizing: border-box; height: 100%;
}}
.member-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 14px 30px rgba(11,60,93,.16);
    border-color: #BFE0EA;
}}
.member-photo {{
    position: relative; flex: 0 0 38%; aspect-ratio: 2 / 3;
    overflow: hidden; background: #EDF5FA;
}}
.member-photo img {{
    width: 100%; height: 100%;
    object-fit: cover; object-position: center top; display: block;
}}
.member-photo-fallback {{
    width: 100%; height: 100%;
    display: flex; align-items: center; justify-content: center;
    font-size: 56px; color: #B8CAD6;
    background: linear-gradient(135deg, #EDF5FA 0%, #DDEAF2 100%);
    user-select: none;
}}
.member-info {{
    flex: 1 1 62%; padding: 18px 22px;
    display: flex; flex-direction: column; justify-content: center;
    gap: 6px; min-width: 0;
}}
.member-name {{
    font-size: 20px; font-weight: 700; color: #0B3C5D;
    margin-bottom: 2px; letter-spacing: .2px; line-height: 1.35;
}}
.member-role {{
    font-size: 16px; font-weight: 600; color: #1D7874;
    margin-bottom: 8px; letter-spacing: .2px; line-height: 1.5;
}}
.member-field {{ font-size: 16px; color: #4A6178; line-height: 1.6; }}
.member-field b {{ color: #12657F; }}

.dir-list {{
    list-style: none; padding: 0; margin: 0;
    counter-reset: dir;
}}
.dir-list li {{
    counter-increment: dir;
    position: relative; padding: 7px 0 7px 34px;
    font-size: 15px; color: #4A6178; line-height: 1.55;
    text-align: justify; text-justify: inter-ideograph;
    border-bottom: 1px dashed #E3EEF5;
}}
.dir-list li:last-child {{ border-bottom: none; padding-bottom: 0; }}
.dir-list li::before {{
    content: counter(dir);
    position: absolute; left: 0; top: 50%;
    transform: translateY(-50%);
    width: 24px; height: 24px; border-radius: 50%;
    background: linear-gradient(135deg, #0B3C5D, #1D7874);
    color: #fff; font-size: 12px; font-weight: 700;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 2px 6px rgba(11,60,93,.25);
}}
.dir-list li b {{ color: #0B3C5D; font-weight: 700; }}

.card.dir-card {{ padding: 18px 22px 10px; }}
.card.dir-card .ct {{ margin-bottom: 6px; font-size: 18px; }}

.stat {{
    background: #fff; border: 1px solid #E3EEF5; border-radius: 14px;
    padding: 22px 16px; text-align: center;
    box-shadow: 0 4px 16px rgba(11,60,93,.07);
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    box-sizing: border-box; height: 100%;
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
    display: flex; align-items: baseline; justify-content: center; gap: 2px;
}}
.stat .num .unit {{
    font-size: 16px; font-weight: 600; color: #1D7874;
    margin-left: 2px; letter-spacing: 0;
}}
.stat .lab {{ font-size: 15px; color: #7A8FA3; margin-top: 8px; letter-spacing: .5px; }}

.stat-grid {{
    display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr;
    gap: 18px; height: 100%; box-sizing: border-box;
}}

.proj {{
    background: #fff; border: 1px solid #E3EEF5; border-radius: 14px;
    padding: 20px 24px; margin-bottom: 14px;
    box-shadow: 0 3px 14px rgba(11,60,93,.06);
    display: flex; gap: 20px; align-items: flex-start;
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    box-sizing: border-box;
}}
.proj:hover {{
    transform: translateX(4px);
    box-shadow: 0 10px 26px rgba(11,60,93,.14);
    border-color: #BFE0EA;
}}
.proj-num {{
    flex: 0 0 auto; width: 44px; height: 44px;
    border-radius: 11px;
    background: linear-gradient(135deg, #0B3C5D 0%, #1D7874 100%);
    color: #fff; font-weight: 800; font-size: 17px;
    display: flex; align-items: center; justify-content: center;
    letter-spacing: .5px; align-self: center;
    box-shadow: 0 4px 12px rgba(11,60,93,.25);
}}
.proj-body {{ flex: 1 1 auto; min-width: 0; }}
.proj-title {{
    font-size: 17px; font-weight: 700; color: #0B3C5D;
    line-height: 1.7; margin-bottom: 12px;
    overflow-wrap: break-word; word-break: break-word;
}}
.proj-meta {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.proj-tag {{
    display: inline-flex; align-items: center;
    padding: 5px 14px; border-radius: 999px;
    background: #EDF5FA; color: #12657F;
    font-size: 14.5px; font-weight: 600;
    letter-spacing: .3px; white-space: nowrap;
}}
.proj-tag.role {{
    background: linear-gradient(135deg, #E6F4F2, #D3EAE5);
    color: #1D7874;
}}

.partner-grid {{
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 18px; margin-bottom: 24px;
}}
.partner-card {{
    position: relative;
    display: flex; align-items: center; gap: 16px;
    background: linear-gradient(135deg, #FFFFFF 0%, #F7FBFD 100%);
    border: 1px solid #E3EEF5; border-radius: 14px;
    padding: 18px 22px 18px 20px;
    text-decoration: none !important;
    box-shadow: 0 3px 14px rgba(11,60,93,.06);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    box-sizing: border-box; overflow: hidden; min-height: 96px;
}}
.partner-card::after {{
    content: "↗"; position: absolute;
    top: 14px; right: 16px;
    font-size: 15px; font-weight: 700;
    color: #1D7874; opacity: .32;
    transition: opacity .25s ease, transform .25s ease;
}}
.partner-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(11,60,93,.14);
    border-color: #BFE0EA;
}}
.partner-card:hover::after {{ opacity: 1; transform: translate(2px, -2px); }}
.partner-logo {{
    flex: 0 0 auto; width: 52px; height: 52px;
    border-radius: 12px;
    background: linear-gradient(135deg, #0B3C5D 0%, #1D7874 100%);
    color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 14px; letter-spacing: .3px;
    box-shadow: 0 4px 12px rgba(11,60,93,.22);
    text-align: center; line-height: 1.05;
    padding: 4px; box-sizing: border-box;
}}
.partner-body {{ flex: 1 1 auto; min-width: 0; padding-right: 16px; }}
.partner-name {{
    font-size: 15px; font-weight: 700; color: #0B3C5D;
    line-height: 1.45; letter-spacing: .2px; word-break: break-word;
}}
.partner-type {{
    display: inline-block; margin-top: 6px;
    font-size: 12px; font-weight: 600; color: #1D7874;
    background: #E6F4F2; padding: 2px 9px;
    border-radius: 999px; letter-spacing: .3px;
}}

.news-list {{ display: flex; flex-direction: column; gap: 14px; margin-bottom: 20px; }}
.news-card {{
    display: block; background: #fff;
    border-radius: 14px; border: 1px solid #E3EEF5;
    border-left: 5px solid #1D7874;
    padding: 20px 24px; margin: 0 !important;
    text-decoration: none !important;
    box-shadow: 0 3px 14px rgba(11,60,93,.06);
    transition: transform .25s, box-shadow .25s, border-color .25s;
    box-sizing: border-box; color: inherit;
}}
a.news-card:hover {{
    transform: translateX(4px);
    box-shadow: 0 10px 26px rgba(11,60,93,.14);
    border-left-color: #0B3C5D;
}}
.exchange-list .news-card {{
    border-left-color: #12657F;
    background: linear-gradient(90deg, #F7FBFD 0%, #FFFFFF 40%);
}}
.exchange-list .news-card:hover {{
    transform: translateX(4px);
    box-shadow: 0 10px 26px rgba(11,60,93,.14);
    border-left-color: #0B3C5D;
}}
.news-date {{ font-size: 14px; color: #1D7874; font-weight: 700; letter-spacing: .5px; margin-bottom: 6px; }}
.news-title {{ font-size: 18px; font-weight: 700; color: #0B3C5D; line-height: 1.55; margin-bottom: 6px; }}
.news-summary {{
    font-size: 15.5px; color: #5A7086; line-height: 1.75; margin-bottom: 8px;
    text-align: justify; text-justify: inter-ideograph;
}}
.news-source {{ font-size: 14px; color: #1D7874; }}

.pub {{
    background: #fff; border-left: 4px solid #1D7874; border-radius: 8px;
    padding: 16px 20px; margin-bottom: 12px;
    box-shadow: 0 2px 10px rgba(11,60,93,.06);
    font-size: 16.5px; color: #40566B; line-height: 1.85;
    text-align: justify; text-justify: inter-ideograph;
}}
.pub b {{ color: #0B3C5D; }}
.pub .yr {{ color: #1D7874; font-weight: 700; }}

.st-key-nav_bar {{
    position: sticky; top: 12px; z-index: 9999;
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    padding: 8px; border-radius: 18px;
    box-shadow: 0 10px 30px rgba(11,60,93,.14);
    border: 1px solid rgba(227,238,245,.95);
    margin-bottom: 26px;
}}
.st-key-nav_bar [data-testid="stHorizontalBlock"] {{ gap: 6px !important; }}
.st-key-nav_bar button {{
    width: 100% !important; min-height: 46px;
    padding: 10px 14px !important;
    border-radius: 12px !important;
    font-size: 16px !important; font-weight: 600 !important;
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
    font-size: 16px !important; font-weight: 600 !important;
    margin: 0 !important; color: inherit !important;
    white-space: nowrap;
}}

/* 语言切换按钮：与导航按钮区别开，用浅蓝底 */
.st-key-nav_bar .st-key-lang_btn button {{
    background: linear-gradient(135deg, #E6F4F2 0%, #D3EAE5 100%) !important;
    color: #1D7874 !important;
    border: 1px solid #BEE0DA !important;
    font-weight: 700 !important;
    letter-spacing: 0 !important;
}}
.st-key-nav_bar .st-key-lang_btn button:hover {{
    background: linear-gradient(135deg, #D3EAE5 0%, #BEE0DA 100%) !important;
    color: #0B3C5D !important;
    border-color: #1D7874 !important;
}}

.alumni-group {{
    position: relative; background: #fff;
    border: 1px solid #E3EEF5; border-radius: 14px;
    padding: 4px 26px 16px;
    box-shadow: 0 4px 16px rgba(11,60,93,.07);
    box-sizing: border-box; height: 100%; overflow: hidden;
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}}
.alumni-group::before {{
    content: ""; position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, #0B3C5D 0%, #1D7874 100%);
}}
.alumni-group:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(11,60,93,.13);
    border-color: #BFE0EA;
}}
.alumni-head {{
    display: flex; align-items: center; gap: 12px;
    padding: 22px 0 14px;
    border-bottom: 1px dashed #E3EEF5;
}}
.alumni-badge {{
    flex: 0 0 auto; padding: 4px 13px; border-radius: 999px;
    background: linear-gradient(135deg, #0B3C5D 0%, #1D7874 100%);
    color: #fff; font-size: 13px; font-weight: 700;
    letter-spacing: 1.5px;
    box-shadow: 0 3px 10px rgba(11,60,93,.22);
}}
.alumni-title {{
    flex: 1 1 auto; font-size: 18px; font-weight: 700;
    color: #0B3C5D; letter-spacing: .5px;
}}
.alumni-list {{ display: flex; flex-direction: column; }}
.alumni-item {{
    display: flex; align-items: flex-start; gap: 14px;
    padding: 15px 0;
    border-bottom: 1px dashed #EDF3F8;
}}
.alumni-item:last-child {{ border-bottom: none; padding-bottom: 4px; }}
.alumni-name {{
    position: relative; flex: 0 0 130px;
    padding-left: 15px;
    font-size: 17px; font-weight: 700;
    color: #0B3C5D; letter-spacing: .3px; line-height: 1.6;
}}
.alumni-name::before {{
    content: ""; position: absolute;
    left: 0; top: 50%; transform: translateY(-50%);
    width: 6px; height: 6px; border-radius: 50%;
    background: #1D7874;
    box-shadow: 0 0 0 3px rgba(29,120,116,.14);
}}
.alumni-dest {{
    flex: 1 1 auto; min-width: 0;
    font-size: 15.5px; color: #4A6178;
    line-height: 1.7; word-break: break-word;
}}
.alumni-dest .tag {{
    display: inline-block; margin-right: 7px;
    padding: 1px 9px; border-radius: 6px;
    background: #EDF5FA; color: #12657F;
    font-size: 13px; font-weight: 700;
    letter-spacing: .3px;
}}

@media (max-width: 900px) {{
    .block-container {{ padding: 0.8rem 1rem 2rem !important; max-width: 100% !important; }}
    .hero {{
        padding: 32px 22px 30px !important;
        border-radius: 16px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        text-align: left !important;
    }}
    .hero h1 {{ font-size: 24px !important; letter-spacing: 1px !important; line-height: 1.35 !important; text-align: left !important; width: 100% !important; }}
    .hero .sub {{ font-size: 14px !important; letter-spacing: 0 !important; text-align: left !important; width: 100% !important; }}
    .hero .en {{ font-size: 12px !important; text-align: left !important; width: 100% !important; }}
    .sec-title {{ font-size: 19px !important; margin: 22px 0 14px !important; padding-left: 11px !important; border-left-width: 4px !important; }}
    .sub-title {{ font-size: 16px !important; margin: 22px 0 6px !important; padding-left: 11px !important; border-left-width: 4px !important; }}
    .sub-desc {{ font-size: 13px !important; margin: 0 0 12px 15px !important; }}
    .grid-row {{ grid-template-columns: 1fr !important; gap: 16px !important; margin-bottom: 16px !important; }}
    .grid-row.member-row {{ grid-template-columns: 1fr !important; gap: 14px !important; margin-bottom: 16px !important; }}
    .card {{ padding: 18px 18px !important; }}
    .card .ct {{ font-size: 17px !important; }}
    .card .cb {{ font-size: 15px !important; line-height: 1.8 !important; text-align: justify !important; text-justify: inter-ideograph !important; }}
    .card .cb p {{ text-align: justify !important; text-justify: inter-ideograph !important; }}
    .img-card-title {{ font-size: 16px !important; }}
    .img-card-desc  {{ font-size: 14px !important; }}
    .grid-row.member-row .member-card {{ flex-direction: row !important; }}
    .grid-row.member-row .member-photo {{ flex: 0 0 32% !important; width: auto !important; aspect-ratio: 2 / 3 !important; }}
    .grid-row.member-row .member-photo-fallback {{ font-size: 40px !important; }}
    .grid-row.member-row .member-info {{ flex: 1 1 68% !important; padding: 14px 16px !important; justify-content: center !important; gap: 4px !important; }}
    .grid-row.member-row .member-name {{ font-size: 16px !important; }}
    .grid-row.member-row .member-role {{ font-size: 13.5px !important; margin-bottom: 6px !important; }}
    .grid-row.member-row .member-field {{ font-size: 12.5px !important; line-height: 1.55 !important; }}
    .dir-list li {{ font-size: 13.5px !important; padding: 6px 0 6px 30px !important; line-height: 1.5 !important; text-align: justify !important; text-justify: inter-ideograph !important; }}
    .dir-list li::before {{ width: 22px !important; height: 22px !important; font-size: 11px !important; }}
    .card.dir-card {{ padding: 14px 16px 8px !important; }}
    .card.dir-card .ct {{ font-size: 16px !important; margin-bottom: 4px !important; }}
    .stat {{ padding: 16px 10px !important; }}
    .stat .num {{ font-size: 30px !important; }}
    .stat .num .unit {{ font-size: 13px !important; }}
    .stat .lab {{ font-size: 13px !important; }}
    .proj {{ padding: 16px 16px !important; gap: 12px !important; }}
    .proj-num {{ width: 36px !important; height: 36px !important; font-size: 14px !important; }}
    .proj-title {{ font-size: 15px !important; }}
    .proj-tag   {{ font-size: 12.5px !important; padding: 4px 10px !important; }}
    .partner-grid {{ grid-template-columns: 1fr !important; gap: 12px !important; }}
    .partner-card {{ padding: 14px 16px 14px 14px !important; min-height: 82px !important; gap: 13px !important; }}
    .partner-logo {{ width: 44px !important; height: 44px !important; font-size: 12px !important; border-radius: 10px !important; }}
    .partner-name {{ font-size: 13.5px !important; }}
    .partner-type {{ font-size: 11px !important; padding: 1px 7px !important; margin-top: 5px !important; }}
    .partner-card::after {{ font-size: 13px !important; top: 12px !important; right: 13px !important; }}
    .news-card {{ padding: 16px 18px !important; }}
    .news-title   {{ font-size: 16px !important; }}
    .news-summary {{ font-size: 14px !important; text-align: justify !important; text-justify: inter-ideograph !important; }}
    .news-date, .news-source {{ font-size: 12.5px !important; }}
    .pub {{ font-size: 14.5px !important; padding: 12px 14px !important; text-align: justify !important; text-justify: inter-ideograph !important; }}
    .st-key-nav_bar {{ padding: 6px !important; border-radius: 14px !important; top: 6px !important; }}
    .st-key-nav_bar [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap !important; }}
    .st-key-nav_bar [data-testid="stHorizontalBlock"] > [data-testid="column"] {{
        flex: 0 0 33.33% !important;
        max-width: 33.33% !important;
    }}
    .st-key-nav_bar button {{ min-height: 38px !important; padding: 6px 6px !important; font-size: 13px !important; letter-spacing: 0 !important; border-radius: 9px !important; }}
    .st-key-nav_bar button p {{ font-size: 13px !important; letter-spacing: 0 !important; }}
    .alumni-group {{ padding: 2px 16px 12px !important; }}
    .alumni-head  {{ padding: 16px 0 11px !important; gap: 8px !important; }}
    .alumni-badge {{ font-size: 11.5px !important; padding: 3px 9px !important; letter-spacing: 1px !important; }}
    .alumni-title {{ font-size: 15.5px !important; }}
    .alumni-item  {{ padding: 11px 0 !important; gap: 10px !important; }}
    .alumni-name  {{ flex: 0 0 100px !important; font-size: 14.5px !important; padding-left: 12px !important; }}
    .alumni-dest  {{ font-size: 13.5px !important; line-height: 1.65 !important; }}
    .alumni-dest .tag {{ font-size: 11.5px !important; padding: 1px 6px !important; }}
}}

@media (max-width: 480px) {{
    .hero h1 {{ font-size: 20px !important; }}
    .hero .sub {{ font-size: 13px !important; }}
    .sec-title {{ font-size: 17px !important; }}
    .card .cb {{ font-size: 14px !important; }}
    .st-key-nav_bar button,
    .st-key-nav_bar button p {{ font-size: 12px !important; }}
    .alumni-name {{ flex: 0 0 88px !important; font-size: 13.5px !important; }}
    .alumni-dest {{ font-size: 12.5px !important; }}
    .sub-title {{ font-size: 15px !important; }}
    .sub-desc  {{ font-size: 12.5px !important; }}
    .partner-logo {{ width: 40px !important; height: 40px !important; font-size: 11px !important; }}
    .partner-name {{ font-size: 13px !important; }}
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ============================================================
# 十三、语言状态与辅助
# ============================================================
if "lang" not in st.session_state:
    st.session_state.lang = "zh"

def t(zh: str, en: str) -> str:
    """根据当前语言返回对应文本。"""
    return en if st.session_state.lang == "en" else zh


def cur_role(role_zh: str) -> str:
    if st.session_state.lang == "en":
        return ROLE_EN.get(role_zh, role_zh)
    return role_zh


def cur_field(field: str) -> str:
    if st.session_state.lang == "en":
        return FIELD_EN.get(field, field)
    return field


def sep_lang() -> str:
    """中英文冒号分隔符。"""
    return ": " if st.session_state.lang == "en" else "："


# ============================================================
# 十四、渲染辅助
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
    t_ = f'<div class="ct">{title_html}</div>' if title_html else ""
    return f'<div class="card">{t_}<div class="cb">{body_html}</div></div>'


def img_card(src: str, title: str = "", desc: str = "") -> str:
    body = ""
    if title or desc:
        body = (
            f'<div class="img-card-body">'
            f'{f"<div class=\"img-card-title\">{title}</div>" if title else ""}'
            f'{f"<div class=\"img-card-desc\">{desc}</div>" if desc else ""}'
            f'</div>'
        )
    return f'<div class="img-card"><img src="{src}">{body}</div>'


def direction_card(img_src: str, title: str, items) -> str:
    sep = sep_lang()
    lis = "".join(f'<li><b>{t_}{sep}</b>{d}</li>' for t_, d in items)
    return (
        f'<div class="card dir-card">'
        f'<div class="ct">{title}</div>'
        f'<ul class="dir-list">{lis}</ul>'
        f'</div>'
    )


def member_card(name: str, role: str, field: str, photo_filename: str = "") -> str:
    photo_url = f"{R2_BASE}/members/{photo_filename}" if photo_filename else ""
    role_display = cur_role(role)
    field_display = cur_field(field)
    label = "Research" if st.session_state.lang == "en" else "研究方向"
    sep = sep_lang()
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
        f'    <div class="member-role">{role_display}</div>'
        f'    <div class="member-field"><b>{label}{sep}</b>{field_display}</div>'
        f'  </div>'
        f'</div>'
    )


def alumni_card(badge: str, title: str, people) -> str:
    items = "".join(
        f'<div class="alumni-item">'
        f'  <div class="alumni-name">{name}</div>'
        f'  <div class="alumni-dest">{dest}</div>'
        f'</div>'
        for name, dest in people
    )
    return (
        f'<div class="alumni-group">'
        f'  <div class="alumni-head">'
        f'    <span class="alumni-badge">{badge}</span>'
        f'    <span class="alumni-title">{title}</span>'
        f'  </div>'
        f'  <div class="alumni-list">{items}</div>'
        f'</div>'
    )


def partner_card(abbr: str, name: str, ptype: str, url: str) -> str:
    return (
        f'<a class="partner-card" href="{url}" target="_blank" rel="noopener">'
        f'  <div class="partner-logo">{abbr}</div>'
        f'  <div class="partner-body">'
        f'    <div class="partner-name">{name}</div>'
        f'    <span class="partner-type">{ptype}</span>'
        f'  </div>'
        f'</a>'
    )


def stat_grid(stats) -> str:
    cells = "".join(
        f'<div class="stat">'
        f'<div class="num">{n}<span class="unit">{u}</span></div>'
        f'<div class="lab">{l}</div>'
        f'</div>'
        for n, u, l in stats
    )
    return f'<div class="stat-grid">{cells}</div>'


def project_list(projects) -> str:
    html = ""
    role_label = "PI" if st.session_state.lang == "en" else "主持"
    coop_label = "Chinese-side Collaborator" if st.session_state.lang == "en" else "中方合作者"
    for i, (title, period, fund, role) in enumerate(projects, start=1):
        role_disp = role_label if role == "主持" else coop_label
        html += (
            f'<div class="proj">'
            f'<div class="proj-num">{i:02d}</div>'
            f'<div class="proj-body">'
            f'<div class="proj-title">{title}</div>'
            f'<div class="proj-meta">'
            f'<span class="proj-tag">📅 {period}</span>'
            f'<span class="proj-tag">💰 {fund}</span>'
            f'<span class="proj-tag role">👤 {role_disp}</span>'
            f'</div></div></div>'
        )
    return html


def partner_grid_html(partners) -> str:
    cards = "".join(partner_card(*p) for p in partners)
    return f'<div class="partner-grid">{cards}</div>'


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


def news_list_html(news, extra_class: str = "") -> str:
    cards = ""
    src_label = "Source" if st.session_state.lang == "en" else "来源"
    sep = sep_lang()
    for n in news:
        url    = (n.get("url") or "").strip()
        date   = n.get("date", "")
        title  = n.get("title", "")
        summ   = n.get("summary", "")
        source = n.get("source", "")
        inner = (
            f'<div class="news-date">📅 {date}</div>'
            f'<div class="news-title">{title}</div>'
            f'<div class="news-summary">{summ}</div>'
            f'<div class="news-source">{src_label}{sep}{source}'
            + (" ↗" if url else "")
            + '</div>'
        )
        if url:
            cards += f'<a class="news-card" href="{url}" target="_blank" rel="noopener">{inner}</a>'
        else:
            cards += f'<div class="news-card">{inner}</div>'
    cls = f"news-list {extra_class}".strip()
    return f'<div class="{cls}">{cards}</div>'


def image_carousel(slides, interval=3000, show_caption=True, max_height=700,
                   fade_duration=1.6, zoom_duration=10, zoom_scale=1.08):
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
            <img src="{src}" alt="{title}" loading="lazy">
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
        display: none;
        position: relative;
        overflow: hidden;
    }}
    .carousel-slide.active {{
        display: block;
        animation: fadeIn {fade_duration}s cubic-bezier(.4, 0, .2, 1) both;
    }}
    .carousel-slide img {{
        width: 100%;
        height: auto;
        max-height: {max_height}px;
        object-fit: contain;
        display: block;
        margin: 0 auto;
        transform: scale(1);
        transform-origin: center center;
        animation: none;
    }}
    .carousel-slide.active img {{
        animation: kenBurns {zoom_duration}s ease-out forwards;
    }}
    @keyframes fadeIn {{
        0%   {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}
    @keyframes kenBurns {{
        0%   {{ transform: scale(1); }}
        100% {{ transform: scale({zoom_scale}); }}
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
        const prevEl = slides[current];
        prevEl.classList.remove('active');
        dots[current].classList.remove('active');
        current = (idx + total) % total;
        const curEl = slides[current];
        void curEl.offsetWidth;
        curEl.classList.add('active');
        dots[current].classList.add('active');
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
    components.html(html, height=max_height + 60, scrolling=False)


# ============================================================
# 十五、各页面
# ============================================================
def page_home():
    show(f'<div class="sec-title">{t("研究组简介", "About the Group")}</div>')

    if st.session_state.lang == "zh":
        intro_text = """
            本研究组隶属于<b>中国科学院烟台海岸带研究所</b>，聚焦<b>黄河口、渤海海峡及渤海近岸区域的物理海洋学过程</b>，
            以黄河口、渤海及黄海近岸海域为主要研究区域，综合运用<b>现场观测与数值模拟</b>等手段，
            系统研究<b>近岸水动力模拟与观测、海洋动力过程智能预报、波流耦合模式改进与开发、拉格朗日粒子追踪与物质输运</b>，
            及其对陆源物质输运、营养盐与污染物扩散、海岸带生态环境的影响，
            为海岸带资源可持续利用与生态环境保护提供科学支撑。<br><br>
            研究组由<b>毛淼华研究员</b>领衔，目前有研究员、特别研究助理及研究生共8人，
            承担<b>国家自然科学基金、中国科学院、烟台市</b>等项目。
        """
        stats = [
            ("4+", "项", "主要研究方向"),
            ("10+", "项", "承担科研项目"),
            ("30+", "篇", "发表学术论文"),
            ("8", "人", "团队成员"),
        ]
    else:
        intro_text = """
            Our group is affiliated with the <b>Yantai Institute of Coastal Zone Research, Chinese Academy of Sciences</b>.
            We focus on <b>physical oceanographic processes in the Yellow River Estuary, the Bohai Strait and the nearshore Bohai Sea</b>,
            integrating <b>field observation and numerical modeling</b> to investigate
            <b>nearshore hydrodynamics, AI-based ocean forecasting, wave–current coupled modeling, and Lagrangian particle tracking and material transport</b>.
            Our research supports sustainable utilization of coastal resources and ecological protection.<br><br>
            The group is led by <b>Prof. Miaohua Mao</b>, with currently 8 members including research staff, postdocs and graduate students,
            supported by projects from <b>NSFC, CAS, and Yantai City</b>.
        """
        stats = [
            ("4+", "", "Research Areas"),
            ("10+", "", "Research Projects"),
            ("30+", "", "Publications"),
            ("8", "", "Team Members"),
        ]

    grid_row(
        [text_card(intro_text), stat_grid(stats)],
        cols="1.6fr 1fr",
        gap="24px",
    )

    show(f'<div class="sec-title">{t("团队成员风采展示", "Group Gallery")}</div>')
    team_slides = [(url, "", "") for url in TEAM_PHOTOS]
    image_carousel(
        team_slides, interval=3000, show_caption=False,
        fade_duration=1.6, zoom_duration=10, zoom_scale=1.08,
    )


def page_research():
    dirs = RESEARCH_DIRECTIONS_EN if st.session_state.lang == "en" else RESEARCH_DIRECTIONS_ZH
    projects = PROJECTS_EN if st.session_state.lang == "en" else PROJECTS_ZH

    show(f'<div class="sec-title">{t("研究方向", "Research Areas")}</div>')
    show(
        f'<div style="color:#5A7086;font-size:16px;margin-bottom:20px;line-height:1.9;">'
        f'{t("课题组聚焦于近岸及河口动力过程的数值模拟与智能预报，主要研究方向包括：", "The group focuses on numerical modeling and intelligent forecasting of nearshore and estuarine dynamics. Main research areas:")}'
        f'</div>'
    )

    for i, (title, items) in enumerate(dirs):
        img_src = RESEARCH_IMAGES[i] if i < len(RESEARCH_IMAGES) else IMG_1
        grid_row(
            [img_card(img_src, "", ""), direction_card(img_src, title, items)],
            cols="1fr 1.6fr",
            gap="22px",
        )

    show(f'<div class="sec-title">{t("承担项目", "Research Projects")}</div>')
    show(project_list(projects))

    # ---------- 国际合作 ----------
    show(f'<div class="sec-title">{t("国际合作", "International Collaboration")}</div>')
    show(
        f'<div style="color:#5A7086;font-size:16px;margin-bottom:20px;line-height:1.9;">'
        f'{t("课题组与全球多家海洋研究机构、气象部门及高校保持长期合作，共同推进近岸动力过程、极端海况预报与气候变化的跨学科研究。", "The group maintains long-term collaborations with leading ocean research institutes, meteorological agencies and universities worldwide to advance interdisciplinary research on nearshore dynamics, extreme sea-state forecasting and climate change.")}'
        f'</div>'
    )
    st.markdown(partner_grid_html(PARTNERS), unsafe_allow_html=True)


def page_team():
    show(f'<div class="sec-title">{t("团队负责人", "Principal Investigator")}</div>')

    bio = MAO_BIO_HTML_ZH if st.session_state.lang == "zh" else MAO_BIO_HTML_EN
    pi_display = PI_NAME if st.session_state.lang == "zh" else PI_NAME_EN
    grid_row([
        f'<div class="img-card" style="min-height: 480px;">'
        f'<img src="{MAO_IMG}" '
        f'     style="aspect-ratio: auto; flex: 1 1 auto; '
        f'            min-height: 480px; height: auto; '
        f'            object-position: top center;">'
        f'</div>',
        text_card(bio, f'👨‍🔬 {pi_display}'),
    ], cols="1fr 2.2fr")

    show(f'<div class="sec-title">{t("团队核心成员", "Team Members")}</div>')
    members = MEMBERS_EN if st.session_state.lang == "en" else MEMBERS_ZH
    for i in range(0, len(members), 3):
        cells = [
            member_card(name, role, field, photo)
            for name, role, field, _email, photo in members[i:i+3]
        ]
        grid_row(cells, cols="1fr 1fr 1fr", gap="20px", extra_class="member-row")

    # ---------- 已毕业研究生去向 ----------
    show(f'<div class="sec-title">{t("已毕业研究生去向", "Alumni Destinations")}</div>')
    show(
        f'<div style="color:#5A7086;font-size:16px;margin-bottom:20px;line-height:1.9;">'
        f'{t("研究组培养的毕业生活跃于国内外高校、科研院所与高新技术企业。", "Our alumni are active in universities, research institutes and high-tech companies both in China and abroad.")}'
        f'</div>'
    )
    if st.session_state.lang == "en":
        grid_row([
            alumni_card("Master", "Master's Graduates", ALUMNI_MASTER_EN),
            alumni_card("Ph.D.", "Ph.D. Graduates", ALUMNI_PHD_EN),
        ], cols="1fr 1fr", gap="24px")
    else:
        grid_row([
            alumni_card("硕士", "已毕业硕士研究生", ALUMNI_MASTER),
            alumni_card("博士", "已毕业博士研究生", ALUMNI_PHD),
        ], cols="1fr 1fr", gap="24px")

    # ---------- 招生 ----------
    show(f'<div class="sec-title">{t("招生信息", "Admissions")}</div>')
    show(f"""
    <div class="card">
      <div class="cb">
        {t("欢迎具有海洋科学、大气科学、环境科学、流体力学、数值模拟、数学以及其他理工科背景的同学报考<b>硕士与博士研究生</b>。",
           "We welcome applicants with backgrounds in ocean science, atmospheric science, environmental science, fluid mechanics, numerical modeling, mathematics and other STEM disciplines to apply for our <b>Master's and Ph.D. programs</b>.")}
      </div>
    </div>
    """)

    # ---------- 招聘 ----------
    show(f'<div class="sec-title">{t("招聘信息", "Openings")}</div>')
    show(f"""
    <div class="card">
      <div class="cb">
        {t("常年招聘<b>特别研究助理</b>，研究方向包括：河口近海数值模拟、风暴潮、海浪、泥沙动力、海岸地貌演变、近海水质生态、海洋 AI 与大数据可视化。",
           "We are continuously recruiting <b>postdoctoral research associates</b> in estuarine and nearshore numerical modeling, storm surge, ocean waves, sediment dynamics, coastal morphodynamics, nearshore water quality and ecology, ocean AI and big-data visualization.")}
      </div>
    </div>
    """)


def page_publications():
    show(f'<div class="sec-title">{t("代表性论文", "Selected Publications")}</div>')
    show(publication_list(PUBLICATIONS))


def page_news():
    news_data = NEWS_EN if st.session_state.lang == "en" else NEWS_ZH
    exch_data = EXCHANGES_EN if st.session_state.lang == "en" else EXCHANGES_ZH

    # ---------- 研究进展 ----------
    show(f'<div class="sub-title">{t("研究进展", "Research Highlights")}</div>')
    show(
        f'<div class="sub-desc">'
        f'{t("课题组最新科研成果及官方报道，点击卡片可跳转到来源网站查看详情。", "Latest research outputs and official coverage. Click a card to view the source.")}'
        f'</div>'
    )
    st.markdown(news_list_html(news_data), unsafe_allow_html=True)

    # ---------- 交流报告 ----------
    show(f'<div class="sub-title">{t("交流报告", "Invited Talks")}</div>')
    show(
        f'<div class="sub-desc">'
        f'{t("课题组成员受邀在国内外高校、科研机构与国际学术会议作报告情况。", "Invited talks by group members at domestic and international universities, research institutes and academic conferences.")}'
        f'</div>'
    )
    st.markdown(
        news_list_html(exch_data, extra_class="exchange-list"),
        unsafe_allow_html=True,
    )

    # ---------- 常用链接 ----------
    show(f'<div class="sec-title">{t("常用链接", "Useful Links")}</div>')
    links = [
        (t("中国科学院烟台海岸带研究所", "Yantai Institute of Coastal Zone Research, CAS"), "http://www.yic.ac.cn/"),
        (t("中国科学院", "Chinese Academy of Sciences"), "https://www.cas.cn/"),
        (t("生态环境部", "Ministry of Ecology and Environment"), "https://www.mee.gov.cn/"),
        (t("国家海洋局", "Ministry of Natural Resources"), "https://www.mnr.gov.cn/"),
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
    show(f'<div class="sec-title">{t("联系方式", "Contact")}</div>')

    if st.session_state.lang == "zh":
        contact_html = (
            f"<b>研究组：</b>{TEAM_NAME}（{PI_NAME} 研究团队）<br>"
            f"<b>地址：</b>山东省烟台市莱山区春晖路 17 号<br>"
            f"<b>邮编：</b>264003<br>"
            f"<b>电话：</b>19953512376（微信同号）<br>"
            f"<b>Email：</b>mhmao@yic.ac.cn"
        )
        contact_title = f"🏛️ {INSTITUTE}"
    else:
        contact_html = (
            f"<b>Group:</b> {TEAM_EN} (PI: Prof. {PI_NAME_EN})<br>"
            f"<b>Address:</b> No. 17 Chunhui Road, Laishan District, Yantai, Shandong, China<br>"
            f"<b>Postal Code:</b> 264003<br>"
            f"<b>Tel:</b> +86 19953512376 (WeChat)<br>"
            f"<b>Email:</b> mhmao@yic.ac.cn"
        )
        contact_title = f"🏛️ {INSTITUTE_EN}"

    grid_row([
        text_card(contact_html, contact_title),
        img_card(MAP_IMG, "", ""),
    ], cols="1.4fr 1fr")

    show(f'<div class="sec-title">{t("合作交流", "Collaboration")}</div>')
    show(f"""
    <div class="card">
      <div class="cb">
        {t("我们欢迎与国内外高校、科研院所在<b>近岸河口动力过程、物质输运、观测技术</b>等方面开展合作研究。",
           "We welcome collaboration with universities and research institutions worldwide in <b>nearshore and estuarine dynamics, material transport, and observation techniques</b>.")}
      </div>
    </div>
    """)


# ============================================================
# 十六、入口
# ============================================================
# Hero
if st.session_state.lang == "zh":
    hero_html = f"""
    <div class="hero">
        <h1>{TEAM_NAME}</h1>
        <p class="sub">{INSTITUTE} {PI_NAME} 研究团队</p>
    </div>
    """
else:
    hero_html = f"""
    <div class="hero">
        <h1>{TEAM_EN}</h1>
        <p class="sub">{INSTITUTE_EN} · Research Group led by Prof. {PI_NAME_EN}</p>
    </div>
    """
show(hero_html)

# 导航项
NAV_ITEMS_ZH = ["🏠 首页", "🔬 研究方向", "👥 团队成员",
                "📄 科研成果", "📰 新闻动态", "📞 联系我们"]
NAV_ITEMS_EN = ["🏠 Home", "🔬 Research", "👥 Team",
                "📄 Publications", "📰 News", "📞 Contact"]
NAV_ITEMS = NAV_ITEMS_EN if st.session_state.lang == "en" else NAV_ITEMS_ZH

if "page_idx" not in st.session_state:
    st.session_state.page_idx = 0
if st.session_state.page_idx >= len(NAV_ITEMS):
    st.session_state.page_idx = 0

with st.container(key="nav_bar"):
    nav_cols = st.columns([1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 0.7], gap="small")
    for i, item in enumerate(NAV_ITEMS):
        is_active = st.session_state.page_idx == i
        with nav_cols[i]:
            if st.button(
                item,
                key=f"nav_btn_{i}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state.page_idx = i
                st.rerun()
    with nav_cols[-1]:
        lang_label = "🌐 中" if st.session_state.lang == "en" else "🌐 EN"
        if st.button(
            lang_label,
            key="lang_btn",
            use_container_width=True,
        ):
            st.session_state.lang = "en" if st.session_state.lang == "zh" else "zh"
            st.rerun()

# 路由
_page = st.session_state.page_idx
if _page == 0:
    page_home()
elif _page == 1:
    page_research()
elif _page == 2:
    page_team()
elif _page == 3:
    page_publications()
elif _page == 4:
    page_news()
elif _page == 5:
    page_contact()

# Footer
if st.session_state.lang == "zh":
    footer_html = """
<div style="text-align:center;color:#5A7086;font-size:13px;margin-top:60px;line-height:1.9;
            text-shadow:0 1px 2px rgba(255,255,255,.85);">
  © 2026 中国科学院烟台海岸带研究所 近岸河口物理海洋研究组<br>
  本站内容仅供学术交流使用
</div>
"""
else:
    footer_html = """
<div style="text-align:center;color:#5A7086;font-size:13px;margin-top:60px;line-height:1.9;
            text-shadow:0 1px 2px rgba(255,255,255,.85);">
  © 2026 Coastal and Estuarine Physical Oceanography Group,<br>
  Yantai Institute of Coastal Zone Research, Chinese Academy of Sciences
</div>
"""
show(footer_html)