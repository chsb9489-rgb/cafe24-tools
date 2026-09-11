# 🛒 Cafe24 E-Commerce Automation Tool Suite

카페24 쇼핑몰 운영 효율을 극대화하기 위해 **Python, Streamlit, Pandas, OpenPyXL** 기반으로
구축된 자동화 및 분석 웹 애플리케이션 포트폴리오입니다.

이 저장소(`cafe24-tools`)는 각 도구로 이동할 수 있는 **통합 허브 페이지**이며,
실제 각 도구는 개별 저장소에서 별도로 관리·배포됩니다.

---

## 🛠️ 공통 기술 스택 (Tech Stack)

* **Language**: Python
* **Web Framework**: Streamlit
* **Data Processing**: Pandas, OpenPyXL
* **Deployment**: GitHub, Streamlit Cloud

---

## 🚀 도구 카탈로그 (총 19종)

### 📦 주문·배송 관리

| 도구 | Repo | 주요 기능 |
|---|---|---|
| 🚚 카페24 송장 자동 매칭기 | `cafe-invoice-matcher` | 주문 목록과 택배사 송장 데이터를 대조하여 수량 불일치·송장 미발행 주문을 정제 |
| 📦 주문-재고 연동 및 출고 가능 여부 체크기 | `cafe24-stock-checker` | 재고와 신규 주문을 매칭해 즉시 출고 가능 주문과 출고 대기 주문을 자동 분리 |
| 📦 합배송 / 분할배송 자동 판정기 | `cafe24-shipment-bundler` | 동일 수령인 주문을 그룹화해 합배송 판정, 박스당 최대 수량 초과 시 분할배송 판정 |
| 🏷️ 운송장 엑셀 출고 검수기 | `cafe24-invoice-inspector` | 주문 내역과 출고/운송장 엑셀을 교차 대조해 출고 누락·수량 불일치 검수 |

### 📊 매출·정산 분석

| 도구 | Repo | 주요 기능 |
|---|---|---|
| 📊 주문 현황 및 매출 분석 대시보드 | `cafe24-order-dashboard` | 일별/월별 매출 추이, 인기 상품 Top 10, 시간대별 주문 분포 시각화 |
| 💰 상품별 원가 & 마진율 자동 계산기 | `cafe24-margin-calculator` | 실결제액 기준 실순이익 산출 (구버전, 실사용 중) |
| 💎 상품별 원가 & 마진율 정밀 계산기 (v2) | `cafe24-margin-calculator-ver2` | 저마진/적자 상품 자동 감지 기능이 추가된 개선 버전 |
| 💳 정산 내역 vs 실입금액 자동 대사기 | `cafe24-settlement-reconciler` | 정산 예정/완료 내역과 은행 입금 내역을 자동 대조 |
| 🧾 매입·매출 엑셀 자동 정리기 (부가세 신고용) | `cafe24-vat-organizer` | 분기별 매출·매입세액 집계 및 납부(환급)세액 자동 산출 |

### 👥 고객 관리

| 도구 | Repo | 주요 기능 |
|---|---|---|
| 🎧 고객 CS 및 취소/반품/교환 데이터 통합 처리기 | `cafe24-cs-manager` | CS 엑셀 내 사유 자동 분류, 비중 통계 및 재발송 대상 추출 |
| 👥 재구매율 & 고객 등급(RFM) 분석기 | `cafe24-rfm-analyzer` | 고객별 R·F·M 분석으로 VIP/이탈위험/휴면 등 세그먼트 자동 분류 |
| 💬 리뷰 자동 수집 & 감성/키워드 분석기 | `cafe24-review-analyzer` | 리뷰 평점 기반 감성 분류, 자주 언급되는 키워드 추출 |

### ⏰ 재고 관리

| 도구 | Repo | 주요 기능 |
|---|---|---|
| ⏰ 재고 소진 예측 & 자동 발주 알림 타이머 | `cafe24-stock-timer` | 판매 속도 기반 품절 임박 D-Day 예측 및 자동 발주서 생성 |
| 📉 데드스톡(장기 미판매 재고) 탐지기 | `cafe24-deadstock-detector` | 오랫동안 팔리지 않은 악성 재고와 묶인 자금 규모를 탐지 |

### 🏷️ 상품 관리

| 도구 | Repo | 주요 기능 |
|---|---|---|
| 📊 상품별 묶음 & 옵션 판매 비중 분석기 | `cafe24-option-analyzer` | 텍스트형 옵션 데이터를 정제해 인기 옵션 조합 및 판매 점유율 분석 |
| 🏪 카페24 상품 대량 등록/수정기 | `cafe24-product-bulk-uploader` | 카페24 정품 엑셀 양식에 상품 데이터를 자동 매핑하여 대량 등록 지원 |

### 🔄 데이터 변환

| 도구 | Repo | 주요 기능 |
|---|---|---|
| 🔄 타 플랫폼 ↔ 카페24 주문 서식 통합 변환기 | `cafe24-format-converter` | 스마트스토어, 쿠팡 등 채널별 주문 엑셀을 카페24 표준 양식으로 변환 |

### 💰 가격·배송 전략

| 도구 | Repo | 주요 기능 |
|---|---|---|
| 🚛 배송비 정책 시뮬레이터 | `cafe24-shipping-simulator` | 무료배송 기준금액 변경 시 배송비 부담과 마진 영향을 시뮬레이션 |
| 🏷️ 경쟁사 가격 모니터링 알리미 | `cafe24-price-monitor` | 우리 가격과 경쟁사 가격을 비교해 가격 경쟁력 열세/우위 상품 파악 |

---

## 💻 허브 페이지 로컬 실행 방법

```bash
git clone https://github.com/[사용자계정]/cafe24-tools.git
cd cafe24-tools
pip install -r requirements.txt
streamlit run app.py
```

허브 페이지에서 각 카드의 **"앱 바로가기"** 버튼을 누르면 개별 도구의 배포된 페이지로 이동합니다.

---

## 📌 참고

* 각 도구는 독립된 저장소에서 관리되며, 이 허브는 링크 모음 및 진입점 역할만 합니다.
* 도구가 추가되거나 URL이 변경되면 `app.py` 내 `CATEGORIES` 목록만 수정하면 자동으로 반영됩니다.
