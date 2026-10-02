# PROJECT_CONTEXT.md

# Color Joys Paint Co.

Version: 1.0

Status: Active Development

Last Updated: September 2026

---

# Project Overview

Color Joys Paint Co. is a production-oriented Paint Store E-Commerce web application built using Flask.

This project is intentionally being developed as if it were a real commercial application instead of a college project.

The primary objective is to learn professional software engineering while building software that is maintainable, scalable, secure, and production ready.

The application allows customers to browse paint products, search and filter products, manage a shopping cart, place orders, complete payments using Razorpay, and manage their order history.

A complete Admin Panel is currently under development.

---

# Project Goals

The project should eventually include every major feature expected in a modern e-commerce platform.

Primary goals include:

• Professional Flask Architecture

• Modular Codebase

• Production-ready Backend

• Clean Bootstrap UI

• Secure Authentication

• Inventory Management

• Online Payments

• Automatic Refunds

• Order Management

• Reports

• Admin Dashboard

• Deployment

The objective is to build software that could realistically be used by a paint store owner.

---

# Current Development Phase

Current Phase

Phase 5

Admin Module

Current Sprint

Phase 5.3

Admin Categories

---

# Current Project Status

Customer Module

Status

Functionally Complete

Completed

✓ Homepage

✓ Responsive Navigation

✓ Hero Carousel

✓ Category Section

✓ Featured Products

✓ Best Sellers

✓ Brands

✓ Testimonials

✓ Footer

✓ Product Listing

✓ Product Details

✓ Search

✓ Category Filter

✓ Brand Filter

✓ Sorting

✓ Pagination

✓ Related Products

✓ Shopping Cart

✓ Buy Now

✓ Checkout

✓ Razorpay Integration

✓ Payment Verification

✓ Orders

✓ Order Details

✓ Order Cancellation

✓ Automatic Refund

✓ Inventory Deduction

✓ Flash Messages

Customer UI Polish

NOT STARTED

This has intentionally been postponed until the complete Admin Module is finished.

Reason

Business functionality always takes priority over cosmetic improvements.

The application must become feature complete before UI polishing begins.

---

# Admin Module Status

Current Status

In Progress

Completed

✓ Admin Folder Structure

✓ Admin Architecture

✓ Flask-Migrate Installed

✓ Admin Model

✓ Initial Database Migration Baseline

✓ Documentation System

Completed

✓ Admin Authentication

✓ Username or email login

✓ Password hash verification

✓ Active-admin validation

✓ Session login and logout

✓ Protected dashboard route

✓ Default admin seed

✓ Dashboard v1 with product, category, and brand totals

✓ Product listing, creation, editing, and image handling

Remaining

Categories

Brands

Products

Inventory

Orders

Reports

Settings

Dashboard follow-up

• Replace placeholder dashboard links with working routes

• Add broader operational summaries as order and inventory modules are completed

---

# Long Term Goal

The final application should be comparable to a small Shopify or WooCommerce store built with Flask.

The objective is not simply to finish features.

The objective is to create software that demonstrates:

• Clean Architecture

• Professional Coding Standards

• Good Documentation

• Security Best Practices

• Maintainability

• Scalability

• Production Quality

---

# Technology Stack

Backend

Python

Flask

SQLAlchemy

SQLite

Flask-Migrate

Frontend

Bootstrap 5

HTML5

CSS3

JavaScript

Jinja2

Icons

Bootstrap Icons

Payment Gateway

Razorpay

Version Control

Git

GitHub

Development Environment

Visual Studio Code

ChatGPT (VS Code)

---

# Development Philosophy

This project follows production-oriented software engineering practices.

Rules

Business Logic belongs inside Services.

Routes should remain small and focused.

Models define persistence only.

Avoid duplicate logic.

Prefer reusable helper functions.

Never redesign completed modules without justification.

Security is reviewed for every feature.

Every completed feature receives its own Git commit.

Architecture is frozen once feature implementation begins.

Customer functionality must remain stable while Admin functionality is developed.

---

# Documentation

The project maintains four permanent documentation files.

AGENTS.md

Permanent development rules.

PROJECT_CONTEXT.md

Complete project encyclopedia.

CHANGELOG.md

History of project changes.

TODO.md

Remaining development roadmap.

Every future ChatGPT or VS Code session should read these files before implementation begins.

