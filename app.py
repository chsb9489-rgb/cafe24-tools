import streamlit as st

# ──────────────────────────────────────────────
# 페이지 기본 설정
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Cafe24 E-Commerce Automation Tool Suite",
    page_icon="🛒",
    layout="wide",
)

# ──────────────────────────────────────────────
# 앱 카탈로그 데이터
# ──────────────────────────────────────────────
TOOLS = [
    {
        "icon": "🚚",
        "title": "카페24 송장 자동 매칭기",
        "repo": "cafe24-invoice-checker",
        "desc": "카페24 주문 목록과 택배사 출력 송장 데이터를 대조하여 출고 수량 불일치 및 송장 미발행 주문을 실시간 정제합니다.",
        "url": "https://cafe24-invoice-checker.streamlit.app/",
    },
    {
        "icon": "📦",
        "title": "주문-재고 연동 및 출고 가능 여부 체크기",
        "repo": "cafe24-stock-checker",
        "desc": "보유 재고 엑셀과 신규 주문 엑셀을 매칭하여 즉시 출고 가능한 주문과 재고 부족으로 인한 출고 대기 주문을 자동 분리합니다.",
        "url": "https://cafe24-stock-checker.streamlit.app/",
    },
    {
        "icon": "📊",
        "title": "주문 현황 및 매출 분석 대시보드",
        "repo": "cafe24-order-dashboard",
        "desc": "기간별 주문 엑셀을 시각화하여 일별/월별 매출 추이, 인기 상품 Top 10, 시간대별 주문 분포 분석 차트를 제공합니다.",
        "url": "https://cafe24-order-dashboard.streamlit.app/",
    },
    {
        "icon": "🎧",
        "title": "고객 CS 및 취소/반품/교환 데이터 통합 처리기",
        "repo": "cafe24-cs-manager",
        "desc": "카페24 CS 엑셀 내 취소, 반품, 교환 사유를 자동 분류하고 사유별 비중 통계 및 재발송 대상 목록을 추출합니다.",
        "url": "https://cafe24-cs-manager.streamlit.app/",
    },
    {
        "icon": "💰",
        "title": "상품별 원가 & 마진율 자동 계산기",
        "repo": "cafe24-margin-calculator",
        "desc": "쿠폰/적립금 할인액을 차감한 실결제액 기준으로 플랫폼 수수료, 택배비, 사입 원가를 감안한 실순이익을 산출합니다.",
        "url": "https://cafe24-margin-calculator.streamlit.app/",
    },
    {
        "icon": "💎",
        "title": "상품별 원가 & 마진율 정밀 계산기 (v2)",
        "repo": "cafe24-margin-calculator-ver2",
        "desc": "실결제액 기준 실순이익 산출 로직을 고도화하여 저마진/적자 상품을 자동 감지하는 개선 버전입니다.",
        "url": "https://cafe24-margin-calculator-ver2.streamlit.app/",
    },
    {
        "icon": "⏰",
        "title": "재고 소진 예측 & 자동 발주 알림 타이머",
        "repo": "cafe24-stock-timer",
        "desc": "최근 판매 속도를 기반으로 품절 임박 D-Day를 예측하고, 목표 안전재고 기준 부족 수량을 계산하여 자동 발주서를 생성합니다.",
        "url": "https://cafe24-stock-timer.streamlit.app/",
    },
    {
        "icon": "🔄",
        "title": "타 플랫폼 ↔ 카페24 주문 서식 통합 변환기",
        "repo": "cafe24-format-converter",
        "desc": "스마트스토어, 쿠팡 등 채널별 주문 엑셀의 열 구조와 주소 포맷을 카페24 업로드용 표준 양식으로 일괄 자동 변환합니다.",
        "url": "https://cafe24-format-converter.streamlit.app/",
    },
    {
        "icon": "📦",
        "title": "카페24 합배송 / 분할배송 자동 판정기",
        "repo": "cafe24-shipment-bundler",
        "desc": "동일 수령인/주소지의 중복 주문(합배송)을 그룹화하여 배송비를 절감하고, 박스당 최대 수량 초과 주문(분할배송)을 판정합니다.",
        "url": "https://cafe24-shipment-bundler.streamlit.app/",
    },
    {
        "icon": "🏷️",
        "title": "운송장 엑셀 출고 검수기 (바코드 검수 보조)",
        "repo": "cafe24-invoice-inspector",
        "desc": "원본 주문 내역과 택배사 출고/운송장 엑셀을 교차 대조하여 출고 누락(미발송) 주문 및 수량 불일치를 정밀 검수합니다.",
        "url": "https://cafe24-invoice-inspector.streamlit.app/",
    },
    {
        "icon": "📊",
        "title": "상품별 묶음 & 옵션 판매 비중 분석기",
        "repo": "cafe24-option-analyzer",
        "desc": "카페24의 복잡한 텍스트형 옵션 데이터를 정제하여 인기 옵션 조합 TOP 20 및 단품 옵션별 판매 점유율(%)을 차트로 제공합니다.",
        "url": "https://cafe24-option-analyzer.streamlit.app/",
    },
]

