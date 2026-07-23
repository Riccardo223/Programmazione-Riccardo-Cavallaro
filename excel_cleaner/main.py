import streamlit as st
import pandas as pd
import re
import io
from rapidfuzz import process


st.set_page_config(
    page_title="Excel Cleaner - Kangoroo",
    page_icon="📊",
    layout="wide"
)

with open("Dizionario/nomi_italiani.txt", "r", encoding="utf-8") as file:
    italian_first_names = file.read().splitlines()

with open("Dizionario/cognomi_italiani.txt", "r", encoding="utf-8") as file:
    italian_surnames = file.read().splitlines()



column_aliases = {
    "ID": ["id", "codice", "numero", "identificativo", "employee id", "matricola"],
    "Nome Cognome": ["nome cognome", "full name", "nominativo", "name", "dipendente", "employee"],
    "Azienda": ["azienda", "company", "ditta", "ragione sociale"],
    "Data": ["data", "date", "giorno"],
    "Orario Inizio": ["inizio", "clock in", "start", "entrata", "inizio turno", "time in"],
    "Orario Fine": ["fine", "clock out", "finish", "uscita", "fine turno", "time out"],
    "Ruolo": ["ruolo", "mansione", "posizione", "qualifica", "titolo", "role", "job_title", "title", "position", "job"],
    "Stipendio Mensile": ["stipendio mensile", "stipendio_mensile", "retribuzione mensile", "paga mensile", "mensile",
                          "monthly salary", "monthly_salary", "salary", "gross salary", "base salary", "monthly pay"],
    "Reparto": ["reparto", "dipartimento", "area", "divisione", "ufficio", "department", "dept", "division", "team",
                "business unit", "bu"],
    "Email": ["email", "e-mail", "indirizzo email", "posta elettronica", "contatto", "mail", "email address",
              "e-mail address", "user email", "contact email"]
}


def build_reverse_lookup(column_aliases):
    """Flattens {canonical_name: [alias1, alias2, ...]} into {alias: canonical_name}
    so a single alias can be looked up directly instead of scanning every list."""
    reverse_lookup = {}
    for canonical_name, alias_list in column_aliases.items():
        for variant in alias_list:
            reverse_lookup[variant] = canonical_name
    return reverse_lookup


reverse_lookup = build_reverse_lookup(column_aliases)


def find_canonical_name(file_column, reverse_lookup):
    """Tries an exact match first (case-insensitive); falls back to fuzzy matching
    to catch small typos (e.g. 'Emial' -> 'Email')."""
    cleaned_column = file_column.lower().strip()

    if cleaned_column in reverse_lookup:
        return reverse_lookup[cleaned_column]
    else:
        alias_list = list(reverse_lookup.keys())
        match, score, _ = process.extractOne(cleaned_column, alias_list)
        if score >= 80:
            return reverse_lookup[match]
        else:
            return None


def clean_generic_text(value):
    """Base cleanup used by most columns: handles missing values,
    strips leading/trailing spaces, and collapses multiple spaces into one."""
    if pd.isna(value):
        return ""
    else:
        text = str(value).strip()
        text = re.sub(r'\s+', ' ', text)
    return text


def clean_full_name(value):
    """Cleans a full name and splits stuck-together words like 'AnnaFranchi' -> 'Anna Franchi'."""
    text = clean_generic_text(value)
    if text == "":
        return ""
    else:
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return text


def fuzzy_check_name(word, reference_list):
    """Compares a single word against a reference list (first names or surnames)
    and flags likely typos without auto-correcting them."""
    if word == "":
        return 'not in register'
    else:
        match, score, _ = process.extractOne(word, reference_list)
        if word.lower() == match.lower():
            return '✓'
        elif score >= 85:
            return '?'
        else:
            return 'not in register'


def check_full_name(value, first_names_list, surnames_list):
    """Splits 'Full Name' into first name + surname and checks each one separately."""
    text = clean_generic_text(value)
    words = text.split()
    if len(words) == 2:
        first_name, surname = words
        first_name_result = fuzzy_check_name(first_name, first_names_list)
        surname_result = fuzzy_check_name(surname, surnames_list)
        return f'name: {first_name_result} | surname: {surname_result}'
    else:
        return "manual control required"


def clean_email(value):
    text = clean_generic_text(value)
    text = text.replace(" ", "")
    return text


def validate_email(value):
    text = clean_generic_text(value)
    text = text.replace(" ", "")
    if text:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(pattern, text):
            return 'valid Email'
        else:
            return 'invalid Email'
    else:
        return 'Email missing'


