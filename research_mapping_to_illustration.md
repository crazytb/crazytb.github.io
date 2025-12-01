# Research Papers Mapping to Architecture Illustration

## 일러스트 구조 분석

박사님의 일러스트는 3개 계층으로 구성:
1. **Cloud Layer** - Intelligent Resource Management
2. **Edge Layer** - Edge Computing & Network Optimization
3. **Device Layer** - Heterogeneous Devices & Services

---

## 📍 논문 매핑 (Layer별)

### ☁️ **CLOUD LAYER - Intelligent Resource Management**

#### 위치: 상단 클라우드 서버들 + 컨테이너 아이콘

**핵심 논문 (5편):**

1. **Neighbor-Aware Shared Container Instance Warming (FGCS 2025/2026)** ⭐
   - 위치: 우측 컨테이너 아이콘
   - 설명: Serverless edge computing, container orchestration
   - 강조: 가장 최신 top-tier 논문

2. **DRQN-based Task Offloading in UAV-MEC (ICTC 2024)**
   - 위치: 클라우드 서버 클러스터
   - 설명: Deep RL 기반 의사결정, partial observability

3. **Opportunistic Task Offloading with Deep RL (ICTC 2023)**
   - 위치: 클라우드 서버 클러스터
   - 설명: DQN 기반 MEC 오프로딩

4. **Cost-efficient NF Deployment in NPNs (ICTC 2023)**
   - 위치: 클라우드 서버 클러스터
   - 설명: 5G network function deployment, Markov decision process

5. **Adaptive Client Training Scale for Federated Learning (ICTC 2023)**
   - 위치: 클라우드 서버 간 연결선
   - 설명: Distributed learning, adaptive scaling

**시각적 표현:**
- 클라우드 아이콘 근처에 "Deep RL", "Container Warming", "Serverless" 키워드 배치
- 우측 컨테이너 아이콘에 **FGCS 2025** 뱃지 추가

---

### 📡 **EDGE LAYER - Edge Computing & Network Optimization**

#### 위치: 중앙 기지국 + WiFi + 체인 아이콘 + 번개

이 계층이 가장 많은 논문 포함 (약 15편)

#### **A. Multi-Link & MAC Protocol (6편)**

**위치: WiFi/체인 아이콘 영역**

1. **HARE: Hybrid ARQ for Multi-Link (IEEE TVT 2023)** ⭐
   - 설명: Adaptive retransmission, 802.11be multi-link
   - 키워드: "Multi-Link MAC"

2. **Multi-Link MAC Performance Analysis (Applied Sciences 2021)**
   - 설명: Synchronous multi-radio multi-link

3. **MU-MIMO+OFDMA MAC Protocol (ICT Express 2020)**
   - 설명: 802.11ax uplink optimization

4. **Full Duplex WLANs VoIP Capacity (IEEE TVT 2017)**
   - 설명: Self-interference cancellation

5. **Adaptive Resource Allocation in Dense WLANs (IEEE TVT 2018)** ⭐
   - 설명: Game-theoretic approach
   - 키워드: "Dense WLAN"

6. **Phase-Divided MAC for MU-MIMO (IEEE TVT 2018)**
   - 설명: Integrated uplink/downlink

**추가 관련 논문:**
- RA-PSM: Rate-aware Power Saving (Wireless Networks 2016)
- Utility-Based Resource Allocation in 802.11ax (Book Chapter 2022)
- Channel Bonding for Dense WLAN (ICOIN 2016)
- Two-phase Resource Allocation for OFDMA (ICTC 2016)

**시각적 표현:**
- 체인 아이콘 근처: "802.11be/ax", "Multi-Link", "OFDMA/MU-MIMO"
- IEEE TVT 뱃지 (3편)

---

#### **B. IoT & Network Routing (5편)**

**위치: 기지국 + IoT 연결 영역**