---

# Source of Truth

The project workspace is always considered the source of truth.

If documentation and code differ,

the code takes priority.

Documentation should then be updated accordingly.

---

# Project Folder Structure

The project follows a modular Flask architecture.

```
paint-store/
│
├── app.py
├── config.py
├── seed.py
├── requirements.txt
├── README.md
├── AGENTS.md
├── PROJECT_CONTEXT.md
├── CHANGELOG.md
├── TODO.md
│
├── database/
│
├── instance/
│
├── migrations/
│
├── models/
│
├── customer/
│
├── admin/
│
├── services/
│
├── utils/
│
├── templates/
│
├── static/
│
├── seeds/
│
└── venv/
```

---

# Folder Responsibilities

## app.py

Application entry point.

Responsibilities

• Creates Flask application

• Loads configuration

• Initializes extensions

• Registers Blueprints

• Starts the application

---

## config.py

Contains application configuration.

Responsibilities

• Database Configuration

• Secret Key

• Razorpay Configuration

• Upload Paths

• Environment Configuration

---

## database/

Contains project database if required.

Current Database

SQLite

---

## instance/

Contains instance-specific files.

Primary usage

SQLite Database

Future

Environment-specific runtime files.

---

## migrations/

Contains Flask-Migrate migration history.

Purpose

Version control for database schema.

Rules

Never manually edit generated migration files unless absolutely necessary.

---

# Models

Location

models/

Purpose

Defines all database tables.

Current Models

Category

Brand

Product

Order

OrderItem

Admin

Future

Settings

Notifications

Audit Logs (possible)

Rules

Models define:

Database schema

Relationships

Constraints

Models should NOT contain business logic.

---

# Customer Module

Location

customer/

Purpose

Contains every customer-facing route.

Responsibilities

Homepage

Products

Product Details

Search

Filters

Cart

Checkout

Orders

Payments

Rules

Customer module should remain stable.

Avoid redesigning completed functionality.

---

# Admin Module

Location

admin/

Purpose

Contains the complete administration panel.

Current Architecture

admin/

Authentication

Dashboard

Products

Categories

Brands

Inventory

Orders

Reports

Settings

Each feature is isolated into its own module.

Business logic should remain outside routes.

---

# Services

Location

services/

Purpose

Contains reusable business logic.

Examples

Inventory calculations

Refund processing

Payment processing

Order processing

Report generation

Rules

Routes should call services.

Services should NOT render templates.

Services should remain reusable.

---

# Utilities

Location

utils/

Purpose

Reusable helper functions.

Examples

Decorators

Validators

PDF Generation

Image Upload

Helper Functions

Rules

Utilities should remain generic.

Avoid application-specific business logic inside utils.

---

# Seeds

Location

seeds/

Purpose

Populate development database.

Contains

Categories

Brands

Products

Rules

Used only for initial sample data.

Production data should be managed from the Admin Panel.

---

# Templates

Location

templates/

Structure

layouts/

customer/

admin/

Rules

Templates are organized by feature.

Shared layouts remain inside layouts/.

Customer and Admin interfaces remain independent.

---

# Static

Location

static/

Contains

CSS

JavaScript

Images

Uploads

Images

Hero

Categories

Brands

Products

Customers

Uploads

Products

Brands

Categories

Rules

Uploaded images are stored inside uploads/.

Original project assets remain inside images/.

---

# Development Philosophy

The architecture follows Separation of Concerns.

Presentation Layer

Templates

↓

Routes

↓

Services

↓

Models

↓

Database

Business logic should never bypass the service layer.

---

# Architecture Decisions

Decision 1

Customer functionality remains frozen while Admin is under development.

Decision 2

Business logic belongs in services.

Decision 3

Routes should remain lightweight.

Decision 4

Models represent persistence only.

Decision 5

Documentation is maintained continuously.

Decision 6

Every feature is independently testable.

Decision 7

Git commits represent one completed feature.

Decision 8

UI polish is intentionally postponed until every major business feature is complete.

---

# Database

Database Engine

SQLite

ORM

SQLAlchemy

Migration Tool

Flask-Migrate

Current Baseline Revision

85e7aa87887a_create_initial_schema

Purpose

The database stores all business data for the Paint Store application.

The application is designed so that business operations interact with the database through SQLAlchemy models and service-layer logic.

---

# Current Database Models

