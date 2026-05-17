# Technical Roadmap V1

## Objective

Transform the macro vision of the project into a real technical execution roadmap.

This roadmap exists to:

- reduce implementation chaos
- avoid overengineering
- define dependency order
- break the system into executable phases
- prepare backend execution

---

# Real Implementation Order

## Phase 1 — Gym Foundation
Build the first functional data source of the system.

Tasks:
- create exercise structure
- create workout templates
- create workout sessions
- calculate training volume
- store training history

---

## Phase 2 — Database Foundation

Tasks:
- connect PostgreSQL (Neon)
- create initial tables
- configure migrations
- create seed scripts

---

## Phase 3 — Backend API

Tasks:
- create FastAPI routes
- create services
- create repositories
- create validation schemas

---

## Phase 4 — Basketball Module

Tasks:
- register basketball sessions
- duration tracking
- intensity tracking
- basketball load calculation

Formula:

Load = duration × intensity

---

## Phase 5 — Recovery Module

Tasks:
- sleep tracking
- hydration tracking
- recovery logs
- automatic fatigue reduction

---

## Phase 6 — Fatigue Engine

Tasks:
- muscular fatigue calculation
- cardiovascular fatigue calculation
- cumulative fatigue logic
- recovery interaction

---

## Phase 7 — Performance Module

Tasks:
- vertical jump tracking
- speed tracking
- explosion metrics
- performance history

---

## Phase 8 — Frontend

Tasks:
- dashboard
- workout screens
- basketball screens
- fatigue dashboard
- graphs

---

## Phase 9 — Deployment

Tasks:
- deploy backend
- deploy frontend
- production validation

---

# MVP V1

The first usable version of the system must allow:

- create exercises
- create workout templates
- register gym sessions
- calculate training volume
- save history

---

# Out of Scope (Current Version)

- machine learning
- wearable integration
- AI recommendations
- microservices
- advanced prediction systems

---

# Technical Dependencies

Gym → required first

Basketball → depends on gym structure

Recovery → depends on training history

Fatigue → depends on recovery + training data

Performance → depends on fatigue data

Machine Learning → depends on large historical datasets

---

# First Backend Sprint

Initial backend implementation:

- User model
- Exercise model
- WorkoutTemplate model
- WorkoutSession model
- CRUD endpoints
- volume calculation logic
- database persistence

---

# Step 10 Completion Criteria

Step 10 is complete when:

- roadmap is documented
- implementation order is defined
- technical dependencies are clear
- backend execution can begin