1. **Deep-RL-Based AoI-Aware AQM for IoT (IEEE IoT Journal 2024)** ⭐
   - 위치: 기지국 → Device 연결선
   - 설명: Age of Information, queue management
   - 키워드: "AoI-aware", "Low-Power"

2. **Priority-Aware Actuation in Industrial Networks (Sensors 2024)**
   - 위치: 기지국 영역
   - 설명: Heterogeneous industrial IoT

3. **Multi-criteria Routing for 6G IoT (Wireless Networks 2024)**
   - 위치: 기지국 중앙
   - 설명: Multi-objective decision making

4. **Improved D2D Routing in B5G (Electronics 2022)**
   - 위치: 디바이스 간 점선 연결
   - 설명: QoS enhancement

5. **Performance Analysis of IoT with Wake-Up Radio (Sensors 2019)**
   - 위치: 기지국 → IoT sensor 연결
   - 설명: Low-power addressing

**시각적 표현:**
- 기지국 근처: "AoI", "Industrial IoT", "6G"
- IEEE IoT Journal 뱃지

---

#### **C. Vehicular Networks (3편)**

**위치: 기지국 ↔ 차량 아이콘 연결**

1. **Opportunistic Offloading with Electro-mobility (IET ITS 2024)**
   - 위치: 차량 아이콘
   - 설명: EV charging infrastructure 활용
   - 키워드: "EV Network"

2. **CSV: Content Service with Vehicular Caching (Sensors 2022)**
   - 위치: 차량 아이콘
   - 설명: Mobile content delivery

3. **Energy Efficient Message in Platoon Systems (Energies 2020)**
   - 위치: 차량 아이콘 (여러 대)
   - 설명: Cooperative driving

**시각적 표현:**
- 차량 아이콘 근처: "V2X", "Vehicular Caching", "Platoon"

---

#### **D. Sensor & AI Application (1편)**

**위치: Edge AI 처리 영역**

1. **GAN-based Sensor Data Augmentation (EAAI 2023)**
   - 위치: 기지국 내부
   - 설명: PIR sensor, people counting
   - 키워드: "AI/ML at Edge"

---

### 📱 **DEVICE LAYER - Heterogeneous Devices & Services**

#### 위치: 하단 디바이스 아이콘들

**관련 논문 (Device-centric 연구):**

1. **Performance Analysis of IoT with Wake-Up Radio (Sensors 2019)**
   - 위치: IoT 센서 아이콘 (드론 아이콘)
   - 설명: Low-power device operation

2. **GAN-based PIR Sensor Data (EAAI 2023)**
   - 위치: IoT 센서 아이콘
   - 설명: Sensor data processing

3. **Priority-Aware Actuation (Sensors 2024)**
   - 위치: 스마트워치 아이콘
   - 설명: Industrial IoT actuators

**시각적 표현:**
- 각 디바이스 아이콘 아래 소속 논문 연도 표시
- "Low-Power", "Real-time", "Energy-Efficient" 키워드

---

## 🔄 **계층 간 연결 (Control & Data Plane)**

### Cloud ↔ Edge 연결선

**위치: 좌측 큰 회색 화살표**

**관련 논문:**
- Task Offloading 시리즈 (ICTC 2023-2024)
- Container Warming (FGCS 2025)
- NF Deployment (ICTC 2023)

**레이블:**
```
Orchestration Commands ↓
Status Reports & Metrics ↑
```

### Edge ↔ Device 연결선

**위치: 좌측 하단 화살표**

**관련 논문:**
- AoI-aware AQM (IEEE IoT 2024)
- Multi-Link MAC (TVT 2023)
- Vehicular Caching (Sensors 2022)

**레이블:**
```
Wireless Communication
(5G/WiFi/V2X)
```

---

## 📊 **일러스트에 추가할 시각적 요소**

### 1. 논문 개수 뱃지 (Layer별)