## Category

Purpose

Stores product categories.

Examples

Interior Paint

Exterior Paint

Primer

Wood Coating

Waterproofing

Painting Tools

Relationships

One Category

↓

Many Products

---

## Brand

Purpose

Stores paint brands.

Examples

Asian Paints

Berger

Nerolac

Dulux

Indigo

Nippon

Relationships

One Brand

↓

Many Products

---

## Product

Purpose

Stores every sellable product.

Typical Information

Product Name

Category

Brand

Price

Discount

Stock

Rating

Description

Image

Featured Status

Best Seller Status

Relationships

Belongs To

Category

Belongs To

Brand

Referenced By

Order Items

---

## Order

Purpose

Stores customer orders.

Contains

Customer Information

Shipping Information

Payment Status

Order Status

Razorpay Order ID

Razorpay Payment ID

Order Date

Total Amount

Relationships

One Order

↓

Many Order Items

---

## OrderItem

Purpose

Stores every product purchased inside an order.

Contains

Product

Quantity

Unit Price

Subtotal

Relationships

Many Order Items

↓

One Product

Many Order Items

↓

One Order

---

## Admin

Purpose

Stores administrator login identity and account status.

Contains

Username

Email

Password Hash

Active Status

Created Timestamp

Updated Timestamp

Rules

Passwords are stored as hashes only.

Admin authentication logic belongs in services, not the model.

---

# Future Database Models

The following models are planned.

Store Settings

Notifications

Activity Logs

Audit Logs

Future models should only be introduced when required by business needs.

Avoid unnecessary tables.

---

# Customer Workflow

Customer Journey

Home Page

↓

Browse Products

↓

Search / Filter / Sort

↓

Product Details

↓

Add to Cart

↓

Checkout

↓

Razorpay Payment

↓

Payment Verification

↓

Order Creation

↓

Inventory Update

↓

Order Success

↓

Orders

↓

Order Details

---

# Shopping Cart Workflow

Product

↓

Add To Cart

↓

Session Cart

↓

Quantity Update

↓

Remove Product

↓

Checkout

↓

Order Creation

---

# Payment Workflow

Checkout

↓

Create Razorpay Order

↓

Customer Pays

↓

Payment Verification

↓

Order Stored

↓

Payment Status Updated

↓

Inventory Deducted

↓

Success Page

---

# Refund Workflow

Customer Cancels Order

↓

Eligibility Check

↓

Refund Service

↓

Razorpay Refund API

↓

Refund Status Updated

↓

Order Status Updated

↓

Inventory Restored

↓

Customer Notification

Refunds should always be processed through the service layer.

Never duplicate refund logic.

---

# Inventory Workflow

Admin Adds Stock

↓

Database Updated

↓

Customer Views Updated Stock

↓

Customer Purchases Product

↓

Order Created

↓

Inventory Deducted

↓

Stock Updated

↓

Low Stock Monitoring

↓

Restock

Inventory calculations should remain centralized.

Avoid duplicate stock calculations.

---

# Search Workflow

Customer Input

↓

Validation

↓

Database Query

↓

Sorting

↓

Pagination

↓

Results

Search functionality should remain efficient and scalable.

---

# Product Filtering Workflow

Category Filter

Brand Filter

Price Sorting

Newest

Featured

Best Seller

Filters should be composable.

Multiple filters should work together.

---

# Order Lifecycle

Pending

↓

Processing

↓

Shipped

↓

Delivered

Cancelled

↓

Refunded

Future admin functionality will manage these transitions.

---

# Planned Admin Workflow

Admin Login

↓

Dashboard

↓

Manage Categories

↓

Manage Brands

↓

Manage Products

↓

Manage Inventory

↓

Manage Orders

↓

Generate Reports

↓

Manage Store Settings

The Admin Panel will become the single source of management for the application.

Manual database editing should never be required.

---

# Business Rules

Inventory must never become negative.

Products with zero stock cannot be purchased.

Payments must be verified before creating successful orders.

Refunds should always restore inventory.

Business logic belongs in services.

Routes should coordinate requests only.

Models define persistence only.

Customer UI should remain independent from Admin UI.

---

# UI Development Strategy

Current Priority

Business Functionality

Postponed

Customer UI Polish

Admin UI Polish

Animations

Loading Skeletons

Accessibility Improvements

SEO