# ──────────────────────────────────────────────
# 스타일 (카드형 레이아웃)
# ──────────────────────────────────────────────
st.markdown(
    """
    <style>
    .tool-card {
        background-color: #1e2130;
        border: 1px solid #313548;
        border-radius: 12px;
        padding: 20px 22px;
        margin-bottom: 16px;
        height: 100%;
    }
    .tool-card h4 {
        margin: 0 0 8px 0;
        font-size: 1.05rem;
    }
    .tool-card p {
        color: #b5b9c9;
        font-size: 0.88rem;
        line-height: 1.5;
        min-height: 72px;
    }
    .tool-repo {
        color: #7d8298;
        font-size: 0.78rem;
        font-family: monospace;
        margin-bottom: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────
# 헤더
# ──────────────────────────────────────────────
st.title("🛒 Cafe24 E-Commerce Automation Tool Suite")
st.markdown(
    "카페24 쇼핑몰 운영 효율을 극대화하기 위해 **Python · Streamlit · Pandas · OpenPyXL** "
    "기반으로 구축된 자동화 및 분석 웹 애플리케이션 포트폴리오입니다."
)

with st.expander("🛠️ 공통 기술 스택 (Tech Stack)"):
    st.markdown(
        """
        - **Language**: Python
        - **Web Framework**: Streamlit
        - **Data Processing**: Pandas, OpenPyXL
        - **Deployment**: GitHub, Streamlit Cloud
        """
    )

st.divider()

# ──────────────────────────────────────────────
# 검색 / 필터
# ──────────────────────────────────────────────
query = st.text_input("🔍 도구 검색", placeholder="예: 송장, 재고, 마진 ...")

filtered_tools = [
    t for t in TOOLS
    if query.strip() == "" or query.strip() in t["title"] or query.strip() in t["desc"]
]

st.caption(f"총 {len(filtered_tools)}개 도구")

# ──────────────────────────────────────────────
# 카드 그리드 (3열)
# ──────────────────────────────────────────────
cols_per_row = 3
for i in range(0, len(filtered_tools), cols_per_row):
    row_tools = filtered_tools[i : i + cols_per_row]
    cols = st.columns(cols_per_row)
    for col, tool in zip(cols, row_tools):
        with col:
            st.markdown(
                f"""
                <div class="tool-card">
                    <h4>{tool['icon']} {tool['title']}</h4>
                    <div class="tool-repo">{tool['repo']}</div>
                    <p>{tool['desc']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.link_button("앱 바로가기 →", tool["url"], use_container_width=True)

st.divider()
st.caption("© Cafe24 E-Commerce Automation Tool Suite · GitHub 저장소별 소스 코드 관리")
