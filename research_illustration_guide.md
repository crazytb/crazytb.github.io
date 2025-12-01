# Research Illustration Guide
## "Intelligent Resource Orchestration for Next-Generation Networks"

---

## Step 1: draw.io로 기본 구조 만들기

### 1.1 draw.io 시작하기

1. 브라우저에서 https://app.diagrams.net 접속
2. **Create New Diagram** 클릭
3. **Blank Diagram** 선택 → 파일명: `research_architecture.drawio`
4. **Create** 클릭

### 1.2 캔버스 설정

1. 우측 **Format Panel**에서:
   - Page Setup → A4 Landscape
   - Background: White (#FFFFFF)
   - Grid: 10px

### 1.3 아이콘 라이브러리 추가

1. 좌측 패널 하단 **More Shapes** 클릭
2. 다음 항목 체크:
   - ✅ **Networking** → Cisco, AWS
   - ✅ **General** → Icons
   - ✅ **Arrows**
   - ✅ **Containers**
3. **Apply** 클릭

---

## Step 2: 상단 제목 영역 만들기

### 2.1 메인 타이틀 박스

1. 좌측에서 **Rectangle** 드래그
2. 속성 설정:
   - Width: 800px, Height: 80px
   - Fill color: #2E5090 (진한 파랑)
   - Line color: None
   - Text color: White (#FFFFFF)
3. 더블클릭하여 텍스트 입력:
   ```
   Intelligent Resource Orchestration
   for Next-Generation Networks
   ```
4. 폰트 설정:
   - Font: Arial Bold
   - Size: 20pt (첫 줄), 16pt (둘째 줄)
   - Align: Center

---

## Step 3: 3개 연구 축 카드 만들기

### 3.1 첫 번째 카드 (Protocol Optimization)

1. **Rectangle** 드래그
2. 속성:
   - Width: 240px, Height: 180px
   - Fill: #E3F2FD (연한 파랑)
   - Stroke: #2E5090 (진한 파랑), 2px
   - Rounded corners: 10px
3. 텍스트 입력:
   ```
   Protocol Optimization

   • MAC Layer Design
   • Multi-link Coordination
   • Dense WLAN Resource Allocation
   • OFDMA/MU-MIMO
   ```
4. 폰트:
   - Title: Arial Bold 14pt
   - Bullets: Arial 11pt

### 3.2 두 번째 카드 (Timely Information Delivery)

1. 첫 번째 카드 복사 (Ctrl+C, Ctrl+V)
2. 우측으로 이동 (20px 간격)
3. 속성 변경:
   - Fill: #E0F2F1 (연한 청록)
   - Stroke: #00A9A5 (청록)
4. 텍스트 변경:
   ```
   Timely Information Delivery

   • Age of Information (AoI)
   • Vehicular Content Caching
   • IoT Network Optimization
   • Priority-aware Actuation
   ```

### 3.3 세 번째 카드 (Edge Intelligence)

1. 두 번째 카드 복사
2. 우측으로 이동
3. 속성 변경:
   - Fill: #FFF3E0 (연한 주황)
   - Stroke: #F57C00 (주황)
4. 텍스트 변경:
   ```
   Edge Intelligence

   • Task Offloading (Deep RL)
   • Serverless Edge Computing
   • UAV-assisted MEC
   • Container Orchestration
   ```

---

## Step 4: Cloud Layer (상위 계층)

### 4.1 Cloud 영역 컨테이너

1. **Rectangle** 드래그
2. 속성:
   - Width: 800px, Height: 150px
   - Fill: Linear gradient (#2E5090 → #5E7FC0)
   - Stroke: #2E5090, 2px
   - Rounded: 5px
3. 레이블 추가 (좌상단):
   ```
   ☁️ CLOUD LAYER - Intelligent Resource Management
   ```

### 4.2 Cloud 서버 아이콘들

1. 좌측 패널에서 **Cisco** 또는 **AWS** 카테고리 선택
2. **Server** 아이콘 4개 드래그하여 Cloud 영역에 배치
3. 서버 간 연결:
   - **Arrow** 도구로 양방향 화살표 연결
   - Arrow style: Bidirectional
   - Color: White (#FFFFFF)

### 4.3 기능 레이블

Cloud 영역 하단에 텍스트 박스 추가:
```
• Container Orchestration  • Deep RL Decision  • Serverless Functions
```

---

## Step 5: Edge Layer (중간 계층)

### 5.1 Edge 영역 컨테이너

1. **Rectangle** 드래그
2. 속성:
   - Width: 800px, Height: 180px
   - Fill: Linear gradient (#00A9A5 → #4DB6AC)
   - Stroke: #00A9A5, 2px
3. 레이블:
   ```
   📡 EDGE LAYER - Network & Computing Optimization
   ```

### 5.2 Edge 디바이스 아이콘

다음 아이콘들을 배치:
- **Base Station** (통신 타워 아이콘)
- **UAV/Drone** (드론 아이콘)
- **Edge Server** (작은 서버 아이콘)
- **WiFi AP** (무선 공유기 아이콘)
- **Femtocell** (소형 기지국 아이콘)

아이콘 배치 레이아웃:
```
[Base Station] ←→ [UAV] ←→ [Edge Server] ←→ [WiFi AP]
                     ↕
              [Femtocell] ←→ [Router]
```

### 5.3 Edge 기능 레이블

```
• MEC Task Offloading  • Multi-link MAC  • Content Caching  • AoI Optimization
```

---

## Step 6: Device Layer (하위 계층)

### 6.1 Device 영역 컨테이너

1. **Rectangle** 드래그
2. 속성:
   - Width: 800px, Height: 150px
   - Fill: Linear gradient (#F57C00 → #FFB74D)
   - Stroke: #F57C00, 2px
3. 레이블:
   ```
   📱 DEVICE LAYER - Heterogeneous End Devices
   ```

### 6.2 Device 아이콘

다음 아이콘들을 배치:
- **Smartphone** 📱
- **Vehicle** 🚗
- **IoT Sensor** 📟
- **Smart Home** 🏠
- **Industrial Robot** 🤖
- **Wearable** ⌚

레이아웃:
```
[Smartphone]  [Vehicle]  [IoT Sensor]  [Smart Home]  [Robot]  [Wearable]
      ↕           ↕           ↕            ↕          ↕         ↕
         (Wireless Communication - 점선으로 Edge Layer와 연결)
```

### 6.3 Device 기능 레이블

```
• Low-power Communication  • AoI-aware Transmission  • Energy Efficiency
```

---

## Step 7: 계층 간 연결

### 7.1 Control & Data Plane

1. Cloud와 Edge 사이에 큰 **양방향 화살표** 추가
2. 화살표 옆 텍스트:
   ```
   Control & Data Plane
   (Orchestration Commands ↓ / Status Reports ↑)
   ```

### 7.2 Wireless Communication

1. Edge와 Device 사이에 **점선 양방향 화살표**
2. 텍스트:
   ```
   Wireless Communication
   (5G/WiFi/IoT Protocols)
   ```

### 7.3 3개 연구 축 → 계층 연결

각 연구 축 카드에서 해당 계층으로 화살표:
- Protocol Optimization → Edge Layer + Device Layer
- Timely Information → Edge Layer + Device Layer
- Edge Intelligence → Cloud Layer + Edge Layer

---

## Step 8: 하단 Publication 강조

### 8.1 Publication 뱃지

1. 3개 **Rounded Rectangle** (약간 작게)
2. 속성:
   - Width: 150px, Height: 60px
   - Fill: #FFD700 (골드)
   - Stroke: #FFA000
3. 텍스트:
   ```
   IEEE TVT
   (3 papers)
   ```
   ```
   IEEE IoT Journal
   (2 papers)
   ```
   ```
   FGCS
   (1 paper)
   ```

---

## Step 9: 색상 팔레트 통일

### 전체 색상 가이드

```css
/* Primary Colors */
Cloud Layer:    #2E5090 (진한 파랑)
Edge Layer:     #00A9A5 (청록)
Device Layer:   #F57C00 (주황)

/* Accent Colors */
Highlights:     #FFD700 (골드)
Text:           #333333 (다크 그레이)
Background:     #FFFFFF (화이트)

/* Gradients */
Cloud:  #2E5090 → #5E7FC0
Edge:   #00A9A5 → #4DB6AC
Device: #F57C00 → #FFB74D
```

---

## Step 10: Export 설정

### 10.1 고해상도 PNG 내보내기

1. **File → Export as → PNG**
2. 설정:
   - **Zoom**: 300% (고해상도)
   - **DPI**: 300
   - **Transparent Background**: 체크 해제 (흰색 배경)
   - **Border Width**: 10px
3. **Export** 클릭
4. 파일명: `research_architecture_300dpi.png`

### 10.2 SVG 내보내기 (편집용)

1. **File → Export as → SVG**
2. 설정:
   - **Text Settings**: Convert labels to SVG
3. **Export** 클릭
4. 파일명: `research_architecture.svg`

---

## PowerPoint 통합 (Step 11)

### 11.1 PowerPoint에서 최종 다듬기

1. PowerPoint 새 슬라이드 (레이아웃: 빈 화면)
2. **삽입 → 그림** → 위에서 만든 PNG 파일 선택
3. 이미지 크기 조정 (슬라이드 80% 채우기)

### 11.2 애니메이션 추가 (선택사항)

**발표용 애니메이션:**

1. 3개 연구 축 카드 선택
   - **애니메이션 → 나타내기 → 와이프**
   - 시차: 0.3초

2. Cloud → Edge → Device 순서대로
   - **애니메이션 → 나타내기 → 페이드**
   - 시차: 0.5초

3. 화살표 연결선
   - **애니메이션 → 나타내기 → 그리기**
   - 방향: 상단에서

### 11.3 텍스트 오버레이 추가

이미지 위에 텍스트 박스 추가:

**좌측 상단:**
```
Research Evolution
2011-2025
```

**우측 하단:**
```
20+ Journal Papers
10+ Conference Papers
```

---

## 추가 팁

### 아이콘 찾기 어려울 때

**대체 방법:**
1. **FontAwesome 이모지 사용**
   - 서버: 🖥️
   - 클라우드: ☁️
   - 모바일: 📱
   - 차량: 🚗
   - WiFi: 📶
   - 로봇: 🤖

2. **Flaticon.com에서 다운로드**
   - 무료 아이콘 검색
   - SVG 형식 다운로드
   - draw.io에 **File → Import** → SVG 파일 선택

### 레이아웃 정렬

1. 여러 객체 선택 (Shift + 클릭)
2. **Arrange → Align → Align Center**
3. **Arrange → Distribute → Horizontally**

### 템플릿 저장

완성 후:
1. **File → Save As Template**
2. 향후 유사한 그림 제작 시 재사용

---

## 완성된 일러스트 사용 시나리오

### 교수 임용 발표

**Slide 1: 연구 개요**
- 이 일러스트를 전체 화면으로
- "제 연구는 3개 계층을 아우르는 통합적 접근입니다"

**Slide 2-4: 각 연구 축 설명**
- Protocol Optimization만 하이라이트
- Timely Information만 하이라이트
- Edge Intelligence만 하이라이트

**Slide 5: 연구 비전**
- 전체 일러스트 + 향후 연구 방향 오버레이

---

## 예상 소요 시간

- **draw.io 작업**: 40-60분
- **PowerPoint 통합**: 10-15분
- **애니메이션 추가**: 10분
- **총 소요 시간**: 약 1-1.5시간

---

## 문제 해결 (Troubleshooting)

### Q: 아이콘이 너무 작아요
A: 아이콘 선택 → **Format → Size** → Width/Height 150% 증가

### Q: 색상이 인쇄 시 다르게 나와요
A: RGB 대신 CMYK 모드 사용, 또는 색상 밝기 10% 증가

### Q: 텍스트가 흐릿해요
A: Export 시 DPI를 300 이상으로 설정, SVG 형식도 함께 저장

### Q: 레이아웃이 복잡해 보여요
A: 여백 늘리기, 아이콘 개수 줄이기, 색상 통일

---

## 다음 단계

1. ✅ draw.io에서 기본 구조 완성
2. ✅ PowerPoint에 통합
3. ✅ 동료/지도교수에게 피드백 요청
4. ✅ 최종 수정 후 발표 자료에 삽입

---

**Good luck with your faculty interview!**
**교수 임용 면접 응원합니다!** 🎓