Responsive Fine Tuning

Reason

Business functionality is significantly more important than visual polish during active feature development.

UI refinement will be completed after all major business modules are implemented.

---

# Deployment Goal

Target

Production Deployment

Possible Platforms

Render

Railway

DigitalOcean

AWS

Deployment work begins only after:

Customer Module Complete

Admin Module Complete

Testing Complete

Performance Review Complete

Security Review Complete

Final UI Polish Complete

---

# Current Implementation Status

This section reflects the actual implementation status of the project.

Only completed features should be marked as completed.

Planned features should remain under future development.

This document should always reflect the current workspace.

---

# Customer Module

Status

Functionally Complete

Current Features

✓ Homepage

✓ Responsive Navigation

✓ Hero Carousel

✓ Welcome Section

✓ Shop by Category

✓ Featured Products

✓ Best Sellers

✓ Brand Showcase

✓ Customer Testimonials

✓ Professional Footer

✓ Product Listing

✓ Product Details

✓ Related Products

✓ Search

✓ Category Filtering

✓ Brand Filtering

✓ Sorting

✓ Pagination

✓ Shopping Cart

✓ Quantity Update

✓ Remove From Cart

✓ Buy Now

✓ Checkout

✓ Razorpay Integration

✓ Payment Verification

✓ Order Creation

✓ Inventory Deduction

✓ Order History

✓ Order Details

✓ Order Cancellation

✓ Automatic Refund

✓ Payment Status Tracking

✓ Order Status Tracking

✓ Flash Messages

The customer side should remain stable during Admin development.

---

# Admin Module

Status

Authentication Complete

Folder structure created.

Admin model and initial migration baseline completed.

Current Progress

✓ Admin directory created

✓ Authentication module structure

✓ Dashboard module structure

✓ Product module structure

✓ Category module structure

✓ Brand module structure

✓ Inventory module structure

✓ Orders module structure

✓ Reports module structure

✓ Settings module structure

✓ Admin model

✓ Flask-Migrate initial schema baseline

✓ Admin login with username or email

✓ Password-hash verification

✓ Active-admin validation

✓ Session login and logout

✓ Dashboard authentication protection

✓ Default admin seed

Upcoming Work

Dashboard

Category Management

Brand Management

Product Management

Inventory Management

Order Management

Reports

Settings

---

# Services Layer

Purpose

Business logic should be implemented inside services.

Examples

Authentication

Inventory

Orders

Payments

Refunds

Reports

Image Processing

Validation

Services should be reusable.

Routes should remain lightweight.

---

# Utilities

Purpose

Reusable helper functionality.

Current Utilities

Decorators

Validators

Helpers

Image Upload

PDF Generator

Future Utilities

Email

Notifications

Background Tasks

Caching

Utilities should never contain business-specific workflows.

---

# Templates

Templates are organized by feature.

Customer templates remain separate from Admin templates.

Every major feature should have its own template folder.

Shared layouts belong inside:

templates/layouts/

Admin layouts belong inside:

templates/admin/

Customer layouts belong inside:

templates/customer/

---

# Static Assets

Current Organization

CSS

JavaScript

Images

Uploads

Images are separated into:

Hero

Products

Brands

Categories

Customers

Uploads are separated into:

Products

Brands

Categories

Uploaded files should never overwrite application assets.

---

# Development Standards

The project follows production-oriented development.

Standards

Routes

Small

Readable

Minimal business logic

Services

Business logic only

Reusable

Testable

Models

Persistence only

Relationships

Constraints

Templates

Presentation only

Utilities

Reusable helper functions

Configuration

Centralized

Environment-ready

Documentation

Always updated

Git

One completed feature

↓

Testing

↓

Commit

↓

Next Feature

---

# Coding Standards

Naming

Use meaningful names.

Avoid abbreviations.

Comments

Explain WHY.

Avoid obvious comments.

Functions

Single responsibility.

Small.

Reusable.

Imports

Standard Library

Third-party Packages

Local Imports

Formatting

Readable.

Consistent.

Professional.

---

# Architecture Principles

Separation of Concerns

Presentation

↓

Routes

↓

Services

↓

Models

↓

Database

No business logic inside templates.

No database queries inside templates.

No duplicated logic inside routes.

Business rules belong in services.

---

# Current Priorities

Priority 1

Complete Admin Dashboard.

