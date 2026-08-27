# HRMS UI Design System Rules

This rule defines the complete design specifications, coding guidelines, layout grids, and rules implemented across the HRMS module (Staff Master, Attendance, and Shift Management).

## Core Technical Constraints

- All HRMS pages must be built using HTML + CSS.
- Use only black, white, and neutral grey styling.
- All input fields, search fields, dropdown trigger buttons, and date fields must have a visible default state border (`1px solid #8c8c8c`) and show a stronger black outline on focus.

## Sidebar Navigation

Under the `HUMAN RESOURCES` navigation section, links must follow this exact order:

1. **Staff Master** (`Staff-Management/index.html`)
2. **Attendance** (`Attendance/index.html`)
3. **Shift Management** (`Shift-Management/index.html`)

## Staff Master Module Rules

- The table columns must be fully dynamic and automatically add/remove column headers and cell records in response to configuration and data keys syncing.
- An active filter notification dot (`●`) must display on the Filters button if any filters are active.
- Reset buttons must clear all checkbox values, restore placeholders, and hide the notification dot.
- Every multi-select dropdown must support Select All and Deselect All controls, automatically toggling options and updating triggers to "All Selected", "X Selected", or default placeholders.
