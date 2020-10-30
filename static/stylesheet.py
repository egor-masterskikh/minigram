from MyFavouriteColors import COLORS


stylesheet = """
#title_bar {
    background-color: #f0f0f0;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}

#CustomWindow {
    background-color: white;
    border-radius: 10px;
}

#title {
    padding-right: 92px;
    color: %s;
}

#login_widget QLineEdit, #register_widget QLineEdit {
    selection-background-color: %s;
    selection-color: white;
    border-width: 2px;
    border-style: solid;
    border-top: 0;
    border-left: 0;
    border-right: 0;
    border-color: black;
}

#login_widget QLineEdit:focus, #register_widget QLineEdit:focus {
    border-color: %s;
}

QCommandLinkButton {
    background: none;
    border: none;
    font-weight: normal;
    color: %s;
}

#valid_symbols_label {
    color: %s;
    margin-bottom: 10px;
}

#register_widget QCheckBox:unchecked, #register_email_error_label, #register_nick_error_label {
    color: %s;
}

#register_widget QCheckBox:checked {
    color: %s;
}

#register_widget QCheckBox::indicator {
    border: none;
}

#length_validator {
    margin-top: 20px;
}

#search {
    margin-right: 10px;
    padding: 5px 5px 5px 10px;
    background-color: #f1f1f1;
    border-radius: 5px;
}

#search:focus {
    background-color: white;
    border: 2px solid %s;
}

#to_menu_page_btn {
    background-color: rgba(0, 0, 0, 0);
    margin-left: 20px;
}

QListWidget, QTableWidget {
    border: none;
}

#message_edit {
    border: none;
}

#dialog_window {
    background-color: %s
}
""" % (COLORS['Сбербанк'], COLORS['Сбербанк'], COLORS['Сбербанк'],
       COLORS['Кобальт синий'], COLORS['Текст на песочном'], COLORS['Карминово-красный'],
       COLORS['Сбербанк'], COLORS['Сбербанк'], COLORS['Сбербанк'])
