# 🛡️ AR Suraksha

> **Offline-first AR safety training simulator for industrial workers in Jharkhand.**

[![SIH 2026](https://img.shields.io/badge/Smart%20India%20Hackathon-2026-blue)](https://www.sih.gov.in/)
[![Problem Statement](https://img.shields.io/badge/PS-SIH26041-orange)](https://www.sih.gov.in/)
[![Theme](https://img.shields.io/badge/Theme-Smart%20Education-0ea5e9)](#)
[![Category](https://img.shields.io/badge/Category-Software-22c55e)](#)

**AR Suraksha** is our proposed mobile-first training solution for industrial safety education. It uses augmented reality scenarios, guided decisions, rule-based assessment, offline storage, synchronization, and QR-verifiable certification to help workers practise safety responses in a realistic but controlled environment.

> **Project status:** Prototype / solution design. This repository documents the proposed architecture, UX, technical approach, research basis, and implementation roadmap. It does not claim that unimplemented modules are production-ready.

## 📌 SIH 2026

| Item | Details |
|---|---|
| Problem Statement ID | **SIH26041** |
| Problem Statement | **AR-Based Vocational Training Simulator** |
| Theme | **Smart Education** |
| Category | **Software** |
| Team ID | **164128** |
| Team | **Adyzen** |
| Target region | **Jharkhand** |

## 🎯 Problem

Industrial safety training can be difficult to practise repeatedly in real environments. Static training material may not provide enough hands-on decision practice, while live drills can be disruptive and resource-intensive.

AR Suraksha proposes a phone-based training layer where a learner can practise safety scenarios, make decisions, receive immediate assessment feedback, and retain results even when connectivity is unavailable.

## 💡 Proposed Solution

The proposed workflow is:

**Scan environment → Launch AR scenario → Identify hazards → Select PPE / response → Receive assessment → Store result offline → Sync when online → Generate verifiable certificate**

### Core scenarios
- 🔥 Fire safety
- 🫧 Gas-leak safety
- ⚙️ Industrial machinery hazards *(roadmap)*

### Core capabilities
- 📱 Android mobile training
- 🥽 AR experiences using AR Foundation + Google ARCore
- 📴 Offline-first training with SQLite
- 🧠 Rule-based scoring and immediate feedback
- 🌐 Hindi + Santali language support
- 🔄 REST API synchronization when online
- 🖥️ Admin dashboard for records and results
- 📜 QR-based certificate verification

## 🏗️ Technical Architecture

```text
┌───────────────────────────────┐
│       WORKER ANDROID APP      │
│        Unity + C#              │
├───────────────────────────────┤
│ AR Foundation + Google ARCore │
│ Training • Assessment • UI    │
└───────────────┬───────────────┘
                │
        Offline-first layer
                │
        ┌───────▼───────┐
        │ SQLite Local  │
        │ Progress/Data │
        └───────┬───────┘
                │ Sync when online
                ▼
        ┌─────────────────┐
        │ FastAPI Backend  │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │ PostgreSQL      │
        │ Central Records │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │ Admin Dashboard │
        │ Results / Certs │
        └─────────────────┘
```

See [docs/architecture.md](docs/architecture.md) for the detailed component plan.

## 🧰 Technology Stack

| Layer | Proposed technology | Purpose |
|---|---|---|
| Mobile | Android | Worker-side application |
| AR | Unity + C# | 3D/AR training experience |
| AR tracking | AR Foundation + Google ARCore | Environment tracking and anchors |
| Local data | SQLite | Offline progress and results |
| Backend | Python + FastAPI | API and synchronization |
| Database | PostgreSQL | Central records |
| Certification | QR-based verification | Certificate validation |

## 📱 Training Flow

1. Select language.
2. Select a safety module.
3. Start the AR scenario.
4. Identify the presented hazard.
5. Select appropriate PPE / response.
6. Complete the scenario.
7. Receive rule-based assessment and feedback.
8. Save progress locally if offline.
9. Synchronize results when connectivity returns.
10. Generate a QR-verifiable certificate when the required assessment is completed.

## 🌐 Offline-First Design

Connectivity should not be a hard dependency for the worker-side training flow.

The proposed design keeps training progress and assessment results on-device using SQLite. When a network connection becomes available, the application can synchronize eligible records with the FastAPI backend and central PostgreSQL database.

More details: [docs/architecture.md](docs/architecture.md)

## 📊 Assessment & Certification

The proposed MVP uses **rule-based scoring** rather than claiming AI assessment.

Assessment can evaluate:
- Hazard identification
- PPE selection
- Response selection
- Scenario completion
- Quiz performance

Successful completion can trigger a **QR-based certificate** designed for later verification.

## 🗣️ Language & Accessibility

The solution is designed around:
- Hindi
- Santali
- Icon-led interfaces
- Simple interaction flows
- Offline operation
- 2D fallback content as a proposed mitigation where AR tracking is difficult

## 📁 Repository Structure

```text
AR---Suraksha/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── project-overview.md
│   ├── research-and-references.md
│   └── implementation-roadmap.md
├── mobile-app/
│   └── README.md
├── backend/
│   └── README.md
├── database/
│   └── README.md
├── assets/
│   ├── ui/
│   └── diagrams/
└── demo/
    └── README.md
```

## 🗺️ Implementation Roadmap

### Phase 1 — MVP
- Android shell
- Fire scenario
- Gas-leak scenario
- AR interaction
- Rule-based assessment
- Local SQLite storage
- QR certificate prototype

### Phase 2 — Pilot
- API synchronization
- PostgreSQL central records
- Admin dashboard
- Hindi + Santali content refinement
- Field testing and usability feedback

### Phase 3 — Expansion
- Additional industrial scenarios
- Broader deployment
- More training analytics
- Proposed AI-adaptive scoring and identity-verification features, subject to pilot validation

See [docs/implementation-roadmap.md](docs/implementation-roadmap.md).

## 📚 Research & References

The repository includes the project's research/reference list in [docs/research-and-references.md](docs/research-and-references.md).

The references cover:
- DGMS safety and legislation
- AR safety-training research
- OSHA emergency/confined-space guidance
- Google ARCore
- Unity AR Foundation
- Android offline-first architecture
- SQLite
- FastAPI
- PostgreSQL

## 🎬 Demo

The project demo materials are documented in [demo/README.md](demo/README.md).

The demo should be understood as a **prototype representation of the proposed product experience**, unless a feature is explicitly marked as implemented.

## ⚠️ Project Status

This repository is being developed for **Smart India Hackathon 2026**.

Current repository purpose:
- Document the solution
- Communicate the architecture
- Preserve research references
- Track implementation
- Provide a transparent roadmap

Features should be marked **Implemented**, **Prototype**, or **Planned** as development progresses.

## 👥 Team

**Team Adyzen — SIH 2026**

- Team ID: **164128**
- Problem Statement: **SIH26041**

## 📄 License

A project license will be added when the team decides the appropriate licensing terms.

---

### 🔗 Documentation

- [Project Overview](docs/project-overview.md)
- [Architecture](docs/architecture.md)
- [Research & References](docs/research-and-references.md)
- [Implementation Roadmap](docs/implementation-roadmap.md)
- [Mobile App](mobile-app/README.md)
- [Backend](backend/README.md)
- [Database](database/README.md)
- [Demo](demo/README.md)