Priority 2

Dashboard.

Priority 3

Category Management.

Priority 4

Brand Management.

Priority 5

Product Management.

Priority 6

Inventory.

Priority 7

Orders.

Priority 8

Reports.

Priority 9

Settings.

Priority 10

Customer & Admin UI Polish.

---

# Definition of Done

A feature is considered complete only when:

✓ Functionality implemented

✓ Tested manually

✓ Existing features unaffected

✓ Documentation updated

✓ TODO updated

✓ CHANGELOG updated

✓ Git commit created

Only after all seven conditions are satisfied should development continue to the next feature.

---

# Future Development Roadmap

The project is being developed in well-defined phases.

Each phase must be completed, tested, documented, committed to Git, and verified before moving to the next phase.

---

## Phase 1

Homepage

Status

Completed

---

## Phase 2

Product Module

Status

Completed

---

## Phase 3

Authentication

Status

Customer functionality completed.

Admin authentication is complete.

---

## Phase 4

Shopping System

Status

Completed

Features

Shopping Cart

Buy Now

Checkout

Orders

Inventory

Razorpay

Automatic Refund

Order History

---

## Phase 5

Admin Module

Status

In Progress

Modules

✓ Authentication

□ Dashboard

□ Categories

□ Brands

□ Products

□ Inventory

□ Orders

□ Reports

□ Settings

Each module should be completed independently.

---

## Phase 6

Final Polish

Planned Work

Customer UI Polish

Admin UI Polish

Responsive Improvements

Animations

Loading Skeletons

Accessibility

SEO

Performance Optimization

Image Optimization

Caching

Deployment Preparation

---

# Long-Term Vision

Color Joys Paint Co. should eventually become a production-ready e-commerce application that demonstrates professional software engineering practices.

The final project should be suitable for:

Portfolio

Technical Interviews

Resume

GitHub Showcase

Real Business Demonstration

Professional Code Review

---

# Technical Decisions

The following decisions are intentionally locked unless a critical reason exists to change them.

Decision 1

Customer functionality remains stable while Admin functionality is developed.

Decision 2

Business logic belongs inside services.

Decision 3

Routes should only coordinate requests and responses.

Decision 4

Models represent persistence only.

Decision 5

Templates should never contain database queries.

Decision 6

Reusable logic belongs inside utils or services.

Decision 7

Every completed feature receives its own Git commit.

Decision 8

Documentation must be updated after major features.

Decision 9

The project workspace is always considered the source of truth.

Decision 10

UI polish is intentionally postponed until all business functionality is complete.

---

# Development Workflow

Every feature should follow the same workflow.

Step 1

Understand the feature.

↓

Step 2

Review existing implementation.

↓

Step 3

Identify affected files.

↓

Step 4

Implement.

↓

Step 5

Manual Testing.

↓

Step 6

Security Review.

↓

Step 7

Performance Review.

↓

Step 8

Update Documentation.

↓

Step 9

Git Commit.

↓

Step 10

Continue.

---

# Git Workflow

One Feature

↓

One Commit

↓

Next Feature

Use Conventional Commits.

Examples

feat(admin): implement authentication

feat(products): add CRUD operations

feat(inventory): implement stock management

fix(cart): validate stock before checkout

refactor(admin): simplify authentication flow

docs(project): update project documentation

---

# Maintenance Guidelines

Keep documentation synchronized with the codebase.

Whenever a feature is completed:

Update

PROJECT_CONTEXT.md

CHANGELOG.md

TODO.md

Create Git Commit

Never allow documentation to become outdated.

---

# Deployment Checklist

Before deployment verify:

✓ Authentication

✓ Authorization

✓ Session Security

✓ File Upload Validation

✓ Razorpay Production Keys

✓ Environment Variables

✓ Database Backup

✓ Error Logging

✓ Performance Testing

✓ Security Review

✓ Mobile Responsiveness

✓ Browser Compatibility

✓ Final UI Polish

✓ Documentation Updated

✓ Git Repository Clean

Only after the checklist is complete should production deployment begin.

---

# End of Document

PROJECT_CONTEXT.md serves as the primary technical reference for this repository.

Whenever the project changes, this document should be reviewed and updated so that it always reflects the current implementation.

This document, together with AGENTS.md, CHANGELOG.md, and TODO.md, forms the permanent memory of the project.