# Fraud Network Intelligence Platform

## Overview

The Fraud Network Intelligence Platform is a graph-based financial analysis system designed to model and analyze financial transaction networks. Rather than treating each transaction as an isolated event, the platform builds a connected representation of banks, entities, accounts, and transactions to support future fraud detection and anti-money laundering (AML) analysis.

This repository is being developed incrementally. The current phase focuses on building a reliable data engineering pipeline and a normalized relational database before introducing graph databases, analytics, and machine learning.

---

# Dataset

This project uses the **IBM Transactions for Anti-Money Laundering (AML)** dataset.

Current dataset:

* HI-Small_Accounts.csv
* HI-Small_Transactions.csv
* HI-Small_Patterns.csv *(not used in the current phase)*

The dataset is loaded into SQLite during the first phase. Pattern data will be incorporated in later phases for validation and model evaluation.

---

# Phase 1 Scope

Current development focuses on:

* Understanding the dataset
* Data normalization
* Relational database design
* ETL pipeline
* Data validation

The following are intentionally postponed:

* Neo4j
* Graph algorithms
* REST APIs
* Dashboard
* Machine Learning
* AI models

---

# Technology Stack

| Component           | Technology               |
| ------------------- | ------------------------ |
| Language            | Python 3                 |
| Relational Database | SQLite                   |
| Dataset             | IBM Transactions for AML |
| ETL                 | Custom Python Pipeline   |

---

# Project Structure

```text
fraud-network-platform/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── database/
│       └── aml.db
│
├── database/
│   ├── schema.sql
│
├── etl/
│   ├── loaders/
│   │   ├── BaseLoader.py
│   │   ├── BankLoader.py
│   │
│   ├── common/
│   │   ├── database.py
│   │   ├── logger.py
│   │   └── validation.py
│
└── app.py
```

---

# Database Design

The relational database is normalized into three core entities.

## Banks

Stores unique financial institutions.

| Column    | Description              |
| --------- | ------------------------ |
| bank_id   | Unique bank identifier   |
| bank_name | Display name of the bank |

---

## Entities

Stores customers or organizations that own financial accounts.

| Column      | Description              |
| ----------- | ------------------------ |
| entity_id   | Unique entity identifier |
| entity_name | Entity name              |

---

## Accounts

Represents bank accounts owned by entities.

| Column         | Description                              |
| -------------- | ---------------------------------------- |
| account_id     | Internal generated identifier            |
| bank_id        | References the owning bank               |
| entity_id      | References the account owner             |
| account_number | Original account number from the dataset |

A unique constraint is maintained on:

```
(bank_id, account_number)
```

This allows identical account numbers to exist at different banks while preventing duplicate accounts within the same bank.

---

# Entity Relationships

```
Entity
   │
 OWNS
   │
Account
   │
HELD_AT
   │
Bank
```

One entity may own multiple accounts.

One bank may contain multiple accounts.

Each account belongs to exactly one entity and one bank.

---

# ETL Pipeline

The ETL process imports the dataset into SQLite in a controlled order.

```
IBM AML Dataset
        │
        ▼
Load Banks
        │
        ▼
Load Entities
        │
        ▼
Load Accounts
        │
        ▼
Load Transactions
        │
        ▼
SQLite Database
```

# Current Status

Completed:

* Project structure
* Database design
* Bank import

In Progress:

* Entity import
* Account import
* Transaction import
* ETL validation

Upcoming:

* Graph database integration
* Graph schema
* Network analytics
* Fraud detection models
