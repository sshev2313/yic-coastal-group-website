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

# ★ 团队合影：从 R2 的 team 文件夹读取
TEAM_PHOTOS = [
    f"{R2_BASE}/team/group1.jpg",
    f"{R2_BASE}/team/group2.jpg",
    f"{R2_BASE}/team/group3.jpg",
    f"{R2_BASE}/team/group4.jpg",
    f"{R2_BASE}/team/group5.jpg",
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
# 五、代表性论文
# ============================================================
PUBLICATIONS = [
    ("2024", "Peng, J., Mao, M.*, Xia, M.",
     "Wave spectra analysis on the spatiotemporal variability of sea states under distinct typhoon tracks in a semi-enclosed sea",
     "Journal of Physical Oceanography", "54(3), 783-807."),
    ("2024", "Mao, M., Xia, M.*",
     "Modeling blue crab (Callinectes sapidus) larval transport and recruitment dynamics in a shallow lagoon-inlet-coastal ocean system",
     "Journal of Geophysical Research-Oceans", "129(5), e2023JC020785."),
    ("2021", "Sahoo, B., Mao, M.*, Xia, M.",
     "Projected changes of water currents and circulation in Lake Michigan under Representative Concentration Pathways scenarios",
     "Journal of Geophysical Research-Oceans", "126, e2020JC016651."),
    ("2020", "Mao, M., Xia, M.",
     "Particle dynamics in the nearshore of Lake Michigan revealed by an observation–modeling system",
     "Journal of Geophysical Research-Oceans", "125, e2019JC015765."),
    ("2020", "Mao, M., Xia, M.",
     "Monthly and episodic dynamics of summer circulation in Lake Michigan",
     "Journal of Geophysical Research-Oceans", "124, e2019JC015932."),
    ("2016", "Mao, M., van der Westhuysen, A.J., Xia, M., Schwab, D.J., Chawla, A.",
     "Modeling wind waves from deep to shallow waters in Lake Michigan using unstructured SWAN",
     "Journal of Geophysical Research-Oceans", "121, 3836-3865."),
    ("2023", "Mao, M., Xia, M.*",
     "Seasonal dynamics of water circulation and exchange flows in a shallow lagoon-inlet-coastal ocean system",
     "Ocean Modelling", "186, 102276."),
    ("2018", "Mao, M., Xia, M.",
     "Wave–current dynamics and interactions at the two inlets of a shallow coastal lagoon system under Hurricane conditions",
     "Ocean Modelling", "129, 124-144. (Most Cited Ocean Modelling Articles published since 2018, extracted from Scopus)"),
    ("2017", "Mao, M., Xia, M.",
     "Dynamics of wave–current–surge interactions in Lake Michigan: A model comparison",
     "Ocean Modelling", "110, 1-20. (Most Cited Ocean Modelling Articles published since 2017, extracted from Scopus)"),
    ("2020", "Xia, M., Mao, M., Niu, Q.",
     "Implementation and comparison of the recent three-dimensional radiation stress theory and vortex-force formalism in an unstructured-grid coastal circulation model",
     "Estuarine, Coastal and Shelf Science", "240, 106771."),
]

# ============================================================
# 六、团队成员（姓名, 职位, 研究方向, 邮箱, 照片文件名）
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
# 七、新闻数据
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
    {"date": "2026-06-03",
     "title": "烟台海岸带所在海浪有效波高智能预报领域取得新突破",
     "summary": "研究团队联合中国计量大学、浙江大学等单位，创新性提出一种融合自适应双层分解与"
                "双向长短期记忆网络－注意力机制的混合智能预测模型，"
                "在 1—6 小时短期预报时效内持续保持优异预测性能，"
                "为波浪能资源开发与海上航行安全保障提供了全新方案。相关成果发表于 Ocean Engineering。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202606/t20260603_8213540.html"},
    {"date": "2026-07-14",
     "title": "烟台海岸带所在温带半封闭海域台风－冷空气复合极端风浪响应机制取得新进展",
     "summary": '研究团队以 2019 年台风"利奇马"过境渤海、同步遭遇北下冷空气这一典型复合极端天气过程为案例，'
                "定量剖析了台风、冷空气两类风场对渤海波浪特征的差异化驱动作用，"
                "厘清了温带半封闭海域与开阔大洋在复合风场下波浪响应的本质差异。"
                "相关成果发表于 Journal of Geophysical Research: Oceans，第一作者为彭婕特别研究助理，通讯作者为毛淼华研究员。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202607/t20260714_8247248.html"},
    {"date": "2026-04-09",
     "title": "烟台海岸带所在渤海风暴潮概率预报研究领域取得新突破",
     "summary": "研究团队成功开发出一套适用于渤海地区的风暴潮概率深度学习框架，"
                "构建了融合 BiLSTM、自适应带宽核密度估计与序列前向选择方法的可解释混合建模体系，"
                "为风暴潮灾害风险评估与预警发布提供了高精度的可解释性概率预报新方案。",
     "source": "中国科学院烟台海岸带研究所",
     "url": "https://yic.cas.cn/xwzx/kydt/202604/t20260409_8183240.html"},
]

