# CHANGELOG.md

All notable changes to this project will be documented in this file.

This project follows the principles of:

- Keep a Changelog
- Semantic Versioning (where applicable)
- Conventional Git Commits

---

# [Unreleased]

This section contains work currently under development.

Current Sprint

Phase 5.3

Admin Categories

## Added

### Admin Authentication Foundation

- Added Admin model with username, email, password hash, active status, and timestamps.
- Registered Admin model in the shared models package.
- Initialized Flask-Migrate migration history.
- Created initial database schema baseline migration.

### Admin Authentication Completion

- Added username-or-email login with password-hash verification and active-admin validation.
- Added session-based admin login and logout.
- Protected the admin dashboard with an authentication decorator.
- Added the default administrator seed.

### Admin Dashboard and Product Management

- Added a protected dashboard with product, category, and brand totals.
- Added admin product listing, creation, and editing workflows.
- Added product image upload handling with generated filenames.

## Changed

### Database Management

- Removed automatic `db.create_all()` initialization from application startup.
- Updated database configuration to support `DATABASE_URL`.
- Updated project status documentation to reflect completed admin authentication, dashboard v1, and product management.

---

# [0.4.0] - Current Development Baseline

This version represents the completion of the complete customer-side e-commerce system before Admin development begins.

## Added

### Homepage

- Responsive Bootstrap Navigation
- Hero Carousel
- Welcome Section
- Shop by Category
- Featured Products
- Best Sellers
- Brand Showcase
- Testimonials
- Professional Footer

---

### Product Module

- Product Model
- Category Model
- Brand Model
- Product Listing
- Product Details
- Related Products
- Product Images
- Search
- Category Filtering
- Brand Filtering
- Sorting
- Pagination

---

### Shopping Cart

- Add to Cart
- Update Quantity
- Remove From Cart
- Buy Now
- Session Cart

---

### Checkout

- Customer Information
- Order Summary
- Shipping Details
- Checkout Validation

---

### Payments

- Razorpay Integration
- Razorpay Order Creation
- Payment Verification
- Payment Status Tracking

---

### Orders

- Order Creation
- Order History
- Order Details
- Order Status Tracking
- Cancel Order

---

### Refunds

- Automatic Refund Processing
- Refund Status Tracking
- Inventory Restoration

---

### Inventory

- Automatic Stock Deduction
- Stock Validation
- Out of Stock Protection

---

### Customer Experience

- Flash Messages
- Responsive Layout
- Related Products
- Search Experience
- Filters

---

### Architecture

- Modular Flask Project Structure
- SQLAlchemy Models
- Blueprint Architecture
- Services Layer
- Utilities Layer
- Template Organization
- Static Asset Organization

---

### Documentation

- AGENTS.md
- PROJECT_CONTEXT.md
- TODO.md
- CHANGELOG.md

---

# Upcoming

## Phase 5

Admin Module

Planned

- Admin Authentication
- Dashboard
- Categories
- Brands
- Products
- Inventory
- Orders
- Reports
- Settings

---

## Phase 6

Final Polish

Planned

- Customer UI Polish
- Admin UI Polish
- Accessibility
- SEO
- Performance Optimization
- Image Optimization
- Responsive Refinements

---

## Phase 7

Testing

Planned

- Manual Testing
- Security Review
- Performance Review
- Authentication Testing
- Payment Testing
- Refund Testing

---

## Phase 8

Deployment

Planned

- Production Configuration
- Environment Variables
- Logging
- Monitoring
- Backup
- Production Deployment

---

# Future Changelog Format

Every completed feature should be added using this format.

## [Version] - YYYY-MM-DD

### Added

- New features

### Changed

- Improvements

### Fixed

- Bug fixes

### Refactored

- Code structure improvements

### Security

- Security improvements

### Documentation

- Documentation updates

### Performance

- Performance optimizations

---

# Git Commit Policy

Every completed feature must satisfy:

✓ Feature Implemented

✓ Tested

✓ Documentation Updated

✓ Git Commit Created

Only then should development continue.