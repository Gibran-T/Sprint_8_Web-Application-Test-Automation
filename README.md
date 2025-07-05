# 🧪 Urban Routes – Sprint 8: Web Application Test Automation

## 📌 Short Description  
Automated test suite for the Urban Routes web application using **Pytest** and **Selenium WebDriver**.  
Developed during **Sprint 8** of the TripleTen QA Engineer Bootcamp.  
This project extends the structure created in [Sprint 7](https://github.com/Gibran-T/urban_routes_project) by adding functional UI tests.

---

## 🗂️ Project Structure

```
urban_routes_project_sprint_8/
├── main.py              # Contains test class and automated test functions
├── data.py              # Constants used in tests (addresses, phone, card, etc.)
├── helpers.py           # Helper functions (e.g., server availability check)
├── requirements.txt     # List of dependencies
├── .gitignore           # Ignore venv and IDE folders
├── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Gibran-T/urban_routes_project_sprint_8.git
cd urban_routes_project_sprint_8
```

2. **Create and activate a virtual environment**
```bash
python -m venv .venv

# Activate:
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Running the Tests

Make sure to replace `URBAN_ROUTES_URL` in `data.py` with your active server URL.  
Then run:

```bash
pytest main.py -v
```

ℹ️ Note: Server links expire after 1 hour or 15 minutes of inactivity.  
Use the helper function `is_url_reachable()` to verify availability before running tests.

---

## ✅ Test Scenarios

| Function | Description |
|----------|-------------|
| `test_set_route` | Sets pickup and destination addresses |
| `test_select_plan` | Chooses the ride plan |
| `test_fill_phone_number` | Inputs phone number and retrieves SMS code |
| `test_fill_card` | Fills payment information |
| `test_comment_for_driver` | Adds message to the driver |
| `test_order_blanket_and_handkerchiefs` | Selects extras |
| `test_order_2_ice_creams` | Orders 2 ice creams using loop |
| `test_car_search_model_appears` | Verifies car model appears in final step |

---

## 📎 Resources & Documentation

- 📄 [📘 Sprint 8 – Project Instructions](https://docs.google.com/document/d/1e0vI4HggTB_KdaJfi387XzNi-59KHPHW/edit?usp=sharing)  
- 📊 [📗 Sprint 8 – Test Case Spreadsheet](https://docs.google.com/spreadsheets/d/1fOeHuOKkFWUSN_iipfXhLZn42mJNhS26uZzp6MRwR4Q/edit?usp=sharing)  
- 🧱 [🏗️ Sprint 7 – Project Foundation (Repo)](https://github.com/Gibran-T/urban_routes_project)

---

## 👨‍💻 Author

**Thiago Gibran Timoteo Nunes**  
QA Engineer | Selenium | Pytest | Manual & Automated Testing  
🇨🇦 Canadian Citizen | 🇧🇷 Brazilian Roots  
🔗 [GitHub](https://github.com/Gibran-T)  
🔗 [LinkedIn](https://www.linkedin.com/in/thiago-gibran-a01489b5/)

---

## 🧠 Quote

> _“Testing leads to failure, and failure leads to understanding.”_  
> — Burt Rutan

---