# ============================================================
# 八、页面基础设置
# ============================================================
st.set_page_config(
    page_title=f"{TEAM_NAME} | {INSTITUTE}",
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# 九、全局样式
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

/* ---------- 修复：Streamlit 的 markdown 容器默认 flex 会把内部元素挤到最小宽度，导致标题无法居中 ---------- */
[data-testid="stMarkdownContainer"] {{
    width: 100% !important;
    align-items: stretch !important;
}}

/* ---------- Hero（居中修复） ---------- */
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
}}
.card .cb b {{ color: #12657F; }}
.card .cb p {{ margin: 0 0 14px; }}
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
   ★ 成员卡片（横向：左照片 右信息）
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
.news-summary {{ font-size: 15.5px; color: #5A7086; line-height: 1.75; margin-bottom: 8px; }}
.news-source {{ font-size: 14px; color: #1D7874; }}

/* ---------- 论文条目 ---------- */
.pub {{
    background: #fff; border-left: 4px solid #1D7874; border-radius: 8px;
    padding: 16px 20px; margin-bottom: 12px;
    box-shadow: 0 2px 10px rgba(11,60,93,.06);
    font-size: 16.5px; color: #40566B; line-height: 1.85;
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
    .card .cb {{ font-size: 15px !important; line-height: 1.8 !important; }}

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

    .stat {{ padding: 16px 10px !important; }}
    .stat .num {{ font-size: 30px !important; }}
    .stat .lab {{ font-size: 13px !important; }}

    .proj {{ padding: 16px 16px !important; gap: 12px !important; }}
    .proj-num {{ width: 36px !important; height: 36px !important; font-size: 14px !important; }}
    .proj-title {{ font-size: 15px !important; }}
    .proj-tag   {{ font-size: 12.5px !important; padding: 4px 10px !important; }}

    .news-card {{ padding: 16px 18px !important; }}
    .news-title   {{ font-size: 16px !important; }}
    .news-summary {{ font-size: 14px !important; }}
    .news-date, .news-source {{ font-size: 12.5px !important; }}

    .pub {{ font-size: 14.5px !important; padding: 12px 14px !important; }}

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
# 十、渲染辅助
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
        html += (
            f'<div class="pub">'
            f'<span class="yr">[{year}]</span> '
            f'<b>{author}</b> {title}. '
            f'<i>{journal}</i>, {detail}'
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


def image_carousel(slides, height=440, interval=4500, show_caption=True):
    """
    通用图片轮播。
    slides:       [(图片URL, 标题, 描述), ...]
    height:       容器高度（像素）
    interval:     自动切换间隔（毫秒）
    show_caption: 是否显示图片上的标题和描述文字
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
    .carousel {{
        position: relative;
        width: 100%;
        max-width: 900px;
        aspect-ratio: 3 / 2;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 28px rgba(11,60,93,.18);
        background: #0B3C5D;
    }}
    .carousel-slide {{
        position: absolute;
        inset: 0;
        opacity: 0;
        transition: opacity .9s ease;
        pointer-events: none;
    }}
    .carousel-slide.active {{ opacity: 1; pointer-events: auto; }}
    .carousel-slide img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        transform: scale(1.02);
        transition: transform 6s ease;
    }}
    .carousel-slide.active img {{ transform: scale(1.08); }}
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
    </script>
    </body>
    </html>
    """
    components.html(html, height=620, scrolling=False)


# ============================================================
# 十一、各页面
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

    # ★ 首页：团队成员风采展示（从 R2 team/ 读取，3 秒切换，图片上无文字）
    show('<div class="sec-title">团队成员风采展示</div>')
    team_slides = [(url, "", "") for url in TEAM_PHOTOS]
    image_carousel(team_slides, interval=3000, show_caption=False)


def page_research():
    show('<div class="sec-title">研究方向</div>')
    show('<div style="color:#5A7086;font-size:16px;margin-bottom:20px;line-height:1.9;">'
         '课题组聚焦于近岸及河口动力过程的数值模拟与智能预报，主要研究方向包括：</div>')

    items = [
        (IMG_1, "🌊 近岸水动力模拟与观测",
         "结合现场观测与先进数值模式，揭示近岸波浪、潮汐及环流的多尺度变化规律。"),
        (IMG_2, "🤖 海洋动力过程智能预报",
         "融合深度学习、时空图神经网络等人工智能方法，开展海浪、风暴潮、潮位等海洋动力要素的"
         "智能建模与高精度预报研究。"),
        (IMG_3, "🌀 波流耦合模式改进与开发",
         "基于非结构网格模式 FVCOM，持续改进波流耦合方案，成功构建了包括渤海、黄河三角洲、"
         "马里兰海湾等多个海域的三维波流动力模式。"),
        (IMG_4, "🧭 拉格朗日粒子追踪与物质输运",
         "应用粒子追踪技术，模拟近岸污染物、沉积物及生物幼体的输运与扩散过程。"),
    ]

    for img, title, desc in items:
        grid_row(
            [img_card(img, "", ""), text_card(desc, title)],
            cols="1fr 1.4fr",
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

    # ★ 团队成员：电脑端 2 行 3 列；手机端 1 列
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
# 十二、入口
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
