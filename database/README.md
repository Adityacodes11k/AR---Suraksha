# Database

## Proposed database

**PostgreSQL** is the proposed central database.

## Conceptual records

The planned data model may include:

- Workers
- Training modules
- Attempts
- Assessment results
- Certificates
- Synchronization records

## Offline synchronization

SQLite is proposed for worker-side local storage. PostgreSQL is proposed for centralized records.

```text
SQLite (device)
      │
      │ sync
      ▼
FastAPI
      │
      ▼
PostgreSQL (central)
```

The exact schema should be finalized during implementation and field testing.
