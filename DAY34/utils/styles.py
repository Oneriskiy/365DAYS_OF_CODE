
def apply_styles_page_one(window, logo_text, input_name, input_lastname, button):
    window.setStyleSheet("""
        background-color: rgba(80, 180, 255, 200);
    """)

    logo_text.setStyleSheet("""
        font-size: 40px;
    
    """)

    input_name.setStyleSheet("""
        padding: 10px 30px;
    """)

    input_lastname.setStyleSheet("""
        padding: 10px 30px;
    """)

    button.setStyleSheet("""
        background-color: black;
        color: white;
        border-radius: 40px;
        border: none;
        padding: 15px 30px;
    """)

def apply_styles_page_two(window_main):
    window_main.setStyleSheet("""
        background-color: rgba(80, 180, 255, 200);
    """)