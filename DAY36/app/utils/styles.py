def apply_styles_page_one(mainText, window, text, button, success, chat):
    mainText.setStyleSheet(
        """
        font-size: 30px;
        background: transparent;
    """
    )

    window.setStyleSheet(
        """
        font-family: Helvetica;
        background-color: rgba(80, 180, 255, 160);
        margin: 0px;
        padding: 0px;
    """
    )

    text.setStyleSheet(
        """
    background-color: rgba(40, 90, 140, 220);
    padding: 10 25px;
    border: 5px solid rgba(40, 90, 140, 220);
    """
    )

    button.setStyleSheet(
        """
    background-color: rgba(40, 90, 140, 220);
    border: 5px solid rgba(40, 90, 140, 220);
    padding: 10 25;
    font-size: 18px;
    """
    )

    success.setStyleSheet(
        """
    background: transparent;
    font-size: 20px;
    border: none;
    """
    )

    chat.setStyleSheet(
        """
                  padding: 10 10;
                  border: 5px solid  rgba(100, 190, 255, 180);
                  font-size: 22px;
              """
    )
