import dearpygui.dearpygui as dpg
import pyhibp
from pyhibp import pwnedpasswords as pw
import re

# --- HIBP Setup ---
pyhibp.set_user_agent(ua="PasswordScanner/1.0 (Password security checker)")

def analyze_password_strength(password: str) -> str:
    """Analyze password for strength based on characters and patterns."""
    results = []

    # Length check
    if len(password) >= 12:
        results.append("✅ Good length")
    elif len(password) >= 8:
        results.append("⚠️ Medium length")
    else:
        results.append("❌ Too short (<8 chars)")

    # Uppercase / lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        results.append("✅ Contains upper & lower case")
    else:
        results.append("❌ Missing upper or lower case")

    # Numbers
    if re.search(r"[0-9]", password):
        results.append("✅ Contains numbers")
    else:
        results.append("❌ No numbers")

    # Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        results.append("✅ Contains special characters")
    else:
        results.append("❌ No special characters")

    # Pattern detection (repeated chars or sequences)
    if re.search(r"(.)\1\1", password):
        results.append("⚠️ Contains repeated characters")
    if re.search(r"1234|abcd|qwerty", password.lower()):
        results.append("⚠️ Contains common sequences")

    return "\n".join(results)


def check_password_callback():
    password = dpg.get_value("password_input")
    if not password:
        dpg.set_value("results_text", "Please enter a password.")
        return

    # Check HIBP
    try:
        breach_count = pw.is_password_breached(password)
    except Exception as e:
        dpg.set_value("results_text", f"Error checking password: {e}")
        return

    if breach_count:
        hibp_result = f"⚠️ Password found in breaches {breach_count} time(s)!"
    else:
        hibp_result = "✅ Password not found in known breaches."

    # Local strength analysis
    strength_result = analyze_password_strength(password)

    # Output results
    dpg.set_value("results_text", f"{hibp_result}\n\nStrength analysis:\n{strength_result}")


# --- GUI ---
dpg.create_context()

with dpg.window(label="Password Scanner", width=500, height=400):
    dpg.add_text("Enter your password:")
    dpg.add_input_text(tag="password_input", password=True, default_value="")

    dpg.add_button(label="Check Password", callback=check_password_callback)
    dpg.add_separator()
    dpg.add_text("Results:")
    dpg.add_text(tag="results_text", default_value="")

dpg.create_viewport(title="Password Scanner", width=520, height=420)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