def clean_date(value):
    """Handles real datetime/Timestamp values directly; falls back to regex
    extraction for plain text dates in DD-MM-YYYY or DD/MM/YYYY format."""
    if hasattr(value, 'strftime'):
        return value.strftime('%Y-%m-%d')

    text = clean_generic_text(value)
    if not text:
        return ""
    match = re.search(r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', text)
    if match:
        day = match.group(1).zfill(2)
        month = match.group(2).zfill(2)
        year = match.group(3)
        return f"{year}-{month}-{day}"
    else:
        return "Unrecognized date format"


def clean_time(value):
    """Handles real time/datetime values directly; otherwise strips stray letters,
    drops a leading date prefix if present, removes seconds, and normalizes
    4-digit times like '1800' into 'HH:MM'."""
    if hasattr(value, 'strftime'):
        return value.strftime('%H:%M')

    text = clean_generic_text(value)
    if not text:
        return ""

    if " " in text:
        text = text.split(" ")[-1]

    text = re.sub(r"[^0-9:]", "", text)
    text = re.sub(r'^(\d{2}:\d{2}):\d{2}$', r'\1', text)
    text = re.sub(r'^(\d{2})(\d{2})$', r'\1:\2', text)
    return text


def clean_salary(value):
    text = clean_generic_text(value)
    if not text:
        return ""
    else:
        text = re.sub(r"[^0-9$]", "", text)
        text = text.replace(" ", "")
    return text + ' $'


def validate_salary(value):
    text = clean_generic_text(value)
    if text:
        return 'Salary inserted'
    return 'Salary Missing'


def clean_department_or_role(value):
    """Title-cases free text, but keeps 'IT' fully uppercase since it's an acronym."""
    text = clean_generic_text(value)
    if not text:
        return ""
    elif text.upper() == 'IT':
        return 'IT'
    return text.title()


# --- SIDEBAR: instructions ---
with st.sidebar:
    st.header("How it works")
    st.write("1️ Upload your Excel file (.xlsx)")
    st.write("2️ Click **Clean file**")
    st.write("3️ Preview the result and download it")
    st.divider()
    st.caption("Excel Cleaner")



st.title("Excel Cleaner")
st.write("Upload an Excel file with employee data to clean it automatically.")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Rows loaded", len(df))
    with col2:
        st.metric("Columns found", len(df.columns))

    if st.button("🧹 Clean file", type="primary"):

        with st.spinner("Cleaning in progress..."):

            # Column recognition: map whatever the file calls each column
            # to the canonical name the cleaning functions expect.
            rename_map = {}
            for column in df.columns:
                canonical_name = find_canonical_name(column, reverse_lookup)
                if canonical_name is not None:
                    rename_map[column] = canonical_name
                else:
                    st.warning(f"Column '{column}' was not recognized and will be left as is")
            df = df.rename(columns=rename_map)

            # Column-by-column cleaning
            df['Nome Cognome'] = df['Nome Cognome'].apply(clean_full_name)
            df['Verifica Anagrafica'] = df['Nome Cognome'].apply(
                check_full_name, args=(italian_first_names, italian_surnames)
            )

            df['Email'] = df['Email'].apply(clean_email)
            df['Stato Email'] = df['Email'].apply(validate_email)

            df['Data'] = df['Data'].apply(clean_date)

            df['Orario Inizio'] = df['Orario Inizio'].apply(clean_time)
            df['Orario Fine'] = df['Orario Fine'].apply(clean_time)

            df['Stipendio'] = df['Stipendio Mensile'].apply(clean_salary)
            df['Stato'] = df['Stipendio Mensile'].apply(validate_salary)

            df['Reparto'] = df['Reparto'].apply(clean_department_or_role)
            df['Ruolo'] = df['Ruolo'].apply(clean_department_or_role)

            column_order = ['ID', 'Nome Cognome', 'Verifica Anagrafica', 'Azienda', 'Data',
                             'Orario Inizio', 'Orario Fine', 'Ruolo', 'Reparto',
                             'Stipendio Mensile', 'Stato', 'Email', 'Stato Email']
            df = df[column_order]

        st.success(" Cleaning completed!")

        # --- TABS to organize the output ---
        tab1, tab2 = st.tabs([" Cleaned data", "⬇ Download"])

        with tab1:
            st.dataframe(df, use_container_width=True)

        with tab2:
            buffer = io.BytesIO()
            df.to_excel(buffer, index=False)
            buffer.seek(0)

            st.download_button(
                label="Download cleaned file",
                data=buffer,
                file_name="cleaned_file.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )