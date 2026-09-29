# System Architecture

## Overview

The proposed architecture has two major sides:

- **Worker side:** Android application with AR training, assessment, local storage and synchronization.
- **Administration side:** backend API, central database and administrative dashboard.

## Components

### 1. Android Application

**Technology:** Unity + C#

Responsibilities:
- Training UI
- Language selection
- Module selection
- Scenario control
- Assessment interaction
- Local progress management

### 2. AR Layer

**Technology:** AR Foundation + Google ARCore

Responsibilities:
- Environment tracking
- AR anchors
- Placement of training elements
- Interactive 3D scenario content

### 3. Training Content

Proposed initial scenarios:
- Fire
- Gas leak

Training content can contain 3D models, animations, prompts and response choices.

### 4. Assessment

The current proposed approach is **rule-based scoring**.

Example conceptual flow:

```text
User action
   ↓
Scenario rule
   ↓
Correct / incorrect
   ↓
Score update
   ↓
Immediate feedback
```

### 5. Offline Storage

**Technology:** SQLite

The proposed local layer stores:
- Progress
- Assessment results
- Pending synchronization data

### 6. Synchronization API

**Technology:** Python + FastAPI

When connectivity is available, the application can send eligible local records to the backend.

### 7. Central Database

**Technology:** PostgreSQL

Proposed responsibilities:
- Worker records
- Assessment results
- Certification records
- Synchronization data
- Administrative reporting data

### 8. Administration

A proposed web dashboard can provide:
- Worker overview
- Assessment results
- Certification status
- Centralized compliance/training records

## Data flow

```text
Worker
  │
  ▼
Android / Unity
  │
  ├── Offline ──► SQLite
  │
  └── Online ──► FastAPI ──► PostgreSQL
                                  │
                                  ▼
                           Admin Dashboard
```

## Proposed future components

The project material identifies these as later-stage ideas rather than MVP requirements:
- Front-camera identity verification
- AI-adaptive scoring
- Additional industrial scenarios
- Wider deployment beyond the initial Jharkhand focus

## Important status note

This document describes the **proposed architecture** from the SIH solution design. It should not be interpreted as proof that every component has already been implemented.
