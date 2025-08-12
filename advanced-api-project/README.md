# 🔍 Testing Strategy for Book API

## Overview
This test suite ensures:
- CRUD operations work correctly.
- Permissions are enforced (only authenticated users can write).
- Filtering, search, and ordering return correct results.
- Serializer validation prevents invalid data.

## Test Coverage
- [x] List & Detail (read, public)
- [x] Create, Update, Delete (write, authenticated only)
- [x] Permission enforcement
- [x] Search & Filter functionality
- [x] Ordering (asc/desc)
- [x] Validation (e.g., future year rejected)

## How to Run
```bash
python manage.py test api