```
Cloud Layer:     [5 papers] - Deep RL & Serverless
Edge Layer:      [15 papers] - MAC & Network Optimization
Device Layer:    [3 papers] - IoT & Sensors
```

### 2. Top-tier 저널 하이라이트 (별표 ⭐)

**Cloud 영역:**
- FGCS 2025 (컨테이너 아이콘 근처)

**Edge 영역:**
- IEEE TVT 2023 (WiFi 아이콘)
- IEEE TVT 2018 (기지국)
- IEEE IoT 2024 (기지국)

### 3. 연구 키워드 클라우드

각 계층에 작은 키워드 추가:

**Cloud:**
- Deep RL
- Serverless
- Container
- UAV-MEC

**Edge:**
- Multi-Link
- AoI
- V2X
- 802.11be/ax
- Dense WLAN

**Device:**
- Low-Power
- IoT
- Sensors
- Energy-Efficient

---

## 📐 **구체적 배치 가이드 (draw.io 작업용)**

### Cloud Layer (상단)

```
[클라우드 아이콘1] ←→ [클라우드 아이콘2] ←→ [클라우드 아이콘3] ←→ [컨테이너 아이콘]
     ↓                    ↓                    ↓                    ↓
  DQN (2023)          DRQN (2024)         NF Deploy           NASCIW (2025)
                                                              ⭐ FGCS
```

### Edge Layer (중앙)

```
[모니터 아이콘]  [체인 아이콘]  [기지국 타워]  [번개 아이콘]
      ↓              ↓              ↓              ↓
   GAN-based    Multi-Link      AoI-aware      Vehicular
   (EAAI)       (TVT 2023⭐)    (IoT 2024⭐)   (IET 2024)
```

### Device Layer (하단)

```
[드론 아이콘]  [스마트폰]  [차량]  [스마트워치]
     ↓            ↓         ↓         ↓
IoT Wake-up   Mobile    V2X     Industrial
(Sensors'19)  Device   Caching  Actuation
```

---

## 🎨 **색상 코딩 제안**

### Layer별 색상

