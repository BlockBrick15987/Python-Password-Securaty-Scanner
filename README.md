# 🔐 Password Scanner

A small GUI application built with [DearPyGui](https://github.com/hoffstadt/DearPyGui) that checks whether a password has been leaked in any known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3) **and** performs local password strength analysis.

## ✨ Features

- **HIBP Check** – Verify if a password appears in any public breach database
- **Occurrence Count** – Shows how many times the password was seen in breaches
- **Password Strength Analysis**:
  - ✅ Usage of **uppercase and lowercase letters**
  - ✅ Inclusion of **numbers**
  - ✅ Inclusion of **special characters**
  - ✅ Detection of **patterns** (e.g., repeated characters like `aaaa`, sequences like `1234`)
- **Clean and Simple GUI** made with DearPyGui
- **Passwords hidden** in the input field for security

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/password-scanner.git
   cd password-scanner
