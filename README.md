# Cortex XSOAR Command Toolkit

CLI toolkit to call common Cortex XSOAR REST endpoints with optional interactive prompts or JSON file inputs. Responses are normalized and written to timestamped JSON files.

**Features**
- CLI aliases for common XSOAR actions
- Interactive prompts when required inputs are missing
- JSON file input support via `arg=`
- Basic HTTP retries and error handling
- Timestamped JSON outputs per command

**Requirements**
- Python 3.10+
- Cortex XSOAR 6.x
- Cortex XSOAR base URL and API key
- TLS certificate file expected at `src/xsoar_command_toolkit/certs/cert.pem`

**Install**
```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

Editable install (installs `xsoar-toolkit` console script):
```powershell
pip install -e .
```

**Configure**
Copy `.env.example` to `.env` and fill values:
```env
XSOAR_API_KEY=API_KEY_HERE
XSOAR_BASE_URL=XSOAR_URL_HERE
```

Note: The app imports settings on startup, so missing env vars will raise a `RuntimeError` before any CLI help is shown.

**Usage**
The CLI accepts `cmd=` and optional `arg=`. Argument order is flexible.

```powershell
xsoar-toolkit health
xsoar-toolkit cmd=check_health_containers
xsoar-toolkit logoutmyself
xsoar-toolkit cmd=logout_everyone
xsoar-toolkit cmd=revoke_api arg=file_path
xsoar-toolkit cmd=create_incident arg=src\\xsoar_command_toolkit\\inputs\\incident_to_create.json
xsoar-toolkit get_incident file_path
xsoar-toolkit cmd=setlist
xsoar-toolkit cmd=search_script file_path
xsoar-toolkit search_incidents arg=file_path
xsoar-toolkit uploadfile file_path
```

Help:
```powershell
xsoar-toolkit --help
```

**Commands (canonical names)**
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

Aliases for each command are listed in `src/xsoar_command_toolkit/configs/settings.py` under `API_COMMANDS`.

**Inputs**
When `arg=` is provided, the tool loads JSON and uses those keys as prompt answers. Example input:
- `src/xsoar_command_toolkit/inputs/incident_to_create.json`

If `arg=` is not provided, the tool prompts for required fields.

**Outputs**
Responses are saved to `src/xsoar_command_toolkit/output` with timestamped filenames.
- Search Script: one file per script
- Search Incidents: one file per incident
- Other commands: one file per command

**Project Layout**
- `src/xsoar_command_toolkit/cli.py`: CLI entrypoint
- `src/xsoar_command_toolkit/main.py`: orchestrator wrapper
- `src/xsoar_command_toolkit/configs/settings.py`: env vars, commands, prompts
- `src/xsoar_command_toolkit/orchestrator/`: routing, payload building, output normalization
- `src/xsoar_command_toolkit/http/`: HTTP client + exceptions
- `src/xsoar_command_toolkit/prompting/`: prompt engine + validation
- `src/xsoar_command_toolkit/utils/`: JSON and file helpers
- `src/xsoar_command_toolkit/inputs/`: sample inputs

