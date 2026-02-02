# Cortex XSOAR Command Toolkit

CLI utility to call common Cortex XSOAR REST endpoints with optional interactive prompts and JSON inputs. It supports health checks, logout, incident operations, list management, script search, and file upload, then writes responses to `output/` as timestamped JSON files.

## Features
- Simple `cmd=` argument to trigger predefined XSOAR actions
- Optional `arg=` JSON file input or interactive prompts
- Built-in HTTP client with retries and basic error handling
- Normalized output saved to `output/` with per-command filenames

## Project Structure
- `main.py`: entrypoint and CLI invocation
- `configs/settings.py`: environment variables, command aliases, prompt questions
- `src/orchestrator.py`: command routing, payload building, API calls
- `src/cortex_xsoar.py`: Cortex XSOAR API client wrapper
- `src/payload_builder.py`: maps prompt/input keys to API payloads
- `src/normalize.py`: output formatting and file writing
- `core/http/`: HTTP client + exceptions
- `prompting/`: prompt engine + validation
- `inputs/`: sample inputs (e.g., `incident_to_create.json`)
- `output/`: generated responses
- `certs/cert.pem`: TLS certificate used for requests

## Requirements
- Python 3.11+ (local `.venv` exists)
- Access to a Cortex XSOAR instance version 6.x + API key

## Setup
1) Create your `.env` from `.env-example`:

```powershell
Copy-Item .env-example .env
```

2) Fill in:

```env
XSOAR_API_KEY=API_KEY_HERE
XSOAR_BASE_URL=XSOAR_URL_HERE
```

## Usage
Run with a command alias. When required inputs are missing, the tool will prompt you.

```powershell
python main.py cmd=health
python main.py cmd=check_health_containers
python main.py cmd=logoutmyself
python main.py cmd=logout_everyone
python main.py cmd=revoke_api
python main.py cmd=create_incident arg=inputs\incident_to_create.json
python main.py cmd=get_incident
python main.py cmd=setlist
python main.py cmd=search_script
python main.py cmd=search_incidents
python main.py cmd=uploadfile
```

### Supported Commands (canonical)
- Check Health
- Check Health Containers
- Logout Myself
- Logout Everyone
- Revoke API
- Create Incident
- Get Incident
- Save List
- Search Incidents
- Search Script
- Upload File

> The CLI accepts multiple aliases for each command (see `configs/settings.py` under `API_COMMANDS`).

## Inputs
Some commands can read JSON from a file via `arg=`. Example file:
- `inputs/incident_to_create.json`

Other commands will request fields interactively when `arg=` is not provided.

## Outputs
Responses are saved to `output/` with a timestamped name.
- Search Script: one file per script
- Search Incidents: one file per incident
- Others: one file per command response

## Notes
- The HTTP client uses TLS verification with `certs/cert.pem`.
- If a command fails or is invalid, the tool prints a usage message.