- **Cloud**: 진한 파랑 (#2E5090)
- **Edge**: 청록색 (#00A9A5)
- **Device**: 주황색 (#F57C00)

### 논문 연도별 색상

- **2024-2025**: 골드 뱃지 (#FFD700) - 최신
- **2022-2023**: 은색 뱃지 (#C0C0C0) - 최근
- **2020 이전**: 회색 뱃지 (#808080) - 초기 연구

### Top-tier 저널 하이라이트

- **IEEE TVT**: 빨간 별 ⭐
- **IEEE IoT**: 파란 별 ⭐
- **FGCS**: 녹색 별 ⭐

---

## 📝 **일러스트 캡션 제안**

### 전체 타이틀

```
Intelligent Resource Orchestration for Next-Generation Networks
From Protocol Design to Edge Intelligence (2011-2025)
```

### Layer별 서브타이틀

**Cloud Layer:**
```
Intelligent Resource Management
• Deep RL-based Decision Making
• Serverless Edge Computing
• UAV-assisted MEC
[5 papers: FGCS, ICTC]
```

**Edge Layer:**
```
Edge Computing & Network Optimization
• Multi-Link MAC (802.11be)
• AoI-aware IoT Networks
• Vehicular Content Delivery
[15 papers: IEEE TVT×3, IEEE IoT×2, IET, Sensors×2]
```

**Device Layer:**
```
Heterogeneous Devices & Services
• Low-Power IoT
• Energy-Efficient Communication
• Real-time Sensing
[3 papers: Sensors, EAAI]
```

---

## 🔢 **통계 요약 (일러스트 코너에 추가)**

### 우측 하단 박스

```
┌─────────────────────────┐
│  Research Output        │
│  • 20+ Journal Papers   │
│  • 10+ Conference       │
│  • 3× IEEE TVT          │
│  • 2× IEEE IoT Journal  │
│  • 1× FGCS              │
│                         │
│  Timeline: 2011-2025    │
│  (14+ years)            │
└─────────────────────────┘
```

---

## 🎯 **교수 임용 발표용 활용 전략**

### Slide 1: 전체 일러스트 제시

**설명:**
"제 연구는 3개 계층을 아우르는 통합적 자원 최적화입니다."

### Slide 2: Cloud Layer 하이라이트

**애니메이션:** Cloud만 밝게, 나머지 흐리게
**설명:** "최근 Edge Intelligence 연구 (2023-2025)"
**강조:** FGCS 2025 serverless paper

### Slide 3: Edge Layer 하이라이트

**애니메이션:** Edge만 밝게
**설명:** "네트워크 최적화의 핵심 (2018-2024)"
**강조:** IEEE TVT 3편

### Slide 4: Device Layer 하이라이트

**애니메이션:** Device만 밝게
**설명:** "실제 응용 및 센서 데이터 처리"

### Slide 5: 전체 연결 강조

**애니메이션:** 화살표들 순차적으로 나타남
**설명:** "Cross-layer 통합 접근"

---

## 📋 **논문 목록 (Layer별 체크리스트)**

### ☁️ Cloud Layer (5편)
- [x] NASCIW - FGCS 2025 ⭐
- [x] DRQN Task Offloading - ICTC 2024
- [x] DQN Task Offloading - ICTC 2023
- [x] NF Deployment - ICTC 2023
- [x] Federated Learning - ICTC 2023

### 📡 Edge Layer (15편)

**MAC Protocol (6편):**
- [x] HARE Multi-Link - IEEE TVT 2023 ⭐
- [x] Multi-Link Performance - Applied Sciences 2021
- [x] MU-MIMO+OFDMA - ICT Express 2020
- [x] Full Duplex VoIP - IEEE TVT 2017
- [x] Adaptive Resource Allocation - IEEE TVT 2018 ⭐
- [x] Phase-Divided MAC - IEEE TVT 2018

**IoT & Routing (5편):**
- [x] AoI-aware AQM - IEEE IoT 2024 ⭐
- [x] Priority-Aware Actuation - Sensors 2024
- [x] Multi-criteria Routing - Wireless Networks 2024
- [x] D2D Routing - Electronics 2022
- [x] IoT Wake-Up Radio - Sensors 2019

**Vehicular (3편):**
- [x] Electro-mobility Offloading - IET ITS 2024
- [x] CSV Vehicular Caching - Sensors 2022
- [x] Platoon Message - Energies 2020

**AI/ML (1편):**
- [x] GAN Sensor Data - EAAI 2023

### 📱 Device Layer (3편)
- [x] IoT Wake-Up Radio - Sensors 2019
- [x] GAN PIR Sensor - EAAI 2023
- [x] Industrial Actuation - Sensors 2024

### 🔄 Cross-Layer (Legacy, 2011-2016)
- [ ] mmWave papers (2013-2015) - 배경 연구
- [ ] Relay selection (2011, 2015) - 초기 연구
- [ ] Rate adaptation (2012-2014) - 기초 연구

---

## ✅ **다음 단계 (To-Do)**

1. **draw.io에서 논문 레이블 추가**
   - 각 아이콘 근처에 대표 논문 제목 (축약)
   - 연도 뱃지 추가

2. **색상 코딩 적용**
   - 최신 논문: 골드 테두리
   - Top-tier: 별 아이콘

3. **키워드 클라우드 배치**
   - Layer별 주요 기술 용어

4. **통계 박스 추가**
   - 우측 하단: 논문 개수, 저널 이름

5. **PowerPoint 애니메이션**
   - Layer별 순차 하이라이트
   - 화살표 방향 애니메이션

---

**완성 예상 시간:** 추가 1-1.5시간
**최종 결과물:** 논문 매핑이 완료된 학술 일러스트

이제 draw.io에서 논문 정보를 추가하실 수 있습니다!
