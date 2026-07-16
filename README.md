# AgencyBot2

Telegram bot for collecting model applications to PRESIDENT agency.

## Files to include
- `main.py` - bot logic
- `config.py` - contains `TOKEN` and `MANAGER_ID`
- `requirements.txt` - dependencies (`aiogram==3.29.1`)
- `keyboards/main_menu.py` - reply keyboards

## Quick setup
1. Create virtualenv: `python3 -m venv venv`
2. Activate: `source venv/bin/activate`
3. Install deps: `pip install -r requirements.txt`
4. Run: `python main.py`

## Notes
- Keep `config.py` private. Use environment variables on production.
- For 24/7 hosting, use VPS, Deta, or paid PythonAnywhere.
