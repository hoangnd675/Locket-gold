# Locket Companion

A small Flask dashboard for service health and diagnostics.

## What it does

- Responsive Vietnamese dashboard.
- Health, account-integration status, and diagnostics endpoints.
- Security headers and JSON error responses.
- Vercel deployment configuration.
- Automated tests.

## Important limitations

This project does **not** unlock Locket Gold, alter subscription entitlements, intercept Locket API traffic, or verify a user's paid plan. Account status is reported as unknown/not connected until an official, supported integration is available. Never enter your Locket password, verification code, session cookie, or other credentials into this project.

The legacy response override in `locket.js` is now a pass-through only. The old mobile configuration placeholder has been removed because it was not a valid installable profile.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

## API

- `GET /api/health`
- `GET /api/account/status`
- `GET /api/diagnostics`

## Tests

```bash
pip install pytest
pytest -q
```

## Deploy

Import this repository into Vercel and deploy with the included `vercel.json`. The Flask entry point is `app.py`.

Locket Companion is an independent project and is not affiliated with or endorsed by Locket.
