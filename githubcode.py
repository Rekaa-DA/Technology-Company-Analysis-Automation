import pandas as pd

# =====================================================
# 1. GOOGLE SHEET CONNECTION
# =====================================================

SHEET_ID = "1GVbuVFtNpaLdB5uf8JopN1rc_6BUEkoQKXXi_RZBY2M"

SHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/"
    f"{SHEET_ID}/export?format=csv"
)

df = pd.read_csv(SHEET_URL)

print("Original Dataset Shape:", df.shape)

print("\nOriginal Columns:")
print(df.columns.tolist())


# =====================================================
# 2. STANDARDIZE COLUMN NAMES
# =====================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

print("\nStandardized Columns:")
print(df.columns.tolist())


# =====================================================
# 3. REQUIRED COLUMNS
# =====================================================

required_columns = [
    "company",
    "repository_name",
    "programming_language",
    "stars",
    "forks",
    "watchers",
    "open_issues",
    "repository_size_kb",
    "license",
    "archived",
    "created_date",
    "updated_date",
    "repository_url"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:

    print("\nMissing Columns:")
    print(missing_columns)

else:

    print("\nAll required columns are available.")


# =====================================================
# 4. SELECT REQUIRED COLUMNS
# =====================================================

df_clean = df[required_columns].copy()


# =====================================================
# 5. HANDLE MISSING VALUES
# =====================================================

df_clean["programming_language"] = (
    df_clean["programming_language"]
    .fillna("Unknown")
)

df_clean["license"] = (
    df_clean["license"]
    .fillna("No License")
)


# =====================================================
# 6. CONVERT NUMERICAL COLUMNS
# =====================================================

numeric_columns = [
    "stars",
    "forks",
    "watchers",
    "open_issues",
    "repository_size_kb"
]

for column in numeric_columns:

    df_clean[column] = pd.to_numeric(
        df_clean[column],
        errors="coerce"
    )

    df_clean[column] = (
        df_clean[column]
        .fillna(0)
        .astype(int)
    )


# =====================================================
# 7. CONVERT ARCHIVED STATUS
# =====================================================

df_clean["archived"] = (
    df_clean["archived"]
    .astype(str)
    .str.lower()
    .map({
        "true": 1,
        "false": 0,
        "active": 0,
        "archived": 1
    })
    .fillna(0)
    .astype(int)
)


# =====================================================
# 8. CONVERT DATE COLUMNS
# =====================================================

df_clean["created_date"] = pd.to_datetime(
    df_clean["created_date"],
    errors="coerce"
)

df_clean["updated_date"] = pd.to_datetime(
    df_clean["updated_date"],
    errors="coerce"
)


# =====================================================
# 9. REMOVE DUPLICATE ROWS
# =====================================================

before_duplicates = len(df_clean)

df_clean = df_clean.drop_duplicates()

after_duplicates = len(df_clean)

print(
    "\nDuplicate Rows Removed:",
    before_duplicates - after_duplicates
)


# =====================================================
# 10. VALIDATE DATA
# =====================================================

print("\nMissing Values:")
print(df_clean.isnull().sum())

print(
    "\nDuplicate Rows:",
    df_clean.duplicated().sum()
)

print(
    "\nClean Dataset Shape:",
    df_clean.shape
)


# =====================================================
# 11. REMOVE TIMEZONE BEFORE EXCEL EXPORT
# =====================================================

df_clean["created_date"] = (
    df_clean["created_date"]
    .dt.tz_localize(None)
)

df_clean["updated_date"] = (
    df_clean["updated_date"]
    .dt.tz_localize(None)
)


# =====================================================
# 12. EXPORT CLEAN DATASET
# =====================================================

df_clean.to_csv(
    "github_cleaned_data.csv",
    index=False,
    encoding="utf-8-sig"
)

df_clean.to_excel(
    "github_cleaned_data.xlsx",
    index=False
)

print(
    "\nClean CSV and Excel files created successfully."
)


# =====================================================
# 13. PREVIEW FINAL DATA
# =====================================================

print("\nFinal Dataset Preview:")

print(df_clean.head())
