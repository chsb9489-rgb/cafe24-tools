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
# 카테고리별 앱 카탈로그 데이터
# ──────────────────────────────────────────────
CATEGORIES = [
    {
        "name": "📦 주문·배송 관리",
        "tools": [
            {
                "icon": "🚚",
                "title": "카페24 송장 자동 매칭기",
                "repo": "cafe-invoice-matcher",
                "desc": "카페24 주문 목록과 택배사 출력 송장 데이터를 대조하여 출고 수량 불일치 및 송장 미발행 주문을 실시간 정제합니다.",
                "url": "https://cafe-invoice-matcher.streamlit.app/",
            },
            {
                "icon": "📦",
                "title": "주문-재고 연동 및 출고 가능 여부 체크기",
                "repo": "cafe24-stock-checker",
                "desc": "보유 재고 엑셀과 신규 주문 엑셀을 매칭하여 즉시 출고 가능한 주문과 재고 부족으로 인한 출고 대기 주문을 자동 분리합니다.",
                "url": "https://cafe24-stock-checker.streamlit.app/",
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
        ],
    },
    {
        "name": "📊 매출·정산 분석",
        "tools": [
            {
                "icon": "📊",
                "title": "주문 현황 및 매출 분석 대시보드",
                "repo": "cafe24-order-dashboard",
                "desc": "기간별 주문 엑셀을 시각화하여 일별/월별 매출 추이, 인기 상품 Top 10, 시간대별 주문 분포 분석 차트를 제공합니다.",
                "url": "https://cafe24-order-dashboard.streamlit.app/",
            },
            {
                "icon": "💰",
                "title": "상품별 원가 & 마진율 자동 계산기",
                "repo": "cafe24-margin-calculator",
                "desc": "쿠폰/적립금 할인액을 차감한 실결제액 기준으로 플랫폼 수수료, 택배비, 사입 원가를 감안한 실순이익을 산출합니다. (구버전, 실사용 중)",
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
                "icon": "💳",
                "title": "카페24 정산 내역 vs 실입금액 자동 대사기",
                "repo": "cafe24-settlement-reconciler",
                "desc": "카페24 정산 예정/완료 내역과 은행 입금 내역을 자동 대조하여 미입금 건, 정산 내역에 없는 입금 건을 찾아줍니다.",
                "url": "https://cafe24-settlement-reconciler.streamlit.app/",
            },
            {
                "icon": "🧾",
                "title": "매입·매출 엑셀 자동 정리기 (부가세 신고용)",
                "repo": "cafe24-vat-organizer",
                "desc": "매출/매입 엑셀을 분기별로 자동 집계하여 공급가액, 부가세액, 납부(환급)세액을 정리합니다.",
                "url": "https://cafe24-vat-organizer.streamlit.app/",
            },
        ],
    },
    {
        "name": "👥 고객 관리",
        "tools": [
            {
                "icon": "🎧",
                "title": "고객 CS 및 취소/반품/교환 데이터 통합 처리기",
                "repo": "cafe24-cs-manager",
                "desc": "카페24 CS 엑셀 내 취소, 반품, 교환 사유를 자동 분류하고 사유별 비중 통계 및 재발송 대상 목록을 추출합니다.",
                "url": "https://cafe24-cs-manager.streamlit.app/",
            },
            {
                "icon": "👥",
                "title": "재구매율 & 고객 등급(RFM) 분석기",
                "repo": "cafe24-rfm-analyzer",
                "desc": "고객별 최근 구매일·빈도·금액을 분석하여 VIP, 이탈 위험, 휴면 고객 등 세그먼트를 자동으로 분류합니다.",
                "url": "https://cafe24-rfm-analyzer.streamlit.app/",
            },
            {
                "icon": "💬",
                "title": "리뷰 자동 수집 & 감성/키워드 분석기",
                "repo": "cafe24-review-analyzer",
                "desc": "리뷰 엑셀을 분석하여 상품별 평점, 긍정/부정 비율, 자주 언급되는 키워드를 자동으로 정리합니다.",
                "url": "https://cafe24-review-analyzer.streamlit.app/",
            },
        ],
    },
    {
        "name": "⏰ 재고 관리",
        "tools": [
            {
                "icon": "⏰",
                "title": "재고 소진 예측 & 자동 발주 알림 타이머",
                "repo": "cafe24-stock-timer",
                "desc": "최근 판매 속도를 기반으로 품절 임박 D-Day를 예측하고, 목표 안전재고 기준 부족 수량을 계산하여 자동 발주서를 생성합니다.",
                "url": "https://cafe24-stock-timer.streamlit.app/",
            },
            {
                "icon": "📉",
                "title": "데드스톡(장기 미판매 재고) 탐지기",
                "repo": "cafe24-deadstock-detector",
                "desc": "재고와 판매 이력을 대조하여 오랫동안 팔리지 않은 악성 재고와, 그로 인해 묶인 자금 규모를 찾아줍니다.",
                "url": "https://cafe24-deadstock-detector.streamlit.app/",
            },
        ],
    },
    {
        "name": "🏷️ 상품 관리",
        "tools": [
            {
                "icon": "📊",
                "title": "상품별 묶음 & 옵션 판매 비중 분석기",
                "repo": "cafe24-option-analyzer",
                "desc": "카페24의 복잡한 텍스트형 옵션 데이터를 정제하여 인기 옵션 조합 TOP 20 및 단품 옵션별 판매 점유율(%)을 차트로 제공합니다.",
                "url": "https://cafe24-option-analyzer.streamlit.app/",
            },
            {
                "icon": "🏪",
                "title": "카페24 상품 대량 등록/수정기",
                "repo": "cafe24-product-bulk-uploader",
                "desc": "카페24 공식 엑셀 양식에 내 상품 데이터를 자동 매핑하여 채워주는 대량 등록/수정 보조 도구입니다.",
                "url": "https://cafe24-product-bulk-uploader.streamlit.app/",
            },
        ],
    },
    {
        "name": "🔄 데이터 변환",
        "tools": [
            {
                "icon": "🔄",
                "title": "타 플랫폼 ↔ 카페24 주문 서식 통합 변환기",
                "repo": "cafe24-format-converter",
                "desc": "스마트스토어, 쿠팡 등 채널별 주문 엑셀의 열 구조와 주소 포맷을 카페24 업로드용 표준 양식으로 일괄 자동 변환합니다.",
                "url": "https://cafe24-format-converter.streamlit.app/",
            },
            {
                "icon": "🔀",
                "title": "타 플랫폼 ↔ 카페24 주문 서식 변환기 (구버전)",
                "repo": "cafe24-order-converter",
                "desc": "스마트스토어, 쿠팡 등 채널별 주문 엑셀을 카페24 업로드용 표준 양식으로 변환하는 초기 버전입니다.",
                "url": "https://cafe24-order-converter.streamlit.app/",
            },
        ],
    },
    {
        "name": "💰 가격·배송 전략",
        "tools": [
            {
                "icon": "🚛",
                "title": "배송비 정책 시뮬레이터",
                "repo": "cafe24-shipping-simulator",
                "desc": "무료배송 기준 금액을 바꿨을 때 회사가 부담하는 배송비와 마진에 미치는 영향을 미리 계산합니다.",
                "url": "https://cafe24-shipping-simulator.streamlit.app/",
            },
            {
                "icon": "🏷️",
                "title": "경쟁사 가격 모니터링 알리미",
                "repo": "cafe24-price-monitor",
                "desc": "우리 가격과 경쟁사 가격을 비교하여 가격 경쟁력이 열세/우위인 상품을 자동으로 찾아줍니다.",
                "url": "https://cafe24-price-monitor.streamlit.app/",
            },
        ],
    },
]

ALL_TOOLS = [tool for cat in CATEGORIES for tool in cat["tools"]]

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
    .category-title {
        margin-top: 8px;
        margin-bottom: 4px;
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
    "기반으로 구축된 자동화 및 분석 웹 애플리케이션 포트폴리오입니다. "
    f"현재 총 **{len(ALL_TOOLS)}개**의 도구가 운영 중입니다."
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
# 검색 / 카테고리 필터
# ──────────────────────────────────────────────
col_search, col_filter = st.columns([2, 1])
with col_search:
    query = st.text_input("🔍 도구 검색", placeholder="예: 송장, 재고, 마진 ...")
with col_filter:
    category_names = ["전체"] + [c["name"] for c in CATEGORIES]
    selected_category = st.selectbox("카테고리 필터", category_names)

# ──────────────────────────────────────────────
# 카테고리별 카드 렌더링
# ──────────────────────────────────────────────
cols_per_row = 3
total_shown = 0

for cat in CATEGORIES:
    if selected_category != "전체" and cat["name"] != selected_category:
        continue

    filtered_tools = [
        t for t in cat["tools"]
        if query.strip() == "" or query.strip() in t["title"] or query.strip() in t["desc"]
    ]
    if not filtered_tools:
        continue

    st.markdown(f"### {cat['name']} <span style='color:#7d8298;font-size:0.9rem;'>({len(filtered_tools)})</span>", unsafe_allow_html=True)

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
                total_shown += 1

    st.markdown("")  # 카테고리 간 여백

if total_shown == 0:
    st.info("검색 조건에 맞는 도구가 없습니다.")

st.divider()
st.caption("© Cafe24 E-Commerce Automation Tool Suite · GitHub 저장소별 소스 코드 관리")
